'''
之前我们把雇主和保洁员，分别定义了两个不相关的类
但是，我们仔细想想，其实他们都是人，其实有很多共性，就拿这个例子来说，他们都有名字
因此，我们先定义一个Person类，代表人，Person在实例化的时候，提供人的名字.
现在Person类有了，就需要使用类的一个功能，就是继承，Employer和Cleaner都是继承Person来的.
所以就默认拥有了Person的所有功能，在这里就是拥有了Person的__init__方法初始化名称的功能.
'''
class Person:
    '''
    基础类
    '''

    def __init__(self, name):
        self.name = name


class Employer(Person):
    '''
    雇主类
    '''

    def call_cleaners(self, count):
        print(self.name, '叫了', count, '个保洁')
        for i in range(count):
            cleaner = Cleaner(f'保洁员{i+1}号')
            cleaner.clean()


class Cleaner(Person):
    '''
    保洁员类
    '''

    def clean(self):
        print(self.name, '正在打扫卫生')


if __name__ == '__main__':
    xiaoming = Employer('小明')
    xiaoming.call_cleaners(10)
