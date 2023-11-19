class Task:
    valid_values = ["TO_DO", "IN_PROGRESS", "DONE"]

    def __init__(self, task_title, task_description, task_detail, task_status):
        self.task_title = task_title
        self.task_description = task_description
        self.task_detail = task_detail
        if task_status not in Task.valid_values:
            raise ValueError("無効な値です。")
        self.task_status = task_status

    def __repr__(self):
        return "This task' name is {task_title} . task description is {task_description} . task_status is {task_status} ".format(task_title = self.task_title, task_description = self.task_description, task_status = self.task_status)

class Task_manager:
    number_of_task_done = 0

    def __init__(self):
        self.task_list = []

    def task_add(self, task_title, task_description, task_detail, task_status):
        task = Task(task_title, task_description, task_detail, task_status)
        self.task_list.append(task)
    
    def count_task(self):
        return len(self.task_list)

    def status_update(self, task, new_status):
        if new_status not in Task.valid_values:
            raise ValueError("無効な値です。")
        else:
            task.task_status = new_status

        if new_status == "DONE":
            Task_manager.number_of_task_done += 1
    
    def get_all_tasks(self):
        return self.task_list


#初期化コード、初期化していないと__init__内の定義が機能しない
task_zero = Task_manager()
task_zero.task_add("presentaiton","aaaa","presentation","TO_DO")
task_count_zero = task_zero.count_task()
all_tasks_zero = task_zero.get_all_tasks()
# task_show = Task.__repr__()

print(task_count_zero)
print(all_tasks_zero)


# 特定のタスクの task_status を確認
if len(all_tasks_zero) > 0:
    first_task_status = all_tasks_zero[0].task_status
    print("タスクのステータス:", first_task_status)
else:
    print("タスクがありません。")


