
import queue

from enum import Enum, auto

class TaskExecResult(Enum):
    DEFAULT = auto()
    SUCCESS = auto()
    FAIL = auto()

class Task:
    def __init__(self, id: int, name: str, args: dict,code:str):
        self._id = id
        self._name = name
        self._args = args
        self._code = code
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def args(self):
        return self._args
    @property
    def code(self):
        return self._code

class TaskGroup:
    def __init__(self):
        self._queue = queue.Queue()
        self._is_runnable = False
        self._input_tasks = list()
        self._output_tasks = list()

    @property
    def is_runnable(self):
        return self._is_runnable

    @is_runnable.setter
    def is_runnable(self, is_runnable: bool):
        self._is_runnable = is_runnable

    @property
    def input_tasks(self):
        return self._input_tasks

    @input_tasks.setter
    def input_tasks(self, input_tasks: list[int]):
        self._input_tasks = input_tasks

    @property
    def output_tasks(self):
        return self._output_tasks

    @output_tasks.setter
    def output_tasks(self, output_tasks: list[int]):
        self._output_tasks = output_tasks

    def add(self, task: Task):
        self._queue.put(task)

    def pop(self) -> Task:
        return self._queue.get()

    def empty(self) -> bool:
        return self._queue.empty()





class TaskResult:
    def __init__(self):
        self._exec_result = TaskExecResult.DEFAULT
        self._val = None
    @property
    def exec_result(self):
        return self._exec_result
    @exec_result.setter
    def exec_result(self,result:TaskExecResult):
        self._exec_result = result
    @property
    def val(self):
        return self._val
    @val.setter
    def val(self,val:any):
        self._val = val