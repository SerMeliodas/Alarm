from PySide6.QtWidgets import QPushButton, QHBoxLayout
from PySide6.QtCore import Signal


class StopAlarmWindow(QPushButton):
    stopAlarm = Signal()

    def __init__(self, parent = None):
        super().__init__(parent)

    def mouseReleaseEvent(self, e):
        self.stopAlarm.emit()
