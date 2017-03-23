# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item
from marshmallow import fields, pre_dump

from wazo_admin_ui.helpers.classful import BaseView, BaseDestinationView
from wazo_admin_ui.helpers.mallow import BaseSchema, BaseAggregatorSchema, extract_form_fields

from .form import SwitchboardForm


class UserSchema(BaseSchema):

    class Meta:
        fields = extract_form_fields(SwitchboardForm)


class SwitchboardSchema(BaseSchema):

    class Meta:
        fields = ('name',)


class AggregatorSchema(BaseAggregatorSchema):
    _main_resource = 'switchboard'

    switchboard = fields.Nested(SwitchboardSchema)
    users = fields.Nested(UserSchema, many=True)

    @pre_dump
    def add_envelope(self, form):
        users = [{'uuid': uuid} for uuid in form.users.data]
        return {'switchboard': form,
                'users': users}


class SwitchboardView(BaseView):

    form = SwitchboardForm
    resource = 'switchboard'
    schema = AggregatorSchema

    @classy_menu_item('.switchboards', 'Switchboards', order=3, icon="desktop")
    def index(self):
        return super(SwitchboardView, self).index()

    def _map_resources_to_form(self, resources):
        data = self.schema().load(resources).data
        users = [user['uuid'] for user in resources['switchboard']['members']['users']]
        return self.form(data=data['switchboard'], users=users)


class SwitchboardDestinationView(BaseDestinationView):

    def list_json(self):
        params = self._extract_params()
        switchboards = self.service.list(**params)
        results = [{'id': sw['uuid'], 'text': sw['name']} for sw in switchboards['items']]
        return self._select2_response(results, switchboards['total'], params)
