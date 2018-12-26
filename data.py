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
from PyQt5.QtCore import  Qt, QPoint


tangram_info = [
    {
        'pos' : [QPoint(0, 0), QPoint(200, 0), QPoint(100, 100)],
        'color' : '#caff67',
        'click' : False,
        'drag' : False,
        'types' : 3,
        'shape' : 'triangle',
    },
    {
        'pos' : [QPoint(0, 0), QPoint(100, 100), QPoint(0, 200)],
        'color' : '#67becf',
        'click' : False,
        'drag' : False,
        'types' : 3,
        'shape' : 'triangle',

    },
    {
        'pos' : [QPoint(200, 0), QPoint(200, 100), QPoint(150, 150), QPoint(150, 50)],
        'color' : '#ef3d61',
        'click' : False,
        'drag' : False,
        'types' : 4,
        'shape' :'parallel',
    },
    {
        'pos' : [QPoint(150, 50), QPoint(150, 150), QPoint(100, 100)],
        'color' : '#f9f51a',
        'click' : False,
        'drag' : False,
        'types' : 3,
        'shape' : 'triangle',
    },
    {
        'pos' : [QPoint(100, 100), QPoint(150, 150), QPoint(100, 200), QPoint(50, 150)],
        'color' : '#a594c0',
        'click' : False,
        'drag' : False,
        'types' : 4,
        'shape' : 'square',
    },
    {
        'pos' : [QPoint(50, 150), QPoint(100, 200), QPoint(0, 200)],
        'color' : '#fa8ecc',
        'click' : False,
        'drag' : False,
        'types' : 3,
        'shape' : 'triangle',
    },
    {
        'pos' : [QPoint(200, 100), QPoint(200, 200), QPoint(100, 200)],
        'color' : '#f6ca29',
        'click' : False,
        'drag' : False,
        'types' : 3,
        'shape' : 'triangle',
    },

]