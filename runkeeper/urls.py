#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^authorize/$', 'runkeeper.views.authorize', name='authorize_runkeeper'),
	url(r'^$', 'runkeeper.views.index', name='home_page'),
)