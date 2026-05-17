"Windy用到的方法"

def ReadQSS(path:str):
    "**读取并返回指定路径的样式表**"
    with open(path, "r",encoding='utf-8') as f:
        return f.read()