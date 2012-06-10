import datetime

from django.utils.translation import ugettext_lazy as _

from ...test.testcases import FieldDefinitionTestMixin
from ...tests.models.utils import BaseModelDefinitionTestCase

from .models import (DateFieldDefinition, DateTimeFieldDefinition,
    TimeFieldDefinition)


class DateTimeFieldDefinitionTestMixin(FieldDefinitionTestMixin):
    field_definition_category = _(u'datetime')

class DateFieldDefinitionTest(DateTimeFieldDefinitionTestMixin,
                              BaseModelDefinitionTestCase):
    field_definition_cls = DateFieldDefinition
    field_defintion_init_kwargs = {'default': datetime.date(1990, 8, 31)}
    field_values = (
        datetime.date.today(),
        datetime.date(1988, 5, 15)
    )

class DateTimeFieldDefinitionTest(DateTimeFieldDefinitionTestMixin,
                                  BaseModelDefinitionTestCase):
    field_definition_cls = DateTimeFieldDefinition
    field_defintion_init_kwargs = {'default': datetime.datetime(1990, 8, 31, 23, 46)}
    field_values = (
        datetime.datetime(2020, 11, 15, 15, 34),
        datetime.datetime(1988, 5, 15, 15, 30)
    )
    
class TimeFieldDefinitionTest(DateTimeFieldDefinitionTestMixin,
                              BaseModelDefinitionTestCase):
    field_definition_cls = TimeFieldDefinition
    field_defintion_init_kwargs = {'default': datetime.time(1, 1)}
    field_values = (
        datetime.time(1, 58, 37),
        datetime.time(17, 56)
    )
