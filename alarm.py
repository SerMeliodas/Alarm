import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtCore import QTimer, QUrl
from PySide6.QtMultimedia import QSoundEffect


class Alarm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._timer = QTimer()
        self._timer.timeout.connect(self.onTimerTimeout)
        self._sound = QSoundEffect()
        self._sound.setSource(QUrl.fromLocalFile("613653_12364629-lq.wav"))
        self._sound.setLoopCount(QSoundEffect.Infinite)
        self._sound.setVolume(0.25)

    def startTimer(self, time):
        self._timer.start(time*1000)

    def onTimerTimeout(self):
        self._timer.stop()
        self._sound.play()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000,500)
        self.alarmWidget = Alarm(self)
        self.inputWidget = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
