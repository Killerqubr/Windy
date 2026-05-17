from PyQt6.QtWidgets import (QSizePolicy, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QGroupBox,
                            QScrollArea, QPushButton, QLabel, QTextEdit)
from PyQt6.QtCore import Qt
from Widgets.VComboBox import VComboBox
import Scripts

def createSettings(parent):
    "内置StackedWidget"

    def createItem(Type , Data: dict, parent:QWidget):
        '把Item的创建封装进方法, 方便多次调用'
        BG = QGroupBox(parent)
        BG.setTitle(Data['Title'])
        BG_Info = QLabel(Data['Info'])
        BG_Layout = QHBoxLayout()
        if True:
            BG_Layout.addWidget(BG_Info)
            BG_Layout.addStretch(1)

        def withComboBox():
            BG_CBox = VComboBox()
            if True:
                for item in Data['Items']:
                    BG_CBox.addItem(item)

            # ? 因为我还没想好怎么把这个ComboBox和它的功能绑定在一起, 所以这里直接用if凑合了
            if str(key) == "StyleSheet":
                "查找所有样式文件"
                CSSFile = Scripts.FindFiles("StyleSheets", ".css")
                "先清空原有的东西, 相当于更新列表"
                BG_CBox.clear()
                for css in CSSFile:
                    BG_CBox.addItem(css)
                "更改样式表"
                "找parent笑传之调调用"
                BG_CBox.currentTextChanged.connect(lambda text: BG.parent().parent().parent().parent().parent().setStyleSheet(Scripts.MD_getStyleSheet(f"StyleSheets/{text}.css"))) # type: ignore
                "更改并保存配置文件"
                config[key]['Items'] = CSSFile

            def updateConfig(text, key):
                "更新配置"
                config[key]['Selected'] = text
                config[key]['SelectedIndex'] = BG_CBox.currentIndex()
                "每次更新都会保存"
                Scripts.SaveCfg("Config.json", config)

            BG_CBox.setCurrentIndex(config[key]['SelectedIndex'])
            BG_CBox.currentTextChanged.connect(lambda text, k=key: updateConfig(text, k))
            Scripts.SaveCfg("Config.json", config)

            BG_Layout.addWidget(BG_CBox)
            return BG
            
        BG.setLayout(BG_Layout)
        if Type == 'ComboBox':
            return withComboBox()

    Settings = QWidget(parent)

    Layout = QVBoxLayout()
    if True:

        Toolbar = QHBoxLayout()
        if True:
            SearchLine = QLineEdit(Settings)
            SearchLine.setPlaceholderText("搜索设置项...")

            TypeFilter = VComboBox(Settings)
            TypeFilter.insertItem(0, "按首字母")
            TypeFilter.insertItem(1, "按类型")

            OrderFilter = VComboBox(Settings)
            OrderFilter.insertItem(0, "正序")
            OrderFilter.insertItem(1, "倒序")

            Toolbar.addWidget(SearchLine)
            Toolbar.addWidget(TypeFilter)
            Toolbar.addWidget(OrderFilter)

        SettingsArea = QScrollArea(Settings)
        SA_Widget, SA_Layout = QWidget(Settings), QVBoxLayout()
        SA_Widget.setProperty('Theme', 'Dark')
        SA_Widget.setObjectName("SA_Widget")
        SA_Widget.setMaximumWidth(930)
        SA_Widget.setStyleSheet("QWidget#SA_Widget {background-color:#242424; border-radius:10px}")
        SA_Widget.setLayout(SA_Layout)
        SettingsArea.setWidget(SA_Widget)
        SettingsArea.setWidgetResizable(True)
        SettingsArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        "通过JSON文件读取项目并添加预制组件"
        '有点像Unity Prefab的说'
        config = Scripts.LoadCfg("Config.json")
        for key, item in config.items():
            Item = createItem(item['Type'], {'Title': item['Title']['zh-CN'], 'Info':item['Info'], 'Items':item['Items']}, SA_Widget)
            SA_Layout.addWidget(Item)
        SA_Layout.addStretch(1)

    Layout.addLayout(Toolbar)
    Layout.addWidget(SettingsArea)

    Settings.setLayout(Layout)
    return Settings

