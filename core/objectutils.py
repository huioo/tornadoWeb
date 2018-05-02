# -*- coding: utf-8 -*-

class ObjectDict(dict):
    """Makes a dictionary behave like an object, with attribute-style access.
    """
    
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value
           

class DBRecord(ObjectDict):
    pass

if __name__ == '__main__':
    person=DBRecord()
    person.age=20
    person['age']='30'
    
    man={'city':'beijing'}
    person.update(man)
    
    print person