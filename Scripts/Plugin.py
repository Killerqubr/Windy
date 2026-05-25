# Scripts/Plugin.py
import sys
import json
import importlib.util
from pathlib import Path
from typing import Dict, Callable, Optional

class PluginManager:
    
    def __init__(self, plugins_dir: str = "Plugins") -> None:
        "接收目录地址并创建插件列表"
        self.plugins_dir = Path(plugins_dir)
        self.plugins = {}

    def Load(self) -> Dict[str, Callable]:
        "加载插件并返回列表"
        if not self.plugins_dir.exists():
            "插件目录必须存在"
            return {}

        for folder in self.plugins_dir.iterdir():
            if not folder.is_dir():
                "不检查非目录对象"
                continue

            pkg_file = folder / "package.json"
            if not pkg_file.exists():
                "插件必须有package.json"
                continue

            try:
                with open(pkg_file, "r", encoding="utf-8") as f:
                    meta = json.load(f)
            except Exception as e:
                continue

            name = meta.get("name")
            if not name:
                "插件必须有 name 属性"
                continue

            if not meta.get("enabled", True):
                "如果已被禁用则不加载"
                continue

            entry_file = folder / meta.get("main", "main.py")
            if not entry_file.exists():
                "查找入口文件"
                continue

            spec = importlib.util.spec_from_file_location(name, entry_file)
            if not spec or not spec.loader:
                "插件必、、须有页面创建方法"
                continue
            
            "临时将插件目录加入path以便其导入模块"
            plugin_dir = str(folder.absolute())
            sys.path.insert(0, plugin_dir)
            
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
            except Exception as e:
                sys.path.pop(0)
                continue
            sys.path.pop(0)
            # 获取入口函数（默认 create_page）
            entry_point = meta.get("entryPoint", "create_page")
            if not hasattr(module, entry_point):
                print(f"[插件] {name} 没有暴露函数 {entry_point}")
                continue
            func = getattr(module, entry_point)
            if not callable(func):
                print(f"[插件] {name} 的 {entry_point} 不是函数")
                continue

            self.plugins[name] = {"entry": func, "meta": meta}
            print(f"[插件] 加载成功：{name} v{meta.get('version', '?')}")

        # 返回入口函数字典，方便主程序直接使用
        return {name: info["entry"] for name, info in self.plugins.items()}