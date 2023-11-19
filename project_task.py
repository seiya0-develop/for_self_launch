class Task:
    #クラス変数はどこからでもアクセス可能
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

    def New_status(self,new_status):
        if new_status not in Task.valid_values:
            raise ValueError("無効な値です。")
        else:
            self.new_status = new_status
            return self.new_status
        
        # if new_status == "DONE":
        #     Task_manager.number_of_task_done += 1
    
    def status_update(self,update_task):
        pass

    
    def get_all_tasks(self):
        return self.task_list


#初期化コード、初期化していないと__init__内の定義が機能しない
task_zero = Task_manager()
task_zero.task_add("presentaiton","aaaa","presentation","TO_DO")
task_count_zero = task_zero.count_task()
all_tasks = task_zero.get_all_tasks()
# task_show = Task.__repr__()

print(task_count_zero)
print(all_tasks)

print(Task.valid_values)


#特定のタスクの task_status を確認
if len(all_tasks) > 0:
    task_zero_status = all_tasks[0].task_status
    print("タスクのステータス:", task_zero_status)
else:
    print("タスクがありません。")

#クラス内の属性とメソッドのリストを表示
print(dir(Task_manager))

#特定のタスクのステータスをアップデートして表示
task_zero_new_status = task_zero.New_status("DONE")
print(task_zero_new_status)

all_tasks[0].task_status = task_zero_new_status
print(all_tasks[0].task_status)

