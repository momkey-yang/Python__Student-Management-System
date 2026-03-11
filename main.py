# 学生管理系统的主入口

# 导入 StudentCMS 这个类
from student_management_system import StudentCMS

if __name__ == '__main__':
    # 创建 StudentCMS() 的实例
    student_cms = StudentCMS()
    # 启动程序
    student_cms.start()