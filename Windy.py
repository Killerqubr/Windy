from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QMainWindow, QPushButton,
    QHBoxLayout, QLineEdit, QStackedWidget, QStatusBar)
import Scripts
from Scripts.Signal import Signal_Manager
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
class Windy(QMainWindow):
    "传闻是*繁花世界*中一位心向意义和宇宙的开发者献给**自己**的礼物"
    "作者Killerqubr | 一个图形化的工具集"

    __version__ = '0.4d5.24'
    "重新构建了组件加载方法"

    def __init__(self, parent=None):
        "初始化"
        super().__init__(parent)
        self.setWindowTitle("Windy")
        # TODO 应添加大小自适应方法，按屏幕比例缩放
        self.setFixedSize(1032, 639)
        Scripts.ReadFontFile('Assests/XNSFengTangHaiYanWei.ttf')
        self.initUI()
        self.initPlugins()
        self.initSignal()
    
    def initUI(self):
        "加载UI"
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
        self.Menu = Scripts.Widget_Basic(parent=self, Name='Menu', MinW=55, CSS="QWidget#Menu {border-right: 1px solid #5e5e5e;}", Prpt=('Theme','Dark'))
        self.Menu_Layout = QVBoxLayout()
        self.Menu.setLayout(self.Menu_Layout)
                
        self.Menu_Layout.addStretch(1)

        LoLayout.addWidget(self.Menu)   
        LoLayout.addWidget(self.StackWindow)
        
        self.Logging_StatBar = QStatusBar()

        "设置主要布局"
        Layout.addLayout(HiLayout)
        Layout.addLayout(LoLayout)
        Layout.addWidget(self.Logging_StatBar)

    def initPlugins(self):
        "加载组件"
        from Scripts.Plugin import PluginManager
        mgr = PluginManager("Plugins")
        plugin_funcs = mgr.Load()   # { "插件A": create_page函数, ... }

        for name, create_page in plugin_funcs.items():
            try:
                page = create_page(self)          # 插件自己负责创建 QWidget
                self.StackWindow.addWidget(page)
                btn = QPushButton(name, self.Menu)
                btn.clicked.connect(lambda _, p=page: self.StackWindow.setCurrentWidget(p))
                self.Menu_Layout.addWidget(btn)
            except Exception as e:
                print(f"[插件] 创建页面失败 {name}: {e}")
            self.Menu_Layout.addWidget(btn) # 添加按钮至菜单栏
            "致: 这个工厂方法使用了类内参数，请不要此方法移入其他文件"
            
    def initSignal(self):
        "绑定全局触发信号"
        Signal_Manager.Logging_Stat.connect(lambda msg, t: self.Logging_StatBar.showMessage(msg, t))
            
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