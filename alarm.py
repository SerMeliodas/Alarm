from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, QUrl
from PySide6.QtMultimedia import QSoundEffect
from stopAlarmWindow import StopAlarmWindow


class Alarm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._timer = QTimer()
        self._timer.timeout.connect(self.onTimerTimeout)

        self._sound = QSoundEffect()
        self._sound.setSource(QUrl.fromLocalFile("613653_12364629-lq.wav"))
        self._sound.setLoopCount(QSoundEffect.Infinite)
        self._sound.setVolume(0.25)

        self._stopWindow = StopAlarmWindow()
        self._stopWindow.stopAlarm.connect(self.stop)

    def startTimer(self, time):
        self._timer.start(time*1000)

    def onTimerTimeout(self):
        self._timer.stop()
        self._sound.play()
        self._stopWindow.show()

    def stop(self):
        self._sound.stop()
        self._stopWindow.close()
