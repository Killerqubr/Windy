from PyQt6.QtCore import QObject, pyqtSignal

class GlobalSignal(QObject):
    "**单例模式** 全局信号管理"
    
    "底部状态栏Logging信息"
    Logging_Stat = pyqtSignal(str, int)
    
"这个实例在任何地方都可以使用...Python真神奇啊"
Signal_Manager = GlobalSignal()