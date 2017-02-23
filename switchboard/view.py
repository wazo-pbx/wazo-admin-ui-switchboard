# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item
from marshmallow import fields, post_load, pre_dump

from wazo_admin_ui.helpers.classful import BaseView
from wazo_admin_ui.helpers.mallow import BaseSchema

from .form import SwitchboardForm


class SwitchboardSchema(BaseSchema):

    class Meta:
        fields = ('name',)


class SwitchboardFormSchema(BaseSchema):
    _main_resource = 'switchboard'

    switchboard = fields.Nested(SwitchboardSchema)

    @post_load(pass_original=True)
    def create_form(self, data, raw_data):
        return SwitchboardForm(data=data['switchboard'])

    @pre_dump
    def add_envelope(self, data):
        return {'switchboard': data}


class SwitchboardView(BaseView):

    form = SwitchboardForm
    resource = 'switchboard'
    schema = SwitchboardFormSchema
    templates = {'list': 'switchboard/list.html',
                 'edit': 'switchboard/view.html'}

    @classy_menu_item('.switchboards', 'Switchboards', order=3, icon="desktop")
    def index(self):
        return super(SwitchboardView, self).index()
