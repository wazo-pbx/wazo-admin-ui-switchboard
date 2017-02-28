# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item
from marshmallow import fields

from wazo_admin_ui.helpers.classful import BaseView
from wazo_admin_ui.helpers.mallow import BaseSchema, BaseAggregatorSchema

from .form import SwitchboardForm


class SwitchboardSchema(BaseSchema):

    class Meta:
        fields = ('name',)


class AggregatorSchema(BaseAggregatorSchema):
    _main_resource = 'switchboard'

    switchboard = fields.Nested(SwitchboardSchema)


class SwitchboardView(BaseView):

    form = SwitchboardForm
    resource = 'switchboard'
    schema = AggregatorSchema

    @classy_menu_item('.switchboards', 'Switchboards', order=3, icon="desktop")
    def index(self):
        return super(SwitchboardView, self).index()

    def _populate_form(self, form):
        users = self.service.get_users()
        user_list = [(user['uuid'], u"{} {}".format(user['firstname'], user['lastname']))
                     for user in users['items']]
        form.users.choices = user_list
        return form
