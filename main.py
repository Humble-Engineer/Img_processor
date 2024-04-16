import sys
from pathlib import Path
import cv2

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap, QImage

# 编译UI文件：PySide6-uic demo.ui -o ui_demo.py
from MainWindow_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    """
    主窗口类，用于显示图像。
    """
    def __init__(self):
        """
        初始化主窗口，创建图像显示标签并加载显示用户选择的图像。
        """
        super().__init__()  # 调用父类构造函数

        self.ui = Ui_MainWindow()  # 实例化UI类
        self.ui.setupUi(self)  # 使用UI类的实例设置主窗口的界面

        self.band()  # 调用band方法进行进一步的初始化或设置

    def band(self):
        """
        绑定按钮或菜单项的点击事件到相应的函数。
        """
        # self.ui.___MENU___.triggered.connect(___FUNCTION___)
        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)

        # 绑定加载图像按钮的点击事件
        self.ui.load_button.clicked.connect(self.load_image)
        # 绑定保存图像按钮的点击事件
        self.ui.save_button.clicked.connect(self.save_image)
        # 绑定灰度化按钮的点击事件
        self.ui.rgb2gray_button.clicked.connect(self.RGB2GRAY)
        # 绑定HSV按钮的点击事件
        self.ui.rgb2hsv_button.clicked.connect(self.RGB2HSV)

    def load_image(self):
        """
        加载并显示原始图像。
        """
        # 弹出文件对话框，让用户选择图像
        initial_dir = "materials"  # 可以指定初始目录
        file_filter = "Image files (*.png *.jpg *.jpeg *.bmp)"  # 指定支持的文件类型
        selected_file, _ = QFileDialog.getOpenFileName(self, "选择图像", initial_dir, file_filter)

        # 如果用户选择了文件，则加载并显示图像
        if selected_file:
            image_path = Path(selected_file)
            self.display_origin_image(image_path)

    def save_image(self):
        """
        保存当前处理完成后的图像。
        """
        # 获取当前显示的QPixmap
        current_pixmap = self.ui.processed_img.pixmap()

        if current_pixmap.isNull():
            print("No image to save.")
            return

        # 弹出保存文件对话框，让用户选择保存位置和文件名
        save_dialog = QFileDialog(self, "保存图像")
        save_dialog.setDefaultSuffix("png")  # 默认文件扩展名
        save_dialog.setNameFilter("PNG Files (*.png)")
        if save_dialog.exec() != QFileDialog.Accepted:
            return

        save_path = save_dialog.selectedFiles()[0]

        # 将QPixmap保存为图像文件
        if not current_pixmap.save(save_path, "PNG"):
            print(f"Failed to save image to {save_path}")

    def display_origin_image(self, image_path):
        """
        显示原始图像
        """
        # 使用 OpenCV 读取图像，并保存为属性
        self.origin_img = cv2.imread(str(image_path))

        if self.origin_img is not None:
            # 将图像从 BGR 转换为 RGB 格式以适应 Qt
            img_rgb = cv2.cvtColor(self.origin_img, cv2.COLOR_BGR2RGB)

            # 创建 QImage 并使用图像数据初始化
            qimg = QImage(img_rgb.data, img_rgb.shape[1], img_rgb.shape[0], QImage.Format_RGB888)

            # 从 QImage 创建原始 QPixmap
            original_pixmap = QPixmap.fromImage(qimg)

            # 获取 QLabel 的尺寸
            label_width = self.ui.origin_img.width()
            label_height = self.ui.origin_img.height()

            # 将 QPixmap 缩放到 QLabel 大小，保持原图长宽比
            scaled_pixmap = original_pixmap.scaled(label_width, label_height)

            # 将缩放后的 QPixmap 设置为 QLabel 的内容
            self.ui.origin_img.setPixmap(scaled_pixmap)
        else:
            # 如果图像加载失败，打印错误信息
            print(f"Failed to load image from {image_path}")

    def display_processed_image(self):
        """
        显示处理后的图像
        """
        if self.processed_img is not None:
            # 将图像从 BGR 转换为 RGB 格式以适应 Qt
            img_rgb = cv2.cvtColor(self.processed_img, cv2.COLOR_BGR2RGB)

            # 创建 QImage 并使用图像数据初始化
            qimg = QImage(img_rgb.data, img_rgb.shape[1], img_rgb.shape[0], QImage.Format_RGB888)

            # 从 QImage 创建原始 QPixmap
            original_pixmap = QPixmap.fromImage(qimg)

            # 获取 QLabel 的尺寸
            label_width = self.ui.processed_img.width()
            label_height = self.ui.processed_img.height()

            # 将 QPixmap 缩放到 QLabel 大小，保持原图长宽比
            scaled_pixmap = original_pixmap.scaled(label_width, label_height)

            # 将缩放后的 QPixmap 设置为 QLabel 的内容
            self.ui.processed_img.setPixmap(scaled_pixmap)
        else:
            # 如果图像加载失败，打印错误信息
            print(f"Failed to show processed image")

    def RGB2GRAY(self):
        """
        将图像转换为灰度图像
        """
        # 使用 OpenCV 将图像转换为灰度图像，并保存为属性
        self.processed_img = cv2.cvtColor(self.origin_img, cv2.COLOR_BGR2GRAY)
        self.display_processed_image()

    def RGB2HSV(self):
        """
        将图像转换为HSV图像
        """
        # 使用 OpenCV 将图像转换为HSV图像，并保存为属性
        self.processed_img = cv2.cvtColor(self.origin_img, cv2.COLOR_BGR2HSV)
        self.display_processed_image()



if __name__ == "__main__":
    # 创建 QApplication 实例
    app = QApplication(sys.argv)

    # 创建主窗口并显示
    main_window = MainWindow()
    main_window.show()

    # 运行应用程序
    sys.exit(app.exec())