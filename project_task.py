from enum import Enum

#タスクのステータス管理のためのクラス
class Task_status(Enum):
    status1 = "TO_DO"
    status2 = "IN_PROGRESS"
    status3 = "DONE"

# print(Task_status.__members__.values())

#新しいタスクを作成するためのクラス
class Task:

    #keep track of number of task
    number_of_task = 0
    #keep track of number of task_done
    number_of_task_done = 0

    #新しいタスクを作成
    def __init__(self, task_title, task_description, task_detail, task_status):
        self.task_title = task_title
        self.task_description = task_description
        self.task_detail = task_detail
        #入力できる3つのステータス以外に文字列が入ってこないか判定
        if task_status not in Task_status.__members__.values():
            raise ValueError("無効な値です。")
        # else:
        self.task_status = task_status
        Task.number_of_task += 1
        
    #タスクのステータスをアップデート
    def status_update(self,new_status):
        
        #入力できる3つのステータス以外に文字列が入ってこないか判定
        if new_status not in Task_status.__members__.values():
            raise ValueError("無効な値です。")
        else:
            self.task_status = new_status

        if new_status == "DONE":
            Task.number_of_task_done += 1
        

task_zero = Task("presentaiton","aaaa","presentation","TO_DO")
print(task_zero.task_status)
print(task_zero.number_of_task)


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



