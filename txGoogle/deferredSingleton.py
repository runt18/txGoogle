from twisted.internet import defer


class DeferredSingleton(type):
    # http://blogs.fluidinfo.com/terry/2008/11/03/a-python-metaclass-for-twisted-allowing-__init__-to-return-a-deferred/

    _instances = {}

    def __call__(cls, *args, **kwargs): # @NoSelf
        if cls not in cls._instances:
            cls._instances[cls] = super(DeferredSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def __new__(mcl, classname, bases, classdict):
        hidden = '__hidden__'
        instantiate = '__instantiate__'
        for name in hidden, instantiate:
            if name in classdict:
                raise Exception('Class %s contains an illegally-named %s method' % (classname, name))
        try:
            origInit = classdict['__init__']
        except KeyError:
            origInit = lambda self: None

        def newInit(self, *args, **kw):
            hiddenDict = dict(args=args, kw=kw, __init__=origInit)
            setattr(self, hidden, hiddenDict)

        def _instantiate(self, DUMMY=None):
            def addSelf(result):
                return (self, result)
            hiddenDict = getattr(self, hidden)
            d = defer.maybeDeferred(hiddenDict['__init__'], self,
                                    *hiddenDict['args'], **hiddenDict['kw'])
            self.dfd = d
            return d.addCallback(addSelf)
        classdict['__init__'] = newInit
        classdict[instantiate] = _instantiate
        return super(DeferredSingleton, mcl).__new__(
            mcl, classname, bases, classdict)
