import pickle
import os
from os import listdir
from os.path import isfile, join


class gestObj(object):

    def popolaLista(self, lista):
        if len(lista) > 0:
            f = []
            for x in lista:
                f.append(x.name + " " + x.surname)
            return f

    def recuperaSalvataggio(self, path, lista):
        if os.path.exists(path) and os.path.getsize(path) != 0:
            with(open(path, "rb")) as openfile:
                while True:
                    try:
                        lista.append(pickle.load(openfile))
                    except EOFError:
                        break

    def addToList(self, obj, lista):
        lista.append(obj)

    def rimuovi(self, strdaeliminare, lista):
        for x in lista:
            if x.name + " " + x.surname == strdaeliminare:
                lista.remove(x)
                break

    def scriviLista(self, path, lista):
        filehandler = open(path, 'wb')
        for x in lista:
            pickle.dump(x, filehandler)

    def getAttributi(self, id, lista):
        for x in lista:
            if x.name + " " + x.surname == id:
                return x



    def getObject(self,id,lista):
        for x in lista:
            if x.name  + x.surname == id:

                return x

    def getObject_message(self,id,lista):
        lista_nuova = []
        for x in lista:
            if x.destinatario == id or x.mittente == id:
                lista_nuova.append(x)
        return lista_nuova

    def getUserPass(self, list):
        credenziali = dict()
        for dati in list:
            credenziali[dati.name+dati.surname] = dati.password
        return credenziali

    def resetpassword(self, name, lista):
        for x in lista:
            if x.name + " " + x.surname == name:
                x.password = "1234"
                return

    def popolaListaAttrezzi(self, listaAtt):
        if len(listaAtt) > 0:
            f = []
            for x in listaAtt:
                f.append(x)
            return f

    def addToListAtt(self, obj, lista):
        lista.append([obj.descr, obj.data_ac, obj.quantita, obj.pr_uni, obj.data_man])

    def rimuoviAttrezzo(self, riga, lista):
        lista.remove(lista[riga])

    def get_lista(self,lista):
        vett = []
        for elem in lista:
             vett.append(elem.name+elem.surname)
        return vett

    def rimuovi_messaggio(self, obj, lista):
        for x in lista:
            if x.mittente == obj.mittente and x.destinatario == obj.destinatario and x.contenuto == obj.contenuto and \
                    x.data == obj.data:
                lista.remove(x)
                break

    def rimuoviPrenotazioni(self, username, path):
        newlist = []
        newlist.clear()
        oldlist = []
        oldlist.clear()
        listafiles = [f for f in listdir(path) if isfile(join(path, f))]
        for file in listafiles:
            with open(path + file, "r") as openfile:
                oldlist = openfile.readlines()
                for elem in oldlist:
                    if elem.replace("\n", "") != username:
                        newlist.append(elem)
            if len(newlist) > 0:
                with open(path + file, "w") as openfile:
                    openfile.writelines(newlist)
            else:
                os.remove(path + file)
            newlist.clear()
            oldlist.clear()

    def rimuoviFiles(self, path, username):
        listafiles = []
        listafiles.clear()
        listafiles = [f for f in listdir(path) if isfile(join(path, f))]
        for file in listafiles:
            if file[:-4] == username:
                os.remove(path+file)




