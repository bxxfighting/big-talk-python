'''
实际生活中，小明其实不用自己去联系10个保洁人员，一般都是给保洁公司打电话说，给我叫10个保洁来干活
因此，我们就定义一个保洁公司类，保洁公司有一个功能就是下订单，雇主只要提供自己的信息和保洁数量即可
所以保洁公司类有一个方法clean_order，用来下订单，接收雇主信息及保洁数量两个参数
同时，保洁公司接收到订单后，还需要分配给对应数量的保洁人员，告诉他们去谁家干活.
因此保洁公司还有一个方法assign_cleaners，用来分配保洁
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
            cleaner.clean(employer)


class Cleaner(Person):
    '''
    保洁员类
    '''

    def clean(self, employer):
        print(self.name, '正在打扫', employer.name, '的家')


if __name__ == '__main__':
    xiaoming = Employer('小明')
    xiaoming.call_cleaners(10)
