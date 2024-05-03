# 本文件供学习测试用
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
'''
#从QWidget类派生的桌面应用程序窗口类
class MyWindow(QWidget):  #QtWidgets模块：包含应用程序类、窗口类、控件类和组件类
	#构造函数
    def __init__(self): 
        super().__init__() # 调用基类的构造函数
        self.setWindowTitle('Hello World') # 设置标题
        self.setWindowIcon(QIcon('./picture/logo.png')) # 可以设置图标
        lab = QLabel('Hello World', self) # 实例化标签
        lab.resize(320,160) # 设置标签大小
        lab.setFont(QFont('Arial', 32, QFont.Weight.Bold)) # 设置字体字号
        lab.setAlignment(Qt.AlignmentFlag.AlignCenter) # 文本在标签内居中
        self.show() # 显示窗口

if __name__ == '__main__':
    app = QApplication(sys.argv) # 创建应用程序，接收来自命令行的参数列表
    win = MyWindow() # 创建窗口,这里初始化的时候不需要QWidget入参
    sys.exit(app.exec()) # 应用程序主循环结束后，调用sys.exit()方法清理现场


'''
import pymysql
import init_db
import students

# 打开数据库连接
try:
    db = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, autocommit=False)
    #print('连接成功！')
except:
    print('something wrong!')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 切换database到lab2
sql = "USE lab2"
try:
    cursor.execute(sql)
except Exception as e:
    print(f"发生错误：{e}")

init_db.init(db, cursor)

with open('./picture/11z.png', 'rb') as image_file:
    image_blob = image_file.read()

students.add_student(db, cursor, "PB21111716", "牢", 22, "CS", image_blob)

# 关闭游标
cursor.close()

#关闭连接
db.close()
