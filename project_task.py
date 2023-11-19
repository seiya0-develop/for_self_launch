#新しいタスクを作成するためのクラス
class Task():
    number_of_task = 0
    number_of_task_done = 0

    #新しいタスクを作成
    def __init__(self,task_description,detail,task_title, task_status):
        self.task_title = task_title
        self.task_description = task_description
        self.detail = detail
        self.task_status = task_status

    #タスクのステータスをアップデート
    def status_update(self,newstatus):
        Task.number_of_task_done =+ 1
        self.task_status = newstatus


#最初に作成するタスク情報をユーザーから受け取る
title = input("Gve a name of new task：　")
explanation = input("what is this task for?：　")
detail = input("what should you do exactry ? todo_list or deadline：　")
task_status = input("what is the status of this task?：　")


