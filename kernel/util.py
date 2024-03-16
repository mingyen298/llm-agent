import json
from typing import Union
import os


class Util:
    @staticmethod
    def mergeAPIDoc(apis_path: str, out_path: str = os.path.join('.', 'full_doc.json')) -> str:
        doc_list = list()
        for _, dirnames, _ in os.walk(apis_path):
            for dir_name in dirnames:
                if dir_name == 'test':
                    continue
                try:
                    with open(os.path.join(apis_path, dir_name, 'document.json'), 'r') as f:
                        # content = f.read()
                        content = json.load(f)
                        doc_list.append(content)
                    
                except:
                    continue
                print(dir_name)
        with open(out_path, 'w') as f:
            json.dump(obj=doc_list, fp=f)

        return out_path

    @staticmethod
    def deserialize(text: str) -> Union[bool, dict]:
        try:
            return True, json.loads(text)
        except:
            return False, dict()
