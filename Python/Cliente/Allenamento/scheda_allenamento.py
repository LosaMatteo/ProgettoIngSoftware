# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scheda_allenamento.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from Data.MessageBox import messageBox
from Model.Cliente import Cliente


class scheda_allenamento(object):
    username = ""
    msg = messageBox()

    def leggiScheda(self):

        objCliente = Cliente()
        objCliente = objCliente.getObject(self.username)
        self.lblNome.setText(self.username)
        try:
            with open("./Staff/Allenamento_staff/file_scheda_allenamento/" + objCliente.name +
                      " " + objCliente.surname + ".txt", "r") as openfile:
                lettura = openfile.readline()
                str = lettura.split("-")
                self.lblDataInizio.setText(str[0])
                self.lblDataFine.setText(str[1])
                temp = openfile.read()
                vett = temp.split("-")
                row = 0
                colonna = 0
                i = 0
                while len(vett) > i+1:
                    self.Tabella.insertRow(row)
                    self.Tabella.setItem(row, colonna, QTableWidgetItem(vett[i]))
                    self.Tabella.setItem(row, colonna + 1, QTableWidgetItem(vett[i + 1]))
                    self.Tabella.setItem(row, colonna + 2, QTableWidgetItem(vett[i + 2]))
                    self.Tabella.setItem(row, colonna + 3, QTableWidgetItem(vett[i + 3]))
                    row += 1
                    i += 4
        except(Exception):
            self.msg.show_popup_ok("si è verificato un Errore.Riprovare")



    def setupUi(self, MainWindow, username):
        self.finestra = MainWindow
        self.username = username
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitolo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitolo.setGeometry(QtCore.QRect(250, 29, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitolo.setFont(font)
        self.lblTitolo.setObjectName("lblTitolo")
        self.Tabella = QtWidgets.QTableWidget(self.centralwidget)
        self.Tabella.setGeometry(QtCore.QRect(160, 170, 501, 301))
        self.Tabella.setObjectName("Tabella")
        self.Tabella.setColumnCount(4)
        self.Tabella.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Tabella.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabella.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabella.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabella.setHorizontalHeaderItem(3, item)
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(330, 70, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setText("")
        self.lblNome.setObjectName("lblNome")
        self.btnIndietro = QtWidgets.QPushButton(self.centralwidget)
        self.btnIndietro.setGeometry(QtCore.QRect(622, 500, 121, 28))
        self.btnIndietro.setObjectName("btnIndietro")
        self.lblTesto_1 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_1.setGeometry(QtCore.QRect(80, 130, 151, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTesto_1.setFont(font)
        self.lblTesto_1.setObjectName("lblTesto_1")
        self.lblTesto_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_2.setGeometry(QtCore.QRect(460, 130, 151, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTesto_2.setFont(font)
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.lblDataInizio = QtWidgets.QLabel(self.centralwidget)
        self.lblDataInizio.setGeometry(QtCore.QRect(220, 121, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDataInizio.setFont(font)
        self.lblDataInizio.setText("")
        self.lblDataInizio.setObjectName("lblDataInizio")
        self.lblDataFine = QtWidgets.QLabel(self.centralwidget)
        self.lblDataFine.setGeometry(QtCore.QRect(590, 120, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDataFine.setFont(font)
        self.lblDataFine.setText("")
        self.lblDataFine.setObjectName("lblDataFine")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.leggiScheda()
        self.btnIndietro.clicked.connect(self.finestra.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scheda di allenamento"))
        self.lblTitolo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Scheda di allenamento</p></body></html>"))
        item = self.Tabella.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Esercizio"))
        item = self.Tabella.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Serie"))
        item = self.Tabella.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ripetizioni"))
        item = self.Tabella.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Recupero"))
        self.btnIndietro.setText(_translate("MainWindow", "Indietro"))
        self.lblTesto_1.setText(_translate("MainWindow", "Data inizio scheda:"))
        self.lblTesto_2.setText(_translate("MainWindow", "Data fine scheda:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = scheda_allenamento()
    ui.setupUi(MainWindow,username= "")
    MainWindow.show()
    sys.exit(app.exec_())
