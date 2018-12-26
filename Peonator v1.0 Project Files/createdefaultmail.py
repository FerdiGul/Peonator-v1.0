# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createdefaultmail.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from os import walk
#import glob,fnmatch

class Ui_CreateDefaultMail(object):

    def setupUi(self, CreateDefaultMail):


        CreateDefaultMail.setObjectName("CreateDefaultMail")
        CreateDefaultMail.setFixedSize(623, 396)
        self.centralWidget = QtWidgets.QWidget(CreateDefaultMail)
        self.centralWidget.setObjectName("centralWidget")
		
        self.cmbx_caseNameMail = QtWidgets.QComboBox(self.centralWidget)
        self.cmbx_caseNameMail.setGeometry(QtCore.QRect(150, 30, 331, 21))
        self.cmbx_caseNameMail.setObjectName("cmbx_caseNameMail")

        self.btn_mail = QtWidgets.QPushButton(self.centralWidget)
        self.btn_mail.setGeometry(QtCore.QRect(175, 320, 131, 51))
        self.btn_mail.setObjectName("btn_mail")
        self.btn_mail.clicked.connect(self.file_open)

        self.btn_copy = QtWidgets.QPushButton(self.centralWidget)
        self.btn_copy.setGeometry(QtCore.QRect(320, 320, 131, 51))
        self.btn_copy.setObjectName("btn_copy")
        self.btn_copy.clicked.connect(self.file_copy)


        
        self.textEdit_mail = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_mail.setGeometry(QtCore.QRect(20, 70, 591, 231))
        self.textEdit_mail.setObjectName("textEdit_mail")
        
        all_cases = open('case_name.txt').read()
        list1 = all_cases.splitlines()

        
        
        for i in list1:
                self.cmbx_caseNameMail.addItem(i)
        
     
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 91, 16))
        self.label.setObjectName("label")
                    
        
        CreateDefaultMail.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(CreateDefaultMail)
        self.statusBar.setObjectName("statusBar")
        CreateDefaultMail.setStatusBar(self.statusBar)

        self.retranslateUi(CreateDefaultMail)
        QtCore.QMetaObject.connectSlotsByName(CreateDefaultMail)

    def retranslateUi(self, CreateDefaultMail):
        _translate = QtCore.QCoreApplication.translate
        CreateDefaultMail.setWindowTitle(_translate("CreateDefaultMail", "Peonator v1.0 - Create Default Mail"))
        self.label.setText(_translate("CreateDefaultMail", "Case Name :"))
        self.btn_mail.setText(_translate("CreateDefaultMail", "GET MAIL and COPY"))
        self.btn_copy.setText(_translate("CreateDefaultMail", "COPY Modified MAIL"))
      


    def file_open(self):

        try:
            #f = []
            #for (dirpath, dirnames, filenames) in walk(".\\DefaultMail\\"):
                #f.extend(filenames)
            if self.cmbx_caseNameMail.currentIndex()==0:
                alarm1 = open('.\\DefaultMail\\alarm1.txt').read()
                self.textEdit_mail.setPlainText(alarm1)
                self.file_copy()
            elif self.cmbx_caseNameMail.currentIndex()==1:
                alarm2 = open('.\\DefaultMail\\alarm2.txt').read()
                self.textEdit_mail.setPlainText(privilege)
                self.file_copy()
            elif self.cmbx_caseNameMail.currentIndex()==2:
                alarm3 = open('.\\DefaultMail\\alarm3.txt').read()
                self.textEdit_mail.setPlainText(alarm3)
                self.file_copy()

            elif self.cmbx_caseNameMail.currentIndex()==3:
                alarm4 = open('.\\DefaultMail\\alarm4.txt').read()
                self.textEdit_mail.setPlainText(alarm4)
                self.file_copy()
            else:
                caseName = self.cmbx_caseNameMail.currentText()
                alarmdefault = open(".\\DefaultMail\\"+caseName+".txt").read()
                self.textEdit_mail.setPlainText(alarmdefault)
                self.file_copy()
			
        except:
            print("Problem was Found !")
            self.showMessageBox('Warning','Be Careful My Dude :) !')
            
            
    def file_copy(self):
            self.textEdit_mail.selectAll()
            self.textEdit_mail.copy()

   
            
        
    def showMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateDefaultMail = QtWidgets.QMainWindow()
    ui = Ui_CreateDefaultMail()
    ui.setupUi(CreateDefaultMail)
    CreateDefaultMail.show()
    sys.exit(app.exec_())

