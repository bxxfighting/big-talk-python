'''
实际生活中，保洁员赶往雇主家、打扫卫生肯定需要花费时间的
因此我们这里使用sleep来等待一段时间，代表花费的时间
sleep接收的参数是秒数
sleep(2)代表等待2秒
使用sleep方法需要先导入
from time import sleep
'''
from time import sleep


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
        clean_company = CleanCompany('爱干净')
        print(self.name, '叫了', clean_company.name, '公司的', count, '个保洁')
        clean_company.clean_order(self, 10)


class CleanCompany:
    '''
    保洁公司
    '''

    def __init__(self, name):
        self.name = name

    def clean_order(self, employer, count):
        '''
        保洁订单
        '''
        self.assign_cleaners(employer, count)

    def assign_cleaners(self, employer, count):
        '''
        分配保洁
        '''
        for i in range(count):
            cleaner = Cleaner(f'保洁员{i+1}号')
            cleaner.go_to_work(employer)


class Cleaner(Person):
    '''
    保洁员类
    '''

    def go_to_work(self, employer):
        print(self.name, '正在前往', employer.name, '的家')
        sleep(2)
        print(self.name, '正在前往', employer.name, '的家')
        self.clean(employer)

    def clean(self, employer):
        print(self.name, '正在打扫', employer.name, '的家')
        sleep(2)
        print(self.name, '打扫完成', employer.name, '的家')


if __name__ == '__main__':
    xiaoming = Employer('小明')
    xiaoming.call_cleaners(10)
