from django.conf.urls import url

from apitest import api, task

urlpatterns = [
    url(r'^$', api.test),
    url(r'^search_business/$', api.search_business),
    url(r'^get_user/$', api.get_user),
    url(r'^search_host/$', api.search_host),
    url(r'^get_task/$', api.get_task),
    url(r'^fast_execute_script/$', api.fast_execute_script),
    url(r'^get_operation/$', api.get_operation),
    url(r'^task/delete_task/$', task.delete_task),
    url(r'^task/get_task_by_id/$', task.get_task_by_id),
    url(r'^task/edit_task/$', task.edit_task),
]

