#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 17:06
# @Author  : Lynn
# @Site    : 
# @File    : customItem.py
# @Software: PyCharm
'''
自定义七巧板控件。
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CustomItem(QObject, QGraphicsItem):
    m_isPressed = False
    m_lastMousePos = QPoint()
    m_translateSpeed = 1.0

    def __init__(self, polygon, parent=None, scene=None):
        super(CustomItem, self).__init__(polygon,parent, scene)

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'):
        if event.button() == Qt.LeftButton:
            point = self.mapToScene(event.pos())
            if(self.contains(event.pos())):
                self.m_isPressed = True

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent'):
        if self.m_isPressed:
            if self.contains(event.pos()):
                mouseDelta = self.mapToScene(event.pos() - self.mapToScene(self.m_lastMousePos))
                # self.translate(mouseDelta)
                self.m_lastMousePos = event.pos()

                self.mouseMoveEvent(event)


    def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent'):
        if event.button() == Qt.LeftButton:
            self.m_isPressed = False
            self.update()
            # if self.contains(event.pos()):
            #     self.emit clicked()


