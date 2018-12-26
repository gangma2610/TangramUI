#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 10:14
# @Author  : Lynn
# @Site    : 
# @File    : interactiveview.py
# @Software: PyCharm
'''
图形视图。
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class InteractiveView(QGraphicsView):
    def __init__(self, parent = None):
        super(InteractiveView, self).__init__(parent)
        self.m_tanslateSpeed = 1.0
        self.m_bMouseTranslate = False # 平移标识
        self.m_tanslateButton = Qt.MouseButton() # 平移按钮
        self.m_lastMousePos = QPoint() # 鼠标最后按下的位置


    def mouseMoveEvent(self, event):
        if self.m_bMouseTranslate:
            mouseDelta = self.mapToScene(event.pos() - self.mapToScene(self.m_lastMousePos))
            self.translate(mouseDelta)
            self.m_lastMousePos = event.pos()

            self.mouseMoveEvent(event)


    def mousePressEvent(self, event):
        if event.button() == self.m_tanslateButton:
            point = self.mapToScene(event.pos())
            if (self.scene().itemAt(point, self.transform()) == None):
                self.m_bMouseTranslate = True
                self.m_lastMousePos = event.pos()

        self.mousePressEvent(event)



    def mouseReleaseEvent(self, event):
        if event.button() == self.m_tanslateButton:
            self.m_bMouseTranslate = False

        self.mouseReleaseEvent(event)


    def keyPressEvent(self, event):
        '''
        上/下/左/右键各个方向移动，空格/回车键旋转
        '''
        if event.key() == Qt.Key_Up:        # 上移
            self.translate(QPoint(0, -2))

        elif event.key() == Qt.Key_Down:    # 下移
            self.translate(QPoint(0, 2))

        elif event.key() == Qt.Key_Left:    # 左移
            self.translate(QPoint(-2, 0))

        elif event.key() == Qt.Key_Right:   # 右移
            self.translate(QPoint(2, 0))

        elif event.key() == Qt.Key_Space:   # 逆时针旋转
            self.rotate(-5)

        elif event.key() == Qt.Key_Enter:   # 顺时针旋转
            self.rotate(5)

        else:
            self.keyPressEvent(event)


    def setTranslateSpeed(self, speed):
        '''
        设置平移速度。
        '''
        if speed >= 0.0 and speed <= 2.0:
            self.m_tanslateSpeed = speed
        else:
            print('current speed: ', self.m_tanslateSpeed)
            print('InteractiveView::setTranslateSpeed: Speed should be in range [0.0, 2.0].')