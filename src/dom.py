__author__ = 'mebusw@163.com'


class UserModel(object):
    def __init__(self):
        super(UserModel, self).__init__()
        self.name = 'Melody'
        self.email = 'a@b.cn'
        self.skype = 'mm'


class User(object):
    def __init__(self):
        self.nickname = 'Noname'
        self.contact = None

    def __str__(self):
        return '%s, %s' % (self.nickname, self.contact)


class Contact(object):
    def __init__(self):
        pass

    def __str__(self):
        return '%s, %s' % (self.email, self.skype)


class Mapper(object):
    @staticmethod
    def ATTR(by):
        def f(instance, domain_label):
            print 'ATTR: %s ==> %s' % (by, domain_label)
            return getattr(instance, by)

        return f

    @staticmethod
    def WRAP(clzVO, keys=[]):
        def f(instance, domain_label):
            print 'WRAP: %s ==> %s ^ %s ' % (keys, domain_label, clzVO)
            vo = clzVO()
            for key in keys:
                setattr(vo, key, getattr(instance, key))
            return vo

        return f


class UserMapper(Mapper):
    nickname = Mapper.ATTR('name')
    contact = Mapper.WRAP(Contact, ['email', 'skype'])
    model = UserModel
    domain = User

    @classmethod
    def prepare(clazz):
        _meta = vars(clazz)
        _fields = dict(
            (key, value) for (key, value) in _meta.iteritems() if not callable(value) and not key.startswith('__'))
        _mappings = dict((key, value) for (key, value) in _meta.iteritems() if
                         not key.startswith('__') and not key in ['domain', 'prepare', 'model'])
        # print _mappings
        clazz.clzDomain = _meta['domain']
        clazz.clzModel = _meta['model']

        def to_vo(instance):
            domain_obj = clazz.clzDomain()
            # domain_obj.name = getattr(instance, 'name')
            for (label, func) in _mappings.iteritems():
                setattr(domain_obj, label, func(instance, label))
            return domain_obj

        setattr(clazz.clzModel, 'to_vo', to_vo)


if __name__ == '__main__':
    # Auto Discover
    UserMapper.prepare()

    user_model = UserModel()
    user = user_model.to_vo()
    print user
