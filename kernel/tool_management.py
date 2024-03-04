
import os


class ToolManagementBase:
    def __init__(self):
        self._cache = dict()

    def get(self, name: str) -> str:
        return NotImplementedError

    def _find(self, name: str) -> str:
        return NotImplementedError


class ToolManagement(ToolManagementBase):
    def __init__(self, path: str):
        super().__init__()
        self._apis_path = path

    def _find(self, name) -> str:
        for _, dir_names, _ in os.walk(self._apis_path):
            for dir in dir_names:
                if dir == name:
                    with open(os.path.join(self._apis_path,dir,"api.py"),"r") as f:
                        
                        return f.read()
        return ""

    def get(self, name: str) -> str:
        if name in self._cache:
            return self._cache[name]
        else:
            val = self._find(name=name)
            self._cache[name] = val
            return val

    def test(self):
        self._find("")


class ToolManagementDB(ToolManagementBase):
    def __init__(self, path: str):
        super().__init__()

    def get(self, name: str):
        pass


if __name__ == "__main__":
    t = ToolManagement("./apis")
    t.test()
