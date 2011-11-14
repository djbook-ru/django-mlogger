# -*- coding: utf-8 -*-
# (c) 2009-2010 Ruslan Popov <ruslan.popov@gmail.com>
# (c) 2010 Maxim M. <shamanu4@gmail.com>

from django.utils import simplejson, datetime_safe
import time, datetime

class DatetimeJSONEncoder(simplejson.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, datetime.date):
            return o.strftime('%Y-%m-%d')
        if isinstance(o, datetime.time):
            return o.strftime('%H:%M:%S')
        elif hasattr(o, '__unicode__'):
            return o.__unicode__()
        else:
            return super(DatetimeJSONEncoder, self).default(o)

