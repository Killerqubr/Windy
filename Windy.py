from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QMainWindow, QPushButton,
    QHBoxLayout, QLineEdit, QStackedWidget, QMessageBox, QDialog)
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
import StackedWidgets as SW
import Scripts
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
class Windy(QMainWindow):
    "传闻是*繁花世界*中一位心向意义和宇宙的开发者献给**自己**的礼物"
    "作者Killerqubr | 一个图形化的工具集"

    __version__ = 'Beta 0.2/5.19'

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Windy")
        self.setFixedSize(1032, 639)
        # TODO 应添加大小自适应方法，按屏幕比例缩放

        "基本Layout和Widget"
        Layout = QVBoxLayout()
        Layout.setContentsMargins(0,0,0,0)
        Layout.setSpacing(0)
        
        CentralLayout = QWidget()
        CentralLayout.setLayout(Layout)
        self.setCentralWidget(CentralLayout)

        "上层布局"
        HiLayout = QHBoxLayout()
        
        # TODO 这里的代码结构待优化
        self.ToolBar = Scripts.Widget_Basic(parent=self, FixedH=60, Name='ToolBar', CSS="QWidget#ToolBar {border-bottom: 1px solid #5e5e5e;}", Prpt=('Theme','Dark'))
        ToolBar_Layout = QHBoxLayout()
        Btn_Quit = QPushButton('退出工具')
        Btn_Quit.setObjectName('SingalShot')
        Btn_Quit.pressed.connect(QApplication.quit)
        ToolBar_Layout.addStretch(1)
        ToolBar_Layout.addWidget(Btn_Quit)
        
        self.ToolBar.setLayout(ToolBar_Layout)
        HiLayout.addWidget(self.ToolBar)
        
        "下层布局"
        LoLayout = QHBoxLayout()
            
        self.StackWindow = QStackedWidget(self)
        self.Menu = Scripts.Widget_Basic(parent=self, Name='Menu', FixedW=55, CSS="QWidget#Menu {border-right: 1px solid #5e5e5e;}", Prpt=('Theme','Dark'))
        self.Menu_Layout = QVBoxLayout()
        self.Menu.setLayout(self.Menu_Layout)
                
        "创建按钮和界面"
        self.createPage(SW.Settings(self), QIcon('Assests/whl.png'), parent=self, ISize=QSize(20,20))
        #self.createPage(SW.Encryption(self), '码', parent=self)
        self.createPage(SW.Hail(self), '冰', parent=self)
        self.Menu_Layout.addStretch(1)

        LoLayout.addWidget(self.Menu)   
        LoLayout.addWidget(self.StackWindow)

        Layout.addLayout(HiLayout)
        Layout.addLayout(LoLayout)

    def createPage(self, Widget:QWidget, QB:QPushButton | str | QIcon, parent:QWidget | None = None, **kwargs) -> None:
        "*工厂方法* 创建页面和按钮使其绑定并添加到布局"
        self.StackWindow.addWidget(Widget) # 添加页面至StackedWidget
        "接受的QB类型: QPushButton | str->仅文字 | QIcon->仅图标"
        "接受的kwargs参数类型: [parent:QWidget, ISize:QSize]"
        if isinstance(QB, str):
            "文本最好只有一个字(考虑到按钮大小)"
            QB = QPushButton(QB, parent)
            QB.clicked.connect(lambda: self.StackWindow.setCurrentWidget(Widget))
        elif isinstance(QB, QIcon):
            # TODO 考虑到图标也可和文字一起做成"带图标的按钮"，故该分支可以优化兼容该组件的创建
            QB = QPushButton(QB, '', parent)
            QB.setIconSize(kwargs['ISize']) if 'ISize' in kwargs else None
        else:
            return
        QB.clicked.connect(lambda: self.StackWindow.setCurrentWidget(Widget)) # 绑定信号
        self.Menu_Layout.addWidget(QB) # 添加按钮至菜单栏
        "致: 这个工厂方法使用了类内参数，请不要此方法移入其他文件"
            
    def mousePressEvent(self, a0) -> None:
        "重写运行时**鼠标点击**事件"
        focused_widget = QApplication.focusWidget()
        "当前点击的控件类不是QLineEdit时, 清除焦点"
        if isinstance(focused_widget, QLineEdit):
            focused_widget.clearFocus()
        QMainWindow.mousePressEvent(self, a0)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    WindyWindow = Windy()

    "加载已保存的样式表"
    config = Scripts.LoadCfg("Config.json")
    if 'StyleSheet' in config:
        style_name = config['StyleSheet']['Selected']  # 获取第一个样式表名称
        try:
            WindyWindow.setStyleSheet(Scripts.MD_getStyleSheet(f"StyleSheets/{style_name}.css"))
        except FileNotFoundError:
            print('样式表加载失败..')

    WindyWindow.show()
    sys.exit(app.exec())