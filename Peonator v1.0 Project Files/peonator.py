# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'peonator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from createdefaultmail import Ui_CreateDefaultMail
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize()
        MainWindow.setFixedSize(537,316)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_eagle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 47, 13))
        self.label.setObjectName("label")
        
        self.cmbx_userID = QtWidgets.QComboBox(self.centralwidget)
        self.cmbx_userID.setGeometry(QtCore.QRect(110, 60, 171, 21))
        self.cmbx_userID.setObjectName("cmbx_userID")

        userID = open('userID.txt').read()
        list1 = userID.splitlines()

        for i in list1:
                self.cmbx_userID.addItem(i)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 61, 16))
        self.label_3.setObjectName("label_3")
        
        self.cmbx_caseName = QtWidgets.QComboBox(self.centralwidget)
        self.cmbx_caseName.setGeometry(QtCore.QRect(110, 20, 411, 21))
        self.cmbx_caseName.setObjectName("cmbbox_caseName")

        case_name = open('case_name.txt').read()
        list1 = case_name.splitlines()

        for i in list1:
                self.cmbx_caseName.addItem(i)

                
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setGeometry(QtCore.QRect(300, 70, 221, 71))
        self.btn_generate.setObjectName("btn_generate")
        self.btn_generate.clicked.connect(self.generate_case)
     

        
        self.text_caseName = QtWidgets.QTextEdit(self.centralwidget)
        self.text_caseName.setEnabled(True)
        self.text_caseName.setGeometry(QtCore.QRect(30, 260, 491, 31))
        self.text_caseName.setObjectName("text_caseName")
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 100, 251, 41))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radio_close = QtWidgets.QRadioButton(self.groupBox_2)
        self.radio_close.setGeometry(QtCore.QRect(100, 20, 82, 17))
        self.radio_close.setObjectName("radio_close")
        self.radio_open = QtWidgets.QRadioButton(self.groupBox_2)
        self.radio_open.setGeometry(QtCore.QRect(20, 20, 61, 17))
        self.radio_open.setObjectName("radio_open")
        
        self.btn_mail = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mail.setGeometry(QtCore.QRect(300, 160, 221, 71))
        self.btn_mail.setObjectName("btn_mail")
        self.btn_mail.clicked.connect(self.openDefaultMailCreator)

        
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 150, 251, 41))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radio_ext = QtWidgets.QRadioButton(self.groupBox_3)
        self.radio_ext.setGeometry(QtCore.QRect(100, 20, 82, 17))
        self.radio_ext.setObjectName("radio_ext")
        self.radio_int = QtWidgets.QRadioButton(self.groupBox_3)
        self.radio_int.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.radio_int.setObjectName("radio_int")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 210, 61, 16))
        self.label_2.setObjectName("label_2")
        
        self.text_generate = QtWidgets.QTextEdit(self.centralwidget)
        self.text_generate.setEnabled(True)
        self.text_generate.setGeometry(QtCore.QRect(110, 210, 171, 23))
        self.text_generate.setObjectName("text_input")

                
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd_New_Case_Name = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Case_Name.setObjectName("actionAdd_New_Case_Name")
        self.actionAdd_New_User_ID = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_User_ID.setObjectName("actionAdd_New_User_ID")
        self.actionAdd_New_User_ID_2 = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_User_ID_2.setCheckable(False)
        self.actionAdd_New_User_ID_2.setObjectName("actionAdd_New_User_ID_2")
        self.actionAdd_New_Case_Name_2 = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Case_Name_2.setObjectName("actionAdd_New_Case_Name_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
        
        
    def generate_case(self):
        try:
            self.text_caseName.clear()
            dateTime = str(datetime.datetime.now().strftime("%Y%m%d"))
            userID   = self.cmbx_userID.currentText()
            
            if self.radio_open.isChecked()==True & self.radio_int.isChecked()==True:

                
                internal = self.radio_int.text()
                caseName = self.cmbx_caseName.currentText()
                inputVal = self.text_generate.toPlainText()
                
                result   = "_"+dateTime+"_"+userID+"_"+internal+"_"+caseName+"_"+inputVal
                self.result(result)

            if self.radio_open.isChecked()==True & self.radio_ext.isChecked()==True:
                
                
                external = self.radio_ext.text()
                caseName = self.cmbx_caseName.currentText()
                inputVal = self.text_generate.toPlainText()
                
                result   = "_"+dateTime+"_"+userID+"_"+external+"_"+caseName+"_"+inputVal
               
                self.text_caseName.setPlainText(result)
                self.result(result)

            if self.radio_close.isChecked()==True & self.radio_int.isChecked()==True:
                
                
                internal = self.radio_int.text()
                caseName = self.cmbx_caseName.currentText()
                inputVal = self.text_generate.toPlainText()
                
                result   = dateTime+"_"+userID+"_"+internal+"_"+caseName+"_"+inputVal
                self.result(result)


            if self.radio_close.isChecked()==True & self.radio_ext.isChecked()==True:
                
                dateTime = str(datetime.datetime.now().strftime("%Y%m%d"))
                userID   = self.cmbx_userID.currentText()
                external = self.radio_ext.text()
                caseName = self.cmbx_caseName.currentText()
                inputVal = self.text_generate.toPlainText()

                result   = dateTime+"_"+userID+"_"+external+"_"+caseName+"_"+inputVal
                self.result(result)
                
        except:
                print("Problem was Found !")
                self.showErrorMessageBox('Warning','Be Careful My Dude :) !')

    def result(self,result):
               
            self.text_caseName.setPlainText(result) 
            self.text_caseName.selectAll()
            self.text_caseName.copy()
            
            caseCreationTime = str(datetime.datetime.now().strftime("%Y-%m-%d"+" "+"H:"+"%H"+" "+"M:"+"%M"+" "+"S:"+"%S"))
            with open('CaseReport.txt', 'a') as caseReport:
                caseReport.write(result+ "\t\t\t\t"+caseCreationTime+"\n")

                
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Peonator v1.0"))
        self.label.setText(_translate("MainWindow", "User ID :"))
        self.label_3.setText(_translate("MainWindow", "Case Name : "))
        self.btn_generate.setText(_translate("MainWindow", "Generate and Copy Case"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Status of Case"))
        self.radio_close.setText(_translate("MainWindow", "Close"))
        self.radio_open.setText(_translate("MainWindow", "Open"))
        self.btn_mail.setText(_translate("MainWindow", "Create Default Mail"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Type"))
        self.radio_ext.setText(_translate("MainWindow", "ext"))
        self.radio_int.setText(_translate("MainWindow", "int"))
        self.label_2.setText(_translate("MainWindow", "Input Value :"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAdd_New_Case_Name.setText(_translate("MainWindow", "Add New Case Name"))
        self.actionAdd_New_User_ID.setText(_translate("MainWindow", "Add New User ID"))
        self.actionAdd_New_User_ID_2.setText(_translate("MainWindow", "&Add New User ID"))
        self.actionAdd_New_Case_Name_2.setText(_translate("MainWindow", "&Add New Case Name"))


    def openDefaultMailCreator(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreateDefaultMail()
        self.ui.setupUi(self.window)
        self.window.show()

    def showErrorMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

