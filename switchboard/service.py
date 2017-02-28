# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService


class SwitchboardService(BaseConfdService):

    resource = 'switchboard'
    confd_resource = 'switchboards'

    def get_users(self):
        return self._confd.users.list()
