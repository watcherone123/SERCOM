# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SERCOM.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SERCOM(object):
    def setupUi(self, SERCOM):
        SERCOM.setObjectName(_fromUtf8("SERCOM"))
        SERCOM.resize(594, 466)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SERCOM.sizePolicy().hasHeightForWidth())
        SERCOM.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Image/serial.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SERCOM.setWindowIcon(icon)
        self.vLayout0 = QtGui.QVBoxLayout(SERCOM)
        self.vLayout0.setObjectName(_fromUtf8("vLayout0"))
        self.txtMain = QtGui.QTextEdit(SERCOM)
        self.txtMain.setFrameShadow(QtGui.QFrame.Sunken)
        self.txtMain.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtMain.setObjectName(_fromUtf8("txtMain"))
        self.vLayout0.addWidget(self.txtMain)
        self.hLayout1 = QtGui.QHBoxLayout()
        self.hLayout1.setObjectName(_fromUtf8("hLayout1"))
        self.lblSend = QtGui.QLabel(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSend.sizePolicy().hasHeightForWidth())
        self.lblSend.setSizePolicy(sizePolicy)
        self.lblSend.setObjectName(_fromUtf8("lblSend"))
        self.hLayout1.addWidget(self.lblSend)
        self.cmbSend = QtGui.QComboBox(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbSend.sizePolicy().hasHeightForWidth())
        self.cmbSend.setSizePolicy(sizePolicy)
        self.cmbSend.setEditable(True)
        self.cmbSend.setObjectName(_fromUtf8("cmbSend"))
        self.hLayout1.addWidget(self.cmbSend)
        self.chkSendLF = QtGui.QCheckBox(SERCOM)
        self.chkSendLF.setObjectName(_fromUtf8("chkSendLF"))
        self.hLayout1.addWidget(self.chkSendLF)
        self.btnSend = QtGui.QPushButton(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSend.sizePolicy().hasHeightForWidth())
        self.btnSend.setSizePolicy(sizePolicy)
        self.btnSend.setObjectName(_fromUtf8("btnSend"))
        self.hLayout1.addWidget(self.btnSend)
        self.btnClear = QtGui.QPushButton(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.hLayout1.addWidget(self.btnClear)
        self.chkHEXShow = QtGui.QCheckBox(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkHEXShow.sizePolicy().hasHeightForWidth())
        self.chkHEXShow.setSizePolicy(sizePolicy)
        self.chkHEXShow.setObjectName(_fromUtf8("chkHEXShow"))
        self.hLayout1.addWidget(self.chkHEXShow)
        self.vLayout0.addLayout(self.hLayout1)
        self.hLayout2 = QtGui.QHBoxLayout()
        self.hLayout2.setObjectName(_fromUtf8("hLayout2"))
        self.lblCOMM = QtGui.QLabel(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCOMM.sizePolicy().hasHeightForWidth())
        self.lblCOMM.setSizePolicy(sizePolicy)
        self.lblCOMM.setObjectName(_fromUtf8("lblCOMM"))
        self.hLayout2.addWidget(self.lblCOMM)
        self.cmbCOMM = QtGui.QComboBox(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbCOMM.sizePolicy().hasHeightForWidth())
        self.cmbCOMM.setSizePolicy(sizePolicy)
        self.cmbCOMM.setMinimumSize(QtCore.QSize(100, 0))
        self.cmbCOMM.setObjectName(_fromUtf8("cmbCOMM"))
        self.hLayout2.addWidget(self.cmbCOMM)
        self.lblBaud = QtGui.QLabel(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblBaud.sizePolicy().hasHeightForWidth())
        self.lblBaud.setSizePolicy(sizePolicy)
        self.lblBaud.setObjectName(_fromUtf8("lblBaud"))
        self.hLayout2.addWidget(self.lblBaud)
        self.cmbBaud = QtGui.QComboBox(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbBaud.sizePolicy().hasHeightForWidth())
        self.cmbBaud.setSizePolicy(sizePolicy)
        self.cmbBaud.setMinimumSize(QtCore.QSize(100, 0))
        self.cmbBaud.setObjectName(_fromUtf8("cmbBaud"))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.hLayout2.addWidget(self.cmbBaud)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hLayout2.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hLayout2.addItem(spacerItem1)
        self.btnOpen = QtGui.QPushButton(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpen.sizePolicy().hasHeightForWidth())
        self.btnOpen.setSizePolicy(sizePolicy)
        self.btnOpen.setMinimumSize(QtCore.QSize(104, 0))
        self.btnOpen.setCheckable(False)
        self.btnOpen.setObjectName(_fromUtf8("btnOpen"))
        self.hLayout2.addWidget(self.btnOpen)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hLayout2.addItem(spacerItem2)
        self.lblStat = QtGui.QLabel(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStat.sizePolicy().hasHeightForWidth())
        self.lblStat.setSizePolicy(sizePolicy)
        self.lblStat.setMinimumSize(QtCore.QSize(20, 0))
        self.lblStat.setText(_fromUtf8(""))
        self.lblStat.setPixmap(QtGui.QPixmap(_fromUtf8("Image/inclosing.png")))
        self.lblStat.setObjectName(_fromUtf8("lblStat"))
        self.hLayout2.addWidget(self.lblStat)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hLayout2.addItem(spacerItem3)
        self.chkHEXSend = QtGui.QCheckBox(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkHEXSend.sizePolicy().hasHeightForWidth())
        self.chkHEXSend.setSizePolicy(sizePolicy)
        self.chkHEXSend.setObjectName(_fromUtf8("chkHEXSend"))
        self.hLayout2.addWidget(self.chkHEXSend)
        self.vLayout0.addLayout(self.hLayout2)
        self.hLayout3 = QtGui.QHBoxLayout()
        self.hLayout3.setObjectName(_fromUtf8("hLayout3"))
        self.lblData = QtGui.QLabel(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblData.sizePolicy().hasHeightForWidth())
        self.lblData.setSizePolicy(sizePolicy)
        self.lblData.setObjectName(_fromUtf8("lblData"))
        self.hLayout3.addWidget(self.lblData)
        self.cmbData = QtGui.QComboBox(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbData.sizePolicy().hasHeightForWidth())
        self.cmbData.setSizePolicy(sizePolicy)
        self.cmbData.setMinimumSize(QtCore.QSize(100, 0))
        self.cmbData.setObjectName(_fromUtf8("cmbData"))
        self.cmbData.addItem(_fromUtf8(""))
        self.cmbData.addItem(_fromUtf8(""))
        self.cmbData.addItem(_fromUtf8(""))
        self.cmbData.addItem(_fromUtf8(""))
        self.hLayout3.addWidget(self.cmbData)
        self.lblChek = QtGui.QLabel(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblChek.sizePolicy().hasHeightForWidth())
        self.lblChek.setSizePolicy(sizePolicy)
        self.lblChek.setObjectName(_fromUtf8("lblChek"))
        self.hLayout3.addWidget(self.lblChek)
        self.cmbChek = QtGui.QComboBox(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbChek.sizePolicy().hasHeightForWidth())
        self.cmbChek.setSizePolicy(sizePolicy)
        self.cmbChek.setMinimumSize(QtCore.QSize(100, 0))
        self.cmbChek.setObjectName(_fromUtf8("cmbChek"))
        self.cmbChek.addItem(_fromUtf8(""))
        self.cmbChek.addItem(_fromUtf8(""))
        self.cmbChek.addItem(_fromUtf8(""))
        self.cmbChek.addItem(_fromUtf8(""))
        self.cmbChek.addItem(_fromUtf8(""))
        self.hLayout3.addWidget(self.cmbChek)
        self.lblStop = QtGui.QLabel(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStop.sizePolicy().hasHeightForWidth())
        self.lblStop.setSizePolicy(sizePolicy)
        self.lblStop.setObjectName(_fromUtf8("lblStop"))
        self.hLayout3.addWidget(self.lblStop)
        self.cmbStop = QtGui.QComboBox(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbStop.sizePolicy().hasHeightForWidth())
        self.cmbStop.setSizePolicy(sizePolicy)
        self.cmbStop.setMinimumSize(QtCore.QSize(100, 0))
        self.cmbStop.setObjectName(_fromUtf8("cmbStop"))
        self.cmbStop.addItem(_fromUtf8(""))
        self.cmbStop.addItem(_fromUtf8(""))
        self.hLayout3.addWidget(self.cmbStop)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hLayout3.addItem(spacerItem4)
        self.cmbMode = QtGui.QComboBox(SERCOM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbMode.sizePolicy().hasHeightForWidth())
        self.cmbMode.setSizePolicy(sizePolicy)
        self.cmbMode.setMinimumSize(QtCore.QSize(65, 0))
        self.cmbMode.setMaximumSize(QtCore.QSize(65, 16777215))
        self.cmbMode.setObjectName(_fromUtf8("cmbMode"))
        self.cmbMode.addItem(_fromUtf8(""))
        self.cmbMode.addItem(_fromUtf8(""))
        self.hLayout3.addWidget(self.cmbMode)
        self.vLayout0.addLayout(self.hLayout3)

        self.retranslateUi(SERCOM)
        self.cmbBaud.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SERCOM)

    def retranslateUi(self, SERCOM):
        SERCOM.setWindowTitle(_translate("SERCOM", "XIVN1987 SERCOM", None))
        self.lblSend.setText(_translate("SERCOM", "输入框：", None))
        self.chkSendLF.setToolTip(_translate("SERCOM", "发送完数据后发送一个换行符", None))
        self.chkSendLF.setText(_translate("SERCOM", "换行", None))
        self.btnSend.setText(_translate("SERCOM", "发送", None))
        self.btnClear.setText(_translate("SERCOM", "清除", None))
        self.chkHEXShow.setText(_translate("SERCOM", "HEX显示", None))
        self.lblCOMM.setText(_translate("SERCOM", "串口号：", None))
        self.lblBaud.setText(_translate("SERCOM", "波特率：", None))
        self.cmbBaud.setItemText(0, _translate("SERCOM", "1200", None))
        self.cmbBaud.setItemText(1, _translate("SERCOM", "2400", None))
        self.cmbBaud.setItemText(2, _translate("SERCOM", "4800", None))
        self.cmbBaud.setItemText(3, _translate("SERCOM", "9600", None))
        self.cmbBaud.setItemText(4, _translate("SERCOM", "14400", None))
        self.cmbBaud.setItemText(5, _translate("SERCOM", "19200", None))
        self.cmbBaud.setItemText(6, _translate("SERCOM", "28800", None))
        self.cmbBaud.setItemText(7, _translate("SERCOM", "57600", None))
        self.cmbBaud.setItemText(8, _translate("SERCOM", "115200", None))
        self.btnOpen.setText(_translate("SERCOM", "打开串口", None))
        self.chkHEXSend.setText(_translate("SERCOM", "HEX发送", None))
        self.lblData.setText(_translate("SERCOM", "数据位：", None))
        self.cmbData.setItemText(0, _translate("SERCOM", "8", None))
        self.cmbData.setItemText(1, _translate("SERCOM", "7", None))
        self.cmbData.setItemText(2, _translate("SERCOM", "6", None))
        self.cmbData.setItemText(3, _translate("SERCOM", "5", None))
        self.lblChek.setText(_translate("SERCOM", "校验位：", None))
        self.cmbChek.setItemText(0, _translate("SERCOM", "None", None))
        self.cmbChek.setItemText(1, _translate("SERCOM", "Odd", None))
        self.cmbChek.setItemText(2, _translate("SERCOM", "Even", None))
        self.cmbChek.setItemText(3, _translate("SERCOM", "One", None))
        self.cmbChek.setItemText(4, _translate("SERCOM", "Zero", None))
        self.lblStop.setText(_translate("SERCOM", "停止位：", None))
        self.cmbStop.setItemText(0, _translate("SERCOM", "1", None))
        self.cmbStop.setItemText(1, _translate("SERCOM", "2", None))
        self.cmbMode.setItemText(0, _translate("SERCOM", "文本", None))
        self.cmbMode.setItemText(1, _translate("SERCOM", "波形", None))

