# 定义学生类，初始化学生信息
class Student(object):
    def __init__(self, name, age, gender, tel, des):
        self.name = name
        self.age = age
        self.gender = gender
        self.tel = tel
        self.description = des

    def __str__(self):
        return f"学生姓名:{self.name}，年龄:{self.age}岁，性别:{self.gender}，电话是:{self.tel}，其他信息有:{self.description}"


# 测试代码
if __name__ == '__main__':
    print(Student("张三", 23, "男", 1383287890, "爱学习"))