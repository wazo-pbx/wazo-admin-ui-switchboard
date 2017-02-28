# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService


class SwitchboardService(BaseConfdService):

    resource = 'switchboard'
    confd_resource = 'switchboards'

    def create(self, resources):
        switchboard = resources.get('switchboard')
        switchboard = self._confd.switchboards.create(switchboard)

        users = resources.get('users')

        if users:
            self.add_members_to_switchboard(switchboard['uuid'], users)

    def update(self, resources):
        switchboard = resources.get('switchboard')
        users = resources.get('users')

        if users:
            self.add_members_to_switchboard(switchboard['uuid'], users)

        self._confd.switchboards.update(switchboard)

    def get_users(self):
        return self._confd.users.list()

    def add_members_to_switchboard(self, switchboard_uuid, users):
        return self._confd.switchboards(switchboard_uuid).update_user_members(users)
