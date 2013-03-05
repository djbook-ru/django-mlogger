# -*- coding: utf-8 -*-
# (c) 2009-2010 Ruslan Popov <ruslan.popov@gmail.com>
# (c) 2010 Maxim M. <shamanu4@gmail.com>

from django.conf import settings
from django.db import models
from django.utils import simplejson
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.dispatch import Signal

from datetime import datetime

from serializers import DatetimeJSONEncoder

class Log(models.Model):

    user = models.ForeignKey(User, related_name='user_log', verbose_name=_(u'user'), null=True, blank=True)
    action = models.CharField(verbose_name=_(u'action'), max_length=64)
    content_type = models.ForeignKey(ContentType,verbose_name=_('content type'))
    oid = models.PositiveIntegerField(verbose_name=_('object id'))
    data = models.TextField(verbose_name=_('data'))
    timestamp = models.DateTimeField(verbose_name=_(u'timestamp'), default=datetime.now)

    class Meta:
        verbose_name = _(u'Log')
        verbose_name_plural = _(u'Logs')
        ordering = ('-timestamp',)


    def __unicode__(self):
        return u'%s %s' % (self.content_type, self.action)

def logging_abstract(instance, action, **kwargs):
    data = {}
    for i in instance.__dict__.keys():
        if '_' == i[0]:
            continue
        data.update( {i: instance.__dict__[i]} )

    response = simplejson.dumps(data, cls=DatetimeJSONEncoder)
    content_type = ContentType.objects.get_for_model(instance)
    log = Log(content_type=content_type, data=response, action=action, oid=instance.pk,
              user=settings.CURRENT_USER)
    log.save()

def logging_postsave(instance, created, **kwargs):
    logging_abstract(instance, created and 'create' or 'update', **kwargs)

def logging_postdelete(instance, **kwargs):
    logging_abstract(instance, 'delete', **kwargs)

def logging_mysignals(sender, **kwargs):
    log = Log(user=sender, model='global action',
              data='', action=kwargs['action'])
    log.save()

signal_log_action = Signal(providing_args=['action'])
signal_log_action.connect(logging_mysignals)
