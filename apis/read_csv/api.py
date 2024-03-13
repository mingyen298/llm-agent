import pandas as pd
from kernel.task import TaskResult, TaskExecResult
import os

def api(args:dict)->TaskResult:
    # os.system("which python")
    task_result = TaskResult()
    count = args.get('count',False)
    if isinstance(count,bool):
        task_result.exec_result = TaskExecResult.FAIL
        return  task_result
    csv_path = "/home/mingyen/Desktop/SideProject/Toolformer/test_maintenance.csv"
    df = pd.read_csv(csv_path)
    # 篩選出指定範圍的 UDI
    df_filtered = df.head(n=count)
    
    task_result.val = df_filtered
    task_result.exec_result = TaskExecResult.SUCCESS

    return task_result  # 返回篩選後的數據
# def api(args:dict)->TaskResult:
#     # os.system("which python")
#     task_result = TaskResult()
#     count = args.get('count',False)
#     if isinstance(count,bool):
#         task_result.exec_result = TaskExecResult.FAIL
#         return  task_result
#     csv_path = "/home/mingyen/Desktop/SideProject/Toolformer/test_maintenance.csv"
#     df = pd.read_csv(csv_path)
#     # 篩選出指定範圍的 UDI
#     df_filtered = df.head(n=count)
#     # df_filtered['type']
#     task_result.val = df_filtered[['Type','Air temperature [K]']]
#     task_result.exec_result = TaskExecResult.SUCCESS

#     return task_result  # 返回篩選後的數據
output = api(args=input)