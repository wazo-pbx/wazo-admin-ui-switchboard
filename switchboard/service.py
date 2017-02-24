# -*- coding: utf-8 -*-
# Copyright 2017 by Sylvain Boily
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService

class SwitchboardService(BaseConfdService):

    resource = 'switchboard'
    confd_resource = 'switchboards'

    def get_users(self):
        return self._generate_user_list(self._confd.users.list())

    def _generate_user_list(self, users):
        user_list = []
        for user in users['items']:
            user_list.append(("{}".format(user['uuid']), u"{} {}".format(user['firstname'], user['lastname'])))
        return user_list
