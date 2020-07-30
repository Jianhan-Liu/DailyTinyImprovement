"""
  @Author       : liujianhan
  @Date         : 2020/7/30 上午10:45
  @Project      : DailyTinyImprovement
  @FileName     : student2.py
  @Description  : 避免重复(如student)的属性方法
"""
from functools import partial


def type_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f"{name} must be a {expected_type}.")
        setattr(self, storage_name, value)

    return prop


class Student:
    # name = type_property('name', str)
    # age = type_property('age', int)
    Integer = partial(type_property, expected_type=int)
    String = partial(type_property, expected_type=str)
    name = String('name')
    age = Integer('age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    st = Student('joey', 20)
    st.name = 13
    print(st.name)
    print(st.age)
