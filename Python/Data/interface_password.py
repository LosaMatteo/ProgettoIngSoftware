from PyQt5 import QtCore, QtGui, QtWidgets
from Data.MessageBox import messageBox
from Model.Cliente import Client
from Model.Personale import Personale


class change_password(object):
    username = ""
    msg = messageBox()

    def imposta_password(self):
        try:
            cliente = Client()
            cliente = cliente.getObject(self.username)
            psw = self.lineEdit.text()
            psw2 = self.lineEdit_2.text()
            if psw == psw2:
                if len(psw) > 8:
                    cliente.password = psw
                    cliente.scriviLista("./Admin/gestione_cliente/CredenzialiClienti.txt")
                    self.msg.show_popup_ok("Salvataggio password è andato a buon fine.")
                    self.finestre.close()
                else:
                    self.msg.show_popup_ok("La password è troppo corta.")
            else:
                self.msg.show_popup_ok("Le due password sono diverse.")
        except:

            staff = Personale()
            staff = staff.getObject(self.username)
            psw = self.lineEdit.text()
            psw2 = self.lineEdit_2.text()
            if psw == psw2:
                staff.password = psw
                staff.scriviLista("./Admin/gestione_personale/CredenzialiStaff.txt")
                self.msg.show_popup_ok("Salvataggio password è andato a buon fine.")
                self.finestre.close()
            else:
                self.msg.show_popup_ok("Le due password sono diverse.")


    def cancel(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def hide_password(self):
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)


    def hide_password_return(self):
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    def hide_password_2(self):
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)

    def hide_password_return_2(self):
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def setupUi(self, MainWindow, names):
        self.finestre = MainWindow
        self.username = names
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblpsw = QtWidgets.QLabel(self.centralwidget)
        self.lblpsw.setGeometry(QtCore.QRect(30, 60, 191, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblpsw.setFont(font)
        self.lblpsw.setObjectName("lblpsw")
        self.lblpsw_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblpsw_2.setGeometry(QtCore.QRect(30, 100, 201, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblpsw_2.setFont(font)
        self.lblpsw_2.setObjectName("lblpsw_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 100, 211, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 60, 211, 31))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(270, 150, 75, 24))
        self.btnCancel.setObjectName("btnCancel")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(360, 150, 81, 24))
        self.btnSave.setObjectName("btnSave")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 150, 121, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./Resources/images/password.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(420, 70, 21, 20))
        self.pushButton_7.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/download.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 110, 21, 16))
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_8.setObjectName("pushButton_8")
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
        self.btnSave.clicked.connect(self.imposta_password)
        self.btnCancel.clicked.connect(self.cancel)
        self.pushButton_7.pressed.connect(self.hide_password)
        self.pushButton_7.clicked.connect(self.hide_password_return)
        self.pushButton_8.pressed.connect(self.hide_password_2)
        self.pushButton_8.clicked.connect(self.hide_password_return_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblpsw.setText(_translate("MainWindow", "Inserisci la nuova password:"))
        self.lblpsw_2.setText(_translate("MainWindow", "Conferma la nuova password:"))
        self.btnCancel.setText(_translate("MainWindow", "Cancell"))
        self.btnSave.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = change_password()
    ui.setupUi(MainWindow, names="")
    MainWindow.show()
    sys.exit(app.exec_())
