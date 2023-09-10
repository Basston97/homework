class MyDataClass:
    class_variable = "I am a class variable"
    
    def __init__(self, value):
        self.value = value
    
    def instance_method(self):
        print(f"Instance method called with value: {self.value}")
    
    @staticmethod
    def static_method():
        print("This is a static method")
    
    @classmethod
    def class_method(cls):
        print(f"This is a class method accessing class variable: {cls.class_variable}")

data_instance = MyDataClass(42)
data_instance.instance_method()  
MyDataClass.static_method()       
MyDataClass.class_method()        

class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print("Creating class using MyMeta")
        attrs['meta_variable'] = "I am a meta variable"
        return super().__new__(cls, name, bases, attrs)

class MyCustomClass(metaclass=MyMeta):
    def method(self):
        print("Method of MyCustomClass")

custom_instance = MyCustomClass()
print(custom_instance.meta_variable)  