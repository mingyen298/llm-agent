import json
from typing import Union

class Util:
    @staticmethod
    def deserialize(text: str) -> Union[bool, dict]:
        try:
            return True, json.loads(text)
        except:
            return False, dict()