# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService


class SwitchboardService(BaseConfdService):

    resource = 'switchboard'
    confd_resource = 'switchboards'

    def create(self, resources):
        resource = resources.get(self.resource)
        sw = self._confd.switchboards.create(resource)

        if resource.get('users') and sw:
            self.add_members_to_switchboard(sw['uuid'], resource['users'])

    def update(self, resources):
        resource = resources.get(self.resource)

        if resource.get('users'):
            self.add_members_to_switchboard(resource['uuid'], resource['users'])

        self._confd.switchboards.update(resource)

    def get_users(self):
        return self._confd.users.list()

    def add_members_to_switchboard(self, switchboard_uuid, members):
        switchboard_members = []

        for member in members:
            switchboard_members.append({'uuid': member})

        return self._confd.switchboards.relations(switchboard_uuid).update_user_members(switchboard_members)
