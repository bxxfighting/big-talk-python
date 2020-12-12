'''
在面向对象编程中，我们都试着将一个实体定义成一个类，不同类对应不同实体
比如，这里小明是雇佣主，那么我们定义雇主类；请保洁员，我们定义保洁员类
雇主有叫保洁的功能，而且可以叫多个保洁，
那么我们给雇主定义一个call_cleaner方法，并且接收保洁个数作为方法的参数.
保洁员有一个功能就是打扫卫生，那么给保洁员定义一个clean方法，表现打扫卫生.
'''
class Employer:

    def __init__(self, name):
        self.name = name

    def call_cleaners(self, count):
        print(self.name, '叫了', count, '个保洁')
        for i in range(count):
            cleaner = Cleaner(f'保洁员{i+1}号')
            cleaner.clean()


class Cleaner:

    def __init__(self, name):
        self.name = name

    def clean(self):
        print(self.name, '正在打扫卫生')


if __name__ == '__main__':
    xiaoming = Employer('小明')
    xiaoming.call_cleaners(10)
