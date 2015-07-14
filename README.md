Domain Object Mapper
====================

## What does it do?
Use DSL style to map object to defined domain object.

## Why use it?
E.g. in Django framework, the db.models classes is for both domain knowledge and database accessing (like DAO or Repository).
According to [Domain Driven Design](), it's better to seperate domain objects from DB models.

## Usage
Suppose you're using Django with a model named `UserModel`, which has defined fields:
```
    name <String>
    email <String>
    skype <String>
```

### Renaming Attributes
...And you designed domain object named `User` which is an entity with a field `nickname:
```
    class User
        self.nickname = 'Jacky'
        ...
```
### Wrapping Attributes
...And `User` is composed of another value object named `Contact`
```
    class Contact:
        self.email
        self.skype

    class User:
        self.nickname = 'Jacky'
        self.contact = Contact()

```
### Unwrapping Attributes

### Filtering Attributes


## Thanks
* Inspired by [Ruby Object Mapper](http://rom-rb.org/guides/basics/mappers/)
