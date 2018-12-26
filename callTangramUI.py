#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 14:58
# @Author  : Lynn
# @Site    : 
# @File    : callTangramUI.py
# @Software: PyCharm
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from TangramUI import Ui_tangramForm
from PyQt5.QtCore import *

from data import tangram_info
from interactiveview import InteractiveView
###################################################################################

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
        self._pixmap_item = QGraphicsPixmapItem(self._imgPix)
        self.scene = QGraphicsScene()
        self.scene.addItem(self._pixmap_item)
        self.graphicsView.setScene(self.scene)

        self.tangram_items = [ [] for i in range(7) ]




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
            # 删除旧图片
            self.scene.clear()
            self._imgPix = QPixmap('./mould/' + self.imgcboBox.currentText())
            self._pixmap_item = QGraphicsPixmapItem(self._imgPix)
            # 添加新图片
            self.scene.addItem(self._pixmap_item)
            self.graphicsView.setScene(self.scene)
            # self.imgLable.setPixmap(self._imgPix)
            # self.imgcboBox.setVisible(True)
        else:
            # 切换到个人设计模块时，进行初始化
            self.imgcboBox.setEnabled(False)
            self.scene.clear()

            # self._pixmap_item = QGraphicsRectItem(50, 50, 100, 100)
            polygon = QPolygonF()
            for item in [QPoint(200, 0), QPoint(200, 100), QPoint(150, 150), QPoint(150, 50)]:
                polygon.append(item)
            self._pixmap_item = QGraphicsPolygonItem(polygon)

            self.scene.addItem(self._pixmap_item)
            # self.scene.addRect(QRect(10, 10, 100, 100))
            # self.scene.addItem()
            self.graphicsView.setScene(self.scene)


            # self.imgLable.clear()
            # self.initImageLable()



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
        self.draw_tangrams()


    def draw_tangrams(self):

        for i in [0, 1, 2, 3, 4, 5, 6]:
            item = tangram_info[i]
            self.drawing(item)

        # self.imgLable.setPixmap(self._imgPix)


    def drawing(self, item):
        pp = QPainter(self._imgPix)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(item['color']))
        pp.setBrush(brush)
        pp.setPen(QColor(item['color']))
        if item['shape'] == 'triangle':
            pp.drawPolygon(item['pos'][0], item['pos'][1], item['pos'][2])
        elif item['shape'] == 'square':
            pp.drawPolygon(item['pos'][0], item['pos'][1], item['pos'][2], item['pos'][3])
        else:
            pp.drawPolygon(item['pos'][0], item['pos'][1], item['pos'][2], item['pos'][3])


    def draw_rect_by_mouse(self):
        if self.personalDesignRBtn.isChecked() == False:
            return;

        # painter = QPainter(self)
        x = self.lastPoint.x() - self.imgLable.x()
        y = self.lastPoint.y() - self.imgLable.y()
        w = self.endPoint.x() - self.imgLable.x() - x
        h = self.endPoint.y() - self.imgLable.y() - y

        pp = QPainter(self._imgPix)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor('#f6ca29'))
        pp.setBrush(brush)
        pp.setPen(QColor('#f6ca29'))
        pp.drawRect(x, y, w, h)
        # self.imgLable.setPixmap(self._imgPix)


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
            # 进行重新绘制
            self.update()
            # self._isDrawing = False


    def selectionchange(self,i):
        '''
        下拉列表中的选项改变后触发事件处理函数。
        :param i:
        :return:
        '''
        self._imgPix = QPixmap('./mould/' + self.imgcboBox.currentText())
        self._pixmap_item = QGraphicsPixmapItem(self._imgPix)
        self.scene.addItem(self._pixmap_item)
        self.graphicsView.setScene(self.scene)
        # self.imgLable.sepp.drawPolygon(item['pos'][0], item['pos'][1], item['pos'][2], item['pos'][3])tPixmap(self._imgPix)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyMainWidget()
    myWidget.show()
    sys.exit(app.exec_())