import queue

from typing import Union
from .util import Util
from .task import Task, TaskGroup
from .tool_management import ToolManagementBase


class TaskParser:
    def __init__(self, tool_management: ToolManagementBase):
        self._tool_management = tool_management

    def topological_sort(self, graph: list[str]) -> Union[bool, list[int], list[int], list[int]]:

        n = len(graph)

        ordered_list = []

        # 建立新的表
        out_degrees_table = dict()
        adj_list = dict()
        in_degrees_counter_table = [0] * n
        visited = []
        output_nodes = []
        input_nodes = []
        q = queue.Queue()

        for v in graph:
            id = v["id"]
            dep = v["dep"]

            for i in dep:
                if not i in adj_list:
                    adj_list[i] = []
                adj_list[i].append(id)

                key = f'{i}->{id}'
                if i == -1:
                    in_degrees_counter_table[id] = 0
                    q.put(id)
                    visited.append(id)
                else:
                    out_degrees_table[key] = 1
                    in_degrees_counter_table[id] = len(dep)

        for i in range(0, len(graph)):
            if not i in adj_list:
                adj_list[i] = []
                output_nodes.append(i)

        # print(out_degrees_table)
        # print(adj_list)
        # print(in_degrees_counter_table)
        # print(visited)
        while not q.empty():

            cur_id = q.get()

            for next_id in adj_list[cur_id]:

                key = f'{cur_id}->{next_id}'

                if key in out_degrees_table:

                    in_degrees_counter_table[next_id] -= 1

                    if in_degrees_counter_table[next_id] == 0:

                        q.put(next_id)
                        visited.append(next_id)
            ordered_list.append(cur_id)

        if len(visited) == n:
            return True, ordered_list, input_nodes, output_nodes
        else:
            return False, ordered_list, input_nodes, output_nodes

    def run(self, text: str) -> TaskGroup:
        task_group = TaskGroup()
        task_group.is_runnable = True
        ok, task_list = Util.deserialize(text=text)
        if not ok:
            task_group.is_runnable = False
            return task_group
        ok, ordered_tasks, input_tasks, output_tasks = self.topological_sort(
            graph=task_list)
        if not ok:
            task_group.is_runnable = False
            return task_group

        for id in ordered_tasks:
            task_dict = task_list[id]
            code = self._tool_management.get(task_dict["name"])
            if code == "":
                task_group.is_runnable = False
                break
            task = Task(
                id=id, name=task_dict["name"], args=task_dict["args"], code=code)
            task_group.add(task=task)

        task_group.input_tasks = input_tasks
        task_group.output_tasks = output_tasks
        return task_group
