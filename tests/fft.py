import cv2
import numpy as np
import matplotlib.pyplot as plt

def perform_fft_and_display(image, crop_size=None):
    """
    使用OpenCV对给定的图像进行傅里叶变换（快速傅里叶变换），并使用matplotlib显示频谱图像。
    可选地，可以指定裁剪大小来放大显示幅度谱的中间部分。

    参数:
        image (numpy.ndarray): 输入图像，应为二维灰度图像或三维彩色图像（BGR顺序）
        crop_size (tuple, optional): 裁剪区域的大小，格式为 (height, width)，默认为 None（不裁剪）
    """

    # 确保图像为浮点类型，便于进行数学运算
    image_float = image.astype(np.float32)

    # 将图像扩展为偶数尺寸，以避免边缘效应
    height, width = image_float.shape[:2]
    pad_height = (height % 2) * (height // 2)
    pad_width = (width % 2) * (width // 2)
    padded_image = np.pad(image_float, ((0, pad_height), (0, pad_width)), mode='constant')

    # 进行离散傅里叶变换（DFT），得到复数形式的频谱
    dft_img = cv2.dft(padded_image, flags=cv2.DFT_COMPLEX_OUTPUT)

    # 提取实部和虚部，以便分别显示
    real_part = np.abs(dft_img[:, :, 0])
    imaginary_part = np.abs(dft_img[:, :, 1])

    # 仅显示幅度谱（通常更常用）
    amplitude_spectrum = np.sqrt(real_part ** 2 + imaginary_part ** 2)
    amplitude_spectrum_shifted = np.fft.fftshift(amplitude_spectrum)

    if crop_size is not None:
        crop_height, crop_width = crop_size
        crop_center = (amplitude_spectrum_shifted.shape[0] // 2, amplitude_spectrum_shifted.shape[1] // 2)  # 中心点坐标

        x_min, x_max = crop_center[1] - crop_width // 2, crop_center[1] + crop_width // 2
        y_min, y_max = crop_center[0] - crop_height // 2, crop_center[0] + crop_height // 2

        cropped_spectrum = amplitude_spectrum_shifted[y_min:y_max, x_min:x_max]

        plt.imshow(cropped_spectrum, cmap='viridis', vmin=0, vmax=np.max(amplitude_spectrum_shifted),
                  extent=(x_min, x_max, y_min, y_max))  # 保持原始坐标范围
    else:
        plt.imshow(amplitude_spectrum_shifted, cmap='viridis', vmin=0, vmax=np.max(amplitude_spectrum_shifted))

    plt.title('Amplitude Spectrum')
    plt.colorbar()
    plt.show()

    # 返回傅里叶变换后的频谱图像
    return dft_img


# 示例：加载一幅图像并进行傅里叶变换及显示，同时放大显示幅度谱的中间部分
input_image = cv2.imread('materials\cells_big_gray.png', cv2.IMREAD_GRAYSCALE)
crop_size = (32, 32)  # 示例：设定裁剪大小为 (512, 512)，可以根据需要调整
perform_fft_and_display(input_image, crop_size=crop_size)