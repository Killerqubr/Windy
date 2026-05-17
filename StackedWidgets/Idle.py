from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QGroupBox,
                            QScrollArea, QPushButton, QLabel, QStackedWidget)
import pyqtgraph as pg
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from Widgets.VComboBox import VComboBox
import Scripts.IdleLib as Lib


def createIdle(parent:QWidget):

    Idle = QWidget(parent)
    Layout = QVBoxLayout()

    def createPage(type:str):
        ScrollArea = QScrollArea()
        SA_Widget, SA_Layout = QWidget(), QVBoxLayout()
        SA_Widget.setProperty('Theme', 'Dark')
        SA_Widget.setObjectName("SA_Widget")
        SA_Widget.setMaximumWidth(930)
        SA_Widget.setStyleSheet("QWidget#SA_Widget {background-color:#242424; border-radius:10px}")
        SA_Widget.setLayout(SA_Layout)

        if type == "Main":
            "摘要栏"
            Abstract_Column = QGroupBox()
            Abstract_Column.setTitle('摘要栏')
            Abstract_Column.setStyleSheet("font-size: 19px")
            if True:
                HLayout = QHBoxLayout()
                VLayout1, VLayout2 = QVBoxLayout(), QVBoxLayout()
                if True:
                    VLayout1.setContentsMargins(20,0,0,0)

                    Label_dt = QLabel()
                    Label_dt.setText("<font face='Latin Modern Math'>dt = 1.00")
                    Label_t = QLabel()
                    Label_t.setText("<font face='Latin Modern Math'>t = 3.00")
                    Label_ft = QLabel()
                    Label_ft.setText("<font face='Latin Modern Math'>f(t) = 0.0000")
                    VLayout1.addWidget(Label_dt)
                    VLayout1.addWidget(Label_t)
                    VLayout1.addWidget(Label_ft)

                HLayout.addLayout(VLayout1)
                HLayout.addLayout(VLayout2)
            Abstract_Column.setLayout(HLayout)

            GraphLayout = QHBoxLayout()
            if True:
                PG_MainFormela, PG_FT = pg.plot(), pg.plot()
                PG_MainFormela.setBackground("#242424")
                PG_FT.setBackground("#242424")
                PG_MainFormela.setMouseEnabled(x=False, y=False) 
                PG_FT.setMouseEnabled(x=False, y=False)
                PG_MainFormela.showGrid(x=True, y=True, alpha=0.3)
                PG_FT.showGrid(x=True, y=True, alpha=0.3)
                PG_MainFormela.setFixedHeight(300)
                PG_FT.setFixedHeight(300)

                GraphLayout.addWidget(PG_MainFormela)
                GraphLayout.addWidget(PG_FT)

            SA_Layout.addWidget(Abstract_Column)
            SA_Layout.addLayout(GraphLayout)
            for i in range(0,10):
                SA_Layout.addWidget(QLabel(f'{i}'))

        elif type == "Help":
            Document = QLabel()
            Document.setText(Lib.getText())
            Document.setStyleSheet("font-family: 'Latin Modern Math', '想念是枫糖海盐味', serif; font-size: 18px; color: white;")
            SA_Layout.addWidget(Document)
            SA_Layout.addStretch(1)

        ScrollArea.setWidget(SA_Widget)
        ScrollArea.setWidgetResizable(True)
        ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        return ScrollArea

    if True:
        
        ToolBarWidget = QWidget(Idle)
        ToolBarWidget.setProperty("Theme", "Dark")
        ToolBarWidget.setStyleSheet("QWidget[Theme='Dark'] {background-color: #242424; border-radius: 10px;}")
        Toolbar = QHBoxLayout()
        if True:

            toPG_Main = QPushButton('主界面', Idle)
            toPG_Help = QPushButton('帮助文档', Idle)

            StartRound = QPushButton("开始回合", Idle)
            StartRound.setObjectName("SingalShot")

            Toolbar.addWidget(toPG_Main)
            Toolbar.addWidget(toPG_Help)
            Toolbar.addStretch(1)
            Toolbar.addWidget(StartRound)

            ToolBarWidget.setLayout(Toolbar)

        StackedWidget = QStackedWidget(Idle)
        StackedWidget.setContentsMargins(0,0,0,0)

        PageMain = createPage('Main')
        PageHelp = createPage('Help')
        StackedWidget.addWidget(PageMain)
        StackedWidget.addWidget(PageHelp)
        toPG_Main.clicked.connect(lambda: StackedWidget.setCurrentWidget(PageMain))
        toPG_Help.clicked.connect(lambda: StackedWidget.setCurrentWidget(PageHelp))

    
    Layout.addWidget(ToolBarWidget)
    Layout.addWidget(StackedWidget)

    Idle.setLayout(Layout)
    return Idle
