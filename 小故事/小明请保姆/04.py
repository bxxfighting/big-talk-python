'''
在实际生活中，我们分配了保洁员，但是不可能立即就打扫卫生
首先保洁员必须先赶到雇主的家才行
因此保洁员类增加新的方法go_to_work，用来表示赶到雇主家
同时保洁公司在分配保洁员后，也是调用go_to_work让保洁先过去
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
        self.clean(employer)

    def clean(self, employer):
        print(self.name, '正在打扫', employer.name, '的家')


if __name__ == '__main__':
    xiaoming = Employer('小明')
    xiaoming.call_cleaners(10)
