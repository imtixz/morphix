class Field:
    def __init__(self):
        pass

class IntegerField(Field):
    def __init__(self):
        pass

    def __str__(self):
        return 'INT'

class FloatField(Field):
    def __init__(self):
        pass

    def __str__(self):
        return 'FLOAT'

class VarCharField(Field):
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return "VARCHAR({})".format(self.length)
    
Column = {
    'IntegerField': IntegerField,
    'FloatField': FloatField,
    'VarCharField': VarCharField
}