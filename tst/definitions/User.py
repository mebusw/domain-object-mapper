from mapper import Mapper


class UserModel(object):
    def __init__(self):
        super(UserModel, self).__init__()

####################

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


