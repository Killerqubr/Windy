from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QGroupBox,
                            QScrollArea, QLabel)
from PyQt6.QtCore import Qt
from Widgets.VComboBox import VComboBox
import Scripts

def Encryption(parent:QWidget | None):
    "*工厂方法* 页面Encryption构造"
    Widget = QWidget(parent)
    Layout = QVBoxLayout()
    
    

    "返回"
    Widget.setLayout(Layout)
    return Widget

