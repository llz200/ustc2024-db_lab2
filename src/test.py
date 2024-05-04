import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit Example')
        self.setGeometry(100, 100, 400, 200)

        # 创建 QLineEdit 对象
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("Enter text here...")
        
        # 创建布局并添加 QLineEdit
        layout = QVBoxLayout()
        layout.addWidget(self.input_box)

        # 创建一个 QWidget 作为主窗口的容器
        container = QWidget()
        container.setLayout(layout)

        # 设置主窗口的布局
        self.setCentralWidget(container)

        # 连接信号到槽函数
        self.input_box.textChanged.connect(self.text_changed)

    def text_changed(self, text):
        print(f"Text changed to: {text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())