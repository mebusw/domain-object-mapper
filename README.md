Domain Object Mapper
====================

## What does it do?
Use DSL style to map object to defined domain object.

## Why use it?
E.g. in Django framework, the db.models classes is for both domain knowledge and database accessing (like DAO or Repository).
According to [Domain Driven Design](), it's better to seperate domain objects from DB models.

## Usage
Suppose you're using Django model named `UserModel`, which defined some fields:
```
    class UserModel
        name  <CharField>
        email <CharField>
        skype <CharField>
```

* Renaming Attributes
...And you designed a domain object `User` which is an entity with a field `nickname`:
```
    class User
        nickname <String>
```
* Wrapping Attributes
...By defining a mapper `UserMapper`, you could map from Django model to domain object:
```
    class UserMapper(Mapper):
        nickname = Mapper.Attr('name')
        contact = Mapper.Wrap(Contact, ['email', 'skype'])
        model = UserModel
        domain = User
```
...Then you'll get `User` which is composed of another value object `Contact`:
```
    class Contact:
        email <String>
        skype <String>

    class User:
        nickname <String>
        contact  <Contact>
```


* Unwrapping Attributes

* Filtering Attributes


## Thanks
* Inspired by [Ruby Object Mapper](http://rom-rb.org/guides/basics/mappers/)
