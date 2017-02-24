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


class UserSchema(BaseSchema):
    firstname = fields.String(attribute='firstname')
    lastname = fields.String(attribute='lastname')


class SwitchboardFormSchema(BaseSchema):
    _main_resource = 'switchboard'

    switchboard = fields.Nested(SwitchboardSchema)
    users = fields.Nested(UserSchema)

    @post_load(pass_original=True)
    def create_form(self, data, raw_data):
        users = []
        return SwitchboardForm(data=data['switchboard'], users=users)

    @pre_dump
    def add_envelope(self, data):
        return {'switchboard': data,
                'users': data}


class SwitchboardView(BaseView):

    form = SwitchboardForm
    resource = 'switchboard'
    schema = SwitchboardFormSchema
    templates = {'list': 'switchboard/list.html',
                 'edit': 'switchboard/view.html'}

    @classy_menu_item('.switchboards', 'Switchboards', order=3, icon="desktop")
    def index(self):
        form = SwitchboardForm()
        form.users.choices = self.service.get_users()
        return super(SwitchboardView, self)._index(form=form)
