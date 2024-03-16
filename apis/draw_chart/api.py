import pandas as pd
import matplotlib.pyplot as plt
import os
from kernel.task import TaskResult, TaskExecResult


def api(args: dict) -> TaskResult:
    task_result = TaskResult()

    result = args.get("result", False)
    if isinstance(result, bool):
        task_result.exec_result = TaskExecResult.FAIL
        return task_result
    chart_type = args.get("chart_type", False)
    if isinstance(chart_type, bool):
        task_result.exec_result = TaskExecResult.FAIL
        return task_result

    result_series = pd.Series(result)
    # 建立繪圖物件
    plt.figure(figsize=(8, 6))
    # 繪製柱狀圖
    result_series.plot(kind=chart_type)
    for i, v in enumerate(result_series):
        plt.text(i, v + 0.2, str(v), ha='center')
    # 建立保存圖片的目錄（如果不存在）
    image_dir = '.'
    # os.makedirs(image_dir, exist_ok=True)
    # 保存圖像並關閉繪圖物件
    image_path = os.path.join(image_dir, 'bar_chart.png')

    plt.savefig(image_path)
    plt.close()

    task_result.val = image_path
    task_result.exec_result = TaskExecResult.SUCCESS

    return task_result



output = api(args=input)