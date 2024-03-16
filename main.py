from kernel.parser import TaskParser
from kernel.runner import TaskRunner
from kernel.tool_management import ToolManagement
from kernel.util import Util
from dotenv import load_dotenv
import os
from openai import OpenAI
from typing import Union

output_tasks = '''[{"tool":"add","id":0,"dep":[-1],"args":{"x":5,"y":100}},{"tool":"sub","id":1,"dep":[0],"args":{"x":"<resource>-0","y":10}}]'''
mutil_tasks = '''[
    {"tool":"add","id":0,"dep":[-1],"args":{"x":5,"y":10}},
    {"tool":"add","id":1,"dep":[0],"args":{"x":9,"y":"<resource>-0"}},
    {"tool":"multiply","id":2,"dep":[1],"args":{"x":"<resource>-1","y":10}},
    {"tool":"sub","id":3,"dep":[2],"args":{"x":"<resource>-2","y":6}}
]'''

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_KEY", ""))


def readFile(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def combineFillArgsPrompt(user_input: str, task_list: str) -> str:
    fill_args_prompt_1 = \
        '''user_input:
    """
    {0}
    """
    These are the task lists found from user input:
    """
    {1}
    """
    '''.format(user_input, task_list)
    fill_args_prompt_2 = readFile('./prompts/fill_args_part2.txt')
    return fill_args_prompt_1 + fill_args_prompt_2


def findDep(user_input:str,system_prompt:str)->str:
    MODEL = "gpt-3.5-turbo"
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content":user_input},
        ],
        temperature=1,
    )
    return response.choices[0].message.content

def fillArgs(user_input:str,task_list:str)->str:
    fill_args_prompt = combineFillArgsPrompt(
        user_input=user_input, task_list=task_list)
    MODEL = "gpt-3.5-turbo"
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content":fill_args_prompt},
        ],
        temperature=1,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    find_dep_prompt = readFile('./prompts/find_dep.txt')
    tool_management = ToolManagement("./apis")
    parser = TaskParser(tool_management=tool_management)
    runner = TaskRunner()

    user_input1 = 'Take 50 to 100 pieces of air temperature data, calculate the number of each temperature, and finally draw it as a bar chart.'
    # user_input1 = 'Take 50 to 100 pieces of Target data, calculate the number of each target, and finally draw it as a bar chart.'
    user_input2 = 'First add 5 to 100, then add 9, then multiply by 10 and then subtract 90'

    

    task_list = findDep(user_input2,system_prompt=find_dep_prompt)

    result =  fillArgs(user_input=user_input2,task_list=task_list)

    print(result)



    tg = parser.run(result)
    if tg.is_runnable:
        print("yes")
        runner.run(task_group=tg)
    else:
        print("no")
