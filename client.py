from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
        self.label1 = QLabel("Enter your hostname:", self)
        self.text = QLineEdit(self)
        self.text.move(70, 30)
        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 30)
        
        self.label3 = QLabel("Enter your host IP:", self)
        self.text1 = QLineEdit(self)
        self.text1.move(70, 100)
        self.label3.move(0, 70)
        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 100)

        self.label4 = QLabel("Enter your api key Shodan:", self)
        self.text2 = QLineEdit(self)
        self.text2.move(70, 170)
        self.label4.move(0, 140)
        self.label5 = QLabel("Answer:", self)
        self.label5.move(10, 170)

        self.button = QPushButton("Send", self)
        self.button.move(10, 250)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()



    def __create_url(self, res):
        openstreetmap_url = "https://openstreetmap.org/?mlat-%s&mlon=12"%(res["latitude"], res["longitude"])
        return openstreetmap_url

    def on_click(self):
        hostname = self.text.text()
        ip = self.text1.text()
        key = self.text2.text()

        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname)
            if res:
                self.label2.setText("Answer%s" % (res["Hello"]))
                self.label2.adjustSize()
                self.show()

    def __query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()