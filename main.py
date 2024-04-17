import sys
from pathlib import Path

import cv2
import numpy as np
import matplotlib.pyplot as plt

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

        # 默认预加载的图像
        self.image_path = "materials\cartoon.png"
        self.origin_img = cv2.imread(self.image_path)
        # 获取图像的维度信息
        self.height, self.width, self.channels = self.origin_img.shape
        # 存储到result_img准备进行处理
        self.result_img = self.origin_img
        # 显示预加载的图像
        self.display_origin_image()

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
        # 绑定重置图像按钮的点击事件
        self.ui.reset_button.clicked.connect(self.reset_image)

        # 绑定图像颜色空间转换按钮的点击事件
        self.ui.color_space_button.clicked.connect(self.change_color_space)
        # 绑定几何变换按钮的点击事件
        self.ui.geometric_button.clicked.connect(self.geometric_transform)
        # 绑定添加噪声按钮的点击事件
        self.ui.noise_button.clicked.connect(self.add_noise)
        # 绑定图像滤波按钮的点击事件
        self.ui.blur_button.clicked.connect(self.image_blur)
        # 绑定傅里叶变换按钮的点击事件
        self.ui.edge_button.clicked.connect(self.edge_detect)
        # 绑定图像直方图按钮的点击事件
        self.ui.draw_button.clicked.connect(self.darw_hist)

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
            # 将路径转换为Path对象
            self.image_path = Path(selected_file)
            # 使用 OpenCV 读取图像，并保存为属性
            self.origin_img = cv2.imread(str(self.image_path))
            # 获取图像的维度信息
            self.height, self.width, self.channels = self.origin_img.shape
            # 当前处理完成的图像与原始图像相同
            self.result_img = self.origin_img
            # 显示原始图像
            self.display_origin_image()

    def save_image(self):
        """
        保存当前处理完成后的图像。
        """
        # 获取当前显示的QPixmap
        current_pixmap = self.ui.result_img.pixmap()

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

    def reset_image(self):
        """
        重置图像，恢复到原始状态。
        """
        self.result_img = self.origin_img
        self.display_result_image()

    def display_origin_image(self):
        """
        显示原始图像
        """
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
            print(f"Failed to display origin image!")

    def display_result_image(self):
        """
        显示处理后的图像
        """
        if self.result_img is not None:

            # 将图像从 BGR 转换为 RGB 格式以适应 Qt
            img_rgb = cv2.cvtColor(self.result_img, cv2.COLOR_BGR2RGB)

            # 创建 QImage 并使用图像数据初始化
            qimg = QImage(img_rgb.data, img_rgb.shape[1], img_rgb.shape[0], QImage.Format_RGB888)

            # 从 QImage 创建原始 QPixmap
            original_pixmap = QPixmap.fromImage(qimg)

            # 获取 QLabel 的尺寸
            label_width = self.ui.result_img.width()
            label_height = self.ui.result_img.height()

            # 将 QPixmap 缩放到 QLabel 大小，保持原图长宽比
            scaled_pixmap = original_pixmap.scaled(label_width, label_height)

            # 将缩放后的 QPixmap 设置为 QLabel 的内容
            self.ui.result_img.setPixmap(scaled_pixmap)
        else:
            # 如果图像加载失败，打印错误信息
            print(f"Failed to display result image!")

    def change_color_space(self):
        """
        图像颜色空间转换
        """
        if (self.ui.color_space_Box.currentText() == "GRAY"):
            try:
                self.result_img = cv2.cvtColor(self.result_img, cv2.COLOR_BGR2GRAY)
            except:
                pass

        elif (self.ui.color_space_Box.currentText() == "HSV"):
            try:
                self.result_img = cv2.cvtColor(self.result_img, cv2.COLOR_BGR2HSV)
            except:
                pass

        elif (self.ui.color_space_Box.currentText() == "YCrCb"):
            try:
                self.result_img = cv2.cvtColor(self.result_img, cv2.COLOR_BGR2YCrCb)
            except:
                pass

        else :
            pass

        self.display_result_image()

    def geometric_transform(self):
        """
        图像几何变换
        """
        if (self.ui.geometric_Box.currentText() == "水平翻转"):
                self.result_img = cv2.flip(self.result_img, 1)
        
        elif (self.ui.geometric_Box.currentText() == "竖直翻转"):
                self.result_img = cv2.flip(self.result_img, 0)
        
        elif (self.ui.geometric_Box.currentText() == "顺时针旋转"):
                self.result_img = cv2.rotate(self.result_img, cv2.ROTATE_90_CLOCKWISE)

        elif (self.ui.geometric_Box.currentText() == "逆时针旋转"):
                self.result_img = cv2.rotate(self.result_img, cv2.ROTATE_90_COUNTERCLOCKWISE)

        else :
            pass
        self.display_result_image()

    def add_noise(self):
        """
        图像加噪
        """
        # 先复制一份原始图像
        temp_img = self.result_img.copy()

        if (self.ui.noise_Box.currentText() == "高斯噪声"):
            mean = 0  # 噪声均值
            variance = 500  # 噪声方差，调整以控制噪声强度

            noise = np.random.normal(mean, variance ** 0.5, temp_img.shape)
            noisy_img = np.clip(temp_img + noise, 0, 255).astype(np.uint8)

            self.result_img = noisy_img

        elif (self.ui.noise_Box.currentText() == "椒盐噪声"):

            probability = 0.01  # 调整椒盐噪声出现的概率以减弱噪声效果

            # 对于灰度图像
            if len(temp_img.shape) == 2:
                mask = np.random.randint(0, 2, size=temp_img.shape, dtype=np.uint8) * probability
                temp_img[mask == 1] = 0  # 将随机位置的像素设为黑色（椒）
                temp_img[mask == 0] = 255  # 将随机位置的像素设为白色（盐）

            # 对于彩色图像
            elif len(temp_img.shape) == 3:
                for channel in range(temp_img.shape[2]):
                    mask = np.random.randint(0, 2, size=temp_img.shape[:2], dtype=np.uint8) * probability
                    temp_img[:, :, channel][mask == 1] = 0  # 将随机位置的像素设为黑色（椒）
                    temp_img[:, :, channel][mask == 0] = 255  # 将随机位置的像素设为白色（盐）

            self.result_img = temp_img  # 更新处理后的图像

        else :
            pass

        self.display_result_image()

    def image_blur(self):
        """
        图像模糊
        """
        if (self.ui.blur_Box.currentText() == "均值滤波"):
            self.result_img = cv2.blur(self.result_img, (3, 3))
        
        elif (self.ui.blur_Box.currentText() == "中值滤波"):
            self.result_img = cv2.medianBlur(self.result_img, 3)
        
        elif (self.ui.blur_Box.currentText() == "高斯滤波"):
            self.result_img = cv2.GaussianBlur(self.result_img, (5, 5), 0.6)

        elif (self.ui.blur_Box.currentText() == "二维卷积"):
            kernel = np.ones((3, 3)) / 9
            self.result_img = cv2.filter2D(self.result_img, -1, kernel, borderType=cv2.BORDER_CONSTANT)

        else :
            pass

        self.display_result_image()

    def edge_detect(self):
        """
        图像边缘检测
        """
        if (self.ui.edge_Box.currentText() == "Laplacian"):
            # 使用Laplacian算子进行边缘检测
            laplacian_img = cv2.Laplacian(self.result_img, cv2.CV_64F)
            laplacian_img = np.uint8(np.absolute(laplacian_img) * 255 / np.max(laplacian_img))
            self.result_img = laplacian_img

        elif (self.ui.edge_Box.currentText() == "Sobel"):
            # 使用Sobel算子进行边缘检测
            sobel_x = cv2.Sobel(self.result_img, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(self.result_img, cv2.CV_64F, 0, 1, ksize=3)
            sobel_img = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
            sobel_img = np.uint8(sobel_img * 255 / np.max(sobel_img))
            self.result_img = sobel_img

        elif (self.ui.edge_Box.currentText() == "Canny"):
            # 使用Canny算子进行边缘检测
            blurred_img = cv2.GaussianBlur(self.result_img, (5, 5), 0.6)
            canny_img = cv2.Canny(blurred_img, 50, 150)
            self.result_img = canny_img

        else:
            pass

        self.display_result_image()

    def darw_hist(self):
        """
        绘制图像直方图
        """
        # 获取图像数据
        img = self.result_img.copy()

        # 检查图像是否为灰度图像
        if len(img.shape) == 3 and img.shape[2] == 3:  # 彩色图像
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转为灰度图像

        # 计算直方图
        hist, bins = np.histogram(img.flatten(), 256, [0, 256])

        # 绘制直方图
        plt.figure(figsize=(10, 6))
        plt.hist(img.flatten(), bins=bins, color='gray')
        plt.title('Image Histogram')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.xlim([0, 256])
        plt.xticks(np.arange(0, 257, 32))
        plt.yticks(np.arange(0, hist.max() + 1, hist.max() // 10))

        # 显示图形
        plt.show()


if __name__ == "__main__":
    # 创建 QApplication 实例
    app = QApplication(sys.argv)

    # 创建主窗口并显示
    main_window = MainWindow()
    main_window.show()

    # 运行应用程序
    sys.exit(app.exec())