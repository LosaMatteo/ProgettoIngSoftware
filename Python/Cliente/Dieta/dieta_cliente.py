from PyQt5 import QtCore, QtGui, QtWidgets
from Cliente.Dieta.dieta_chetogenica import dieta_chetogenica
from Cliente.Dieta.dieta_ipercalorica import dieta_ipercalorica
from Cliente.Dieta.dieta_ipocalorica import dieta_ipocalorica
from Data.MessageBox import messageBox
from Model.Cliente import Client


class dieta_cliente(object):
    username = ""
    cliente = Client()
    msg = messageBox()

    def salva_ogg_cliente(self):
        self.cliente = self.cliente.getObject(self.username)
        self.cliente.altezza = str(self.lineEdit_2.text())
        self.cliente.peso = str(self.lineEdit.text())
        self.cliente.eta = str(self.lineEdit_4.text())

    def calcola_bmi(self):
        try:
            altezza = float(self.lineEdit_2.text()) / 100
            peso = float(self.lineEdit.text())
            self.salva_ogg_cliente()
            bmi = peso / (altezza * altezza)
            self.label_3.setText(str(bmi.__round__(2)))
        except Exception:
            self.msg.show_popup_exception("Non hai inserito altezza, peso ed età!")

    def scrivi_su_file(self):
        try:
            file = open("./Cliente/Dieta/file_dieta/" + self.username + ".txt", "w")
            file.write(
                self.label_3.text() + "-" + self.label_6.text() + "-" + self.label_13.text() + "-" + self.lineEdit.text() + "\n")
            file.write(self.plainTextEdit.toPlainText())
            file.close()
            self.msg.show_popup_ok("Dati fisiologici e preferenze salvate")
        except Exception:
            self.msg.show_popup_exception("Errore nel salvataggio")

    def calcola_peso(self):
        try:
            altezza = float(self.lineEdit_2.text()) / 100
            eta = int(self.lineEdit_4.text())
            self.salva_ogg_cliente()
            sesso = self.comboBox.currentText()
            coefficiente_peso_maschio = 100
            coefficiente_peso_femmina = 112
            weight = 0
            if sesso == "maschio":
                weight = 0.8 * (altezza * 100 - coefficiente_peso_maschio) + eta / 2
            elif sesso == "femmina":
                weight = 0.8 * (altezza * 100 - coefficiente_peso_femmina) + eta / 2
            self.label_6.setText(str(weight.__round__(2)))
        except Exception:
            self.msg.show_popup_exception("Non hai inserito altezza, peso ed età!")

    def calcolo_ADS(self):
        lavoro = self.comboBox_2.currentText()
        attivita_fisica = self.comboBox_3.currentText()
        if lavoro == "Lavori edile" or lavoro == "Lavori agricoli" or lavoro == "Operaio/a(pesante)":
            coefficiente_lavoro = 15
        else:
            coefficiente_lavoro = 10

        if attivita_fisica == "oltre 5 ore settimanali":
            coefficiente_attivita = 20
        elif attivita_fisica == "da 3 a 5 ore settimanali":
            coefficiente_attivita = 15
        else:
            coefficiente_attivita = 10
        coefficiente = coefficiente_attivita + coefficiente_lavoro
        return coefficiente

    def calcolo_calorie(self):
        try:
            self.salva_ogg_cliente()
            if self.cliente.gender == "maschio":
                MB = 66 + (13.7 * float(self.cliente.peso)) + (5 * float(self.cliente.altezza)) \
                     - (6.8 * float(self.cliente.eta))
                self.label_10.setText(str(MB.__round__(2)))
                fabbisogno_calorico = 1 * float(self.cliente.peso) * 24
                fabbisogno_calorico += (fabbisogno_calorico * self.calcolo_ADS()) / 100
                self.label_13.setText(str(fabbisogno_calorico.__round__(2)))
                self.label_10.setText(str(MB.__round__(2)))
            elif self.cliente.gender == "femmina":
                MB = 655 + (9.6 * float(self.cliente.peso)) + (1.8 * float(self.cliente.altezza)) \
                     - (4.7 * float(self.cliente.eta))
                self.label_10.setText(str(MB.__round__(2)))
                fabbisogno_calorico = 0.9 * float(self.cliente.peso) * 24
                fabbisogno_calorico += (fabbisogno_calorico * self.calcolo_ADS()) / 100
                self.label_13.setText(str(fabbisogno_calorico.__round__(2)))
                self.label_10.setText(str(MB.__round__(2)))
        except Exception:
            self.msg.show_popup_exception("Non hai inserito altezza, peso ed età!")

    def popola_lista_dieta(self):
        with open("./Cliente/Dieta/file_dieta/dieta.txt", "r") as openfile:
            lettura = openfile.read()
        lettura = lettura.split("\n")
        for elem in lettura:
            self.listWidget.addItem(elem)
            self.listWidget.show()

    def apri_dieta_chetogenica(self):
        self.dieta_chetogenica = QtWidgets.QMainWindow()
        self.ui = dieta_chetogenica()
        self.ui.setupUi(self.dieta_chetogenica)
        self.dieta_chetogenica.show()

    def apri_dieta_ipocalorica(self):
        self.dieta_ipocalorica = QtWidgets.QMainWindow()
        self.ui = dieta_ipocalorica()
        self.ui.setupUi(self.dieta_ipocalorica)
        self.dieta_ipocalorica.show()

    def apri_dieta_ipercalorica(self):
        self.dieta_ipercalorica = QtWidgets.QMainWindow()
        self.ui = dieta_ipercalorica()
        self.ui.setupUi(self.dieta_ipercalorica)
        self.dieta_ipercalorica.show()

    def apri_interfacce(self):
        if self.listWidget.currentItem().text() == "dieta chetogenica":
            self.apri_dieta_chetogenica()
        elif self.listWidget.currentItem().text() == "dieta ipocalorica":
            self.apri_dieta_ipocalorica()
        elif self.listWidget.currentItem().text() == "dieta ipercalorica":
            self.apri_dieta_ipercalorica()

    def setupUi(self, Form, username):
        self.username = username
        Form.setObjectName("Form")
        Form.resize(763, 528)
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(40, 20, 571, 481))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 571, 357))
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 0, 121, 251))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(50, 200, 104, 31))
        self.comboBox.setMaxVisibleItems(2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(80, 120, 71, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 70, 71, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.btnBMI = QtWidgets.QPushButton(self.page)
        self.btnBMI.setGeometry(QtCore.QRect(20, 270, 151, 32))
        self.btnBMI.setObjectName("pushButton")
        self.btnPesoForma = QtWidgets.QPushButton(self.page)
        self.btnPesoForma.setGeometry(QtCore.QRect(330, 270, 151, 32))
        self.btnPesoForma.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(10, 310, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(90, 310, 51, 21))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(150, 310, 51, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(330, 310, 121, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(460, 310, 51, 21))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(520, 310, 41, 21))
        self.label_7.setObjectName("label_7")
        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setGeometry(QtCore.QRect(250, 60, 311, 131))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("./Resources/images/pngDieta/logoMPT.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 160, 71, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 571, 357))
        self.page_2.setObjectName("page_2")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 191, 201))
        self.label_8.setObjectName("label_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 100, 201, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_3.setGeometry(QtCore.QRect(100, 150, 201, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.btnCalorie = QtWidgets.QPushButton(self.page_2)
        self.btnCalorie.setGeometry(QtCore.QRect(50, 200, 113, 31))
        self.btnCalorie.setObjectName("pushButton_3")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(0, 250, 131, 21))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(210, 250, 31, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setGeometry(QtCore.QRect(210, 280, 31, 21))
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(140, 250, 51, 21))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(140, 280, 51, 21))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(0, 280, 131, 21))
        self.label_14.setObjectName("label_14")
        self.label_20 = QtWidgets.QLabel(self.page_2)
        self.label_20.setGeometry(QtCore.QRect(330, 220, 221, 151))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("./Resources/images/pngDieta/calcolo-fabbisogno-calorico.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 571, 357))
        self.page_3.setObjectName("page_3")
        self.listWidget = QtWidgets.QListWidget(self.page_3)
        self.listWidget.setGeometry(QtCore.QRect(240, 60, 261, 192))
        self.listWidget.setObjectName("listWidget")
        self.label_17 = QtWidgets.QLabel(self.page_3)
        self.label_17.setGeometry(QtCore.QRect(10, 30, 211, 101))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page_3)
        self.label_18.setGeometry(QtCore.QRect(30, 130, 171, 121))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("./Resources/images/pngDieta/immagine_dieta.jpeg"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.page_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 50, 441, 261))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_15 = QtWidgets.QLabel(self.page_4)
        self.label_15.setGeometry(QtCore.QRect(30, 10, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.btnSalva = QtWidgets.QPushButton(self.page_4)
        self.btnSalva.setGeometry(QtCore.QRect(412, 327, 111, 21))
        self.btnSalva.setObjectName("pushButton_5")
        self.toolBox.addItem(self.page_4, "")
        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.popola_lista_dieta()
        self.btnBMI.clicked.connect(self.calcola_bmi)
        self.btnPesoForma.clicked.connect(self.calcola_peso)
        self.btnCalorie.clicked.connect(self.calcolo_calorie)
        self.listWidget.clicked.connect(self.apri_interfacce)
        self.btnSalva.clicked.connect(self.scrivi_su_file)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-weight:600;\">Inserisci i tuoi dati:</span><br/></p><p>Altezza(cm): <br/></p><p>Peso(kg):<br/></p><p>Età:<br/></p><p>Sesso:</p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "maschio"))
        self.comboBox.setItemText(1, _translate("Form", "femmina"))
        self.btnBMI.setText(_translate("Form", "Calcola BMI"))
        self.btnPesoForma.setText(_translate("Form", "Calcola Peso Forma"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>Il tuo BMI è: </p></body></html>"))
        self.label_4.setText(_translate("Form", "kg/m2"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p>Il tuo Peso Forma è:</p></body></html>"))
        self.label_7.setText(_translate("Form", "kg"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Calcola BMI e Peso Forma"))
        self.label_8.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">Imposta i seguenti parametri:</span></p><p><br/></p><p>Lavoro:</p><p><br/>Attività Fisica:</p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Form", "Casalingo/a o collaboratore domestico"))
        self.comboBox_2.setItemText(1, _translate("Form", "Commesso/a"))
        self.comboBox_2.setItemText(2, _translate("Form", "Dirigente"))
        self.comboBox_2.setItemText(3, _translate("Form", "Impiegato"))
        self.comboBox_2.setItemText(4, _translate("Form", "Lavori agricoli"))
        self.comboBox_2.setItemText(5, _translate("Form", "Lavori edili"))
        self.comboBox_2.setItemText(6, _translate("Form", "Libero professionista"))
        self.comboBox_2.setItemText(7, _translate("Form", "Operaio/a (leggero)"))
        self.comboBox_2.setItemText(8, _translate("Form", "Operaio/a (pesante)"))
        self.comboBox_2.setItemText(9, _translate("Form", "Studente"))
        self.comboBox_3.setItemText(0, _translate("Form", "Nessuna"))
        self.comboBox_3.setItemText(1, _translate("Form", "fino a 2 ore settimanali"))
        self.comboBox_3.setItemText(2, _translate("Form", "da 3 a 5 ore settimanali"))
        self.comboBox_3.setItemText(3, _translate("Form", "oltre 5 ore settimanali"))
        self.btnCalorie.setText(_translate("Form", "Calcola ora!"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p>Metabolismo basale:</p></body></html>"))
        self.label_11.setText(_translate("Form", "Kcal"))
        self.label_12.setText(_translate("Form", "Kcal"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p>Fabbisogno Calorico:</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2),
                                 _translate("Form", "Calcola Fabbisogno e Metabolismo Basale"))
#        self.lineEdit_3.setPlaceholderText(_translate("Form", "seleziona una dieta"))
        self.label_17.setText(_translate("Form",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Diete che </span></p><p align=\"center\"><span style=\" font-size:12pt;\">potrebbero interessarti</span></p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "Dieta"))
        self.label_15.setText(_translate("Form",
                                         "<html><head/><body><p>Segnala al nutrizionista eventuali allergie o preferenze alimentari:</p><p><br/></p><p><br/></p></body></html>"))
        self.btnSalva.setText(_translate("Form", "Salva"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Form", "Note per il nutrizionista"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = dieta_cliente()
    ui.setupUi(Form, username="")
    Form.show()
    sys.exit(app.exec_())
