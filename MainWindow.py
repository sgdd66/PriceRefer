# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from .FileWindow import FileWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 705)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.filewindow=FileWindow()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(70, 260, 641, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(110, 30, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.label_6.setObjectName("label_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 80, 87, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(30, 80, 72, 15))
        self.label_7.setObjectName("label_7")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 130, 87, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(30, 130, 72, 15))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(30, 180, 72, 15))
        self.label_9.setObjectName("label_9")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(110, 180, 87, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(250, 30, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(240, 80, 91, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(250, 130, 91, 19))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_4.setGeometry(QtCore.QRect(250, 190, 91, 19))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_5.setGeometry(QtCore.QRect(370, 190, 91, 19))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_6.setGeometry(QtCore.QRect(370, 130, 91, 19))
        self.checkBox_6.setObjectName("checkBox_6")
        self.tabWidget_shell = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_shell.setGeometry(QtCore.QRect(0, -20, 641, 341))
        self.tabWidget_shell.setObjectName("tabWidget_shell")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.checkBox_shell = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_shell.setGeometry(QtCore.QRect(30, 250, 91, 19))
        self.checkBox_shell.setObjectName("checkBox_shell")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 571, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.comboBox_board9 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_board9.setObjectName("comboBox_board9")
        self.comboBox_board9.addItem("")
        self.comboBox_board9.addItem("")
        self.comboBox_board9.addItem("")
        self.comboBox_board9.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_board9, 0, 1, 1, 1)
        self.checkBox_board9_0 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_board9_0.setObjectName("checkBox_board9_0")
        self.gridLayout_2.addWidget(self.checkBox_board9_0, 0, 2, 1, 1)
        self.checkBox_board9_1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_board9_1.setObjectName("checkBox_board9_1")
        self.gridLayout_2.addWidget(self.checkBox_board9_1, 0, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.comboBox_board7 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_board7.setObjectName("comboBox_board7")
        self.comboBox_board7.addItem("")
        self.comboBox_board7.addItem("")
        self.comboBox_board7.addItem("")
        self.comboBox_board7.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_board7, 1, 1, 1, 1)
        self.checkBox_board7_0 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_board7_0.setObjectName("checkBox_board7_0")
        self.gridLayout_2.addWidget(self.checkBox_board7_0, 1, 2, 1, 1)
        self.checkBox_board7_1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_board7_1.setObjectName("checkBox_board7_1")
        self.gridLayout_2.addWidget(self.checkBox_board7_1, 1, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)
        self.comboBox_board8 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_board8.setObjectName("comboBox_board8")
        self.comboBox_board8.addItem("")
        self.comboBox_board8.addItem("")
        self.comboBox_board8.addItem("")
        self.comboBox_board8.addItem("")
        self.comboBox_board8.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_board8, 2, 1, 1, 1)
        self.checkBox_board8_0 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_board8_0.setObjectName("checkBox_board8_0")
        self.gridLayout_2.addWidget(self.checkBox_board8_0, 2, 2, 1, 1)
        self.checkBox_board8_1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_board8_1.setObjectName("checkBox_board8_1")
        self.gridLayout_2.addWidget(self.checkBox_board8_1, 2, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)
        self.comboBox_board6 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_board6.setObjectName("comboBox_board6")
        self.comboBox_board6.addItem("")
        self.comboBox_board6.addItem("")
        self.comboBox_board6.addItem("")
        self.comboBox_board6.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_board6, 3, 1, 1, 1)
        self.checkBox_board6_0 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_board6_0.setObjectName("checkBox_board6_0")
        self.gridLayout_2.addWidget(self.checkBox_board6_0, 3, 2, 1, 1)
        self.checkBox_board6_1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_board6_1.setObjectName("checkBox_board6_1")
        self.gridLayout_2.addWidget(self.checkBox_board6_1, 3, 3, 1, 1)
        self.tabWidget_shell.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_shell.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget_shell.addTab(self.tab_6, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 70, 511, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)
        self.comboBox_board2 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_board2.setObjectName("comboBox_board2")
        self.comboBox_board2.addItem("")
        self.comboBox_board2.addItem("")
        self.comboBox_board2.addItem("")
        self.comboBox_board2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_board2, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)
        self.comboBox_board1 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_board1.setObjectName("comboBox_board1")
        self.comboBox_board1.addItem("")
        self.comboBox_board1.addItem("")
        self.comboBox_board1.addItem("")
        self.comboBox_board1.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_board1, 1, 1, 1, 1)
        self.checkBox_board1_0 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_board1_0.setObjectName("checkBox_board1_0")
        self.gridLayout_3.addWidget(self.checkBox_board1_0, 1, 2, 1, 1)
        self.checkBox_board1_1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_board1_1.setObjectName("checkBox_board1_1")
        self.gridLayout_3.addWidget(self.checkBox_board1_1, 1, 3, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget2.setGeometry(QtCore.QRect(50, 50, 551, 211))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_18.setObjectName("label_18")

        self.buttonGroup1=QtWidgets.QButtonGroup(self.layoutWidget2)
        self.buttonGroup2=QtWidgets.QButtonGroup(self.layoutWidget2)
        self.gridLayout_4.addWidget(self.label_18, 2, 0, 1, 1)
        self.radioButton_board4_2 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_board4_2.setChecked(True)
        self.radioButton_board4_2.setAutoExclusive(False)
        self.radioButton_board4_2.setObjectName("radioButton_board4_2")
        self.gridLayout_4.addWidget(self.radioButton_board4_2, 1, 4, 1, 1)
        self.radioButton_board5_1 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_board5_1.setChecked(True)
        self.radioButton_board5_1.setObjectName("radioButton_board5_1")
        self.gridLayout_4.addWidget(self.radioButton_board5_1, 2, 3, 1, 1)
        self.radioButton_board4_1 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_board4_1.setAutoExclusive(False)
        self.radioButton_board4_1.setObjectName("radioButton_board4_1")
        self.gridLayout_4.addWidget(self.radioButton_board4_1, 1, 3, 1, 1)

        self.radioButton_board5_2 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_board5_2.setObjectName("radioButton_board5_2")
        self.gridLayout_4.addWidget(self.radioButton_board5_2, 2, 4, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)
        self.comboBox_board4 = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_board4.setObjectName("comboBox_board4")
        self.comboBox_board4.addItem("")
        self.comboBox_board4.addItem("")
        self.comboBox_board4.addItem("")
        self.comboBox_board4.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_board4, 1, 1, 1, 1)
        self.radioButton_board4_0 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_board4_0.setObjectName("radioButton_board4_0")
        self.gridLayout_4.addWidget(self.radioButton_board4_0, 1, 2, 1, 1)
        self.buttonGroup1.addButton(self.radioButton_board4_0)
        self.buttonGroup1.addButton(self.radioButton_board4_1)
        self.buttonGroup1.addButton(self.radioButton_board4_2)
        self.buttonGroup2.addButton(self.radioButton_board5_1)
        self.buttonGroup2.addButton(self.radioButton_board5_2)
        self.comboBox_board5 = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_board5.setObjectName("comboBox_board5")
        self.comboBox_board5.addItem("")
        self.comboBox_board5.addItem("")
        self.comboBox_board5.addItem("")
        self.comboBox_board5.addItem("")
        self.comboBox_board5.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_board5, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)
        self.comboBox_board3 = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_board3.setObjectName("comboBox_board3")
        self.comboBox_board3.addItem("")
        self.comboBox_board3.addItem("")
        self.comboBox_board3.addItem("")
        self.comboBox_board3.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_board3, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.pushButton_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calculate.setGeometry(QtCore.QRect(540, 620, 93, 28))
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(61, 21, 661, 211))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_P_in = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_P_in.setText("101325")
        self.lineEdit_P_in.setObjectName("lineEdit_P_in")
        self.gridLayout.addWidget(self.lineEdit_P_in, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.lineEdit_T_in = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_T_in.setText("293")
        self.lineEdit_T_in.setObjectName("lineEdit_T_in")
        self.gridLayout.addWidget(self.lineEdit_T_in, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_P = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_P.setText("2760")
        self.lineEdit_P.setObjectName("lineEdit_P")
        self.gridLayout.addWidget(self.lineEdit_P, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.lineEdit_Qn = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Qn.setText("11.367")
        self.lineEdit_Qn.setObjectName("lineEdit_Qn")
        self.gridLayout.addWidget(self.lineEdit_Qn, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_n = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_n.setText("1450")
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.gridLayout.addWidget(self.lineEdit_n, 2, 1, 1, 1)
        self.radioButton_single = QtWidgets.QRadioButton(self.widget)
        self.radioButton_single.setChecked(True)
        self.radioButton_single.setObjectName("radioButton_single")
        self.gridLayout.addWidget(self.radioButton_single, 2, 2, 1, 1)
        self.radioButton_double = QtWidgets.QRadioButton(self.widget)
        self.radioButton_double.setObjectName("radioButton_double")
        self.gridLayout.addWidget(self.radioButton_double, 2, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 3, 2, 1,1)
        self.lineEdit_density = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_density.setObjectName("lineEdit_density")
        self.lineEdit_density.setText("7850")
        self.gridLayout.addWidget(self.lineEdit_density, 3, 1, 1, 1)
        self.lineEdit_axle = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_axle.setText("0")
        self.lineEdit_axle.setObjectName("lineEdit_axle")
        self.gridLayout.addWidget(self.lineEdit_axle, 3, 3, 1, 1)
        self.layoutWidget.raise_()
        self.tabWidget.raise_()
        self.pushButton_calculate.raise_()
        self.radioButton_single.raise_()
        self.radioButton_double.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.lineEdit_density.raise_()
        self.lineEdit_axle.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_shell.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "报价计算"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_shell.setText(_translate("MainWindow", "加脚板组"))
        self.label_10.setText(_translate("MainWindow", "进气箱"))
        self.comboBox_board9.setItemText(0, _translate("MainWindow", "6"))
        self.comboBox_board9.setItemText(1, _translate("MainWindow", "8"))
        self.comboBox_board9.setItemText(2, _translate("MainWindow", "10"))
        self.comboBox_board9.setItemText(3, _translate("MainWindow", "12"))
        self.checkBox_board9_0.setText(_translate("MainWindow", "带法兰"))
        self.checkBox_board9_1.setText(_translate("MainWindow", "带加强筋"))
        self.label_11.setText(_translate("MainWindow", "蜗壳"))
        self.comboBox_board7.setItemText(0, _translate("MainWindow", "6"))
        self.comboBox_board7.setItemText(1, _translate("MainWindow", "8"))
        self.comboBox_board7.setItemText(2, _translate("MainWindow", "10"))
        self.comboBox_board7.setItemText(3, _translate("MainWindow", "12"))
        self.checkBox_board7_0.setText(_translate("MainWindow", "带法兰"))
        self.checkBox_board7_1.setText(_translate("MainWindow", "带加强筋"))
        self.label_12.setText(_translate("MainWindow", "共用侧板"))
        self.comboBox_board8.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox_board8.setItemText(1, _translate("MainWindow", "10"))
        self.comboBox_board8.setItemText(2, _translate("MainWindow", "12"))
        self.comboBox_board8.setItemText(3, _translate("MainWindow", "14"))
        self.comboBox_board8.setItemText(4, _translate("MainWindow", "16"))
        self.checkBox_board8_0.setText(_translate("MainWindow", "带法兰"))
        self.checkBox_board8_1.setText(_translate("MainWindow", "带加强筋"))
        self.label_13.setText(_translate("MainWindow", "后侧板"))
        self.comboBox_board6.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox_board6.setItemText(1, _translate("MainWindow", "10"))
        self.comboBox_board6.setItemText(2, _translate("MainWindow", "12"))
        self.comboBox_board6.setItemText(3, _translate("MainWindow", "14"))
        self.checkBox_board6_0.setText(_translate("MainWindow", "带法兰"))
        self.checkBox_board6_1.setText(_translate("MainWindow", "带加强筋"))
        self.tabWidget_shell.setTabText(self.tabWidget_shell.indexOf(self.tab_2), _translate("MainWindow", "机壳组"))
        self.tabWidget_shell.setTabText(self.tabWidget_shell.indexOf(self.tab_5), _translate("MainWindow", "进风口组"))
        self.tabWidget_shell.setTabText(self.tabWidget_shell.indexOf(self.tab_6), _translate("MainWindow", "叶轮组"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "机壳组"))
        self.label_14.setText(_translate("MainWindow", "法兰"))
        self.comboBox_board2.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox_board2.setItemText(1, _translate("MainWindow", "10"))
        self.comboBox_board2.setItemText(2, _translate("MainWindow", "12"))
        self.comboBox_board2.setItemText(3, _translate("MainWindow", "16"))
        self.label_15.setText(_translate("MainWindow", "进风筒"))
        self.comboBox_board1.setItemText(0, _translate("MainWindow", "4"))
        self.comboBox_board1.setItemText(1, _translate("MainWindow", "5"))
        self.comboBox_board1.setItemText(2, _translate("MainWindow", "6"))
        self.comboBox_board1.setItemText(3, _translate("MainWindow", "8"))
        self.checkBox_board1_0.setText(_translate("MainWindow", "带防磨板"))
        self.checkBox_board1_1.setText(_translate("MainWindow", "带整流圈与整流筒"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "进风口组"))
        self.label_18.setText(_translate("MainWindow", "中盘/后盘"))
        self.radioButton_board4_2.setText(_translate("MainWindow", "复杂堆焊"))
        self.radioButton_board5_1.setText(_translate("MainWindow", "中等堆焊"))
        self.radioButton_board4_1.setText(_translate("MainWindow", "中等堆焊"))
        self.radioButton_board5_2.setText(_translate("MainWindow", "复杂堆焊"))
        self.label_17.setText(_translate("MainWindow", "叶片"))
        self.comboBox_board4.setItemText(0, _translate("MainWindow", "6"))
        self.comboBox_board4.setItemText(1, _translate("MainWindow", "8"))
        self.comboBox_board4.setItemText(2, _translate("MainWindow", "10"))
        self.comboBox_board4.setItemText(3, _translate("MainWindow", "12"))
        self.radioButton_board4_0.setText(_translate("MainWindow", "简单堆焊"))
        self.comboBox_board5.setItemText(0, _translate("MainWindow", "10"))
        self.comboBox_board5.setItemText(1, _translate("MainWindow", "12"))
        self.comboBox_board5.setItemText(2, _translate("MainWindow", "14"))
        self.comboBox_board5.setItemText(3, _translate("MainWindow", "16"))
        self.comboBox_board5.setItemText(4, _translate("MainWindow", "20"))
        self.label_16.setText(_translate("MainWindow", "前盘"))
        self.comboBox_board3.setItemText(0, _translate("MainWindow", "6"))
        self.comboBox_board3.setItemText(1, _translate("MainWindow", "8"))
        self.comboBox_board3.setItemText(2, _translate("MainWindow", "10"))
        self.comboBox_board3.setItemText(3, _translate("MainWindow", "12"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "叶轮组"))
        self.pushButton_calculate.setText(_translate("MainWindow", "计算"))
        self.label.setText(_translate("MainWindow", "进气压力（Pa）"))
        self.label_2.setText(_translate("MainWindow", "进气温度（K）"))
        self.label_4.setText(_translate("MainWindow", "全压（Pa）"))
        self.label_3.setText(_translate("MainWindow", "流量（立方米/秒）"))
        self.label_5.setText(_translate("MainWindow", "转速（转/分钟）"))
        self.radioButton_single.setText(_translate("MainWindow", "单吸"))
        self.radioButton_double.setText(_translate("MainWindow", "双吸"))
        self.label_19.setText(_translate("MainWindow", "材料密度（千克/立方米）"))
        self.label_20.setText(_translate("MainWindow", "主轴重量（千克）"))

class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)

    def setConnect(self,func):
        self.pushButton_calculate.clicked.connect(func)

if __name__=="__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())