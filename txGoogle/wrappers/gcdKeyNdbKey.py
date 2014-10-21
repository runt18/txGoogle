import array
import struct
import base64
import unittest


_MAX_LONG = 2L ** 63    # Use 2L, see issue 65.    http://goo.gl/ELczz
_MAX_KEYPART_BYTES = 500

TYPE_DOUBLE = 1
TYPE_FLOAT = 2
TYPE_INT64 = 3
TYPE_UINT64 = 4
TYPE_INT32 = 5
TYPE_FIXED64 = 6
TYPE_FIXED32 = 7
TYPE_BOOL = 8
TYPE_STRING = 9
TYPE_GROUP = 10
TYPE_FOREIGN = 11


class BadValueError(Exception):
    pass


class BadArgumentError(Exception):
    pass


class ProtocolBufferDecodeError(Exception):
    pass


class ProtocolBufferEncodeError(Exception):
    pass


class ProtocolBufferReturnError(Exception):
    pass


class Model(object):
    def __init__(self):
        raise NotImplementedError


class Encoder:

    NUMERIC = 0
    DOUBLE = 1
    STRING = 2
    STARTGROUP = 3
    ENDGROUP = 4
    FLOAT = 5
    MAX_TYPE = 6

    def __init__(self):
        self.buf = array.array('B')
        return

    def buffer(self):
        return self.buf

    def put8(self, v):
        if v < 0 or v >= (1 << 8):
            raise ProtocolBufferEncodeError('u8 too big')
        self.buf.append(v & 255)
        return

    def put16(self, v):
        if v < 0 or v >= (1 << 16):
            raise ProtocolBufferEncodeError('u16 too big')
        self.buf.append((v >> 0) & 255)
        self.buf.append((v >> 8) & 255)
        return

    def put32(self, v):
        if v < 0 or v >= (1L << 32):
            raise ProtocolBufferEncodeError('u32 too big')
        self.buf.append((v >> 0) & 255)
        self.buf.append((v >> 8) & 255)
        self.buf.append((v >> 16) & 255)
        self.buf.append((v >> 24) & 255)
        return

    def put64(self, v):
        if v < 0 or v >= (1L << 64):
            raise ProtocolBufferEncodeError('u64 too big')
        self.buf.append((v >> 0) & 255)
        self.buf.append((v >> 8) & 255)
        self.buf.append((v >> 16) & 255)
        self.buf.append((v >> 24) & 255)
        self.buf.append((v >> 32) & 255)
        self.buf.append((v >> 40) & 255)
        self.buf.append((v >> 48) & 255)
        self.buf.append((v >> 56) & 255)
        return

    def putVarInt32(self, v):
        buf_append = self.buf.append
        if v & 127 == v:
            buf_append(v)
            return
        if v >= 0x80000000 or v < -0x80000000:
            raise ProtocolBufferEncodeError('int32 too big')
        if v < 0:
            v += 0x10000000000000000
        while True:
            bits = v & 127
            v >>= 7
            if v:
                bits |= 128
            buf_append(bits)
            if not v:
                break
        return

    def putVarInt64(self, v):
        buf_append = self.buf.append
        if v >= 0x8000000000000000 or v < -0x8000000000000000:
            raise ProtocolBufferEncodeError('int64 too big')
        if v < 0:
            v += 0x10000000000000000
        while True:
            bits = v & 127
            v >>= 7
            if v:
                bits |= 128
            buf_append(bits)
            if not v:
                break
        return

    def putVarUint64(self, v):
        buf_append = self.buf.append
        if v < 0 or v >= 0x10000000000000000:
            raise ProtocolBufferEncodeError('uint64 too big')
        while True:
            bits = v & 127
            v >>= 7
            if v:
                bits |= 128
            buf_append(bits)
            if not v:
                break
        return

    def putFloat(self, v):
        a = array.array('B')
        a.fromstring(struct.pack("<f", v))
        self.buf.extend(a)
        return

    def putDouble(self, v):
        a = array.array('B')
        a.fromstring(struct.pack("<d", v))
        self.buf.extend(a)
        return

    def putBoolean(self, v):
        if v:
            self.buf.append(1)
        else:
            self.buf.append(0)
        return

    def putPrefixedString(self, v):
        v = str(v)
        self.putVarInt32(len(v))
        self.buf.fromstring(v)
        return

    def putRawString(self, v):
        self.buf.fromstring(v)

    _TYPE_TO_METHOD = {
            TYPE_DOUBLE: putDouble,
            TYPE_FLOAT: putFloat,
            TYPE_FIXED64: put64,
            TYPE_FIXED32: put32,
            TYPE_INT32: putVarInt32,
            TYPE_INT64: putVarInt64,
            TYPE_UINT64: putVarUint64,
            TYPE_BOOL: putBoolean,
            TYPE_STRING: putPrefixedString
    }

    _TYPE_TO_BYTE_SIZE = {
            TYPE_DOUBLE: 8,
            TYPE_FLOAT: 4,
            TYPE_FIXED64: 8,
            TYPE_FIXED32: 4,
            TYPE_BOOL: 1
    }


class Decoder:
    def __init__(self, buf, idx, limit):
        self.buf = buf
        self.idx = idx
        self.limit = limit
        return

    def avail(self):
        return self.limit - self.idx

    def buffer(self):
        return self.buf

    def pos(self):
        return self.idx

    def skip(self, n):
        if self.idx + n > self.limit:
            raise ProtocolBufferDecodeError('truncated')
        self.idx += n
        return

    def skipData(self, tag):
        t = tag & 7
        if t == Encoder.NUMERIC:
            self.getVarInt64()
        elif t == Encoder.DOUBLE:
            self.skip(8)
        elif t == Encoder.STRING:
            n = self.getVarInt32()
            self.skip(n)
        elif t == Encoder.STARTGROUP:
            while 1:
                t = self.getVarInt32()
                if (t & 7) == Encoder.ENDGROUP:
                    break
                else:
                    self.skipData(t)
            if (t - Encoder.ENDGROUP) != (tag - Encoder.STARTGROUP):
                raise ProtocolBufferDecodeError('corrupted')
        elif t == Encoder.ENDGROUP:
            raise ProtocolBufferDecodeError('corrupted')
        elif t == Encoder.FLOAT:
            self.skip(4)
        else:
            raise ProtocolBufferDecodeError('corrupted')

    def get8(self):
        if self.idx >= self.limit:
            raise ProtocolBufferDecodeError('truncated')
        c = self.buf[self.idx]
        self.idx += 1
        return c

    def get16(self):
        if self.idx + 2 > self.limit:
            raise ProtocolBufferDecodeError('truncated')
        c = self.buf[self.idx]
        d = self.buf[self.idx + 1]
        self.idx += 2
        return (d << 8) | c

    def get32(self):
        if self.idx + 4 > self.limit:
            raise ProtocolBufferDecodeError('truncated')
        c = self.buf[self.idx]
        d = self.buf[self.idx + 1]
        e = self.buf[self.idx + 2]
        f = long(self.buf[self.idx + 3])
        self.idx += 4
        return (f << 24) | (e << 16) | (d << 8) | c

    def get64(self):
        if self.idx + 8 > self.limit:
            raise ProtocolBufferDecodeError('truncated')
        c = self.buf[self.idx]
        d = self.buf[self.idx + 1]
        e = self.buf[self.idx + 2]
        f = long(self.buf[self.idx + 3])
        g = long(self.buf[self.idx + 4])
        h = long(self.buf[self.idx + 5])
        i = long(self.buf[self.idx + 6])
        j = long(self.buf[self.idx + 7])
        self.idx += 8
        return ((j << 56) | (i << 48) | (h << 40) | (g << 32) | (f << 24)
                        | (e << 16) | (d << 8) | c)

    def getVarInt32(self):
        b = self.get8()
        if not (b & 128):
            return b

        result = long(0)
        shift = 0

        while 1:
            result |= (long(b & 127) << shift)
            shift += 7
            if not (b & 128):
                if result >= 0x10000000000000000L:
                    raise ProtocolBufferDecodeError('corrupted')
                break
            if shift >= 64:
                raise ProtocolBufferDecodeError('corrupted')
            b = self.get8()

        if result >= 0x8000000000000000L:
            result -= 0x10000000000000000L
        if result >= 0x80000000L or result < -0x80000000L:
            raise ProtocolBufferDecodeError('corrupted')
        return result

    def getVarInt64(self):
        result = self.getVarUint64()
        if result >= (1L << 63):
            result -= (1L << 64)
        return result

    def getVarUint64(self):
        result = long(0)
        shift = 0
        while 1:
            if shift >= 64:
                raise ProtocolBufferDecodeError('corrupted')
            b = self.get8()
            result |= (long(b & 127) << shift)
            shift += 7
            if not (b & 128):
                if result >= (1L << 64):
                    raise ProtocolBufferDecodeError('corrupted')
                return result
        return result

    def getFloat(self):
        if self.idx + 4 > self.limit:
            raise ProtocolBufferDecodeError('truncated')
        a = self.buf[self.idx:self.id + 4]
        self.idx += 4
        return struct.unpack("<f", a)[0]

    def getDouble(self):
        if self.idx + 8 > self.limit:
            raise ProtocolBufferDecodeError('truncated')
        a = self.buf[self.idx:self.id + 8]
        self.idx += 8
        return struct.unpack("<d", a)[0]

    def getBoolean(self):
        b = self.get8()
        if b != 0 and b != 1:
            raise ProtocolBufferDecodeError('corrupted')
        return b

    def getPrefixedString(self):
        length = self.getVarInt32()
        if self.idx + length > self.limit:
            raise ProtocolBufferDecodeError('truncated')
        r = self.buf[self.idx: self.idx + length]
        self.idx += length
        return r.tostring()

    def getRawString(self):
        r = self.buf[self.idx:self.limit]
        self.idx = self.limit
        return r.tostring()

    _TYPE_TO_METHOD = {
            TYPE_DOUBLE: getDouble,
            TYPE_FLOAT: getFloat,
            TYPE_FIXED64: get64,
            TYPE_FIXED32: get32,
            TYPE_INT32: getVarInt32,
            TYPE_INT64: getVarInt64,
            TYPE_UINT64: getVarUint64,
            TYPE_BOOL: getBoolean,
            TYPE_STRING: getPrefixedString
    }


class ProtocolMessage:

    def Encode(self):
        try:
            return self._CEncode()
        except NotImplementedError:
            e = Encoder()
            self.Output(e)
            return e.buffer().tostring()

    def _CEncode(self):
        raise NotImplementedError

    def MergeFromString(self, s):
        self.MergePartialFromString(s)
        dbg = []
        if not self.IsInitialized(dbg):
            raise ProtocolBufferDecodeError('\n\t'.join(dbg))

    def MergePartialFromString(self, s):
        try:
            self._CMergeFromString(s)
        except NotImplementedError:
            a = array.array('B')
            a.fromstring(s)
            d = Decoder(a, 0, len(a))
            self.TryMerge(d)

    def _CMergeFromString(self, s):
        raise NotImplementedError

    def Output(self, e):
        dbg = []
        if not self.IsInitialized(dbg):
            raise ProtocolBufferEncodeError('\n\t'.join(dbg))
        self.OutputUnchecked(e)
        return

    def lengthVarInt32(self, n):
        return self.lengthVarInt64(n)

    def lengthVarInt64(self, n):
        if n < 0:
            return 10
        result = 0
        while 1:
            result += 1
            n >>= 7
            if n == 0:
                break
        return result

    def lengthString(self, n):
        return self.lengthVarInt32(n) + n


class Path_Element(ProtocolMessage):
    has_type_ = 0
    type_ = ""
    has_id_ = 0
    id_ = 0
    has_name_ = 0
    name_ = ""

    def __init__(self, contents=None):
        if contents is not None:
            self.MergeFromString(contents)

    def type(self):
        return self.type_

    def set_type(self, x):
        self.has_type_ = 1
        self.type_ = x

    def id(self):
        return self.id_

    def set_id(self, x):
        self.has_id_ = 1
        self.id_ = x

    def has_id(self):
        return self.has_id_

    def name(self):
        return self.name_

    def set_name(self, x):
        self.has_name_ = 1
        self.name_ = x

    def IsInitialized(self, debug_strs=None):
        initialized = 1
        if (not self.has_type_):
            initialized = 0
            if debug_strs is not None:
                debug_strs.append('Required field: type not set.')
        return initialized

    def ByteSize(self):
        n = 0
        n += self.lengthString(len(self.type_))
        if (self.has_id_):
            n += 1 + self.lengthVarInt64(self.id_)
        if (self.has_name_):
            n += 1 + self.lengthString(len(self.name_))
        return n + 1

    def OutputUnchecked(self, out):
        out.putVarInt32(18)
        out.putPrefixedString(self.type_)
        if (self.has_id_):
            out.putVarInt32(24)
            out.putVarInt64(self.id_)
        if (self.has_name_):
            out.putVarInt32(34)
            out.putPrefixedString(self.name_)

    def TryMerge(self, d):
        while 1:
            tt = d.getVarInt32()
            if tt == 12:
                break
            if tt == 18:
                self.set_type(d.getPrefixedString())
                continue
            if tt == 24:
                self.set_id(d.getVarInt64())
                continue
            if tt == 34:
                self.set_name(d.getPrefixedString())
                continue
            if (tt == 0):
                raise ProtocolBufferDecodeError
            d.skipData(tt)


class Path(ProtocolMessage):

    def __init__(self, contents=None):
        self.element_ = []
        if contents is not None:
            self.MergeFromString(contents)

    def element_size(self):
        return len(self.element_)

    def element_list(self):
        return self.element_

    def add_element(self):
        x = Path_Element()
        self.element_.append(x)
        return x

    def IsInitialized(self, debug_strs=None):
        initialized = 1
        for p in self.element_:
            if not p.IsInitialized(debug_strs):
                initialized = 0
        return initialized

    def ByteSize(self):
        n = 0
        n += 2 * len(self.element_)
        for i in xrange(len(self.element_)):
            n += self.element_[i].ByteSize()
        return n

    def OutputUnchecked(self, out):
        for i in xrange(len(self.element_)):
            out.putVarInt32(11)
            self.element_[i].OutputUnchecked(out)
            out.putVarInt32(12)

    def TryMerge(self, d):
        while d.avail() > 0:
            tt = d.getVarInt32()
            if tt == 11:
                self.add_element().TryMerge(d)
                continue
            if (tt == 0):
                raise ProtocolBufferDecodeError
            d.skipData(tt)


class Reference(ProtocolMessage):
    has_app_ = 0
    app_ = ""
    has_name_space_ = 0
    name_space_ = ""
    has_path_ = 0

    def __init__(self, contents=None):
        self.path_ = Path()
        if contents is not None:
            self.MergeFromString(contents)

    def app(self):
        return self.app_

    def set_app(self, x):
        self.has_app_ = 1
        self.app_ = x

    def path(self):
        return self.path_

    def mutable_path(self):
        self.has_path_ = 1
        return self.path_

    def IsInitialized(self, debug_strs=None):
        initialized = 1
        if (not self.has_app_):
            initialized = 0
            if debug_strs is not None:
                debug_strs.append('Required field: app not set.')
        if (not self.has_path_):
            initialized = 0
            if debug_strs is not None:
                debug_strs.append('Required field: path not set.')
        elif not self.path_.IsInitialized(debug_strs):
            initialized = 0
        return initialized

    def OutputUnchecked(self, out):
        out.putVarInt32(106)
        out.putPrefixedString(self.app_)
        out.putVarInt32(114)
        out.putVarInt32(self.path_.ByteSize())
        self.path_.OutputUnchecked(out)
        if (self.has_name_space_):
            out.putVarInt32(162)
            out.putPrefixedString(self.name_space_)

    def TryMerge(self, d):
        while d.avail() > 0:
            tt = d.getVarInt32()
            if tt == 106:
                self.set_app(d.getPrefixedString())
                continue
            if tt == 114:
                length = d.getVarInt32()
                tmp = Decoder(d.buffer(), d.pos(), d.pos() + length)
                d.skip(length)
                self.mutable_path().TryMerge(tmp)
                continue
            if tt == 162:
                self.set_name_space(d.getPrefixedString())
                continue
            if (tt == 0):
                raise ProtocolBufferDecodeError
            d.skipData(tt)


class Key(object):
    """An immutable datastore key.

    For flexibility and convenience, multiple constructor signatures are
    supported.

    The primary way to construct a key is using positional arguments:
    - Key(kind1, id1, kind2, id2, ...).

    This is shorthand for either of the following two longer forms:
    - Key(pairs=[(kind1, id1), (kind2, id2), ...])
    - Key(flat=[kind1, id1, kind2, id2, ...])

    Either of the above constructor forms can additionally pass in another
    key using parent=<key>.    The (kind, id) pairs of the parent key are
    inserted before the (kind, id) pairs passed explicitly.

    You can also construct a Key from a 'url-safe' encoded string:
    - Key(urlsafe=<string>)

    For esoteric purposes the following constructors exist:
    - Key(reference=<reference>) -- passing in a low-level Reference object
    - Key(serialized=<string>) -- passing in a serialized low-level Reference
    - Key(<dict>) -- for unpickling, the same as Key(**<dict>)

    The 'url-safe' string is really a websafe-base64-encoded serialized
    Reference, but it's best to think of it as just an opaque unique
    string.

    Additional constructor keyword arguments:
    - app=<string> -- specify the application id
    - namespace=<string> -- specify the namespace

    If a Reference is passed (using one of reference, serialized or
    urlsafe), the args and namespace keywords must match what is already
    present in the Reference (after decoding if necessary).    The parent
    keyword cannot be combined with a Reference in any form.


    Keys are immutable, which means that a Key object cannot be modified
    once it has been created.    This is enforced by the implementation as
    well as Python allows.

    For access to the contents of a key, the following methods and
    operations are supported:

    - repr(key), str(key) -- return a string representation resembling
        the shortest constructor form, omitting the app and namespace
        unless they differ from the default value.

    - key1 == key2, key1 != key2 -- comparison for equality between Keys.

    - hash(key) -- a hash value sufficient for storing Keys in a dict.

    - key.pairs() -- a tuple of (kind, id) pairs.

    - key.flat() -- a tuple of flattened kind and id values, i.e.
        (kind1, id1, kind2, id2, ...).

    - key.app() -- the application id.

    - key.id() -- the string or integer id in the last (kind, id) pair,
        or None if the key is incomplete.

    - key.string_id() -- the string id in the last (kind, id) pair,
        or None if the key has an integer id or is incomplete.

    - key.integer_id() -- the integer id in the last (kind, id) pair,
        or None if the key has a string id or is incomplete.

    - key.namespace() -- the namespace.

    - key.kind() -- a shortcut for key.pairs()[-1][0].

    - key.parent() -- a Key constructed from all but the last (kind, id)
        pairs.

    - key.urlsafe() -- a websafe-base64-encoded serialized Reference.

    - key.serialized() -- a serialized Reference.

    - key.reference() -- a Reference object.    The caller promises not to
        mutate it.

    Keys also support interaction with the datastore; these methods are
    the only ones that engage in any kind of I/O activity.    For Future
    objects, see the document for ndb/tasklets.py.

    - key.get() -- return the entity for the Key.

    - key.get_async() -- return a Future whose eventual result is
        the entity for the Key.

    - key.delete() -- delete the entity for the Key.

    - key.delete_async() -- asynchronously delete the entity for the Key.

    Keys may be pickled.

    Subclassing Key is best avoided; it would be hard to get right.
    """

    __slots__ = ['__reference', '__pairs', '__app', '__namespace']

    def __new__(cls, *_args, **kwargs):
        """Constructor.    See the class docstring for arguments."""
        if _args:
            if len(_args) == 1 and isinstance(_args[0], dict):
                if kwargs:
                    raise TypeError('Key() takes no keyword arguments when a dict is the '
                                                    'the first and only non-keyword argument (for '
                                                    'unpickling).')
                kwargs = _args[0]
            else:
                if 'flat' in kwargs:
                    raise TypeError('Key() with positional arguments '
                                                    'cannot accept flat as a keyword argument.')
                kwargs['flat'] = _args
        self = super(Key, cls).__new__(cls)
        # Either __reference or (__pairs, __app, __namespace) must be set.
        # Either one fully specifies a key; if both are set they must be
        # consistent with each other.
        if 'reference' in kwargs or 'serialized' in kwargs or 'urlsafe' in kwargs:
            self.__reference = _ConstructReference(cls, **kwargs)
            self.__pairs = None
            self.__app = None
            self.__namespace = None
        elif 'pairs' in kwargs or 'flat' in kwargs:
            self.__reference = None
            (self.__pairs,
             self.__app,
             self.__namespace) = self._parse_from_args(**kwargs)
        else:
            raise TypeError('Key() cannot create a Key instance without arguments.')
        return self

    @staticmethod
    def _parse_from_args(pairs=None, flat=None, app=None, namespace=None,
                                             parent=None):
        if flat:
            if pairs is not None:
                raise TypeError('Key() cannot accept both flat and pairs arguments.')
            if len(flat) % 2:
                raise ValueError('Key() must have an even number of positional '
                                                 'arguments.')
            pairs = [(flat[i], flat[i + 1]) for i in xrange(0, len(flat), 2)]
        else:
            pairs = list(pairs)
        if not pairs:
            raise TypeError('Key must consist of at least one pair.')
        for i, (kind, id) in enumerate(pairs):
            if isinstance(id, unicode):
                id = id.encode('utf8')
            elif id is None:
                if i + 1 < len(pairs):
                    raise BadArgumentError(
                        'Incomplete Key entry must be last')
            else:
                if not isinstance(id, (int, long, str)):
                    raise TypeError('Key id must be a string or a number; received %r' %
                                                    id)
            if isinstance(kind, type):
                kind = kind._get_kind()
            if isinstance(kind, unicode):
                kind = kind.encode('utf8')
            if not isinstance(kind, str):
                    raise TypeError('Key kind must be a string or Model class; '
                                                    'received %r' % kind)
            if not id:
                id = None
            pairs[i] = (kind, id)
        if parent is not None:
            if not isinstance(parent, Key):
                raise BadValueError(
                        'Expected Key instance, got %r' % parent)
            if not parent.id():
                raise BadArgumentError(
                    'Parent cannot have incomplete key')
            pairs[:0] = parent.pairs()
            if app:
                if app != parent.app():
                    raise ValueError('Cannot specify a different app %r '
                                                     'than the parent app %r' %
                                                     (app, parent.app()))
            else:
                app = parent.app()
            if namespace is not None:
                if namespace != parent.namespace():
                    raise ValueError('Cannot specify a different namespace %r '
                                                     'than the parent namespace %r' %
                                                     (namespace, parent.namespace()))
            else:
                namespace = parent.namespace()

        return tuple(pairs), app, namespace

    def app(self):
        """Return the application id."""
        if self.__app is None:
            self.__app = self.__reference.app()
        return self.__app

    def pairs(self):
        """Return a tuple of (kind, id) pairs."""
        pairs = self.__pairs
        if pairs is None:
            pairs = []
            for elem in self.__reference.path().element_list():
                kind = elem.type()
                if elem.has_id():
                    id_or_name = elem.id()
                else:
                    id_or_name = elem.name()
                if not id_or_name:
                    id_or_name = None
                tup = (kind, id_or_name)
                pairs.append(tup)
            self.__pairs = pairs = tuple(pairs)
        return pairs

    def reference(self):
        """Return the Reference object for this Key.

        This is a entity_pb.Reference instance -- a protocol buffer class
        used by the lower-level API to the datastore.

        NOTE: The caller should not mutate the return value.
        """
        if self.__reference is None:
            self.__reference = _ConstructReference(self.__class__,
                                                                                         pairs=self.__pairs,
                                                                                         app=self.__app,
                                                                                         namespace=self.__namespace)
        return self.__reference

    def urlsafe(self):
        """Return a url-safe string encoding this Key's Reference.

        This string is compatible with other APIs and languages and with
        the strings used to represent Keys in GQL and in the App Engine
        Admin Console.
        """
        # This is 3-4x faster than urlsafe_b64decode()
        urlsafe = base64.b64encode(self.reference().Encode())
        return urlsafe.rstrip('=').replace('+', '-').replace('/', '_')


def _ConstructReference(cls, pairs=None, flat=None,
                                                reference=None, serialized=None, urlsafe=None,
                                                app=None, namespace=None, parent=None):
    """Construct a Reference; the signature is the same as for Key."""
    if cls is not Key:
        raise TypeError('Cannot construct Key reference on non-Key class; '
                                        'received %r' % cls)
    if (bool(pairs) + bool(flat) + bool(reference) + bool(serialized) +
            bool(urlsafe)) != 1:
        raise TypeError('Cannot construct Key reference from incompatible keyword '
                                        'arguments.')
    if flat or pairs:
        if flat:
            if len(flat) % 2:
                raise TypeError('_ConstructReference() must have an even number of '
                                                'positional arguments.')
            pairs = [(flat[i], flat[i + 1]) for i in xrange(0, len(flat), 2)]
        elif parent is not None:
            pairs = list(pairs)
        if not pairs:
            raise TypeError('Key references must consist of at least one pair.')
        if parent is not None:
            if not isinstance(parent, Key):
                raise BadValueError(
                        'Expected Key instance, got %r' % parent)
            pairs[:0] = parent.pairs()
            if app:
                if app != parent.app():
                    raise ValueError('Cannot specify a different app %r '
                                                     'than the parent app %r' %
                                                     (app, parent.app()))
            else:
                app = parent.app()
            if namespace is not None:
                if namespace != parent.namespace():
                    raise ValueError('Cannot specify a different namespace %r '
                                                     'than the parent namespace %r' %
                                                     (namespace, parent.namespace()))
            else:
                namespace = parent.namespace()
        reference = _ReferenceFromPairs(pairs, app=app, namespace=namespace)
    else:
        if parent is not None:
            raise TypeError('Key reference cannot be constructed when the parent '
                                            'argument is combined with either reference, serialized '
                                            'or urlsafe arguments.')
        if urlsafe:
            serialized = _DecodeUrlSafe(urlsafe)
        if serialized:
            reference = _ReferenceFromSerialized(serialized)
        if not reference.path().element_size():
            raise RuntimeError('Key reference has no path or elements (%r, %r, %r).'
                                                 % (urlsafe, serialized, str(reference)))
        # TODO: ensure that each element has a type and either an id or a name
        if not serialized:
            reference = _ReferenceFromReference(reference)
        # You needn't specify app= or namespace= together with reference=,
        # serialized= or urlsafe=, but if you do, their values must match
        # what is already in the reference.
        if app is not None:
            if app != reference.app():
                raise RuntimeError('Key reference constructed uses a different app %r '
                                                     'than the one specified %r' %
                                                     (reference.app(), app))
        if namespace is not None:
            if namespace != reference.name_space():
                raise RuntimeError('Key reference constructed uses a different '
                                                     'namespace %r than the one specified %r' %
                                                     (reference.name_space(), namespace))
    return reference


def _ReferenceFromPairs(pairs, reference=None, app=None, namespace=None):
    """Construct a Reference from a list of pairs.

    If a Reference is passed in as the second argument, it is modified
    in place.    The app and namespace are set from the corresponding
    keyword arguments, with the customary defaults.
    """
    if reference is None:
        reference = Reference()
    path = reference.mutable_path()
    last = False
    for kind, idorname in pairs:
        if last:
            raise BadArgumentError(
                    'Incomplete Key entry must be last')
        t = type(kind)
        if t is str:
            pass
        elif t is unicode:
            kind = kind.encode('utf8')
        else:
            if issubclass(t, type):
                modelclass = kind
                if not issubclass(modelclass, Model):
                    raise TypeError('Key kind must be either a string or subclass of '
                                                    'Model; received %r' % modelclass)
                kind = modelclass._get_kind()
                t = type(kind)
            if t is str:
                pass
            elif t is unicode:
                kind = kind.encode('utf8')
            elif issubclass(t, str):
                pass
            elif issubclass(t, unicode):
                kind = kind.encode('utf8')
            else:
                raise TypeError('Key kind must be either a string or subclass of Model;'
                                                ' received %r' % kind)
        if not (1 <= len(kind) <= _MAX_KEYPART_BYTES):
            raise ValueError('Key kind string must be a non-empty string up to %i'
                                             'bytes; received %s' %
                                             (_MAX_KEYPART_BYTES, kind))
        elem = path.add_element()
        elem.set_type(kind)
        t = type(idorname)
        if t is int or t is long:
            if not (1 <= idorname < _MAX_LONG):
                raise ValueError('Key id number is too long; received %i' % idorname)
            elem.set_id(idorname)
        elif t is str:
            if not (1 <= len(idorname) <= _MAX_KEYPART_BYTES):
                raise ValueError('Key name strings must be non-empty strings up to %i '
                                                 'bytes; received %s' %
                                                 (_MAX_KEYPART_BYTES, idorname))
            elem.set_name(idorname)
        elif t is unicode:
            idorname = idorname.encode('utf8')
            if not (1 <= len(idorname) <= _MAX_KEYPART_BYTES):
                raise ValueError('Key name unicode strings must be non-empty strings up'
                                                 ' to %i bytes; received %s' %
                                                 (_MAX_KEYPART_BYTES, idorname))
            elem.set_name(idorname)
        elif idorname is None:
            elem.set_id(0)
            last = True
        elif issubclass(t, (int, long)):
            if not (1 <= idorname < _MAX_LONG):
                raise ValueError('Key id number is too long; received %i' % idorname)
            elem.set_id(idorname)
        elif issubclass(t, basestring):
            if issubclass(t, unicode):
                idorname = idorname.encode('utf8')
            if not (1 <= len(idorname) <= _MAX_KEYPART_BYTES):
                raise ValueError('Key name strings must be non-empty strings up to %i '
                                                 'bytes; received %s' % (_MAX_KEYPART_BYTES, idorname))
            elem.set_name(idorname)
        else:
            raise TypeError('id must be either a numeric id or a string name; '
                                            'received %r' % idorname)

    if app:
        reference.set_app(app)
    if namespace:
        reference.set_name_space(namespace)
    return reference


def _ReferenceFromReference(reference):
    """Copy a Reference."""
    new_reference = Reference()
    new_reference.CopyFrom(reference)
    return new_reference


def _ReferenceFromSerialized(serialized):
    """Construct a Reference from a serialized Reference."""
    if not isinstance(serialized, basestring):
        raise TypeError('serialized must be a string; received %r' % serialized)
    elif isinstance(serialized, unicode):
        serialized = serialized.encode('utf8')
    return Reference(serialized)


def _DecodeUrlSafe(urlsafe):
    """Decode a url-safe base64-encoded string.

    This returns the decoded string.
    """
    if not isinstance(urlsafe, basestring):
        raise TypeError('urlsafe must be a string; received %r' % urlsafe)
    if isinstance(urlsafe, unicode):
        urlsafe = urlsafe.encode('utf8')
    mod = len(urlsafe) % 4
    if mod:
        urlsafe += '=' * (4 - mod)
    # This is 3-4x faster than urlsafe_b64decode()
    return base64.b64decode(urlsafe.replace('-', '+').replace('_', '/'))


def getPairsFromUrlSafe(urlSafe):
    ndbKey = Key(urlsafe=urlSafe)
    return ndbKey.pairs()


def urlSafeFromPairs(datasetId, pairs):
    ndbKeyNew = Key(app=datasetId, pairs=pairs)
    return ndbKeyNew.urlsafe()
