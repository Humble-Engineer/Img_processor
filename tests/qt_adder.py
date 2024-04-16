import time

from PySide6.QtWidgets import QApplication, QMainWindow

# 编译UI文件：PySide6-uic demo.ui -o ui_demo.py
from demo_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        """
        主窗口类的构造函数。

        该函数在创建MainWindow类的实例时被调用，用于初始化用户界面和设置窗口的各种属性。
        
        参数:
        self - 表示MainWindow类的实例本身。

        返回值:
        无
        """
        super(MainWindow, self).__init__()  # 调用父类的构造函数
        self.ui = Ui_MainWindow()  # 实例化UI类
        self.ui.setupUi(self)  # 使用UI类的实例设置主窗口的界面

        self.band()  # 调用band方法进行进一步的初始化或设置

    def band(self):

        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)

        # 将cal_button的点击事件与handle方法连接
        self.ui.cal_button.clicked.connect(self.handle)

        pass

    def handle(self):
        """
        处理加法操作，并在用户界面显示进度和结果。
        
        无参数
        无返回值
        """

        # 初始化进度条和结果展示区域
        self.ui.progressBar.setValue(0)
        self.ui.result.setText("?")

        # 获取两个加数的值
        a = self.ui.number1.value()
        b = self.ui.number2.value()
        # 计算结果
        result = a + b

        # 获取延迟时间设置
        time_cost = self.ui.delay.value()

        # 模拟耗时操作，更新进度条
        for index, _ in enumerate(range(time_cost)):
            time.sleep(1)
            progress = index*100 // time_cost
            self.ui.progressBar.setValue(progress)

        # 完成操作，设置进度条为100%
        self.ui.progressBar.setValue(100)

        # 显示计算结果
        self.ui.result.setText(str(result))



if __name__ == '__main__':

    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出
