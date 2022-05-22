from PyQt5.QtWidgets import *
from veritabani import *
from login_qt import login
from anapencerepythonqt import anapencere
import sys


class LoginPage(QMainWindow, login):
    def __init__(self):
        super(LoginPage, self).__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.GirisYap)



    def GirisYap(self):
        username = self.kullanici.text()
        userpassword = self.kullanici_2.text()
        if username == "a" and userpassword == "a":
            anapencere = anapencerePage()
            widget.addWidget(anapencere)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            widget.setFixedWidth(800)
            widget.setFixedHeight(614)




class anapencerePage(QMainWindow, anapencere):
    def __init__(self):
        super(anapencerePage, self).__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.ogrencikaydet)

        self.ogrenci_listele()



    def ogrencikaydet(self):
        ogrenci = self.lineEdit.text()
        yas = self.lineEdit_2.text()
        cinsiyet = self.lineEdit_4.text()
        okul = self.lineEdit_3.text()
        insert(ogrenci, yas, cinsiyet, okul)
        self.ogrenci_listele()

    def ogrenci_listele(self):
        ogrenciler = print_all()
        if ogrenciler != "":
            yazi = ""
            for i in ogrenciler:
                if int(i[2])>15:
                    cikis = "8:00"
                    giris = "23:00"
                else:
                    cikis = "8:00"
                    giris = "19:00"
                yazi += f"{i[0]}  Ad-Soyad: {i[1]}   Yaş: {i[2]}   Cinsiyet: {i[3]}   Okul: {i[4]}  Çıkış: {cikis}  Giriş: {giris}\n"
            self.label_5.setText(yazi)

        else:
            self.label_5.setText('Öğrenciniz bulunmamaktadır')




create_table()
app = QApplication(sys.argv)
pencere = LoginPage()
widget = QStackedWidget()
widget.addWidget(pencere)
widget.show()
widget.setFixedWidth(380)
widget.setFixedHeight(659)
app.exec_()
