from PyQt5.QtWidgets import QMessageBox


class messageBox(object):



    def show_popup_retry_cancel(self,str):

        self.msg = QMessageBox()
        self.msg.setWindowTitle("Atheneo Fitness")
        self.msg.setText(str)
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)
        self.msg.setDefaultButton(QMessageBox.Retry)
        self.msg.setDetailedText("The details are as follows:")
        self.msg.show()

    def show_popup_ok(self,str):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Atheneo Fitness")
        self.msg.setText(str)
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setDefaultButton(QMessageBox.Retry)
        self.msg.show()

    def show_popup_question(self, str):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Atheneo Fitness")
        self.msg.setText(str)
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msg.setDefaultButton(QMessageBox.No)
        risposta = self.msg.exec_()
        if risposta == QMessageBox.Yes:
            return True
        elif risposta == QMessageBox.No:
            return False

    def show_popup_ok_details(self,str):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Atheneo Fitness")
        self.msg.setText(str)
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setDefaultButton(QMessageBox.Retry)
        self.msg.setDetailedText("la password non può essere lunga piu di 10 caratteri")

        self.msg.show()

    def show_popup_exception(self,str):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Atheneo Fitness")
        self.msg.setText(str)
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setDefaultButton(QMessageBox.Retry)
        self.msg.show()

    def show_popup_listWidget(self,str):

        self.msg = QMessageBox()
        self.msg.setWindowTitle("Atheneo Fitness")
        self.msg.setText("ERRORE")
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setDefaultButton(QMessageBox.Retry)
        self.msg.setDetailedText(str)
        self.msg.show()
