'''
之前的示例我们发现一个问题，保洁员总是依次去雇主家，顺序一直是不变的
这是因为我们的程序在一个线程中是顺序执行的，通过for循环，先调用了谁，谁就先执行
执行完了，下面的才会执行
但是实际生活中，保洁员肯定是同时赶往雇主家的，所以我们需要使用多线程来完成
'''
from time import sleep
from threading import Thread


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
        cleaners = self.select_cleaners(count)
        for cleaner in cleaners:
            t = Thread(target=self.assign_task, args=(cleaner, employer))
            t.start()

    def select_cleaners(self, count):
        '''
        选择保洁
        '''
        cleaners = []
        for i in range(count):
            cleaner = Cleaner(f'保洁员{i+1}号')
            cleaners.append(cleaner)
        return cleaners

    def assign_task(self, cleaner, employer):
        '''
        分配任务
        '''
        cleaner.go_to_work(employer)


class Cleaner(Person):
    '''
    保洁员类
    '''

    def go_to_work(self, employer):
        print(self.name, '正在前往', employer.name, '的家')
        sleep(2)
        print(self.name, '已经到达', employer.name, '的家')
        self.clean(employer)

    def clean(self, employer):
        print(self.name, '正在打扫', employer.name, '的家')
        sleep(2)
        print(self.name, '打扫完成', employer.name, '的家')


if __name__ == '__main__':
    xiaoming = Employer('小明')
    xiaoming.call_cleaners(10)
