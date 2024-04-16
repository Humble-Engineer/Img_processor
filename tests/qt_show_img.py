import sys
from pathlib import Path
import cv2

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    """
    主窗口类，用于显示图像。
    """
    def __init__(self):
            """
            初始化主窗口，创建图像显示标签并加载显示用户选择的图像。
            """
            super().__init__()  # 调用父类构造函数

            # 创建一个 QLabel 用于显示图像，并居中对齐
            self.image_label = QLabel(self)
            self.image_label.setAlignment(Qt.AlignCenter)

            # 弹出文件对话框，让用户选择图像
            initial_dir = "materials"  # 可以指定初始目录
            file_filter = "Image files (*.png *.jpg *.jpeg *.bmp)"  # 指定支持的文件类型
            selected_file, _ = QFileDialog.getOpenFileName(self, "选择图像", initial_dir, file_filter)

            # 如果用户选择了文件，则加载并显示图像
            if selected_file:
                image_path = Path(selected_file)
                self.display_image(image_path)

            # 调整窗口大小以适应图像大小
            self.resize(self.width, self.height)


    def display_image(self, image_path):
        """
        加载并显示图像。
        
        :param image_path: 图像文件路径
        """
        # 使用 OpenCV 读取图像
        img = cv2.imread(str(image_path))

        # 获取图像尺寸
        img_height, img_width, _ = img.shape

        # 设置窗口高度和宽度为图像的尺寸
        self.height = img_height
        self.width = img_width

        # 设置 QLabel 以固定大小显示图像
        self.image_label.setFixedSize(img_width, img_height)

        if img is not None:
            # 将图像从 BGR 转换为 RGB 格式以适应 Qt
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # 创建 QImage 并使用图像数据初始化
            qimg = QImage(img_rgb.data, img_rgb.shape[1], img_rgb.shape[0], QImage.Format_RGB888)

            # 从 QImage 创建 QPixmap
            pixmap = QPixmap.fromImage(qimg)

            # 将 QPixmap 设置为 QLabel 的内容
            self.image_label.setPixmap(pixmap)
        else:
            # 如果图像加载失败，打印错误信息
            print(f"Failed to load image from {image_path}")

            

if __name__ == "__main__":
    # 创建 QApplication 实例
    app = QApplication(sys.argv)

    # 创建主窗口并显示
    main_window = MainWindow()
    main_window.show()

    # 运行应用程序
    sys.exit(app.exec())