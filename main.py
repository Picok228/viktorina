import random

from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(1000,600)

lbl = QLabel("Вікторина")
numberlbl = QLabel("Номер переможця")
startBtn = QPushButton("Дізнатися переможця")

main_line = QVBoxLayout()
main_line.addWidget(lbl)
main_line.addWidget(numberlbl)
main_line.addWidget(startBtn)


window.setLayout((main_line))


def banana():
    a = random.randint(1,10)
    numberlbl.setText(str(a))

startBtn.clicked.connect(banana)
window.show()
app.exec()