import sys
import init_db
import selects
from PyQt6.QtWidgets import QPushButton, QMessageBox, QApplication, QVBoxLayout, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout
from PyQt6.QtWidgets import QLineEdit, QDialog
from PyQt6.QtGui import QIcon

class Entertext(QDialog):
    def __init__(self, content):
        super().__init__()
        self.text = ''
        self.setWindowTitle(f'请输入要查询的{content}')
        self.resize(320, 200)
        self.setWindowIcon(QIcon('./picture/logo.png'))
        self.init_ui()
    
    def init_ui(self):
        # 创建 QLineEdit 对象
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("在此输入...")

        # 创建确认按钮
        self.closeButton = QPushButton('确认', self)
        self.closeButton.clicked.connect(self.get_text)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.input_box)
        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(self.closeButton)
        layout.addLayout(bottomLayout)
        self.setLayout(layout)

    def get_text(self):
        self.text = self.input_box.text()
        self.accept()

    def get_entered_text(self):
        return self.text
        

class select_allTable(QWidget):
    def __init__(self, db, cursor, kind, name = ''):
        super().__init__()
        self.db = db
        self.cursor = cursor
        self.kind = kind
        self.name = name
        tablename = ['学生名单','课程']
        self.setWindowTitle(tablename[kind&1])
        self.resize(1024, 768)
        self.setWindowIcon(QIcon('./picture/logo.png'))
        self.init_ui()

    def init_ui(self):
        if (self.kind == 1):
            info = selects.select_classes_all(self.db, self.cursor)
        else:
            if (self.kind == 0):
                info = selects.select_students_all(self.db, self.cursor)
            else:
                info = selects.select_students_name(self.db, self.cursor, self.name)
        #print(info)
        # 创建表格
        try:
            if (self.kind != 1):
                leninfo = 4
                self.table = QTableWidget(len(info), leninfo)
                self.table.setHorizontalHeaderLabels(['学号','姓名','年龄','专业'])
            else:
                leninfo = 3
                self.table = QTableWidget(len(info), leninfo)
                self.table.setHorizontalHeaderLabels(['课程号','课程名','学分'])
        except Exception as e:
            print(f"发生错误：{e}")
            return
        
        # 填充表格数据
        for i in range(len(info)):
            for j in range(leninfo):
                    item = QTableWidgetItem(str(info[i][j]))
                    self.table.setItem(i, j, item)

        # 创建关闭按钮
        self.closeButton = QPushButton('Close', self)
        self.closeButton.clicked.connect(self.close)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(self.closeButton)
        layout.addLayout(bottomLayout)
        self.setLayout(layout)



class Main_Window(QWidget):
    def __init__(self, db, cursor):
        super().__init__()
        self.db = db
        self.cursor = cursor
        self.setWindowTitle('学籍管理系统')
        self.resize(1024, 768)
        self.setWindowIcon(QIcon('./picture/logo.png'))
        self.btn1 = QPushButton('查看学生名单', self)
        self.btn2 = QPushButton('查看全部课程', self)
        self.btn3 = QPushButton('按姓名查询', self)
        self.btn4 = QPushButton('按学号查询或修改', self)
        self.btn5 = QPushButton('新增学生', self)
        self.btn6 = QPushButton('新增课程', self)
        self.btn7 = QPushButton('新增奖项', self)
        self.btn8 = QPushButton('新增惩罚', self)
        self.btn9 = QPushButton('修改课程', self)
        self.btn10 = QPushButton('重置数据库', self)
        self.init_ui()

    def init_ui(self):
        self.btn1.resize(128, 64)
        self.btn1.move(106, 100)   #按钮的位置
        self.btn1.clicked.connect(self.check_all_students) #使用connect绑定事件，点击按钮时触发

        self.btn2.resize(128, 64)
        self.btn2.move(447, 100)   #按钮的位置
        self.btn2.clicked.connect(self.check_all_classes) #使用connect绑定事件，点击按钮时触发

        self.btn3.resize(128, 64)
        self.btn3.move(788, 100)   #按钮的位置
        self.btn3.clicked.connect(self.check_student_name) #使用connect绑定事件，点击按钮时触发

        self.btn4.resize(128, 64)
        self.btn4.move(106, 300)   #按钮的位置
        self.btn4.clicked.connect(self.check_student_info) #使用connect绑定事件，点击按钮时触发

        self.btn5.resize(128, 64)
        self.btn5.move(447, 300)   #按钮的位置
        self.btn5.clicked.connect(self.check_student_info) #使用connect绑定事件，点击按钮时触发

        self.btn6.resize(128, 64)
        self.btn6.move(788, 300)   #按钮的位置
        self.btn6.clicked.connect(self.check_student_info) #使用connect绑定事件，点击按钮时触发

        self.btn7.resize(128, 64)
        self.btn7.move(106, 500)   #按钮的位置
        self.btn7.clicked.connect(self.check_student_info) #使用connect绑定事件，点击按钮时触发

        self.btn8.resize(128, 64)
        self.btn8.move(447, 500)   #按钮的位置
        self.btn8.clicked.connect(self.check_student_info) #使用connect绑定事件，点击按钮时触发

        self.btn9.resize(128, 64)
        self.btn9.move(788, 500)   #按钮的位置
        self.btn9.clicked.connect(self.check_student_info) #使用connect绑定事件，点击按钮时触发

        self.btn10.resize(128, 32)
        self.btn10.move(800, 700)   #按钮的位置
        self.btn10.clicked.connect(self.reset_db) #使用connect绑定事件，点击按钮时触发

    def check_all_students(self):
        self.tableWindow = select_allTable(self.db, self.cursor, 0, '')
        self.tableWindow.show()
    
    def check_all_classes(self):
        self.tableWindow = select_allTable(self.db, self.cursor, 1, '')
        self.tableWindow.show()

    def check_student_name(self):
        getname = Entertext('姓名')
        if getname.exec():
            # 如果用户点击确认按钮，则获取输入的文本
            name = getname.get_entered_text()
            self.tableWindow = select_allTable(self.db, self.cursor, 2, name)
            self.tableWindow.show()
    
    def check_student_info(self):
        widget = QWidget()
        QMessageBox.information(widget, 'Pop message', 'OK') #触发的事件时弹出会话框

    def reset_db(self):
        init_db.init(self.db, self.cursor)
        widget = QWidget()
        QMessageBox.information(widget, '信息', '成功重置数据库') #触发的事件时弹出会话框



