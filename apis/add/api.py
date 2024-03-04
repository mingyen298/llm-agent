from kernel.task import TaskResult, TaskExecResult


def add(args: dict) -> TaskResult:
    task_result = TaskResult()
    x = args.get("x", False)
    if not x:
        task_result.exec_result = TaskExecResult.FAIL
        return task_result
    y = args.get("y", False)
    if not y:
        task_result.exec_result = TaskExecResult.FAIL
        return task_result

    task_result.val = x + y
    task_result.exec_result = TaskExecResult.SUCCESS

    return task_result


output = add(args=input)
