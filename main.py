from kernel.parser import TaskParser
from kernel.runner import TaskRunner
from kernel.tool_management import ToolManagement
import pandas
test_data = '[{"id":0,"name":"a","args":{},"dep":[-1]},{"id":1,"name":"a","args":{},"dep":[0]},{"id":2,"name":"a","args":{},"dep":[1]},{"id":3,"name":"a","args":{},"dep":[1]},{"id":4,"name":"a","args":{},"dep":[2,3]}]'
test_data_circled = '[{"id":0,"name":"a","args":{},"dep":[4]},{"id":1,"name":"a","args":{},"dep":[0]},{"id":2,"name":"a","args":{},"dep":[1]},{"id":3,"name":"a","args":{},"dep":[1]},{"id":4,"name":"a","args":{},"dep":[2,3]}]'
test_data_circled2 = '[{"id":0,"name":"a","args":{},"dep":[-1]},{"id":1,"name":"a","args":{},"dep":[0]},{"id":2,"name":"a","args":{},"dep":[1]},{"id":3,"name":"a","args":{},"dep":[1,4]},{"id":4,"name":"a","args":{},"dep":[2,3]}]'


# 2 outputs and 1 output
test_data2 = '[{"id":0,"name":"a","args":{},"dep":[-1]},{"id":1,"name":"a","args":{},"dep":[0]},{"id":2,"name":"a","args":{},"dep":[1]},{"id":3,"name":"a","args":{},"dep":[1]}]'
# 3 outputs and 1 output
test_data3 = '[{"id":0,"name":"a","args":{},"dep":[-1]},{"id":1,"name":"a","args":{},"dep":[0]},{"id":2,"name":"a","args":{},"dep":[1]},{"id":3,"name":"a","args":{},"dep":[1]},{"id":4,"name":"a","args":{},"dep":[1]}]'
# 3 outputs and circled
test_data3_circled = '[{"id":0,"name":"a","args":{},"dep":[-1]},{"id":1,"name":"a","args":{},"dep":[0,4]},{"id":2,"name":"a","args":{},"dep":[1]},{"id":3,"name":"a","args":{},"dep":[1]},{"id":4,"name":"a","args":{},"dep":[1,3]}]'

# 2 inputs and 1 output
test_data_mut_input = '[{"id":0,"name":"a","args":{},"dep":[-1]},{"id":1,"name":"a","args":{},"dep":[-1]},{"id":2,"name":"a","args":{},"dep":[0,1]},{"id":3,"name":"a","args":{},"dep":[2]}]'


# 2 inputs and 2 output
test_data_mut_input_and_output = '[{"id":0,"name":"a","args":{},"dep":[-1]},{"id":1,"name":"a","args":{},"dep":[-1]},{"id":2,"name":"a","args":{},"dep":[0,1]},{"id":3,"name":"a","args":{},"dep":[2]},{"id":4,"name":"a","args":{},"dep":[2]}]'

# test_data_1 = '[{"id":0,"name":"add","args":{"x":2,"y":3},"dep":[-1]}]'
test_data_1 = '[{"id":0,"name":"read_csv","args":{"count":20},"dep":[-1]}]'
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
