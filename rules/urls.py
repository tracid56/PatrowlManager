# -*- coding: utf-8 -*-

"""URL routes for alerting rules."""

from django.conf.urls import url

from django.urls import path
from . import views, apis


alertrule_list = apis.AlertRuleSet.as_view({
    'get': 'list',
    'post': 'create'
})

alertrule_detail = apis.AlertRuleSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

alertrule_enable = apis.AlertRuleSet.as_view({
    'get': 'enable'
})

alertrule_disable = apis.AlertRuleSet.as_view({
    'get': 'disable'
})

alertrule_duplicate = apis.AlertRuleSet.as_view({
    'get': 'duplicate'
})

urlpatterns = [
    # API Views
    # ex: /rules/api/v1/alerting/list
    url(r'^api/v1/alerting/list$',
        apis.list_alerting_rules_api, name='list_alerting_rules_api'),
    # ex: /rules/api/v1/alerting/1
    url(r'^api/v1/alerting/by-id/(?P<rule_id>[0-9]+)$',
        apis.get_alerting_rule_api, name='get_alerting_rule_api'),
    # ex: /rules/api/v1/delete
    url(r'^api/v1/delete$',
        apis.delete_rules_api, name='delete_rules_api'),
    # ex: /rules/api/v1/delete/1
    url(r'^api/v1/delete/(?P<rule_id>[0-9]+)$',
        apis.delete_rule_api, name='delete_rule_api'),
    # ex: /rules/api/v1/add
    url(r'^api/v1/add$',
        apis.add_rule_api, name='add_rule_api'),
    # ex: /rules/api/v1/duplicate/3
    url(r'^api/v1/alerting/duplicate/(?P<rule_id>[0-9]+)$',
        apis.duplicate_rule_api, name='duplicate_rule_api'),
    # ex: /rules/api/v1/change_status/3
    url(r'^api/v1/change_status/(?P<rule_id>[0-9]+)$',
        apis.toggle_rule_status_api, name='toggle_rule_status_api'),
    # ex: /rules/api/v1/send/slack
    # url(r'^api/v1/send/slack$',
    #     apis.send_slack_message_api, name='send_slack_message_api'),


    # AlertRule
    path('api/v1/alertrule/', alertrule_list, name='alertrule-list'),
    path('api/v1/alertrule/<int:pk>/', alertrule_detail, name='alertrule-detail'),
    path('api/v1/alertrule/<int:pk>/enable/', alertrule_enable, name='alertrule-enable'),
    path('api/v1/alertrule/<int:pk>/disable/', alertrule_disable, name='alertrule-disable'),
    path('api/v1/alertrule/<int:pk>/duplicate/', alertrule_duplicate, name='alertrule-duplicate'),

    # WEB Views
    # ex: /rules/list
    url(r'^list$', views.list_rules_view, name='list_rules_view'),
    url(r'^alerts/list$', views.list_alertrules_view, name='list_alertrules_view'),

]
