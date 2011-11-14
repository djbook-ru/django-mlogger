# -*- coding: utf-8 -*-
# (c) 2009-2010 Ruslan Popov <ruslan.popov@gmail.com>
# (c) 2010 Maxim M. <shamanu4@gmail.com>

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from logger.models import Log

class __Log(admin.ModelAdmin):
    list_display = ('user', 'action', 'content_type', 'timestamp')
admin.site.register(Log, __Log)
Log.description = _(u'This model consists of all meaningful events of system.')
