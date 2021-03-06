import os
from os import listdir
from os.path import isfile, join

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QFileDialog
from Model.Cliente import Cliente
from Data.MessageBox import messageBox
import shutil
import os

class dieta_staff(object):
    msg_box = messageBox()
    cliente = Cliente()
    peso = 0

    def allega_file(self):
        try:
            filename = QFileDialog.getOpenFileName()
            return filename[0]
        except(Exception):
            return

    def apri_file(self):
        path = self.allega_file()
        if path != "":
            estensione = path.split(".")
            indice = len(estensione)
            nome_cliente = self.username.replace(" ", "")
            data_odierna = QDate.currentDate().toString()
            data_odierna = data_odierna.replace(" ", "_")
            self.eliminaFileDietaVecchi("./Cliente/Dieta/file_dieta/")
            shutil.copy(path,"./Cliente/Dieta/file_dieta/"+ nome_cliente +"_dieta_personale_"+
                        data_odierna + "." +estensione[indice - 1])
            self.msg_box.show_popup_ok("il file è stato inviato correttamente!")
            self.finestra.close()
        else:
            self.msg_box.show_popup_exception("Errore")

    def eliminaFileDietaVecchi(self, path):
        lista_files = [f for f in listdir(path) if isfile(join(path, f))]
        for elem in lista_files:
            if elem.startswith(self.username.replace(" ", "") + "_dieta_personale_"):
                os.remove(path+elem)

    def popola_dati_fisiologici(self):
        nome_cliente = self.username.replace(" ", "")
        if os.path.exists("./Cliente/Dieta/file_dieta/" + nome_cliente + ".txt"):
            with open ("./Cliente/Dieta/file_dieta/" + nome_cliente + ".txt", "r") as openfile:
                lettura = openfile.readline()
                lettura = lettura.split("-")
                riga = openfile.readline()
                self.lineEdit.setText(lettura[0])
                self.lineEdit_2.setText(lettura[1])
                self.lineEdit_3.setText(lettura[2])
                self.peso = float(lettura[3])
                self.plainTextEdit.setPlainText(riga)
        else:
            return

    def nascondi(self):
        self.label_15.hide()
        self.label_22.hide()
        self.label_23.hide()
        self.label_24.hide()
        self.label_20.hide()
        self.lineEdit_8.hide()
        self.label_21.hide()
        self.lineEdit_9.hide()
        self.label_17.hide()
        self.lineEdit_7.hide()
        self.btnCalcolaNutrienti.hide()
        self.label_18.hide()
        self.label_19.hide()
        self.listWidget_3.hide()

    def appari(self):
        nome_cliente = self.username.replace(" ", "")
        if os.path.exists("./Cliente/Dieta/file_dieta/" + nome_cliente + ".txt"):
            self.plainTextEdit.hide()
            self.label_15.show()
            self.label_22.show()
            self.label_23.show()
            self.label_24.show()
            self.label_20.show()
            self.lineEdit_8.show()
            self.label_21.show()
            self.lineEdit_9.show()
            self.label_17.show()
            self.lineEdit_7.show()
            self.btnCalcolaNutrienti.show()
            self.label_18.show()
            self.label_19.show()
            self.listWidget_3.show()
            self.popola_mostra_suggerimenti()
        else:
            self.msg_box.show_popup_ok('il cliente non ha ancora indicato i dati fisiologici')

    def popola_mostra_suggerimenti(self):
        if self.peso < float(self.lineEdit_2.text()):
            self.label_22.setText("dieta ipercalorica")
            self.label_24.setText("maggiore di " + self.lineEdit_3.text()  + " kcal " )
        else:
            self.label_22.setText("dieta ipocalorica")
            self.label_24.setText("minore di " + self.lineEdit_3.text() + " kcal ")

    def calcola(self):
        try:
            carboidrati = float(self.lineEdit_8.text())
            grassi = float(self.lineEdit_9.text())
            proteine = float(self.lineEdit_7.text())
            fabbisogno = str(carboidrati * 4 + grassi * 9 + proteine * 4)
            self.label_19.setText(fabbisogno + " Kcal ")
        except(Exception):
            self.lineEdit_8.clear()
            self.lineEdit_7.clear()
            self.lineEdit_9.clear()


    def setupUi(self, MainWindow, username):
        self.username = username
        self.finestra = MainWindow
        cliente_nome = self.username.replace(" ", "")
        self.cliente = self.cliente.getObject(cliente_nome)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 567)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(10, 10, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(135, 60, 291, 101))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(166, 39, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 70, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 70, 113, 21))
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 100, 113, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 100, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 130, 113, 21))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 130, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnAllegaFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnAllegaFile.setGeometry(QtCore.QRect(160, 460, 261, 31))
        self.btnAllegaFile.setObjectName("pushButton_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(40, 200, 481, 241))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(50, 210, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(100, 370, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(50, 370, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.btnCalcolaNutrienti = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcolaNutrienti.setGeometry(QtCore.QRect(240, 370, 75, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btnCalcolaNutrienti.setFont(font)
        self.btnCalcolaNutrienti.setObjectName("pushButton_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(130, 370, 91, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(130, 310, 91, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(50, 400, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(350, 400, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(50, 310, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(50, 340, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(130, 340, 91, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(220, 240, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(50, 260, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(120, 290, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.rbtnSuggerimenti = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtnSuggerimenti.setGeometry(QtCore.QRect(40, 180, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.rbtnSuggerimenti.setFont(font)
        self.rbtnSuggerimenti.setObjectName("radioButton")
        self.rbtnNoteCliente = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtnNoteCliente.setGeometry(QtCore.QRect(310, 180, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.rbtnNoteCliente.setFont(font)
        self.rbtnNoteCliente.setObjectName("radioButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 200, 481, 241))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.plainTextEdit.hide()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lblNome.setText(self.username)
        self.nascondi()
        self.rbtnSuggerimenti.clicked.connect(self.appari)
        self.btnAllegaFile.clicked.connect(self.apri_file)
        self.popola_dati_fisiologici()
        self.rbtnNoteCliente.clicked.connect(self.plainTextEdit.show)
        self.btnCalcolaNutrienti.clicked.connect(self.calcola)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblNome.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Faccenda Andrea</p><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Dati fisiologici:</p><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>BMI:</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Peso forma:</p><p><br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Fabbisogno:</p><p><br/></p></body></html>"))
        self.btnAllegaFile.setText(_translate("MainWindow", "Allega file  dieta"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p>Dopo aver analizzato i dati fisiologici-metabolici</p><p> è consigliata una dieta:</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p>Proteine:<br/></p></body></html>"))
        self.btnCalcolaNutrienti.setText(_translate("MainWindow", "CALCOLA"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p>Kcal totali dopo aver inserito le grammature:</p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p>Carboidrati:</p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p>Grassi:</p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p>Con un fabbisogno calorico giornaliero</p><p></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.rbtnSuggerimenti.setText(_translate("MainWindow", "Mostra suggerimenti"))
        self.rbtnNoteCliente.setText(_translate("MainWindow", "Mostra note del cliente"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = dieta_staff()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


