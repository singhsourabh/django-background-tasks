from background_task import background
from task.models import Todo

@background(schedule=1)
def add_todo(count):
    for i in range(count):
        Todo.objects.create(name='task'+ str(i))