from kernel.parser import TaskParser
from kernel.runner import TaskRunner
from kernel.tool_management import ToolManagement
from kernel.util import Util
from dotenv import load_dotenv
import os
from openai import OpenAI
from typing import Union


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

    # user_input1 = 'Take 1 to 100 pieces of process temperature data, calculate the number of each temperature, and finally draw it as a pie chart.'
    # user_input1 = 'Take 30 to 100 pieces of process temperature data, calculate the number of each temperature, and finally draw it as a bar chart.'

    while True:
        print("Enter instructions:")
        user_input = input()
    
        # print(input)
        task_list = findDep(user_input,system_prompt=find_dep_prompt)
        print(f'''call api:\n{task_list}''')
        result =  fillArgs(user_input=user_input,task_list=task_list)

        # print(result)




        tg = parser.run(result)
        if tg.is_runnable:
            # print("yes")
            runner.run(task_group=tg)
        else:
            print("no")
