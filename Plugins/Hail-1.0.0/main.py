from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                            QStatusBar, QPushButton)
from PyQt6.QtCore import QTimer
import pyqtgraph as pg
from random import randint
from Widgets.VComboBox import VComboBox
import lib
import time
from Scripts.Signal import Signal_Manager

def create_page(parent):
    "作者/页面设计 Killerqubr | 冰雹猜想计算器(炒冷饭说是)"
    Widget = QWidget(parent)

    def startup_Cal():
        if Flag_Accessable:
 
            Signal_Manager.Logging_Stat.emit('Hail.py触发了信号！', 1000)
            StatusBar.setStyleSheet("color:#535353")
            StatusBar.showMessage(f"正在计算...")
            HailInput.setDisabled(True)
            ProceedButton.setDisabled(True)
            ModeSelector.setDisabled(True)
            HailGraph.clear()

            TStart = time.perf_counter()
            Result = {}
            if int(HailInput.text()) >= 1:
                Result = lib.HailCal(float(HailInput.text()))
            elif int(HailInput.text()) <= -1:
                Result = lib.HailCalN(float(HailInput.text()))
            TFin = time.perf_counter()
            TElapsed = (TFin-TStart)*1000

            StatusBar.setStyleSheet("color:#aaaaaa")
            StatusBar.showMessage(f'计算时间{TElapsed:.0f}ms')

            "更改图表"
            Timer = QTimer(Widget)
            Timer.setInterval(200)

            def Unlocker():
                "撬锁器(bushi"
                HailInput.setDisabled(False)
                ModeSelector.setDisabled(False)
                ProceedButton.setDisabled(False)

            # 熟练使用列表表达式be like:
            GrpX = [i for i in range(0, Result['Steps']+1)]
            curve = HailGraph.plot( pen=pg.mkPen('#bf514e', width=3))
            if ModeSelector.currentText() == '脉冲':
                curve.setData(GrpX, Result['Value'])
                HailGraph.setTitle(f"峰值{int(max(Result['Value']))} / 长度{len(GrpX)-1} {'/ [无限循环的数列]' if Result['IsCyclic'] is True else ''}")
                Unlocker()

            elif ModeSelector.currentText() == '动画化':
                def AnimCal(i, tS):
                    "通过调用自身不断启用singalShot"
                    if i <= Result['Steps']:
                        curve.setData(GrpX[0:i+1], Result['Value'][0:i+1])
                        "需要动画在20秒内完成, 每个间隔最长400ms"
                        AnimDur = (int(20/(Result['Steps']+0.001))*1000) if (int(20/(Result['Steps']+0.001))*1000) <=400 else 400
                        QTimer.singleShot(AnimDur, lambda: AnimCal(i + 1, tS))
                        HailGraph.setTitle(f"动画序列{i}/{Result['Steps']+1} | 当前值{int(Result['Value'][i])} / 当前峰值{int(max(Result['Value'][0:i+1]))} {'/ [无限循环的数列]' if Result['IsCyclic'] is True else ''}")
                    else:
                        HailGraph.setTitle(f"动画序列{i}/{Result['Steps']+1} | 峰值{int(max(Result['Value']))} {'/ [无限循环的数列]' if Result['IsCyclic'] is True else ''}")
                        TFin = time.perf_counter()
                        TElapsed = (TFin-TStart)*1000
                        StatusBar.showMessage(f'动画时间{TElapsed:.0f}ms')
                        Unlocker()

                TStart = time.perf_counter()
                AnimCal(0, TStart)
                return
    
    # 一个旗子;判断是否能进行计算...就是个优化代码结构的东西
    Flag_Accessable = False

    def value_Check():
        "QLineEdit的内容更改时触发"
        # * vC内部函数的nonlocal把Flag_Accessable从createHail传到vC内部,
        # * 然后vC的闭包Failure再把这个变量传达其自己内部, 从而在vC和闭包内部都能修改这个外部变量
        nonlocal Flag_Accessable
        def Failure():
            "滴~验证失败"
            nonlocal Flag_Accessable
            Flag_Accessable = False

            ProceedButton.setDisabled(True)
            return
        def Succeed():
            "滴~好人卡"
            nonlocal Flag_Accessable
            Flag_Accessable = True

            ProceedButton.setDisabled(False)
            return Flag_Accessable

        try:
            Input = int(HailInput.text())
            if Input >= 1:
                StatusBar.setStyleSheet("color:#d2d2d2")
                StatusBar.showMessage(f"数字 {HailInput.text()} 可以进行冰雹计算 > 按下回车键/点击按钮开始!")
                Succeed()
            elif Input <= -1:
                StatusBar.setStyleSheet("color:#000000; background-color: white")
                StatusBar.showMessage(f"[负数模式] 数字 {HailInput.text()} 可以进行冰雹计算 > 按下回车键/点击按钮开始!")
                HailGraph.setTitle(f"负数计算下的很多数字都会陷入无限循环,故当有重复的数出现时,计算将停止")
                Succeed()
            else:
                StatusBar.setStyleSheet("color:#bf514e")
                StatusBar.showMessage(f"字符 {HailInput.text()} 无效！")
                Failure()
            if len(str(Input)) >= 309:
                StatusBar.setStyleSheet("color:#bf514e")
                "int类型最高20位 | float类型最高308位"
                StatusBar.showMessage(f"这个数字太大了...")
                Failure()
        except ValueError:
            if HailInput.text() == '':
                StatusBar.setStyleSheet("color:#b2b2b2")
                MessageWouldShow = ['Tips: (catch到一颗冰雹)(threw掉了)', 'Tips: 27是一个很神奇的数字..' 'Tips: 会不会有枫叶猜想呢? (想到了分形)', 'Tips: 从天而降, 砸中了你, 我不是故意~', 'Tips: 负数的3N+1有不少循环体呢! 如-10>-5>-14>-7>-20>-10...']
                StatusBar.showMessage(MessageWouldShow[randint(0,len(MessageWouldShow)-1)])
                HailGraph.setTitle("冰雹计算器 | 版本1.0")
                Failure()
                return
            StatusBar.setStyleSheet("color:#bf514e")
            StatusBar.showMessage(f"字符 {HailInput.text()} 无效！")
            Failure()

    Layout = QVBoxLayout()
    if True:

        Toolbar = QHBoxLayout()
        if True:
            HailInput = QLineEdit(Widget)
            HailInput.setPlaceholderText("试着输入一个整数...")
            HailInput.setMaxLength(309)
            HailInput.returnPressed.connect(startup_Cal)
            HailInput.textChanged.connect(value_Check)

            HailGraph = pg.plot()
            HailGraph.setBackground('#242424')
            HailGraph.showGrid(x=True, y=True)
            HailGraph.setMouseEnabled(x=False, y=False) 
            HailGraph.setTitle("冰雹计算器 | 版本1.0")

            ModeSelector = VComboBox(Widget)
            ModeSelector.addItem('脉冲')
            ModeSelector.addItem('动画化')

            ProceedButton = QPushButton("计算")
            ProceedButton.setObjectName("SingalShot")
            ProceedButton.setDisabled(True)
            ProceedButton.pressed.connect(startup_Cal)

            Toolbar.addWidget(HailInput)
            Toolbar.addWidget(ModeSelector)
            Toolbar.addWidget(ProceedButton)

        StatusBar = QStatusBar()
        StatusBar.showMessage("作者 Killerqubr(代码/页面设计) | 版本1.0")

    Layout.addLayout(Toolbar)
    Layout.addWidget(HailGraph)
    Layout.addWidget(StatusBar)

    "返回构造结果"
    Widget.setLayout(Layout)
    return Widget