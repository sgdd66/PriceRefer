#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""报价软件程序主入口"""

from PyQt5 import QtWidgets
import sys
from PriceRefer.MainWindow import MyWindow
from PriceRefer.DataProcess import DataSource,PartArea
import numpy as np

def Calculate():

    P_in=float(mywin.lineEdit_P_in.text())
    T_in=float(mywin.lineEdit_T_in.text())
    P=float(mywin.lineEdit_P.text())
    Qn=float(mywin.lineEdit_Qn.text())
    n=float(mywin.lineEdit_n.text())
    density=float(mywin.lineEdit_density.text())
    axle=float(mywin.lineEdit_axle.text())
    if mywin.radioButton_single.isChecked():
        isSingle=True
    if mywin.radioButton_double.isChecked():
        isSingle=False


    boardThick=np.zeros(11)
    boardThick[1] = float(mywin.comboBox_board1.currentText())
    boardThick[2] = float(mywin.comboBox_board2.currentText())
    boardThick[3] = float(mywin.comboBox_board3.currentText())
    boardThick[4] = float(mywin.comboBox_board4.currentText())
    boardThick[5] = float(mywin.comboBox_board5.currentText())
    boardThick[6] = float(mywin.comboBox_board6.currentText())
    boardThick[7] = float(mywin.comboBox_board7.currentText())
    boardThick[8] = float(mywin.comboBox_board8.currentText())
    boardThick[9] = float(mywin.comboBox_board9.currentText())
    boardThick[10] = float(mywin.comboBox_board9.currentText())

    ratio=np.zeros(11)+1
    if(mywin.checkBox_board1_0.isChecked()):
        ratio[1]+=0.2
    if(mywin.checkBox_board1_1.isChecked()):
        ratio[1]+=1

    if(mywin.radioButton_board4_0.isChecked()):
        ratio[4]+=0.05
    if mywin.radioButton_board4_1.isChecked():
        ratio[4]+=0.1
    if mywin.radioButton_board4_2.isChecked():
        ratio[4]+=0.15

    if mywin.radioButton_board5_1.isChecked():
        ratio[5]+=0.05
    if mywin.radioButton_board5_2.isChecked():
        ratio[5]+=0.05

    if mywin.checkBox_board6_0.isChecked():
        ratio[6]+=0.05
    if mywin.checkBox_board6_1.isChecked():
        ratio[6]+=0.2

    if mywin.checkBox_board7_0.isChecked():
        ratio[7]+=0.05
    if mywin.checkBox_board7_1.isChecked():
        ratio[7]+=0.2

    if mywin.checkBox_board8_0.isChecked():
        ratio[8]+=0.05
    if mywin.checkBox_board8_1.isChecked():
        ratio[8]+=0.1

    if mywin.checkBox_board9_0.isChecked():
        ratio[9]+=0.05
        ratio[10]+=0.05
    if mywin.checkBox_board9_1.isChecked():
        ratio[9]+=0.2
        ratio[10]+=0.2

    if mywin.checkBox_shell.isChecked():
        ratio[6] += 0.05
        ratio[7] += 0.05
        ratio[8] += 0.05
        ratio[9] += 0.05
        ratio[10] += 0.05

    data = DataSource(P_in, T_in, P, Qn, n, isSingle,boardThick)
    weight=data.getWeight(ratio,density)
    # weight=np.zeros(11)
    str=''
    for i in range(1,11):
        str+=PartArea[i]+"重量：{:.2f}KG\n\n".format(weight[i])
    str+="主轴重量：{:.2f}KG\n\n".format(axle)
    str+="总重：{:.2f}KG".format(np.sum(weight)+axle)

    mywin.filewindow.textBrowser.setText(str)
    mywin.filewindow.show()

app = QtWidgets.QApplication(sys.argv)
mywin = MyWindow()
mywin.setConnect(Calculate)
mywin.show()
sys.exit(app.exec_())