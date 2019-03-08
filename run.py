#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-08 11:41
# @Author  : Lynn
# @Site    : 
# @File    : run.py
# @Software: PyCharm

from callTangramUI import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyMainWidget()

    myWidget.show()
    sys.exit(app.exec_())
