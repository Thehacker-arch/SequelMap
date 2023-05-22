from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import *
import sys

class MainWindow(QWidget):
    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.resize(1457, 684)
        self.setWindowIcon(QtGui.QIcon('C:\\Users\\vishu\\Downloads\\prevent-sql-exploit-icon.ico'))
        self.setWindowTitle("SequelMap")
        self.setStyleSheet("background-color: rgb(52, 54, 56); border-color: rgb(255, 255, 255);")

        label = QLabel("S E Q U E L   M A P", self)
        label.move(520, 10)
        label.setFont(QFont("Alma Mono"))
        label.setStyleSheet("color: rgb(221, 206, 222); font-size: 22px")

        label1 = QLabel("[*] Website URL:", self)
        label1.move(10, 80)
        font = QFont("Roboto Mono")
        font.setBold(True)
        label1.setFont(font)
        label1.setStyleSheet("color: rgb(178, 183, 191); font-size: 18px")

        pixmap = QLabel(self)
        img = QPixmap('C:\\Users\\vishu\\Downloads\\prevent-sql-exploit-icon.ico')
        pixmap.setPixmap(img)
        pixmap.move(10,1)

        borderLine = QLabel(self)
        borderLine.setFont(QFont("Roboto Mono"))
        borderLine.setText("|   [*] ONLINE | Main Proxy: 127.0.0.1:8080 | [+] Donate Here: bc1qhq2q8qeuc80llrex0jjvk26ewvjsmrx6pxewdk | [!] We are not responsible for any kind of misuse.   |")
        borderLine.setStyleSheet("font-size: 15px; color: rgb(200, 200, 200); background-color: rgb(43, 43, 43);")
        borderLine.move(0, 663)

        # MAIN CODE
        self.main = QTextEdit(self)
        self.main.setFont(QFont("Roboto Mono"))
        self.main.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 244, 248); font-size: 18px")
        self.main.resize(810, 518)
        self.main.move(10,120)

        self.urlentry = QLineEdit(self)
        self.urlentry.setFont(QFont("SimSun"))
        self.urlentry.setStyleSheet("color: rgb(23, 28, 29); background-color: rgb(201, 250, 255); font-size: 18px")
        self.urlentry.resize(500, 25)
        self.urlentry.move(190, 80)

        self.scan = QPushButton(self)
        self.font_button = QFont("Robot Mono")
        self.font_button.setBold(True)
        self.scan.setFont(self.font_button)
        self.scan.setStyleSheet("font-size: 15px; color: rgb(255, 255, 255); background-color: rgb(116, 110, 114); border-color: rgb(192, 192, 206);")        
        self.scan.resize(120, 27)
        self.scan.move(700, 80)
        self.scan.setText("S C A N")

        self.show()
        self.scan.clicked.connect(self.do)

    def do(self) -> None:
        url = self.urlentry.text()
        self.main.append(url)
        self.main.append("[INFO]: Vunlerable !!")


app = QApplication(sys.argv)
a = MainWindow()
sys.exit(app.exec_())
