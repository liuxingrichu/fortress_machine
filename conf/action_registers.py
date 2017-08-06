#!/usr/bin/env python
# -*- coding:utf-8 -*-

from modules import views

actions = {
    'start_session': views.start_session,
    'syncdb': views.syncdb,
    'create_fortressusers': views.create_fortressusers,
    'create_groups': views.create_groups,
    'create_hosts': views.create_hosts,
    'create_bindhosts': views.create_bindhosts,
    'create_remoteusers': views.create_remoteusers,

}
