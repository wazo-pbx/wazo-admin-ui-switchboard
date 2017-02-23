# -*- coding: utf-8 -*-
# Copyright 2017 by Sylvain Boily
# SPDX-License-Identifier: GPL-3.0+

from flask_login import current_user
from xivo_confd_client import Client as ConfdClient


class SwitchboardService(object):

    def __init__(self, confd_config):
        self.confd_config = confd_config

    @property
    def _confd(self):
        token = current_user.get_id()
        return ConfdClient(token=token, **self.confd_config)

    def list(self):
        return self._confd.switchboards.list()

    def get(self, switchboard_uuid):
        return {'switchboard': self._confd.switchboards.get(switchboard_uuid)}

    def update(self, resources):
        switchboard = resources.get('switchboard')
        self._confd.switchboards.update(switchboard)

    def create(self, resources):
        switchboard = resources.get('switchboard')
        switchboard = self._confd.switchboards.create(switchboard)

    def delete(self, switchboard_uuid):
        switchboard = self._confd.switchboards.get(switchboard_uuid)
        self._confd.switchboards.delete(switchboard_uuid)
