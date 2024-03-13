from kernel.task import TaskResult, TaskExecResult


def api(args: dict) -> TaskResult:
    task_result = TaskResult()
    x = args.get("x", False)
    if isinstance(x,bool):
        task_result.exec_result = TaskExecResult.FAIL
        return task_result
    y = args.get("y", False)
    if isinstance(y,bool):
        task_result.exec_result = TaskExecResult.FAIL
        return task_result
    x = int(x)
    y = int(y)
    task_result.val = x * y
    task_result.exec_result = TaskExecResult.SUCCESS

    return task_result


output = api(args=input)
