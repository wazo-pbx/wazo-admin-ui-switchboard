# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService
from wazo_admin_ui.helpers.confd import confd


class SwitchboardService(BaseConfdService):

    resource_name = 'switchboard'
    resource_confd = 'switchboards'

    def create(self, resources):
        resource = super(SwitchboardService, self).create(resources)
        self._update_members(resources, resource)

    def update(self, resources):
        super(SwitchboardService, self).update(resources)
        self._update_members(resources)

    def _update_members(self, resources, resource=None):
        switchboard = resources.get(self.resource_name)
        users = switchboard.get('users')

        if resource is None:
            resource = switchboard['uuid']

        if users:
            self._update_members_to_switchboard(resource, self._generate_users(users))

    def _update_members_to_switchboard(self, switchboard, users):
        return confd.switchboards(switchboard).update_user_members(users)

    def _generate_users(self, users):
        return [{'uuid': user} for user in users]
