class Task:
    valid_values = ["TO_DO", "IN_PROGRESS", "DONE"]

    def __init__(self, task_title, task_description, task_detail, task_status):
        self.task_title = task_title
        self.task_description = task_description
        self.task_detail = task_detail
        if task_status not in Task.valid_values:
            raise ValueError("無効な値です。")
        self.task_status = task_status

class Task_manager:
    number_of_task_done = 0

    def __init__(self):
        self.task_list = []

    def task_add(self, task_title, task_description, task_detail, task_status):
        task = Task(task_title, task_description, task_detail, task_status)
        self.task_list.append(task)
    
    def get_task_detail(self):
        self.task_title = Task.task_title
        self.task_description = Task.task_description
        self.task_detail = Task.task_detail
        self.task_status = Task.task_status

    
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
task_zero.count_task
print(task_zero.get_task_detail)
# print(task_zero.task_status)
# print(task_zero.number_of_task)
# print("the current number of tasks done is " + str(task_zero.number_of_task_done))

# task_zero.status_update("DONE")
# print("current task status of task_zero is " + task_zero.task_status)
# print("the current number of tasks done is " + str(task_zero.number_of_task_done))

# #最初に作成するタスク情報をユーザーから受け取る
# title = input("Give a name of new task：　")
# task_description = input("what is this task for?：　")
# detail = input("what should you do exactry ? todo_list or deadline：　")
# task_status = input("what is the status of this task?：　")


# #最初のタスクをインスタンスクラスを作成
# first_task = Task(title,task_description,detail,task_status)


# #2つ目に作成するタスク情報をユーザーから受け取る
# title2 = input("Gve a name of new task：　")
# explanation2 = input("what is this task for?：　")
# detail2 = input("what should you do exactry ? todo_list or deadline：　")
# task_status2 = input("what is the status of this task?：　")

# second_task = Task(title2,explanation2,detail2,task_status2)



