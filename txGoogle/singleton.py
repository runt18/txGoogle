class Singleton(type):
    """
    Singleton pattern to be used as metaclass.
    for info see: http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):  # @NoSelf
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


if __name__ == "__main__":
    """
    Simple self test. The Dummy class is another way to create a singleton class and
    we test if the two can work together.
    """

    class Dummy(object):
        DUMVAR = "Hello Insign.it!"

        @classmethod
        def testje(cls):
            print(cls.DUMVAR)

    class K1(Dummy):
        __metaclass__ = Singleton

        def __init__(self):
            self.testje()

    class K2(object):
        __metaclass__ = Singleton

    k1 = K1()
    k11 = K1()  # should not run the __init__ method
    k2 = K2()

    print(Singleton._instances)  # or print(K2._instances) or K1... will print the same info
