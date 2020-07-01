# coding=utf-8
import json

from django.http import JsonResponse

from apitest.models import Script


def delete_task(request):
    """
    删除任务
    """
    data_json = json.loads(request.body)
    task_id = data_json.get('task_id')
    script = Script.objects.get(id=task_id)
    script.delete()

    scripts = Script.objects.values()
    script_list = []
    for script in scripts:
        script_list.append(script)

    return JsonResponse({'result': True, 'data': script_list})


def get_task_by_id(request):
    """
    通过任务id获取任务
    """
    data_json = json.loads(request.body)
    task_id = data_json.get('task_id')
    script = Script.objects.values().filter(id=task_id)

    for tmp in script:
        data = tmp

    return JsonResponse({'result': True, 'data': data})


def edit_task(request):
    """
    编辑/添加任务
    """
    data_json = json.loads(request.body)
    task_id = data_json.get('task_id')
    if task_id != '':
        script = Script.objects.get(id=task_id)
    else:
        script = Script()

    task_name = data_json.get('task_name')
    task_content = data_json.get('task_content')
    task_params = data_json.get('task_params')
    task_desc = data_json.get('task_desc')

    script.script_name = task_name
    script.script_content = task_content
    script.default_params = task_params
    script.script_desc = task_desc
    script.save()

    return JsonResponse({'result': True, 'data': "success"})