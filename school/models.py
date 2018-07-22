from django.db import models
from django.utils import timezone

class JSONField(models.TextField):
    """
    JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly.
    Django snippet #1478

    example:
        class Page(models.Model):
            data = JSONField(blank=True, null=True)


        page = Page.objects.get(pk=5)
        page.data = {'title': 'test', 'type': 3}
        page.save()
    """

    def to_python(self, value):
        if value == "":
            return None

        try:
            if isinstance(value, str):
                return json.loads(value)
        except ValueError:
            pass
        return value

    def from_db_value(self, value, *args):
        return self.to_python(value)

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None
        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder)
        return value

class Nome(models.Model):

    nome = models.CharField(max_length=100)

    declinazione = models.CharField(
        max_length=45,
        choices=(
            [
                ('prima declinazione (ae)', 'prima declinazione (ae)'),
                ('seconda declinazione (i)', 'seconda declinazione (i)'),
                ('terza declinazione (is)', 'terza declinazione (is)'),
                ('quarta declinazione (us)', 'quarta declinazione (us)'),
                ('quinta declinazione (ei)', 'quinta declinazione (ei)'),
                ('prima coniugazione', 'prima coniugazione'),
                ('seconda coniugazione', 'seconda coniugazione'),
                ('terza coniugazione', 'terza coniugazione'),
                ('quarta coniugazione', 'quarta coniugazione'),
                ('coniugazione mista', 'coniugazione mista'),
                ('prima classe', 'aggettivo prima classe'),
                ('seconda classe', 'aggettivo seconda classe'),
                ('invariabile', 'invariabile'),
            ]
        ),
        default='prima declinazione (ae)',
    )

    significato = models.CharField(max_length=100)

    particolarita = models.CharField(
        max_length = 3,
        choices=(
            [
            ('si', 'si'),
            ('no', 'no'),
            ]
        ),
        default='no',
    )

    jsonResponse = JSONField(blank=True, null=True)
    def publish(self):
        self.save()

    def __str__(self):
        return self.nome

class Declina(models.Model):
    nome = models.CharField(max_length=100)

import json

from django.db import models
from django.core.serializers.json import DjangoJSONEncoder