# coding=utf-8
import base64
import json
from time import sleep

from django.http import JsonResponse
from blueking.component.shortcuts import get_client_by_request
from apitest.models import Script, Operation


def test(request):
    """
    测试接口
    """
    return JsonResponse({'result': True, 'message': 'hello', 'data': 'hello'})


def search_business(request):
    """
    查找业务
    """
    client = get_client_by_request(request)
    result = client.cc.search_business()

    biz = []
    if result.get('result', False):
        for info in result['data']['info']:
            biz.append({
                'id': info['bk_biz_id'] or info['bid'],
                'name': info['bk_biz_name']
            })

    return JsonResponse({'result': True, 'data': biz})


def get_user(request):
    """
    获取用户
    """
    user_name = request.user.username
    return JsonResponse({'result': True, 'data': user_name})


def search_host(request):
    """
    查找主机
    """
    data_json = json.loads(request.body)
    bk_biz_id = data_json.get('bk_biz_id')

    client = get_client_by_request(request)
    kwargs = {"bk_biz_id": bk_biz_id}
    result = client.cc.search_host(kwargs)

    bk_host_ips = []
    if result.get('result', False):
        for info in result['data']['info']:
            bk_host_ips.append(
                {"ip": info['host']['bk_host_innerip'],
                 "os_name": info['host']['bk_os_name']}
            )

    return JsonResponse({'result': True, 'data': bk_host_ips})


def get_task(request):
    """
    获取任务
    """
    scripts = Script.objects.values()
    # 结果是QuerySet，需要转为list
    script_list = []
    for script in scripts:
        script_list.append(script)

    return JsonResponse({'result': True, 'data': script_list})


def fast_execute_script(request):
    """
    执行脚本
    """
    client = get_client_by_request(request)
    data_json = json.loads(request.body)

    script_param = data_json.get('script_param')
    bk_biz_id = data_json.get('bk_biz_id')
    ip_lists = data_json.get('ip_list')
    task_id = data_json.get('task_id')
    user = data_json.get('user')

    biz = get_biz_name(bk_biz_id, request)
    # [{'name': '实验专用业务'}]
    for re in biz:
        biz_name = re['name']
    if task_id != '':
        script_obj = Script.objects.get(id=task_id)
    else:
        return JsonResponse({'result': False, 'data': 'Task is Empty'})

    ip_list = []
    if len(ip_lists) > 0:
        for ip in ip_lists:
            ip_list.append({
                "bk_cloud_id": 0,
                "ip": ip['ip']
            })
    else:
        return JsonResponse({'result': False, 'data': 'Ip is Empty'})

    script = script_obj.script_content.format(script_param)
    encode_str = base64.b64encode(script.encode("utf-8"))
    script_content = str(encode_str, 'utf-8')
    kwargs = {
        "bk_biz_id": bk_biz_id,
        "script_content": script_content,
        "account": "root",
        "script_type": 1,
        "ip_list": ip_list
    }
    result = client.job.fast_execute_script(kwargs)

    if result.get('result', False):
        kwargs = {
            "bk_biz_id": bk_biz_id,
            "job_instance_id": result['data']['job_instance_id']
        }
    result = client.job.get_job_instance_log(kwargs)

    flag = True
    while flag:
        if result.get('result', False):
            for data in result['data']:
                if data['is_finished'] is not True:
                    sleep(1)
                    result = client.job.get_job_instance_log(kwargs)
                else:
                    flag = False
                    break

    for data in result['data']:
        operation = Operation()
        operation.status = data['status']
        operation.user = user
        operation.biz = biz_name
        operation.script_id = script_obj.id
        operation.result = result['result']
        operation.machine_numbers = len(ip_list)

        for step_result in data['step_results']:
            operation.log = step_result['ip_logs']
            for ip_log in step_result['ip_logs']:
                operation.start_time = ip_log['start_time']
                operation.end_time = ip_log['end_time']
        operation.save()

    return JsonResponse({'result': True, 'data': result['message']})


def get_biz_name(bk_biz_id, request):
    """
    获取业务名称
    """
    client = get_client_by_request(request)
    result = client.cc.search_business()

    biz = []
    if result.get('result', False):
        for info in result['data']['info']:
            if str(info['bk_biz_id']) == bk_biz_id:
                biz.append({
                    'name': info['bk_biz_name']
                })
                return biz

    return biz


def get_operation(request):
    """
    获取执行记录
    """
    operations = Operation.objects.values()

    operation_list = []
    for operation in operations:
        operation_list.append(operation)

    return JsonResponse({'result': True, 'data': operation_list})
