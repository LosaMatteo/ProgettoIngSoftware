from PyQt5 import QtCore, QtGui, QtWidgets
from Python.Data.MessageBox import messageBox
from Python.Model.Cliente import Cliente
from Python.Model.Personale import Personale


class change_password(object):
    username = ""
    msg = messageBox()

    def imposta_password(self):
        try:
            objCliente = Cliente()
            objCliente = objCliente.getObject(self.username)
            password1 = self.txtPassword_1.text()
            password2 = self.txtPassword_2.text()
            if password1 == password2:
                if len(password1) > 8:
                    objCliente.password = password1
                    objCliente.scriviLista("./Admin/gestione_cliente/CredenzialiClienti.txt")
                    self.msg.show_popup_ok("Salvataggio password è andato a buon fine.")
                    self.finestre.close()
                else:
                    self.msg.show_popup_ok("La password è troppo corta.")
            else:
                self.msg.show_popup_ok("Le due password sono diverse.")
        except:
            objPersonale = Personale()
            objPersonale = objPersonale.getObject(self.username)
            password1 = self.txtPassword_1.text()
            password2 = self.txtPassword_2.text()
            if password1 == password2:
                if len(password1) > 8:
                    objPersonale.password = password1
                    objPersonale.scriviLista("./Admin/gestione_personale/CredenzialiStaff.txt")
                    self.msg.show_popup_ok("Salvataggio password è andato a buon fine.")
                    self.finestre.close()
                else:
                    self.msg.show_popup_ok("La password è troppo corta.")
            else:
                self.msg.show_popup_ok("Le due password sono diverse.")

    def cancella(self):
        self.txtPassword_1.clear()
        self.txtPassword_2.clear()


    def mostraPassword(self):
        self.txtPassword_2.setEchoMode(QtWidgets.QLineEdit.Normal)

    def nascondiPassword(self):
        self.txtPassword_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def setupUi(self, MainWindow, names):
        self.finestre = MainWindow
        self.username = names
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblPassword_1 = QtWidgets.QLabel(self.centralwidget)
        self.lblPassword_1.setGeometry(QtCore.QRect(30, 60, 191, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPassword_1.setFont(font)
        self.lblPassword_1.setObjectName("lblPassword_1")
        self.lblPassword_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblPassword_2.setGeometry(QtCore.QRect(30, 100, 201, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPassword_2.setFont(font)
        self.lblPassword_2.setObjectName("lblPassword_2")
        self.txtPassword_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword_2.setGeometry(QtCore.QRect(240, 100, 211, 31))
        self.txtPassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword_2.setObjectName("txtPassword_2")
        self.txtPassword_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword_1.setGeometry(QtCore.QRect(240, 60, 211, 31))
        self.txtPassword_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword_1.setObjectName("txtPassword_1")
        self.btnCancella = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancella.setGeometry(QtCore.QRect(270, 150, 75, 24))
        self.btnCancella.setObjectName("btnCancella")
        self.btnSalva = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalva.setGeometry(QtCore.QRect(360, 150, 81, 24))
        self.btnSalva.setObjectName("btnSave")
        self.lblIcona = QtWidgets.QLabel(self.centralwidget)
        self.lblIcona.setGeometry(QtCore.QRect(60, 150, 121, 121))
        self.lblIcona.setText("")
        self.lblIcona.setPixmap(QtGui.QPixmap("./Resources/images/password.png"))
        self.lblIcona.setScaledContents(True)
        self.lblIcona.setObjectName("lblIcona")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/download.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnMostraPassword = QtWidgets.QPushButton(self.centralwidget)
        self.btnMostraPassword.setGeometry(QtCore.QRect(420, 110, 21, 16))
        self.btnMostraPassword.setText("")
        self.btnMostraPassword.setIcon(icon)
        self.btnMostraPassword.setIconSize(QtCore.QSize(20, 20))
        self.btnMostraPassword.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnSalva.clicked.connect(self.imposta_password)
        self.btnCancella.clicked.connect(self.cancella)
        self.btnMostraPassword.pressed.connect(self.mostraPassword)
        self.btnMostraPassword.clicked.connect(self.nascondiPassword)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cambio password"))
        self.lblPassword_1.setText(_translate("MainWindow", "Inserisci la nuova password:"))
        self.lblPassword_2.setText(_translate("MainWindow", "Conferma la nuova password:"))
        self.btnCancella.setText(_translate("MainWindow", "Cancell"))
        self.btnSalva.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = change_password()
    ui.setupUi(MainWindow, names="")
    MainWindow.show()
    sys.exit(app.exec_())
