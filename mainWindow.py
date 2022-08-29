from PySide6.QtWidgets import (QMainWindow, QWidget, QLineEdit,
                               QGridLayout, QPushButton, QDateTimeEdit)
from alarm import Alarm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000, 500)
        self.setWindowTitle(u"Alarm")

        self.centralWidget = QWidget()
        self.mainLayout = QGridLayout()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        self.dateInput = QDateTimeEdit()
        self.dateInput.setDisplayFormat("HH:mm")
        self.alarmWidget = Alarm(self)
        self.startButton = QPushButton()
        self.startButton.setText(u"start alarm")

        self.mainLayout.addWidget(self.dateInput)
        self.mainLayout.addWidget(self.startButton)
        self.startButton.clicked.connect(self.start)

    def start(self):
        time = self.dateInput.time()
        print(time.hour()*60+time.minute())
        self.alarmWidget.startTimer(time.hour()*60+time.minute())
