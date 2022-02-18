import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pynput import keyboard
import time
import threading
from datetime import datetime


class MyWidget2(QWidget):
    def __init__(self, classhwtest, name):
        QWidget.__init__(self)

        self.welcome = QLabel("Hi, " + name)
        self.tag = QLabel("Here's what you have coming up.")
        self.classarray = classhwtest
        self.welcome.setAlignment(Qt.AlignTop)
        f = QFont("Thasadith", 90)
        f3 = QFont("Thasadith", 30)
        f2 = QFont("Times New Roman", 25)
        f.setBold(True)
        self.welcome.setFont(f)
        self.tag.setFont(f3)

        self.tablex = QTableWidget()
        self.tablex.setFont(f2)
        self.tablex.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablex.setFrameStyle(QFrame.NoFrame)
        header = ["Class", "Time", "Tests", "Homework"]
        self.tablex.setRowCount(5)
        self.tablex.setColumnCount(4)
        for x in range(len(classhwtest)):
            for y in range(len(classhwtest[x])):
                self.tablex.setItem(x, y, QTableWidgetItem(classhwtest[x][y]))
        self.tablex.setHorizontalHeaderLabels(header)
        self.header = self.tablex.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.Stretch)
        self.tablex.resizeColumnsToContents()
        self.tablex.resizeRowsToContents()

        rowTotalHeight = 0;

        count = self.tablex.verticalHeader().count();
        for i in range(count):
            if not self.tablex.verticalHeader().isSectionHidden(i):
                rowTotalHeight += self.tablex.verticalHeader().sectionSize(i);

        if not self.tablex.horizontalScrollBar().isHidden():
            rowTotalHeight += self.tablex.horizontalScrollBar().height();

        if not self.tablex.horizontalHeader().isHidden():
            rowTotalHeight += self.tablex.horizontalHeader().height();

        self.tablex.setMinimumHeight(rowTotalHeight);

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.welcome)
        self.layout.addWidget(self.tag)
        self.layout.addWidget(self.tablex)
        self.layout.insertStretch(-1, 1)
        self.setLayout(self.layout)
        self.tag.setMargin(-2)

    # @Slot()
    def magic(self):
        self.fade(self.welcome)

    def magic2(self):
        self.unfade(self.welcome)

    def resizeEvent(self, event: PyQt5.QtGui.QResizeEvent):
        p = QPalette()
        gradient = QRadialGradient(QPointF((self.size().width()) / 2, (self.size().height()) / 2), 300)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(1.0, QColor(166, 193, 254))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

    def keyPressEvent(self, event):
        print("got a key event of ", QKeySequence(event.key()).toString())
        if QKeySequence(event.key()).toString() == 'F':
            self.fade(self.welcome)
        elif QKeySequence(event.key()).toString() == 'Q':
            self.fade(self.to)
        elif QKeySequence(event.key()).toString() == 'W':
            self.fade(self.swipe)
        elif QKeySequence(event.key()).toString() == 'U':
            self.unfade(self.welcome)


class MyWidget(QWidget):
    def __init__(self, school, widgetx, window):
        QWidget.__init__(self)

        # self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
        # "Hola Mundo", "Привет мир"]

        self.window = window
        self.widgetx = widgetx
        self.button = QPushButton("Click me!")
        self.button2 = QPushButton("No, click me!")
        self.welcome = QLabel("Welcome to")
        self.to = QLabel(school + "!")
        self.swipe = QLabel("Please swipe to continue...")
        self.welcome.setAlignment(Qt.AlignTop)
        self.to.setAlignment(Qt.AlignTop)
        self.swipe.setAlignment(Qt.AlignRight)
        f = QFont("Thasadith", 70)
        f2 = QFont("Thasadith", 50)
        f3 = QFont("Thasadith", 20)
        f.setBold(True)
        f3.setBold(True)
        self.welcome.setFont(f)
        self.to.setFont(f2)
        self.swipe.setFont(f3)

        # self.tablex = QTableWidget()
        # header = ["Class", "Time"]
        # self.tablex.setRowCount(5)
        # self.tablex.setColumnCount(5)
        # self.tablex.setHorizontalHeaderLabels(header)
        # self.tablex.setItem(0, 0, QTableWidgetItem("Math"))

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.welcome)
        self.layout.addWidget(self.to)
        # self.layout.addWidget(self.tablex)
        self.layout.insertStretch(-1, 1)
        self.layout.addWidget(self.swipe)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button.clicked.connect(self.magic)
        self.button2.clicked.connect(self.magic2)

    # @Slot()
    def magic(self):
        self.fade(self.welcome)

    def magic2(self):
        self.window.setCentralWidget(self.widgetx)

    def resizeEvent(self, event: PyQt5.QtGui.QResizeEvent):
        p = QPalette()
        gradient = QRadialGradient(QPointF((self.size().width()) / 2, (self.size().height()) / 2), 300)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(1.0, QColor(166, 193, 254))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

    def keyPressEvent(self, event):
        print("got a key event of ", QKeySequence(event.key()).toString())
        if QKeySequence(event.key()).toString() == 'Return':
            self.window.setCentralWidget(self.widgetx)
        elif QKeySequence(event.key()).toString() == 'Q':
            self.fade(self.to)
        elif QKeySequence(event.key()).toString() == 'W':
            self.fade(self.swipe)
        elif QKeySequence(event.key()).toString() == 'U':
            self.unfade(self.welcome)

    def fade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def unfade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()

    classhwtest = [['History', '8:30 - 9:20', '11/22/19', '11/14/19, 11/20/19'],
                   ['Math', '9:30 - 10:20', '11/22/19', ' '],
                   ['PE', '10:30 - 11:20', ' ', ' '],
                   ['Lunch', '11:30 - 12:30', ' ', ' ']]

    widget2 = MyWidget2(classhwtest, "Sebastian")
    widget = MyWidget("Manhattan College", widget2, window)

    window.setCentralWidget(widget)
    p = QPalette()
    gradient = QRadialGradient(QPointF((window.size().width()) / 2, (window.size().height()) / 2), 600)
    gradient.setColorAt(0.0, QColor(255, 255, 255))
    gradient.setColorAt(1.0, QColor(166, 193, 254))
    p.setBrush(QPalette.Window, QBrush(gradient))
    window.setPalette(p)
    window.showFullScreen()
    print(window.size())

    sys.exit(app.exec_())
