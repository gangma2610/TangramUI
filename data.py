#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 18:59
# @Author  : Lynn
# @Site    : 
# @File    : data.py
# @Software: PyCharm
'''
七巧板基本信息。
'''
from PyQt5.QtCore import  Qt, QPoint, QPointF


tangram_info = [
    {
        'pos' : [QPoint(0, 0), QPoint(296, 0), QPoint(148, 148)], # 绿色
        'color' : '#fe9535',
        'click' : False,
        'drag' : False,
        'types' : 3,
        'shape' : 'triangle',
    },
    {
        'pos' : [QPoint(0, 0), QPoint(148, 148), QPoint(0, 296)], # 橙色
        'color' : '#3fa539',
        'click' : False,
        'drag' : False,
        'types' : 3,
        'shape' : 'triangle',

    },
    {
        'pos' : [QPoint(296, 0), QPoint(296, 148), QPoint(222, 222), QPoint(222, 74)], # 黄色
        'color' : '#f6f334',
        'click' : False,
        'drag' : False,
        'types' : 4,
        'shape' :'parallel',
    },
    {
        'pos' : [QPoint(222, 74), QPoint(222, 222), QPoint(148, 148)], # 粉色
        'color' : '#c31ca7',
        'click' : False,
        'drag' : False,
        'types' : 3,
        'shape' : 'triangle',
    },
    {
        'pos' : [QPoint(148, 148), QPoint(222, 222), QPoint(148, 296), QPoint(74, 222)], # 蓝色
        'color' : '#333dfe',
        'click' : False,
        'drag' : False,
        'types' : 4,
        'shape' : 'square',
    },
    {
        'pos' : [QPoint(74, 222), QPoint(148, 296), QPoint(0, 296)], # 紫色
        'color' : '#ff87c4',
        'click' : False,
        'drag' : False,
        'types' : 3,
        'shape' : 'triangle',
    },
    {
        'pos' : [QPoint(296, 148), QPoint(296, 296), QPoint(148, 296)], # 红色
        'color' : '#f00800',
        'click' : False,
        'drag' : False,
        'types' : 3,
        'shape' : 'triangle',
    },

]


img_name_list = [
    '1.jpg', '4.jpg', '5.jpg', 'cat01.jpg',
    'animal01.jpg', 'people01.jpg', 'people02.jpg'
]