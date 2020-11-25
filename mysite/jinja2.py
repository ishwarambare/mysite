from crispy_forms.templatetags.crispy_forms_filters import as_crispy_form, as_crispy_field
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        "crispy": as_crispy_form,
        "as_crispy": as_crispy_field,
        'url': reverse,
    })
    return env
