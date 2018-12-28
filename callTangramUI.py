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

from data import tangram_info, img_name_list

###################################################################################

class MyMainWidget(QWidget, Ui_tangramForm):
    def __init__(self, parent=None):
        super(MyMainWidget, self).__init__(parent)
        self.setupUi(self)

        # 下拉列表添加图片信息
        self.imgcboBox.addItems(
            img_name_list
        )
        self.imgcboBox.currentIndexChanged.connect(self.selectionchange) # 下拉列表添加事件处理
        # Radio Button 添加事件处理
        self.sourceImageRBtn.toggled.connect(lambda : self.btnstate(self.sourceImageRBtn))
        self.personalDesignRBtn.toggled.connect(lambda : self.btnstate(self.personalDesignRBtn))
        # push button 添加事件处理
        self.saveBtn.clicked.connect(self.btnSave_Clicked)
        # 默认显示 图像实例中的选中图像
        self._imgPix = QPixmap('./mould/' + self.imgcboBox.currentText())
        self._pixmap_item = QGraphicsPixmapItem(self._imgPix)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scene = QGraphicsScene()
        self.scene.addItem(self._pixmap_item)
        self.scene.setSceneRect(0, 0, 900, 600)
        # 添加场景
        self.graphicsView.setScene(self.scene)



    def btnSave_Clicked(self):
        '''
        单击保存按钮，保存场景中的图片。
        '''
        self.scene.clearSelection()
        self._imgPix = QPixmap(900, 600)
        self._imgPix.fill(Qt.white)

        painter = QPainter(self._imgPix)
        painter.setRenderHint(QPainter.Antialiasing)
        self.scene.render(painter)
        print('Saving image： res/e_image.jpg ...')
        self._imgPix.save('res/e_image.jpg')
        print('Saved.')


    def btnstate(self, btn):
        '''
        RadioButton发生变化时出发事件处理函数。
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

        else:
            # 切换到个人设计模块时，进行初始化
            self.imgcboBox.setEnabled(False)
            self.scene.clear()

            for item in tangram_info: # 绘画每个七巧板
                polygon=QPolygonF()
                for p in item['pos']:
                    polygon.append(p)

                pen = QPen()
                pen.setColor(QColor(item['color']))
                brush = QBrush(Qt.SolidPattern)
                brush.setColor(QColor(item['color']))
                self.scene.addPolygon(polygon, pen=pen, brush=brush)
                all_items = self.scene.items()
                for item in all_items:
                    item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)

            self.graphicsView.setScene(self.scene)


    def keyPressEvent(self, event):
        '''
         上/下/左/右键各个方向移动，空格/回车键旋转
        '''
        # itm = self.scene.focusItem()
        itms = self.scene.selectedItems()
        if len(itms) != 1:
            return;

        itm = itms[0]

        if event.key() == Qt.Key_W:  # 上移
            itm.setPos(itm.x(), itm.y() - 1)

        elif event.key() == Qt.Key_S:  # 下移
            itm.setPos(itm.x(), itm.y() + 1)


        elif event.key() == Qt.Key_A:  # 左移
            itm.setPos(itm.x() - 1, itm.y())

        elif event.key() == Qt.Key_D:  # 右移
            itm.setPos(itm.x() + 1, itm.y())

        elif event.key() == Qt.Key_E:  # 逆时针旋转
            pt = itm.boundingRect().center()
            itm.setTransformOriginPoint(pt.x(), pt.y())
            itm.setRotation(itm.rotation() - 5)

        elif event.key() == Qt.Key_R:  # 顺时针旋转
            pt = itm.boundingRect().center()
            itm.setTransformOriginPoint(pt.x(), pt.y())
            itm.setRotation(itm.rotation() + 5)

        else:
            pass


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