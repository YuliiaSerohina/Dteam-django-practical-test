from django.conf import settings


def settings_context(request):
    return {
        'settings': {
            'DEBUG': settings.DEBUG,
            'LANGUAGE_CODE': settings.LANGUAGE_CODE,
            'TIME_ZONE': settings.TIME_ZONE,
        }
    }
