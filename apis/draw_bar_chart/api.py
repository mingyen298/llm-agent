import matplotlib.pyplot as plt
import os
from kernel.task import TaskResult, TaskExecResult


def api(args:dict)->TaskResult:
    task_result = TaskResult()
    column = args.get('column',False)
    if isinstance(column,bool):
        task_result.exec_result = TaskExecResult.FAIL
        return task_result
    df = args.get('df',False)
    if isinstance(df,bool):
        task_result.exec_result = TaskExecResult.FAIL
        return task_result
    plt.figure(figsize=(8, 6))
    df[column].value_counts().plot(kind='bar')
    plt.xlabel(column)
    plt.ylabel('count')
    # plt.title('Target bar chart')

    # 確定圖片保存路徑，這裡將圖片保存在臨時目錄下
    image_dir = '.'
    image_path = os.path.join(image_dir, f'API_1_bar_chart.png')
    plt.savefig(image_path)
    plt.close()  # 關閉 plt 對象釋放資源s

    task_result.val = image_path
    task_result.exec_result = TaskExecResult.SUCCESS

    return task_result

output = api(args=input)