class Task:
    #クラス変数はどこからでもアクセス可能
    valid_values = ["TO_DO", "IN_PROGRESS", "DONE"]

    def __init__(self, task_title, task_description, task_detail, task_status):
        self.task_title = task_title
        self.task_description = task_description
        self.task_detail = task_detail
        if task_status not in Task.valid_values:
            raise ValueError("invalid value")
        self.task_status = task_status

    def __repr__(self):
        return "This task' name is {task_title} . task description is {task_description} . task_status is {task_status} ".format(task_title = self.task_title, task_description = self.task_description, task_status = self.task_status)

class Task_manager:
    number_of_task_done = 0

    def __init__(self):
        self.task_list = []
        #   self.task_dict = {}
    
    def __repr__(self):
        return "To manege Task." 

    def task_add(self, task_title, task_description, task_detail, task_status):
        task = Task(task_title, task_description, task_detail, task_status)
        self.task_list.append(task)
        # self.task_dict[task] = task
    
    def count_task(self):
        return len(self.task_list)
    
    def del_task(self,task_number):
        del self.task_list[task_number]
        
    def new_status(self,task_number,new_status):
        if new_status not in Task.valid_values:
            raise ValueError("無効な値です。")
        else:
            try:
                task_number < len(self.task_list)
                self.task_list[task_number].task_status = new_status
            except:
                pass
        
# Task_manager.number_of_task_done += 1
    
    def status_update(self,update_task):
        pass

    
    def get_all_tasks(self):
        return self.task_list


print("trial code is start from here")
print("========================")

#初期化コード、初期化していないと__init__内の定義が機能しない
task_zero = Task_manager()
task_zero.task_add("presentaiton","aaaa","presentation","TO_DO")
task_zero.task_add("presentaitonb","bbbb","nnnnn","TO_DO")

task_count_zero = task_zero.count_task()
all_tasks = task_zero.get_all_tasks()

print(task_count_zero)
print(all_tasks)
print(Task.valid_values)


#特定のタスクの task_status を確認
if len(all_tasks) > 0:
    task_zero_status = all_tasks[0].task_status
    print("task status : ", task_zero_status)
else:
    print("No task")

#クラス内の属性とメソッドのリストを表示
print(dir(Task_manager))

#特定のタスクのステータスをアップデートして表示
task_zero_new_status = task_zero.new_status(0,"DONE")
print(task_zero_new_status)


# all_tasks[0].task_status = task_zero_new_status
# print(all_tasks[0].task_status)

print("trial code is end up here")
print("========================")


# ＝＝＝＝＝＝＝＝＝

# task_title, task_description, task_detail, task_status


#最初のタスクを作成します
one_title = input("task_name here : ")
one_description = input("what is the description of this Task ? : ")
one_task_detail = input("please write here detail of this Task : ")
one_task_status = input("Already  this task is decided to do ? : ")

task_one = Task_manager()
task_one.task_add(one_title,one_description,one_task_detail,one_task_status)


if len(all_tasks) > 0:
    task_one_count = task_one.count_task()
    print("The number of task is :", task_one_count)
else:
    print("No task")


#二つ目のタスクを作成します
two_title = input("task_name here : ")
two_description = input("what is the description of this Task ? : ")
two_task_detail = input("please write here detail of this Task : ")
two_task_status = input("Already  this task is decided to do ? : ")


task_one.task_add(two_title,two_description,two_task_detail,two_task_status)


if len(all_tasks) > 0:
    task_one_count = task_one.count_task()
    print("The number of task is :", task_one_count)
else:
    print("NO task")

current_all_task = task_one.get_all_tasks()

#すべてのタスクの現在のステータスを表示します。

for i, task in enumerate(current_all_task):
    print("task" + current_all_task[i].task_title + " is new status : [" + current_all_task[i].task_status+ "]")


print("task_status update is needed ? : ") 
task_one_update_target = int(input("which task? : "))
task_one_update = input("what is the new status of this task ? : ") 
 
task_one.new_status(task_one_update_target,task_one_update)

# current_all_task[int(task_one_update_target)].task_status = task_one_update
# print("タスク" + current_all_task[int(task_one_update_target)].task_title + " の新しいステータスは[" + task_one_update + "] です。")
print("task" + str(current_all_task[task_one_update_target].task_title) + " is new status : [" + str(current_all_task[task_one_update_target].task_status) + "]")


task_one_delete = int(input("would you like to delete task ? : "))

task_one.del_task(task_one_delete)
# del current_all_task[task_one_delete]

if len(all_tasks) > 0:
    task_one_count = task_one.count_task()
    print("The number of task is :", task_one_count)
else:
    print("No task")
