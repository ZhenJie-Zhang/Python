# 1.	類別繼承的練習-employee
# 有一小公司，其人事薪資的制度如下：
# 公司每個員工皆有姓名、性別、到職日、電話和住址等基本資料。
# 一般職員只有本薪；
# 一級主管則另有本薪、午餐津貼、交通津貼和職務加給；
# 二級主管則有本薪、午餐津貼和職務加給。
# 午餐津貼為1800元，交通津貼為2000元，
# 職務加給一級主管為5000元，二級主管為3000元。
# 每個員工皆有可能加班，加班費為本薪除以240乘以1.5倍再乘以加班時數。
# 在main()中產生六個實例分別為一級主管、二級主管及一般職員且分有加班及無加班兩種
# (資料直接透過建構子hard code在程式中)，並列印其基本資料及當月薪資。
LunchAllowance = 1800
TransportAllowance = 2000


def information(employee):
    print(employee)
    print('　　加班: {}(小時)'.format(employee.over_time_hour))
    print('　　底薪: ${:6d}'.format(employee.base_salary))
    print('　加班費: ${:6d}'.format(round(employee.over_time_pay(employee.over_time_hour))))
    if employee.__class__.__name__ != 'FullTimeEmp':
        print('職務加給: ${:6d}'.format(employee.DutyAllowance))
        print('午餐津貼: ${:6d}'.format(LunchAllowance))
    elif employee.__class__.__name__ != 'SecondarySupervisor':
        print('交通津貼: ${:6d}'.format(TransportAllowance))
    print('　本月薪: ${:6d}'.format(employee.salary()))


class Employee(object):
    def __init__(self, name, sex, date_arrival, address):
        self.name = name
        self.sex = sex
        self.date_arrival = date_arrival
        self.address = address

    def __str__(self):
        return '　姓名: {}\t　性別: {}\t 到職日: {}\t　地址: {}' \
            .format(self.name, self.sex, self.date_arrival, self.address)


class FullTimeEmp(Employee):
    def __init__(self, name, sex, date_arrival, address):
        super(FullTimeEmp, self).__init__(name, sex, date_arrival, address)
        self.over_time_hour = 0
        self.base_salary = 35000

    def over_time_pay(self, over_time_hour=0):
        self.over_time_hour = over_time_hour
        return self.base_salary / 240 * 1.5 * over_time_hour

    def salary(self):
        return self.base_salary + round(self.over_time_pay(self.over_time_hour))

    def __str__(self):
        return super(FullTimeEmp, self).__str__() + '\t職等: {}'.format(self.__class__.__name__)


class SecondarySupervisor(FullTimeEmp):
    def __init__(self, name, sex, date_arrival, address):
        super(SecondarySupervisor, self).__init__(name, sex, date_arrival, address)
        self.DutyAllowance = 3000

    def salary(self):
        return (self.base_salary + round(self.over_time_pay(self.over_time_hour))) + \
               LunchAllowance + self.DutyAllowance


class PrimarySupervisor(FullTimeEmp):
    def __init__(self, name, sex, date_arrival, address):
        super(PrimarySupervisor, self).__init__(name, sex, date_arrival, address)
        self.DutyAllowance = 5000

    def salary(self):
        return (self.base_salary + round(self.over_time_pay(self.over_time_hour))) + \
               LunchAllowance + self.DutyAllowance + TransportAllowance


def main():
    jay = FullTimeEmp("Jay", "Male", "2019-07-19", "Taipei")
    jay.over_time_hour = 40
    information(jay)
    print('==============================================')
    tina = SecondarySupervisor("Tina", "Female", "2020-01-15", "Tainan")
    tina.over_time_hour = 20
    information(tina)
    print('==============================================')
    sam = PrimarySupervisor("Sam", "Male", "2020-07-15", "American")
    sam.over_time_hour = 10
    information(sam)
    print('==============================================')


main()
