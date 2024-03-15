from kernel.task import TaskResult, TaskExecResult


def api(args: dict) -> TaskResult:
    task_result = TaskResult()
    data = args.get('data', False)
    if isinstance(data, bool):
        task_result.exec_result = TaskExecResult.FAIL
        return task_result
    column = args.get('column', False)
    if isinstance(data, bool):
        task_result.exec_result = TaskExecResult.FAIL
        return task_result

    target_list = data[column]
    count_dict = target_list.value_counts().to_dict()

    task_result.val = count_dict
    task_result.exec_result = TaskExecResult.SUCCESS
    return task_result
