# -*- coding: utf-8 -*-

import django
from django.conf import settings
DJANGO_MAJOR_VERSION =  int(django.__version__.split('.')[0])
if DJANGO_MAJOR_VERSION < 2:
    from django.core.urlresolvers import reverse_lazy
else:
    from django.urls import reverse_lazy

__all__ = (
    'settings',
)


default_settings = {
    'SLACK_CLIENT_ID': None,
    'SLACK_CLIENT_SECRET': None,

    'SLACK_AUTHORIZATION_URL': 'https://slack.com/oauth/authorize',
    'SLACK_OAUTH_ACCESS_URL': 'https://slack.com/api/oauth.access',
    'SLACK_SUCCESS_REDIRECT_URL': reverse_lazy('slack_success'),
    'SLACK_ERROR_REDIRECT_URL': '/',

    'SLACK_SCOPE': 'identify,read,post',
    'SLACK_USER_SCOPE': 'identity.avatar,identity.basic,identity.email,identity.team',

    'SLACK_PIPELINES': [
        'django_slack_oauth.pipelines.log_request',
        'django_slack_oauth.pipelines.slack_user'
    ]
}


class Settings(object):
    def __init__(self, app_settings, defaults):
        for k, v in defaults.items():
            setattr(self, k, getattr(app_settings, k, v))

settings = Settings(settings, default_settings)

