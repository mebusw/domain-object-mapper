__author__ = 'mebusw@163.com'


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

#
# if __name__ == '__main__':
#     # Auto Discover
#     UserMapper.prepare()
#
#     user_model = UserModel()
#     user = user_model.to_vo()
#     print user
