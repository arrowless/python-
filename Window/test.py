import sys
import numpy as np
from PIL import Image

from PyQt5.QtGui import QImage, QPixmap, QIcon, QColor
from PyQt5.QtCore import pyqtSlot, QSize, Qt
from PyQt5.QtWidgets import QApplication, QTextBrowser, QWidget, QLabel, QPushButton, QFileDialog, QFrame


class Example(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # -----------------------------#
        #   界面显示相关内容
        # -----------------------------#
        self.initUI()

    def initUI(self):
        # -----------------------------#
        #   初始化标题，界面大小
        # -----------------------------#
        self.resize(900, 540)
        self.setWindowTitle('光学遥感图像目标检测地面测试系统')

        # -----------------------------#
        #   获取图片按钮
        # -----------------------------#
        self.btn_photo = QPushButton('获取图片', self)
        self.btn_photo.setToolTip('点击后从电脑中读取图片')
        # self.btn_photo.setIcon(QIcon("img/icon/Search.jpeg"))
        self.btn_photo.setIconSize(QSize(30, 30))
        self.btn_photo.resize(100, 40)
        self.btn_photo.move(10, 10)
        self.btn_photo.clicked.connect(self.openimage)

        # -----------------------------#
        #   写一段话
        #   放到10,500
        #   拉伸长度为200,30
        # -----------------------------#
        self.text_browser = QTextBrowser(self)
        self.text_browser.move(10, 500)
        self.text_browser.resize(200, 30)
        self.text_browser.setText("Happy New Day")
        self.text_browser.setStyleSheet("border:none;background-color:rgba(100,255,255,255)")

        # -----------------------------#
        #   写一段话
        #   放到10,60
        #   拉伸长度为200,30
        # -----------------------------#
        self.origin_text = QTextBrowser(self)
        self.origin_text.setTextColor(QColor(23, 32, 32))
        self.origin_text.move(10, 60)
        self.origin_text.resize(200, 30)
        self.origin_text.setText("Inputs:")
        self.origin_text.setStyleSheet("border:none;background-color:rgba(0,0,0,0)")

        # -----------------------------#
        #   写一段话
        #   放到10,60
        #   拉伸长度为200,30
        # -----------------------------#
        self.output_text = QTextBrowser(self)
        self.output_text.move(480, 60)
        self.output_text.resize(200, 30)
        self.output_text.setText("Outputs:")
        self.output_text.setStyleSheet("border:none;background-color:rgba(0,0,0,0)")

        # -----------------------------#
        #   搞个箭头好看点
        # -----------------------------#
        self.arrow_text = QTextBrowser(self)
        self.arrow_text.move(410, 275)
        self.arrow_text.resize(200, 50)
        self.arrow_text.setText("→")
        self.arrow_text.setStyleSheet("border:none;background-color:rgba(0,0,0,0);font-size:50px")

        # -----------------------------#
        #   设置显示的图片
        # -----------------------------#
        self.label_h = 384
        self.label_w = 384
        self.label_show_input = QLabel(self)
        self.label_show_input.move(10, 100)
        self.label_show_input.setFixedSize(self.label_w, self.label_h)
        self.label_show_input.setText("Inputs!")
        self.label_show_input.setStyleSheet("QLabel{background:white;}")
        self.label_show_input.setObjectName("Inputs")

        # -----------------------------#
        #   设置显示的图片
        # -----------------------------#
        self.label_h = 384
        self.label_w = 384
        self.label_show_camera = QLabel(self)
        self.label_show_camera.move(480, 100)
        self.label_show_camera.setFixedSize(self.label_w, self.label_h)
        self.label_show_camera.setText("Outputs!")
        self.label_show_camera.setStyleSheet("QLabel{background:white;}")
        self.label_show_camera.setObjectName("Outputs")

        self.show()

    # -----------------------------#
    #   打开图片模式
    # -----------------------------#
    @pyqtSlot()
    def openimage(self):
        imgName, _ = QFileDialog.getOpenFileName(self, "打开图片", "", "Images (*.jpg, *.png);;All Files(*)")
        if len(imgName) == 0:
            return
        show = Image.open(imgName).convert("RGB")
        show = show.resize([self.label_w, self.label_h])

        showImage = QImage(np.array(show), np.shape(show)[1], np.shape(show)[0], QImage.Format_RGB888)
        self.label_show_input.setPixmap(QPixmap.fromImage(showImage))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
