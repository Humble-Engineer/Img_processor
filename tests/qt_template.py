from PySide6.QtWidgets import QApplication, QMainWindow

# 编译UI文件：PySide6-uic demo.ui -o ui_demo.py
from demo_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()  # UI类的实例化()
        self.ui.setupUi(self)

        self.band()

    def band(self):

        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)

        pass


if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出
