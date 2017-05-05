# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService
from wazo_admin_ui.helpers.confd import confd


class SwitchboardService(BaseConfdService):

    resource_confd = 'switchboards'

    def create(self, resource):
        switchboard_created = super(SwitchboardService, self).create(resource)
        resource['uuid'] = switchboard_created['uuid']
        self._update_members(resource)

    def update(self, switchboard):
        super(SwitchboardService, self).update(switchboard)
        self._update_members(switchboard, switchboard['members'])

    def _update_members(self, switchboard, members):
        confd.switchboards(switchboard).update_user_members(members.get('users'))
