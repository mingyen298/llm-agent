from kernel.parser import TaskParser
from kernel.runner import TaskRunner
from kernel.tool_management import ToolManagement
import pandas

output_tasks = '''[{"tool":"add","id":0,"dep":[-1],"args":{"x":5,"y":100}},{"tool":"sub","id":1,"dep":[0],"args":{"x":"<resource>-0","y":10}}]'''
mutil_tasks = '''[
    {"tool":"add","id":0,"dep":[-1],"args":{"x":5,"y":10}},
    {"tool":"add","id":1,"dep":[0],"args":{"x":9,"y":"<resource>-0"}},
    {"tool":"multiply","id":2,"dep":[1],"args":{"x":"<resource>-1","y":10}},
    {"tool":"sub","id":3,"dep":[2],"args":{"x":"<resource>-2","y":6}}
]'''
if __name__ == "__main__":
    tool_management = ToolManagement("./apis")
    parser = TaskParser(tool_management=tool_management)
    runner = TaskRunner()

    tg = parser.run(mutil_tasks)
    if tg.is_runnable:
        print("yes")
        runner.run(task_group=tg)
    else:
        print("no")

    # print(p.run(test_data))
    # print(p.run(test_data_circled))
    # print(p.run(test_data_circled2))
    # print(p.run(test_data2))
    # print(p.run(test_data3))
    # print(p.run(test_data3_circled))
    # print(p.run(test_data_mut_input))
    # print(p.run(test_data_mut_input_and_output))
