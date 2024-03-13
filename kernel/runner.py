from typing import Union
from .util import Util
from .task import Task, TaskGroup,TaskResult,TaskExecResult
import os
import pandas as pd

class TaskRunner:
    def __init__(self):
        self._resource_map = dict()
    def reset(self):
        pass

    def _saveTaskResult(self,id:int,task_result:TaskResult):
        uni_key = f'<resource>-{id}'
        self._resource_map[uni_key] = task_result.val

    def _processTask(self,task:Task)->TaskResult:
        for k , v in task.args.items():
            if v in self._resource_map:
                task.args[k] = self._resource_map[v]
            
        local_vars = {"input": task.args}
        exec(task.code, globals(), local_vars)
        task_result = local_vars["output"]
        return task_result
    
    def run(self,task_group:TaskGroup):
        temp = None
        while not task_group.empty():
            task = task_group.pop()
            task_result = self._processTask(task=task)
            if task_result.exec_result != TaskExecResult.SUCCESS :
                break
            self._saveTaskResult(id=task.id,task_result=task_result)
            # print()
            temp = task_result.val
            # print(task.id)
        print(temp)