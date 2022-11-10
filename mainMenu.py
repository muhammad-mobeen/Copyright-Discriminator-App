from curses import window
import random
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

from image_scraper import *


def transfer(search_txt):
    app.exec()
    ImgScrap = ImagesScraper()
    ImgScrap(search_txt)

widgets = {
    "scrap_label": [],
    "scrap_textbox": [],
    "scrap_btn": [],
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Scrapinator")
# window.setFixedWidth(800)
# window.setFixedHeight(500)
window.setMinimumSize(800,500)
window.setStyleSheet("background: #161219;")
grid = QGridLayout()



def frame1():
    # Scrap Label
    scrap_label = QLabel("Enter search term:")
    scrap_label.setAlignment(QtCore.Qt.AlignRight)
    scrap_label.setWordWrap(True)
    scrap_label.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 75px;"
    )
    widgets["scrap_label"].append(scrap_label)

    # Search Textbox
    scrap_textbox = QLineEdit()
    place_lst = ["Faisal Mosque", "Pakistan Monument", "Naran Kaghan", "Minar e Pakistan"]
    scrap_textbox.setPlaceholderText(place_lst[random.randint(0, len(place_lst)-1)])
    scrap_textbox.setStyleSheet(
        "background: #2a2130;" +
        "font-size: 20px;" +
        "color: white;" +
        "border: None;"
    )
    widgets["scrap_textbox"].append(scrap_textbox)

    # Scrap Button
    scrap_btn = QPushButton("Scrap Images")
    scrap_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    scrap_btn.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 25px;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 25px 0;" +
        "margin: 10px 200px;}" +
        "*:hover{background: '#BC006C';}"
    )
    scrap_btn.clicked.connect(transfer(scrap_textbox.text()))
    widgets["scrap_btn"].append(scrap_btn)

    grid.addWidget(widgets["scrap_label"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["scrap_textbox"][-1], 0, 2, 1, 2)
    grid.addWidget(widgets["scrap_btn"][-1], 1, 0, 1, 4)

frame1()


window.setLayout(grid)

window.show()
sys.exit(app.exec())