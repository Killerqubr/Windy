"Windy用到的方法"
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

def ReadQSS(path:str) -> str:
    "读取并返回指定路径的样式表"
    with open(path, "r",encoding='utf-8') as f:
        return f.read()
    
def Widget_Basic(parent:QWidget | None = None, **kwargs) -> QWidget:
    "*工厂方法* 通过参数创建最基本的QWidget组件"
    Widget = QWidget(parent)
    "接受的kwargs参数类型: [FixedH, FixedW:int; FixedS, Prpt:tuple; Name, CSS:str]"
    try:
        Widget.setFixedHeight(kwargs['FixedH']) if 'FixedH' in kwargs else None
        Widget.setFixedWidth(kwargs['FixedW']) if 'FixedW' in kwargs else None
        Widget.setFixedSize(kwargs['FixedS']) if 'FixedS' in kwargs else None
        
        Widget.setObjectName(kwargs['Name']) if 'Name' in kwargs else None
        Widget.setStyleSheet(kwargs['CSS']) if 'CSS' in kwargs else None
        Widget.setProperty(kwargs['Prpt'][0], kwargs['Prpt'][1]) if 'Prpt' in kwargs else None
    except:
        return Widget
        # ! 如果某一个参数设置失败(比如传递的Prpt不是tuple)，在其之后的设置会停止并返回Widget
        # ! 可能造成一些难以解释的样式bug，故在此声明
    
    "一般运用于如菜单栏、工具栏等无依赖性QWidget的创建"
    return Widget

def Advanced_aW(layout:QHBoxLayout | QVBoxLayout, **kwargs:list[QWidget | QVBoxLayout | QHBoxLayout]) -> None:
    "一次性将载入的参数添加到Layout中"
    "接受的kwargs参数类型: [aW:list, aH:list]"
    if 'aW' in kwargs:
        for Item in kwargs['aW']:
            layout.addWidget(Item) if isinstance(Item, QWidget) else None
    if 'aH' in kwargs:
        for Item in kwargs['aH']:
            layout.addLayout(Item) if isinstance(Item, QVBoxLayout | QHBoxLayout) else None
    else:
        ...