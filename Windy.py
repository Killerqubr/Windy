from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QMainWindow, QPushButton,
    QHBoxLayout, QLineEdit, QStackedWidget
)
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
import Scripts, StackedWidgets

class Windy(QMainWindow):
    "*现代化UI*的工具箱"
    "传闻这是Killerqubr花费了无数心思做出的前端作品"

    __version__ = '2026/5/18 | Beta0.1'

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Windy")
        self.setFixedSize(1032, 639)

        Layout = QVBoxLayout()
        Layout.setContentsMargins(0,0,0,0)
        Layout.setSpacing(0)

        if True:
            HiLayout = QHBoxLayout()
            if True:
                ToolBar = QWidget(self)
                ToolBar.setFixedHeight(80)
                ToolBar.setObjectName("ToolBar")
                ToolBar.setStyleSheet("QWidget#ToolBar {background-color: #242424; border-bottom: 1px solid #5e5e5e;}")
                HiLayout.addWidget(ToolBar)
                
            LoLayout = QHBoxLayout()
            if True:
                self.Menu = QWidget(self)
                self.Menu.setObjectName("Menu")
                self.MainLayout = QVBoxLayout()
                if True:
                # 遍历文件来添加按钮
                    self.OpenSettings = QPushButton(QIcon("Assests/whl.png"), '', self.Menu)
                    self.OpenSettings.setIconSize(QSize(20,20))
                    self.OpenHail = QPushButton("冰", self.Menu)
                    self.MainLayout.addWidget(self.OpenSettings)
                    self.MainLayout.addWidget(self.OpenHail)
                    self.MainLayout.addStretch(1)

                self.Menu.setStyleSheet("QWidget#Menu {background-color: #242424; border-right: 1px solid #5e5e5e;}")
                self.Menu.setFixedWidth(55)

                self.Menu.setLayout(self.MainLayout)
                LoLayout.addWidget(self.Menu)

                self.StackWindow = QStackedWidget(self)
                

                if True:
                    SettingPage = StackedWidgets.createSettings(self.StackWindow)
                    HailPage = StackedWidgets.createHail(self.StackWindow)

                    self.createStackedPages(SettingPage, self.OpenSettings)
                    self.createStackedPages(HailPage, self.OpenHail)

                LoLayout.addWidget(self.StackWindow)

        CentralLayout = QWidget()
        CentralLayout.setLayout(Layout)
        self.setCentralWidget(CentralLayout)

        Layout.addLayout(HiLayout)
        Layout.addLayout(LoLayout)

    def createStackedPages(self, Page:QWidget, Button:QPushButton):
        self.StackWindow.addWidget(Page)
        Button.clicked.connect(lambda: self.StackWindow.setCurrentWidget(Page))

    def mousePressEvent(self, a0):
        "重写鼠标点击事件"
        focused_widget = QApplication.focusWidget()
        "当前点击的控件不是LineEdit时, 清除焦点"
        if isinstance(focused_widget, QLineEdit):
            focused_widget.clearFocus()
        QMainWindow.mousePressEvent(self, a0)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    WindyWindow = Windy()

    # 加载已保存的指定样式表
    config = Scripts.LoadCfg("Config.json")
    if 'StyleSheet' in config:
        style_name = config['StyleSheet']['Selected']  # 获取第一个样式表名称
        try:
            WindyWindow.setStyleSheet(Scripts.MD_getStyleSheet(f"StyleSheets/{style_name}.css"))
        except FileNotFoundError:
            print('样式表加载失败..')

    WindyWindow.show()
    sys.exit(app.exec())