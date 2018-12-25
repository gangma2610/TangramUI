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

        # 下拉列表添加图片信息
        self.imgcboBox.addItems(
            [
                '1.jpg', '4.jpg', '5.jpg', 'b1.jpg', 'b2.jpg',  'cat01.jpg',
                'animal01.jpg', 'people01.jpg', 'people02.jpg'
             ]
        )
        self.imgcboBox.currentIndexChanged.connect(self.selectionchange) # 下拉列表添加事件处理
        # Radio Button 添加事件处理
        self.sourceImageRBtn.toggled.connect(lambda : self.btnstate(self.sourceImageRBtn))
        self.personalDesignRBtn.toggled.connect(lambda : self.btnstate(self.personalDesignRBtn))
        # 默认显示 图像实例中的选中图像
        self._imgPix = QPixmap('./mould/' + self.imgcboBox.currentText())
        self.imgLable.setPixmap(self._imgPix)

        self.lastPoint = QPoint()
        self.endPoint = QPoint()


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
            # 切换到个人设计模块时，进行初始化
            self.imgcboBox.setEnabled(False)
            self.imgLable.clear()
            self.initImageLable()



    def initImageLable(self):
        '''
        初始化图像展示区域。
        :return:
        '''
        # 设置大小为 900 * 600
        self._imgPix = QPixmap()
        self._imgPix = QPixmap(900, 600)
        self._imgPix.fill(Qt.white)
        self.imgLable.setPixmap(self._imgPix)

        self.lastPoint = QPoint()
        self.endPoint = QPoint()


    def paintEvent(self, event):
        '''
        绘画事件。
        :param event:
        :return:
        '''
        if self.personalDesignRBtn.isChecked() == False:
            return;

        x = self.lastPoint.x() - self.imgLable.x()
        y = self.lastPoint.y() - self.imgLable.y()
        w = self.endPoint.x() - self.imgLable.x() - x
        h = self.endPoint.y() - self.imgLable.y() - y

        pp = QPainter(self._imgPix)
        print(x, y, w, h)
        # pp.setBrush(QColor(0, 0, 0))
        pp.drawRect(x, y, w, h)

        # painter.drawPixmap(0, 0, self._imgPix)
        self.imgLable.setPixmap(self._imgPix)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint


    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()


    def mouseReleseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()


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