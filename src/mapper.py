__author__ = 'mebusw@163.com'


class Mapper(object):
    @staticmethod
    def Attr(by):
        def f(instance, domain_label):
            print 'ATTR: %s ==> %s' % (by, domain_label)
            return getattr(instance, by)

        return f

    @staticmethod
    def Wrap(clz_vo, keys=[]):
        def f(instance, domain_label):
            print 'WRAP: %s ==> %s ^ %s ' % (keys, domain_label, clz_vo)
            vo = clz_vo()
            for key in keys:
                setattr(vo, key, getattr(instance, key))
            return vo

        return f

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
            for (label, func) in _mappings.iteritems():
                setattr(domain_obj, label, func(instance, label))
            return domain_obj

        setattr(clazz.clzModel, 'to_vo', to_vo)
