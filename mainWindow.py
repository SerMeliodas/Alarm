from PySide6.QtWidgets import (QMainWindow, QWidget, QLineEdit,
                               QGridLayout, QPushButton)
from alarm import Alarm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000, 500)

        self.centralWidget = QWidget()
        self.mainLayout = QGridLayout()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        self.alarmWidget = Alarm(self)
        self.inputWidget = QLineEdit()
        self.startButton = QPushButton()

        self.mainLayout.addWidget(self.inputWidget)
        self.mainLayout.addWidget(self.startButton)
        self.startButton.clicked.connect(lambda: self.alarmWidget.startTimer(int(self.inputWidget.text())))
