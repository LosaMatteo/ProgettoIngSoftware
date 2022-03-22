from PyQt5 import QtCore, QtGui, QtWidgets
from Data.MessageBox import messageBox
from Model.Admin import admin
from Model.Cliente import Client
from Admin.GUI_Admin import GUI_Admin
from Cliente.GUI_client import GUI_client
from Model.Personale import Personale
from Staff.GUI_staff import GUI_staff


class Ui_ATHENEO(object):

    objClient = Client()
    objPersonale = Personale()
    admin1 = admin("admin","1")
    listaaccessi = []


    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = GUI_Admin()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_windowCL(self,names):
        self.GUI_client = QtWidgets.QMainWindow()
        self.ui = GUI_client()
        self.ui.setupUi(self.GUI_client,names)
        self.GUI_client.show()

    def open_window_admin(self,names):
        self.GUI_Admin = QtWidgets.QMainWindow()
        self.ui = GUI_Admin()
        self.ui.setupUi(self.GUI_Admin,names)
        self.GUI_Admin.show()

    def cancel(self):
        self.lblError.setText("")
        self.txtBox_user.setText("")
        self.txtBox_psw.setText("")

    def open_window_staff(self,names):
        self.GUI_staff = QtWidgets.QMainWindow()
        self.ui = GUI_staff()
        self.ui.setupUi(self.GUI_staff,names)
        self.GUI_staff.show()

    def split_line(self):
        self.objClient.recuperaSalvataggio("./Admin/gestione_cliente/CredenzialiClienti.txt")
        self.objPersonale.recuperaSalvataggio("./Admin/gestione_personale/CredenzialiStaff.txt")
        self.listaaccessi.clear()
        credenziali_admin = dict()
        credenziali_admin[self.admin1.username] = self.admin1.password
        self.listaaccessi.append(credenziali_admin)
        self.listaaccessi.append(self.objPersonale.getClCred())
        self.listaaccessi.append(self.objClient.getClCred())

    def login_check(self):
        datiaccesso = []
        datiaccesso.clear()
        self.metodo = messageBox()
        self.lblError.setText("")
        user = self.txtBox_user.text()
        if user[-1] == " ":
            user = user[:-1]
        psw = self.txtBox_psw.text()
        i = 0

        for elem in self.listaaccessi:
            for usernames in elem.keys():
                if usernames == user and elem[usernames] == psw:
                    datiaccesso.append(i)
                    datiaccesso.append(user)
                    return datiaccesso
            i+=1
        datiaccesso.append(-1)
        return datiaccesso

    def login(self):
        datiaccesso = self.login_check()
        if datiaccesso[0] == 0:

            self.open_window_admin(datiaccesso[1])
            self.finestra.close()
        elif datiaccesso[0] == 1:
            self.open_window_staff(datiaccesso[1])
            self.finestra.close()
        elif datiaccesso[0] == 2:
            self.open_windowCL(datiaccesso[1])
            self.finestra.close()
        else:
            self.metodo.show_popup_retry_cancel("username o password errata.")

    def hide_password(self):
        self.txtBox_psw.setEchoMode(QtWidgets.QLineEdit.Normal)

    def hide_password_return(self):
        self.txtBox_psw.setEchoMode(QtWidgets.QLineEdit.Password)

    def setupUi(self, ATHENEO):
        self.finestra = ATHENEO
        ATHENEO.setObjectName("ATHENEO")
        ATHENEO.resize(867, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ATHENEO.sizePolicy().hasHeightForWidth())
        ATHENEO.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        ATHENEO.setFont(font)
        ATHENEO.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ATHENEO)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(190, 20, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.lblUser = QtWidgets.QLabel(self.centralwidget)
        self.lblUser.setGeometry(QtCore.QRect(230, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblUser.setFont(font)
        self.lblUser.setObjectName("lblUser")
        self.txtBox_user = QtWidgets.QLineEdit(self.centralwidget)
        self.txtBox_user.setGeometry(QtCore.QRect(330, 160, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.txtBox_user.setFont(font)
        self.txtBox_user.setText("")
        self.txtBox_user.setObjectName("txtBox_user")
        self.lblPsw = QtWidgets.QLabel(self.centralwidget)
        self.lblPsw.setGeometry(QtCore.QRect(230, 220, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblPsw.setFont(font)
        self.lblPsw.setObjectName("lblPsw")
        self.txtBox_psw = QtWidgets.QLineEdit(self.centralwidget)
        self.txtBox_psw.setGeometry(QtCore.QRect(330, 220, 201, 31))
        self.txtBox_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtBox_psw.setObjectName("txtBox_psw")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(280, 280, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.lblInfo = QtWidgets.QLabel(self.centralwidget)
        self.lblInfo.setGeometry(QtCore.QRect(220, 380, 521, 16))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblInfo.setFont(font)
        self.lblInfo.setObjectName("lblInfo")
        self.lblLogo = QtWidgets.QLabel(self.centralwidget)
        self.lblLogo.setGeometry(QtCore.QRect(580, 80, 201, 101))
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap("Resources/images/palestra.jpg"))
        self.lblLogo.setObjectName("lblLogo")
        self.lblError = QtWidgets.QLabel(self.centralwidget)
        self.lblError.setGeometry(QtCore.QRect(300, 100, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lblError.setFont(font)
        self.lblError.setText("")
        self.lblError.setObjectName("lblError")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(440, 280, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(500, 230, 21, 16))
        self.pushButton_7.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/images/pngGUI_client/download.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_7.setObjectName("pushButton_7")
        ATHENEO.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ATHENEO)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 21))
        self.menubar.setObjectName("menubar")
        ATHENEO.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ATHENEO)
        self.statusbar.setObjectName("statusbar")
        ATHENEO.setStatusBar(self.statusbar)

        self.retranslateUi(ATHENEO)
        QtCore.QMetaObject.connectSlotsByName(ATHENEO)
        self.split_line()
        self.btnLogin.clicked.connect(self.login)
        self.btnCancel.clicked.connect(self.cancel)
        self.pushButton_7.pressed.connect(self.hide_password)
        self.pushButton_7.clicked.connect(self.hide_password_return)


    def retranslateUi(self, ATHENEO):
        _translate = QtCore.QCoreApplication.translate
        ATHENEO.setWindowTitle(_translate("ATHENEO", "ATHENEO - Login"))
        self.lblTitle.setText(_translate("ATHENEO", "ATHENEO  FITNESS  CLUB"))
        self.lblUser.setText(_translate("ATHENEO", "Username"))
        self.lblPsw.setText(_translate("ATHENEO", "Password"))
        self.btnLogin.setText(_translate("ATHENEO", "Login"))
        self.lblInfo.setText(_translate("ATHENEO", "Atheneo Fitness Club, Via Washington 25, Pizzo Calabro, RC"))
        self.btnCancel.setText(_translate("ATHENEO", "Cancella"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ATHENEO = QtWidgets.QMainWindow()
    ui = Ui_ATHENEO()
    ui.setupUi(ATHENEO)
    ATHENEO.show()
    sys.exit(app.exec_())

