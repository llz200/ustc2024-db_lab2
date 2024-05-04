import sys
import pymysql
from PyQt6.QtWidgets import QPushButton, QMessageBox, QApplication, QWidget
import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)
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


    window = Window.Main_Window(db, cursor)
    window.show()
    sys.exit(app.exec())