from student import Student
import json
import time


class StudentCMS(object):
    # 记录学生信息
    def __init__(self):
        self.student_info = []

    # 用于展示：提示界面
    @staticmethod
    def show_view():
        print('*' * 30)
        print("本学生管理系统V2.0可完成如下操作：")
        print("\t1.添加学生")
        print("\t2.修改学生")
        print("\t3.删除学生")
        print("\t4.查询某个学生信息")
        print("\t5.显示所有学生信息")
        print("\t6.保存信息")
        print("\t0.退出系统")
        print('*' * 30)

    # 定义函数 add_student(),表示 添加学生
    def add_student(self):
        name = input("请输入要添加的学生的 姓名：")
        age = input("请输入要添加的学生的 年龄：")
        gender = input("请输入要添加的学生的 性别：")
        tel = input("请输入要添加的学生的 手机号：")
        des = input("最后请输入要添加的学生的其他信息（爱好、兴趣等）：")
        student = Student(name, age, gender, tel, des)
        self.student_info.append(student)
        print(f"学生{student.name}的信息添加成功！", "\n")

    # 定义函数 update_student(),表示 修改学生
    def update_student(self):
        update_name = input("请输入要修改信息的学生姓名：")
        for student in self.student_info:
            if student.name == update_name:
                result = input("请输入要修改的内容（姓名、年龄、性别、电话、其他信息）：").strip()
                if result == "姓名":
                    student.name = input("请输入修改后的学生 姓名：").strip()
                    print("学生的姓名信息修改成功！\n")
                elif result == "年龄":
                    student.age = input("请输入修改后的学生 年龄：").strip()
                    print("学生的年龄信息修改成功！\n")
                elif result == "性别":
                    student.gender = input("请输入修改后的学生 性别：").strip()
                    print("学生的性别信息修改成功！\n")
                elif result == "电话":
                    student.tel = input("请输入修改后的学生 电话：").strip()
                    print("学生的电话信息修改成功！\n")
                elif result == "其他信息":
                    student.description = input("请输入修改后的学生 其他信息：").strip()
                    print("学生的其他信息修改成功！\n")
                else:
                    print("输入的信息不准确，请确认后重新输入！\n")
                break

        else:
            print("要修改的学生姓名不存在！\n")

    # 定义函数 del_student(),表示 删除学生
    def delete_student(self):
        del_name = input("请输入要删除的学生姓名：")
        for student in self.student_info:
            if student.name == del_name:
                self.student_info.remove(student)
                print(f"学生：{del_name} 的信息已成功删除！\n")
                break
        else:
            print("要删除的学生姓名不存在！\n")
        # self.student_info = [student for student in self.student_info if student.name != del_name] # 列表推导式

    # 定义函数 show_one_student(),表示 查询某个学生信息
    def show_one_student(self):
        show_name = input("请输入要查询的学生姓名：")
        for student in self.student_info:
            if student.name == show_name:
                print(student, "\n")
                break
        else:
            print("查询的学生姓名不存在，请添加后重试！\n")

    # 定义函数 show_all_student(),表示 显示所有学生信息
    def show_all_student(self):
        # 判断学生列表中是否有信息
        if len(self.student_info) > 0:
            # 通过for循环遍历所有学生类对象，并打印
            for student in self.student_info:
                print(student)
        else:
            print("当前学生信息为空，请添加后重试！")
        print()

    # 定义函数 save_student(),表示 保存学生信息
    def save_student(self):
        # 流程：[学生对象, 学生对象...] => [{学生信息}, {学生信息}...] => "[{学生信息}, {学生信息}...]" => 写到 student.txt 文件中
        try:
            with open('./student.txt', 'w', encoding='utf-8') as f:
                for student in self.student_info:
                    # 将字典格式转成JSON格式并写入
                    student_data = json.dumps(student.__dict__, ensure_ascii=False) + '\n'
                    f.write(student_data)
        except Exception as e:
            print(f"保存失败！异常为：{e}\n")
        else:
            print("学生信息保存成功！\n")

    # 定义函数 load_student(),表示 加载学生信息
    def load_student(self):
        try:
            with open('./student.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    # 跳过空行
                    if not line:
                        continue
                    # 将JSON字符串转回字典
                    student_dict = json.loads(line)
                    # student = Student(**student_dict)   # 字典解包，批量传值
                    student = Student(student_dict["name"], student_dict["age"], student_dict["gender"], student_dict["tel"], student_dict["description"])
                    self.student_info.append(student)
        except FileNotFoundError:
            # 文件不存在时的友好提示，不报错
            print("未找到学生信息文件student.txt，将创建新文件！")
            f = open('./student.txt', 'w', encoding='utf-8')
            f.close()
        else:
            if len(self.student_info) >0:
                print(f"成功加载{len(self.student_info)}条学生信息！\n")


    # 定义函数 start(),表示 程序开始执行
    def start(self):
        print('.' * 9, "Loading", '.' * 9)
        # 加载学生信息
        self.load_student()
        while True:
            # 休眠 1s
            time.sleep(1)
            StudentCMS.show_view()    # 静态方法调用方式2： 类名.方法名()    推荐
            # self.show_view()        # 静态方法调用方式1： 对象名.方法名()  可以但是并不推荐
            select_num = input("请输入要执行的操作对应的数字：").strip()
            #  添加学生
            if select_num == '1':
                self.add_student()
            # 修改学生
            elif select_num == '2':
                self.update_student()
            # 删除学生
            elif select_num == '3':
                self.delete_student()
            # 查询某个学生信息
            elif select_num == '4':
                self.show_one_student()
            # 显示所有学生信息
            elif select_num == '5':
                self.show_all_student()
            # 保存信息
            elif select_num == '6':
                self.save_student()
            elif select_num == '0':
                # 退出系统时，需要二次确认
                result = input("确认要退出系统吗？(Y/N):")
                if result.upper() == 'Y':
                    # 退出系统，信息自动保存
                    # self.save_student()
                    print("感谢您的使用，再见！")
                    break
                else:
                    print("取消退出\n")
            else:
                print("输入有误，新功能正在玩命开发中，请耐心等待.....\n")


# 在 main 函数中测试代码
if __name__ == '__main__':
    sms = StudentCMS()
    # print(sms.student_info)
    sms.start()
