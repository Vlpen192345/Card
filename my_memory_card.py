from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle

app = QApplication([])
window = QWidget()
window.resize(500, 300)
window.setWindowTitle('Memo question')
a = QLabel('Каких народов не было?')
h1 = QHBoxLayout()
h2 = QHBoxLayout()

x = QHBoxLayout()
y = QVBoxLayout()
y1 = QVBoxLayout()
ab = QGroupBox('Варианты ответов')
a1 = QRadioButton('Зилоты')
a2 = QRadioButton('Смурфики')
a3 = QRadioButton('Тролли')
a4 = QRadioButton('Ослы')

answers = [a1, a2, a3, a4]

c = QPushButton('Ответить')
y.addWidget(a1)
y.addWidget(a2)
y1.addWidget(a3)
y1.addWidget(a4)

RGroup = QButtonGroup()
RGroup.addButton(a1)
RGroup.addButton(a2)
RGroup.addButton(a3)
RGroup.addButton(a4)

x.addLayout(y)
x.addLayout(y1)
ab.setLayout(x)
h2.addWidget(ab)

abc = QGroupBox('Правильный ответ')
q = QLabel('Смурфики')
q1 = QLabel('Что-то')
s1 = QHBoxLayout()
s2 = QHBoxLayout()
s3 = QHBoxLayout()

v1 = QVBoxLayout()
v1.addWidget(q, alignment = (Qt.AlignHCenter | Qt.AlignHCenter))
v1.addWidget(q1)
s1.addWidget(a)
abc.setLayout(v1)
s2.addWidget(abc)

s3.addWidget(c, stretch = 2, alignment = (Qt.AlignHCenter | Qt.AlignHCenter))
s = QVBoxLayout()
s.addLayout(s1)
s.addLayout(s2)
abc.hide()

s.addLayout(h2)
s.setSpacing(20)
s.addLayout(s3)

s.setSpacing(30)
#s.addLayout(h3)
window.setLayout(s)

def show_result():
    ab.hide()
    abc.show()
    c.setText('Следующий вопрос')

def show_question():
    abc.hide()
    ab.show()
    c.setText('Ответить')
    
    RGroup.setExclusive(False)
    a1.setChecked(False)
    a2.setChecked(False)
    a3.setChecked(False)
    a4.setChecked(False)
    RGroup.setExclusive(True)

def check_ans():
    if answers[0].isChecked():
        show_result()
        q1.setText('Правильно!')
    else:
        show_result()
        q1.setText('Неправильно!')

class Question():
    def __init__(self, question, right_ans, w1, w2, w3):
        self.question = question
        self.right_ans = right_ans
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

def ask(question, right_ans, w1, w2, w3):
    shuffle(answers)
    answers[0].setText(right_ans)
    answers[1].setText(w1)
    answers[2].setText(w2)
    answers[3].setText(w3)
    
    ask.setText('Каких народов не было?')

    show_question()
    show_result()

def start_test():
    if 'Следующий вопрос' == c.text():
        show_question()
    elif 'Ответить' == c.text():
        show_result()  

c.clicked.connect(check_ans)

window.show()
app.exec_()