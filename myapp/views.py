from django.shortcuts import render
from celery_project.celery import add
from myapp.tasks import sub
from celery.result import AsyncResult



# Enqueue Task using delay()
# def index(request):
#     print("Results: ")
#     result1 = add.delay(10, 20)
#     print("Result1: ", result1)
#     result2 = sub.delay(80, 10)
#     print("Result2: ", result2)

    
#     return render(request, "myapp/index.html")

# Enqueue Task using apply_async()

# def index(request):
#     print("Results: ")
#     result1 = add.apply_async(args=[10, 20])
#     print("Result1: ", result1)
#     result2 = sub.apply_async(args=[70, 20])
#     print("Result2: ", result2)

    
#     return render(request, "myapp/index.html")

#  Display  addition value after task execution
def index(request):
    result = add.delay(10, 30)
    print("ready: ", result.ready())
    print("Successful: ", result.successful())
    print("Fail: ", result.failed())
    return render(request, "myapp/index.html", {'result': result})

def check_result(request, task_id):
    # Retrieve the task result using the task_id
    result = AsyncResult(task_id)
    # print("ready: ", result.ready())
    # print("Successful: ", result.successful())
    # print("Fail: ", result.failed())
    return render(request, 'myapp/result.html', {'result':result})


def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")