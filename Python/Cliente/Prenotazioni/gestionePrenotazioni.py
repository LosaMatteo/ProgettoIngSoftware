import os
from os import listdir
from os.path import isfile, join

from PyQt5.QtCore import QDate

from Python.Data.MessageBox import messageBox


class GestionePrenotazioniCorsi(object):
    msg = messageBox()

    def assegnaAttributi(self, date, time, path):
        path += date
        for elem in time:
            if elem.__contains__("-"):
                numero = elem.split("-")
                for t in numero:
                    path += " " + t
            else:
                path += " " + elem
        path += ".txt"
        return path

    def scriviPrenotazione(self, path, username):
        with open(path, "a") as file:
            file.write(username + "\n")

    def controllaDoppione(self, vett, username):
        for elem in vett:
            if elem[:-1] == username:
                return False
        return True

    def prenota(self, limite_massimo, path, username):
        if os.path.exists(path):
            with open(path, "r") as openfile:
                lettura = openfile.readlines()
            if len(lettura) < limite_massimo and self.controllaDoppione(lettura, username):
                self.scriviPrenotazione(path, username)
                self.msg.show_popup_ok("la tua prenotazione è andata a buon fine.")
            else:
                self.msg.show_popup_ok("Le prenotazioni sono al completo o sei già prenotato per questo turno.")
        else:
            self.scriviPrenotazione(path, username)
            self.msg.show_popup_ok("la tua prenotazione è andata a buon fine.")

    def cmbAttive(self, path):
        if os.path.exists(path):
            with open(path, "r") as openfile:
                lettura = openfile.readlines()
            return len(lettura)
        else:
            return 0

    def elimina(self, path):
        listafiles = [f for f in listdir(path) if isfile(join(path, f))]
        for elem in listafiles:
            if QDate.currentDate() > QDate.fromString(elem[:10], "dd.MM.yyyy"):
                os.remove(path + elem)

    def annullaPrenotazione(self, username, path, data):
        nuova_lista= []
        nuova_lista.clear()
        vecchia_lista = []
        vecchia_lista.clear()
        with open(path + data, "r") as openfile:
            vecchia_lista = openfile.readlines()
            for elem in vecchia_lista:
                if elem.replace("\n", "") != username:
                    nuova_lista.append(elem)
        if len(nuova_lista) > 0:
            with open(path + data, "w") as openfile:
                openfile.writelines(nuova_lista)
        else:
            os.remove(path + data)


    def trovaCliente(self, path, utente):
        listafiles_prenotazioni_utente = []
        listafiles = [f for f in listdir(path) if isfile(join(path, f))]
        for file in listafiles:
            with open(path + file, "r") as openfile:
                lettura = openfile.readlines()
                for elem in lettura:
                    array = elem.split("\n")
                    for str in array:
                        if str == utente:
                            listafiles_prenotazioni_utente.append(file)

        return listafiles_prenotazioni_utente