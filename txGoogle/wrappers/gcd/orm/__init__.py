def isOrmEntity(entity):
    return isinstance(entity, OrmEntity)

from txGoogle.wrappers.gcd.orm.ormEntity import OrmEntity
from mappedProperty import MappedProperty
from mappedNestedEntityProperty import MappedNestedEntityProperty
from mappedKsKeyProperty import MappedKsKeyProperty
from mappedJsonStringProperty import MappedJsonStringProperty
