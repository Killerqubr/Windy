from pathlib import Path
import json

def LoadCfg(path:str):
    "加载 JSON"
    if not Path(path).exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def SaveCfg(path:str, data):
    "保存 JSON"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def FindFiles(path:str, suffix:str):
    "查找指定路径下的所有指定后缀的文件的文件名"
    p = Path(path)
    return [f.stem for f in p.glob(f"**/*{suffix}")]

# 以下是模块的槽函数
def MD_getStyleSheet(path:str):
    "获取指定路径的样式表内容"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()