# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import Blueprint
from flask_menu.classy import register_flaskview


from .service import SwitchboardService
from .view import SwitchboardView

switchboard = Blueprint('switchboard', __name__, template_folder='templates',
                       static_folder='static', static_url_path='/%s' % __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']
        config = dependencies['config']

        SwitchboardView.service = SwitchboardService(config['confd'])
        SwitchboardView.register(switchboard, route_base='/switchboards')
        register_flaskview(switchboard, SwitchboardView)

        core.register_blueprint(switchboard)
