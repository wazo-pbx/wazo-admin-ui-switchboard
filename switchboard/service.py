# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService
from wazo_admin_ui.helpers.confd import confd


class SwitchboardService(BaseConfdService):

    resource_name = 'switchboard'
    resource_confd = 'switchboards'

    def create(self, resource):
        switchboard_created = super(SwitchboardService, self).create(resource)
        resource['uuid'] = switchboard_created['uuid']
        self._update_members(resource)

    def update(self, resource):
        super(SwitchboardService, self).update(resource)
        self._update_members(resource)

    def _update_members(self, switchboard):
        users = switchboard.get('users')

        if users:
            self._update_members_to_switchboard(switchboard, self._generate_users(users))

    def _update_members_to_switchboard(self, switchboard, users):
        return confd.switchboards(switchboard).update_user_members(users)

    def _generate_users(self, users):
        return [{'uuid': user} for user in users]
