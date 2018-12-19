# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TangramUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tangramForm(object):
    def setupUi(self, tangramForm):
        tangramForm.setObjectName("tangramForm")
        tangramForm.resize(1200, 610)
        tangramForm.setMaximumSize(QtCore.QSize(1200, 610))
        self.groupBox = QtWidgets.QGroupBox(tangramForm)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 91, 91))
        self.groupBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.sourceImageRBtn = QtWidgets.QRadioButton(self.groupBox)
        self.sourceImageRBtn.setGeometry(QtCore.QRect(0, 10, 81, 20))
        self.sourceImageRBtn.setChecked(True)
        self.sourceImageRBtn.setObjectName("sourceImageRBtn")
        self.personalDesignRBtn = QtWidgets.QRadioButton(self.groupBox)
        self.personalDesignRBtn.setGeometry(QtCore.QRect(0, 60, 81, 20))
        self.personalDesignRBtn.setObjectName("personalDesignRBtn")
        self.line = QtWidgets.QFrame(tangramForm)
        self.line.setGeometry(QtCore.QRect(100, 16, 21, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(tangramForm)
        self.line_2.setGeometry(QtCore.QRect(281, 14, 20, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(tangramForm)
        self.line_3.setGeometry(QtCore.QRect(290, 0, 16, 611))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.imgLable = QtWidgets.QLabel(tangramForm)
        self.imgLable.setGeometry(QtCore.QRect(302, 2, 900, 600))
        self.imgLable.setObjectName("imgLable")
        self.imgcboBox = QtWidgets.QComboBox(tangramForm)
        self.imgcboBox.setGeometry(QtCore.QRect(120, 10, 161, 26))
        self.imgcboBox.setEditable(True)
        self.imgcboBox.setObjectName("imgcboBox")

        self.retranslateUi(tangramForm)
        QtCore.QMetaObject.connectSlotsByName(tangramForm)

    def retranslateUi(self, tangramForm):
        _translate = QtCore.QCoreApplication.translate
        tangramForm.setWindowTitle(_translate("tangramForm", "Tangram UI"))
        self.sourceImageRBtn.setText(_translate("tangramForm", "图形实例"))
        self.personalDesignRBtn.setText(_translate("tangramForm", "个人设计"))
        self.imgLable.setText(_translate("tangramForm", "TextLabel"))

import apprcc_rc
