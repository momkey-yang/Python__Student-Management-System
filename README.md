# Python 学生信息管理系统
独立开发的轻量级学生信息管理系统，基于面向对象设计，实现完整的增删改查和数据持久化功能。

## 功能列表
- ✅ 学生信息录入（学号/姓名/年龄/班级，支持输入校验）
- ✅ 信息修改（按学号精准修改）
- ✅ 信息删除（单个/批量删除）
- ✅ 多条件查询（姓名模糊查询）
- ✅ 数据保存到JSON文件，重启不丢失
- ✅ 异常处理（文件读写失败）

## 技术栈
- Python 3.8+
- 面向对象编程（OOP）：封装/继承
- 文件I/O：JSON格式数据持久化
- 异常处理：try-except捕获常见错误
- 模块化设计：源码按功能拆分（模型/逻辑分离）

## 快速开始
### 环境要求
- Python 3.8 及以上版本

### 运行步骤
1. 克隆仓库
   ```bash
   git clone https://github.com/你的用户名/python-student-management-system.git
   cd python-student-management-system
2. 运行主程序
   ```bash
python main.py
