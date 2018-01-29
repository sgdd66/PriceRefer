#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""报价软件程序主入口"""

from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from PriceRefer.MainWindow import MyWindow
from PriceRefer.DataProcess import DataSource
import numpy as np

def Calculate():

    P_in=float(mywin.lineEdit_P_in.text())
    T_in=float(mywin.lineEdit_T_in.text())
    P=float(mywin.lineEdit_P.text())
    Qn=float(mywin.lineEdit_Qn.text())
    n=float(mywin.lineEdit_n.text())
    density=float(mywin.lineEdit_density.text())
    axle=float(mywin.lineEdit_axle.text())
    other=float(mywin.lineEdit_other.text())
    De=float(mywin.lineEdit_De.text())
    hasInputBox =mywin.checkBox_inputBox.isChecked()

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

    data.design(P_in, T_in, P, Qn, n, De, isSingle)
    if(mywin.comboBox_kind.currentText()!="null" and mywin.comboBox_kind.currentText()!=""):
        data.getDataByKind(mywin.comboBox_kind.currentText())
    else:
        data.getDataByInput()
    data.getArea(boardThick)
    weight=data.getWeight(ratio,density,hasInputBox)

    # str=''
    # for i in range(1,11):
    #     str+=PartArea[i]+"重量：{:.2f}KG\n\n".format(weight[i])
    # str+="主轴重量：{:.2f}KG\n\n".format(axle)
    # str+="总重：{:.2f}KG\n\n".format(np.sum(weight)+axle)

    str=''
    str+="叶轮组：{:.2f}KG\n".format(weight[3]+weight[4]+weight[5])
    str+="机壳组：{:.2f}KG\n".format(weight[6]+weight[7]+weight[8]+weight[9]+weight[10])
    str+="进风口组：{:.2f}KG\n".format(weight[1]+weight[2])
    str+="主轴：{:.2f}KG\n".format(axle)
    str+="其它：{:.2f}KG\n".format(other)
    str+="总重：{:.2f}KG\n".format(np.sum(weight)+axle+other)
    if data.isSingle:
        str+="机型：{0:.1f}-{1}X{2}".format(data.psi*5,1,int(data.ns))
    else:
        str += "机型：{0:.1f}-{1}X{2}".format(data.psi * 5, 2, int(data.ns))
    if hasInputBox:
        str+="No{:.2f}F".format(data.D2/100)
    else:
        str += "No{:.2f}D".format(data.D2/100)

    mywin.textBrowser_outcome.setText(str)
    return str

def setComboBoxKind():
    P_in=float(mywin.lineEdit_P_in.text())
    T_in=float(mywin.lineEdit_T_in.text())
    P=float(mywin.lineEdit_P.text())
    Qn=float(mywin.lineEdit_Qn.text())
    n=float(mywin.lineEdit_n.text())
    De=float(mywin.lineEdit_De.text())
    if mywin.radioButton_single.isChecked():
        isSingle=True
    else:
        isSingle=False
    data.design(P_in, T_in, P, Qn, n,De,isSingle)
    kinds=data.selectKind()

    combo=mywin.comboBox_kind

    for i in range(len(kinds)):
        combo.setItemText(i+1,kinds[i])


def save():
    file_path = QtWidgets.QFileDialog.getSaveFileName(mywin, '保存', "计算报告", "文本文件 (*.txt);;all files(*.*)")
    file = open(file_path[0], 'w')
    tempstr=Calculate()
    str = ''
    str += "进气压力：{0}Pa\n\n".format(float(mywin.lineEdit_P_in.text()))
    str += "进气温度：{0}K\n\n".format(float(mywin.lineEdit_T_in.text()))
    str += "全压：{0}Pa\n\n".format(float(mywin.lineEdit_P.text()))
    str += "流量：{0}m3/s\n\n".format(float(mywin.lineEdit_Qn.text()))
    str += "转速：{0}r/min\n\n".format(float(mywin.lineEdit_n.text()))
    str += "密度：{0}KG/m3\n\n".format(float(mywin.lineEdit_density.text()))
    str += "主轴+轴盘重量：{0}KG\n\n".format(float(mywin.lineEdit_axle.text()))
    str += "其它重量：{0}KG\n\n".format(float(mywin.lineEdit_other.text()))
    str += "叶轮直径：{0}mm\n\n".format(data.D2)
    if mywin.checkBox_inputBox.isChecked():
        str += "F式进气\n\n"
    else:
        str += "D式进气\n\n"

    if mywin.radioButton_single.isChecked():
        str += "单向进气\n\n"
    if mywin.radioButton_double.isChecked():
        str += "双向进气\n\n"

    str += "机壳组：\n"
    if mywin.checkBox_shell.isChecked():
        str += "加脚板组\n"
    str += "进气箱:{0}mm".format(mywin.comboBox_board9.currentText())
    if mywin.checkBox_board9_0.isChecked():
        str += "    带法兰"
    if mywin.checkBox_board9_1.isChecked():
        str += "    带加强筋"
    str += "\n"

    str += "蜗壳:{0}mm".format(mywin.comboBox_board7.currentText())
    if mywin.checkBox_board7_0.isChecked():
        str += "    带法兰"
    if mywin.checkBox_board7_1.isChecked():
        str += "    带加强筋"
    str += "\n"

    str += "公用侧板:{0}mm".format(mywin.comboBox_board8.currentText())
    if mywin.checkBox_board8_0.isChecked():
        str += "    带法兰"
    if mywin.checkBox_board8_1.isChecked():
        str += "    带加强筋"
    str += "\n"

    str += "后侧板:{0}mm".format(mywin.comboBox_board6.currentText())
    if mywin.checkBox_board6_0.isChecked():
        str += "    带法兰"
    if mywin.checkBox_board6_1.isChecked():
        str += "    带加强筋"
    str += "\n\n"

    str += "进风口组\n"
    str += "法兰：{0}mm\n".format(mywin.comboBox_board2.currentText())
    str += "进风筒：{0}mm".format(mywin.comboBox_board1.currentText())
    if mywin.checkBox_board1_0.isChecked():
        str += "    带防磨板"
    if mywin.checkBox_board1_1.isChecked():
        str += "    带整流圈与整流筒"
    str += "\n\n"

    str += "叶轮组：\n"
    str += "前盘：{0}mm\n".format(mywin.comboBox_board3.currentText())
    str += "叶片：{0}mm".format(mywin.comboBox_board4.currentText())

    if mywin.radioButton_board4_0.isChecked():
        str += "    简单堆焊"
    elif mywin.radioButton_board4_1.isChecked():
        str += "    中等堆焊"
    elif mywin.radioButton_board4_2.isChecked():
        str += "    复杂堆焊"
    else:
        str += "    无堆焊"
    str += "\n"

    str += "中盘/后盘：{0}mm".format(mywin.comboBox_board5.currentText())

    if mywin.radioButton_board5_1.isChecked():
        str += "    中等堆焊"
    elif mywin.radioButton_board5_2.isChecked():
        str += "    复杂堆焊"
    else:
        str += "    无堆焊"
    str += "\n\n"

    str += tempstr

    file.write(str)
    file.close()

from PriceRefer import img_rc
app = QtWidgets.QApplication(sys.argv)
pixmap=QtGui.QPixmap(":/welcome.png")
splash=QtWidgets.QSplashScreen(pixmap)
splash.show()


n = QtCore.QDateTime.currentDateTime()
now = QtCore.QDateTime.currentDateTime()
while n.secsTo(now) <= 2:

    now = QtCore.QDateTime.currentDateTime()
    app.processEvents()


data = DataSource()
mywin = MyWindow()
mywin.setConnect_calculate(Calculate)
mywin.setConnect_combo_kind(setComboBoxKind)
mywin.setConnect_save(save)
mywin.show()
splash.finish(mywin)
sys.exit(app.exec_())



