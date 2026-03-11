# 学生管理系统 V1.0
一个基于 Python 开发的轻量级学生信息管理小程序，支持学生信息的添加、修改、删除、查询、保存/加载等核心功能。

## 项目介绍
### 功能清单
- ✅ 添加学生信息（姓名、年龄、性别、手机号、其他兴趣/爱好信息）
- ✅ 修改指定学生的信息（姓名/年龄/性别/电话/其他信息）
- ✅ 删除指定学生信息
- ✅ 单学生信息查询 / 全量学生信息展示
- ✅ 本地文件持久化（JSON 格式保存到 `student.txt`）
- ✅ 程序启动自动加载本地已保存的学生信息

### 技术栈
- 编程语言：Python 3.x
- 核心技术：面向对象编程（OOP）、文件 I/O、JSON 数据序列化
- 依赖：无第三方依赖，纯 Python 内置库实现

## 快速开始
### 运行步骤
1. 克隆本仓库到本地
   ```bash
   git clone https://github.com/momkey-yang/Python__Student-Management-System.git
   cd Python__Student-Management-System

2. 运行程序
   ```bash
   python main.py

3. 按照终端提示输入数字执行对应操作

   <img width="317" height="307" alt="image" src="https://github.com/user-attachments/assets/75df1951-369c-49b9-a948-5546ff5d3a65" />

## 注意事项
1. 学生信息会保存到项目根目录的 student.txt 文件中，删除该文件会清空所有本地存储的信息；
2. 程序启动时会自动加载 student.txt，若文件不存在会自动创建；
3. 所有输入操作均在终端完成，暂不支持图形化界面

## 后续优化
1. 增加学号字段，保证学生信息的唯一性；
2. 实现按年龄 / 性别等条件筛选查询；
3. 增加数据校验（如手机号格式、年龄为数字等）；
4. 拓展为图形化界面（Tkinter/PyQt）；
5. 接入数据库MySQL 替代本地文本文件存储；


