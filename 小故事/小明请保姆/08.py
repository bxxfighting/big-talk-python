'''
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

    def call_cleaners(self, clean_company, count):
        print(self.name, '叫了', clean_company.name, '公司的', count, '个保洁')
        clean_company.clean_order(self, count)


class CleanCompany:
    '''
    保洁公司
    '''
    cleaners = {}
    no_seed = 0

    def __init__(self, name):
        self.name = name

    def _gen_no(self):
        self.no_seed += 1
        return self.no_seed

    def add_cleaner(self, name):
        no = self._gen_no()
        data = {
            'no': no,
            'name': name,
            'status': '空闲',
        }
        cleaner = Cleaner(**data)
        self.cleaners[no] = cleaner
        print('{}成功入职'.format(name))

    def delete_cleaner(self, no):
        if no not in self.cleaners.keys():
            print('此编号不存在')
            return
        if self.cleaners[no].status != '空闲':
            print('此保洁正在干活，不能解雇')
            return
        cleaner = self.cleaners.pop(no)
        print('已经解雇{}'.format(cleaner.name))

    def clean_order(self, employer, count):
        '''
        保洁订单
        '''
        result, cleaners = self.select_cleaners(count)
        if result == False:
            return
        for cleaner in cleaners:
            t = Thread(target=self.assign_task, args=(cleaner, employer))
            t.start()

    def select_cleaners(self, count):
        '''
        选择保洁
        '''
        free_cleaners = [cleaner for cleaner in self.cleaners.values() if cleaner.status == '空闲']
        if len(free_cleaners) < count:
            print('保洁员不足，请重新选择数量')
            return False, []
        cleaners = []
        for i in range(count):
            cleaner = free_cleaners[i]
            # 被选择了，状态就设置成工作中
            cleaner.status = '工作中'
            cleaners.append(cleaner)
        return True, cleaners

    def assign_task(self, cleaner, employer):
        '''
        分配任务
        '''
        cleaner.go_to_work(employer)


class Cleaner(Person):
    '''
    保洁员类
    '''

    def __init__(self, no, name, status):
        self.no = no
        self.name = name
        self.status = status

    def go_to_work(self, employer):
        print(self.name, '正在前往', employer.name, '的家')
        sleep(2)
        print(self.name, '已经到达', employer.name, '的家')
        self.clean(employer)

    def clean(self, employer):
        print(self.name, '正在打扫', employer.name, '的家')
        sleep(2)
        print(self.name, '打扫完成', employer.name, '的家')
        # 干完活了，就再次成为空闲状态
        self.status = '空闲'


if __name__ == '__main__':
    # 实例化几个雇主
    xiaoming = Employer('小明')
    xiaohong = Employer('小红')
    xiaogou = Employer('小狗')
    xiaohua = Employer('小花')
    xiaoju = Employer('小菊')

    # 实例化一个清洁公司爱干净
    clean_company = CleanCompany('爱干净')
    # 清洁公司招收100个员工
    for i in range(100):
        clean_company.add_cleaner('张{}'.format(i))

    # 大家都去爱干净公司叫保洁
    xiaoming.call_cleaners(clean_company, 10)
    xiaohong.call_cleaners(clean_company, 20)
    xiaogou.call_cleaners(clean_company, 30)
    xiaohua.call_cleaners(clean_company, 40)
    # 小花在叫的时候，爱干净公司已经不足10个空闲的保洁了，所以不成功
    xiaoju.call_cleaners(clean_company, 10)
    sleep(10)
    # 等待10秒后再叫，现在有的保洁已经完成了工作，所以就可以成功叫到保洁
    xiaoju.call_cleaners(clean_company, 10)
