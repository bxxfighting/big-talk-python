'''
保洁公司在分配保洁时，实际工作情况应该是，先从保洁队伍里抽出10个人
然后把这10个人叫过来说，你们去谁谁家干活
因此，我们把原来的分配保洁，分成两步，先选择保洁，然后再分配他们任务
把原来的assign_cleaners方法删除，新增加两个方法
一个是select_cleaners，用来选择对应数量的保洁员，接收保洁数量，返回实例化好的保洁列表
一个是assign_task，用来给保洁指派任务
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
        cleaners = self.select_cleaners(employer, count)
        for cleaner in cleaners:
            self.assign_task(cleaner, employer)

    def select_cleaners(self, employer, count):
        '''
        分配保洁
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
        print(self.name, '正在前往', employer.name, '的家')
        self.clean(employer)

    def clean(self, employer):
        print(self.name, '正在打扫', employer.name, '的家')
        sleep(2)
        print(self.name, '打扫完成', employer.name, '的家')


if __name__ == '__main__':
    xiaoming = Employer('小明')
    xiaoming.call_cleaners(10)
