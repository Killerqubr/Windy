def getText():
    return """<font face='想念是枫糖海盐味'><font size='4'><font color=#bf514e>介绍</font></font><br><br>
    欢迎来到枫'数'增量，一个基于指数增量(Exponential Idle)的增量游戏。<br>你的目标是在指定时间内修改参数来获得大量的金钱。不要被这些数字和符号吓倒，这个游戏非常简单!<br><br>
    <font size='4'><font color=#bf514e>时刻</font></font><br><br>
    这个游戏中的每一秒钟都被划分为<font color=#bf514e>2</font>个时刻，每过一个时刻，t会增加dt/2，函数值也会按照公式更新。<br>
    <font color=#5e5e5e>由于作者比较懒所以砍掉了点击功能（</font><br><br>
    <font size='4'><font color=#bf514e>公式</font></font><br><br>
    这个公式展示了各个数值在每一个时刻的计算方法，公式的右侧使用上方摘要栏中的数值进行运算。<br>
    例如，如果f(t)=10，b=1，x=2，dt=3，右侧将等于<br><br>
    <font face='Latin Modern Math'><font size='4'>f(t) × e<sup>bxdt</sup> = 10 × e<sup>1×2×3</sup><br>
    = 4034.29</font></font><br><br>
    左侧代表的是f(t)的最新值，等号表示了此次更新，所以这一个时刻之后，f(t)的值将会变成4034.29。<br>
    接下来的一个时刻会再次进行同样的运算。你可以购买新的变量和升级来改变这一等式。<br>
    这些值越高，f(t)增加得越快。因此，这个游戏的关键是购买变量和升级，并通过重算增加“b”的值（见下文）<br><br><br><br>"""

def update():
    pass