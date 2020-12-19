'''
之前总是一个保洁公司提供服务，这样容易出现垄断
由于保洁的需求增多了，所以涌现出一大批保洁公司，用户有了更多的选择了
这里主要是使用随机数操作
'''
import os
import xlsxwriter
from random import randint
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


class CleanerList:
    '''
    保洁清单
    '''

    def __init__(self, clean_company):
        self.clean_company = clean_company
        self.filename = f'{clean_company.name}.data'
        self.load_cleaners()

    def save_cleaners(self):
        with open(self.filename, 'w') as fp:
            for cleaner in self.clean_company.cleaners.values():
                fp.write('name:{}|no:{}'.format(cleaner.name, cleaner.no))
                fp.write('\n')

    def load_cleaners(self):
        if not os.path.exists(self.filename):
            self.clean_company.cleaners = {}
        else:
            with open(self.filename, 'r') as fp:
                lines = fp.readlines()
                if lines:
                    for line in lines:
                        name, no = line.split('|')
                        name = name.split(':')[1]
                        no = int(no.split(':')[1])
                        self.clean_company.cleaners[no] = Cleaner(no, name, '空闲')
                else:
                    self.clean_company.cleaners = {}


class CleanCompany:
    '''
    保洁公司
    '''
    cleaners = {}
    no_seed = 0

    def __init__(self, name):
        self.name = name
        self.cleaner_list = CleanerList(self)

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
        self.cleaner_list.save_cleaners()

    def delete_cleaner(self, no):
        if no not in self.cleaners.keys():
            print('此编号不存在')
            return
        if self.cleaners[no].status != '空闲':
            print('此保洁正在干活，不能解雇')
            return
        cleaner = self.cleaners.pop(no)
        print('已经解雇{}'.format(cleaner.name))
        self.cleaner_list.save_cleaners()

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

    def export_cleaner_to_excel(self):
        '''
        导出保洁信息到excel中
        '''
        workbook = xlsxwriter.Workbook('{}.xlsx'.format(self.name))
        worksheet = workbook.add_worksheet()
        row = 0
        col = 0
        for cleaner in self.cleaners.values():
            worksheet.write(row, col, cleaner.no)
            worksheet.write(row, col+1, cleaner.name)
            row += 1
        workbook.close()


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
    employer_list = []
    xiaoming = Employer('小明')
    employer_list.append(xiaoming)
    xiaohong = Employer('小红')
    employer_list.append(xiaohong)
    xiaogou = Employer('小狗')
    employer_list.append(xiaogou)
    xiaohua = Employer('小花')
    employer_list.append(xiaohua)
    xiaoju = Employer('小菊')
    employer_list.append(xiaoju)

    clean_companys = []
    # 实例化一个清洁公司爱干净
    aiganjing = CleanCompany('爱干净')
    if not aiganjing.cleaners:
        # 清洁公司招收80个员工
        for i in range(80):
            aiganjing.add_cleaner('张{}'.format(i+1))
    clean_companys.append(aiganjing)

    # 实例化一个清洁公司爱整洁
    aizhengjie = CleanCompany('爱整洁')
    if not aizhengjie.cleaners:
        # 清洁公司招收50个员工
        for i in range(50):
            aizhengjie.add_cleaner('王{}'.format(i+1))
    clean_companys.append(aizhengjie)

    # 实例化一个清洁公司爱清洁
    aiqingjie = CleanCompany('爱清洁')
    if not aiqingjie.cleaners:
        # 清洁公司招收30个员工
        for i in range(30):
            aiqingjie.add_cleaner('李{}'.format(i+1))
    clean_companys.append(aiqingjie)

    # 现在有三家保洁公司了，大家可以有了更多选择
    for employer in employer_list:
        employer.call_cleaners(clean_companys[randint(0, len(clean_companys)-1)], randint(1, 50))

    sleep(5)
    # 现在想导出保洁的信息到excel中，老板要看一下
    for company in clean_companys:
        print(company.name)
        company.delete_cleaner(list(company.cleaners.keys())[0])
        company.export_cleaner_to_excel()
