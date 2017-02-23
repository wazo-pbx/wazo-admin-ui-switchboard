# -*- coding: utf-8 -*-
# Copyright 2017 by Sylvain Boily
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.service import BaseConfdService

class SwitchboardService(BaseConfdService):

    resource = 'switchboard'
    confd_resource = 'switchboards'
