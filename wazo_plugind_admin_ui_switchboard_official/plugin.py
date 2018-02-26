# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint
from wazo_admin_ui.helpers.destination import register_destination_form, register_listing_url

from .service import SwitchboardService
from .view import SwitchboardView, SwitchboardDestinationView
from .form import SwitchboardDestinationForm


switchboard = create_blueprint('switchboard', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        SwitchboardView.service = SwitchboardService()
        SwitchboardView.register(switchboard, route_base='/switchboards')
        register_flaskview(switchboard, SwitchboardView)

        SwitchboardDestinationView.service = SwitchboardService()
        SwitchboardDestinationView.register(switchboard, route_base='/switchboard_destination')

        register_destination_form('switchboard', l_('Switchboard'), SwitchboardDestinationForm)
        register_listing_url('switchboard', 'switchboard.SwitchboardDestinationView:list_json')

        core.register_blueprint(switchboard)
