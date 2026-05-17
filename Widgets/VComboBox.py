from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import pyqtSignal, Qt

class VComboBox(QComboBox):
    "重载的自定义QComboBox"

    # PyQt6中使用 pyqtSignal定义信号
    sig_popup = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.view().window().setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint) # type: ignore
        self.view().window().setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground) # type: ignore

    def showPopup(self) -> None:
        self.sig_popup.emit()
        super().showPopup()
        
        # 返回 popup 所在的顶级窗口
        popup = self.view().window() # type: ignore
        popup.move(popup.x(), popup.y()+4) # type: ignore