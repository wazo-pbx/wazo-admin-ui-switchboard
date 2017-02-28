# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint

from .service import SwitchboardService
from .view import SwitchboardView

switchboard = create_blueprint('switchboard', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']
        config = dependencies['config']

        SwitchboardView.service = SwitchboardService(config['confd'])
        SwitchboardView.register(switchboard, route_base='/switchboards')
        register_flaskview(switchboard, SwitchboardView)

        core.register_blueprint(switchboard)
