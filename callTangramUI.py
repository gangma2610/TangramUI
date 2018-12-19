#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 14:58
# @Author  : Lynn
# @Site    : 
# @File    : callTangramUI.py
# @Software: PyCharm
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import *
from TangramUI import Ui_tangramForm
from PyQt5.QtCore import  Qt, QPoint

class MyMainWidget(QWidget, Ui_tangramForm):
    def __init__(self, parent=None):
        super(MyMainWidget, self).__init__(parent)
        self.setupUi(self)

        # self.imgcboBox.addItem('1.jpg')
        # self.imgcboBox.addItem('4.jpg')
        self.imgcboBox.addItems(
            [
                '1.jpg', '4.jpg', '5.jpg', 'b1.jpg', 'b2.jpg',  'cat01.jpg',
                'animal01.jpg', 'people01.jpg', 'people02.jpg'
             ]
        )
        self.imgcboBox.currentIndexChanged.connect(self.selectionchange)
        self.sourceImageRBtn.toggled.connect(lambda : self.btnstate(self.sourceImageRBtn))
        self.personalDesignRBtn.toggled.connect(lambda : self.btnstate(self.personalDesignRBtn))
        # 默认显示 图像实例中的选中图像
        self._imgPix = QPixmap('./mould/' + self.imgcboBox.currentText())
        self.imgLable.setPixmap(self._imgPix)


    def btnstate(self, btn):
        '''
        RadioButton发生变化时出发事件处理函数。
        :param btn:
        :return:
        '''
        if (btn.objectName() == self.sourceImageRBtn.objectName() and btn.isChecked() == True) \
            or (btn.objectName() == self.personalDesignRBtn.objectName() and btn.isChecked() == False):
            self.imgcboBox.setEnabled(True)
            #显示当前选中的图像
            self._imgPix = QPixmap('./mould/' + self.imgcboBox.currentText())
            self.imgLable.setPixmap(self._imgPix)
            # self.imgcboBox.setVisible(True)
        else:
            self.imgcboBox.setEnabled(False)
            self.imgLable.clear()
            # self._imgPix = QPixmap('./mould/painting.jpg')
            # self.imgLable.setPixmap(self._imgPix)
            self._imgPix = QPixmap()
            self.lastPoint = QPoint()
            self.endPoint = QPoint()
            self.initImageLable()
            self.imgLable.setPixmap(self._imgPix)

    def initImageLable(self):
        '''
        初始化图像展示区域。
        :return:
        '''
        # 设置大小为 900 * 600
        self._imgPix = QPixmap(900, 600)
        self._imgPix.fill(Qt.white)


    def selectionchange(self,i):
        '''
        下拉列表中的选项改变后触发事件处理函数。
        :param i:
        :return:
        '''
        self._imgPix = QPixmap('./mould/' + self.imgcboBox.currentText())
        self.imgLable.setPixmap(self._imgPix)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyMainWidget()
    myWidget.show()
    sys.exit(app.exec_())