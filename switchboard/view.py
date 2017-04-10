# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask import jsonify, request
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView, LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response

from .form import SwitchboardForm


class SwitchboardView(BaseView):

    form = SwitchboardForm
    resource = 'switchboard'

    @classy_menu_item('.switchboards', 'Switchboards', order=3, icon="desktop")
    def index(self):
        return super(SwitchboardView, self).index()

    def _map_resources_to_form(self, resources):
        users = [user['uuid'] for user in resources['switchboard']['members']['users']]
        form = self.form(data=resources['switchboard'], users=users)
        form.users.choices = self._build_setted_choices(resources['switchboard']['members']['users'])
        return form

    def _build_setted_choices(self, users):
        results = []
        for user in users:
            if user.get('lastname'):
                text = '{} {}'.format(user.get('firstname'), user['lastname'])
            else:
                text = user.get('firstname')
            results.append((user['uuid'], text))
        return results

    def _map_form_to_resources(self, form, form_id=None):
        resources = {'switchboard': form.to_dict()}
        if form_id:
            resources['switchboard']['uuid'] = form_id
        return resources

    def _map_resources_to_form_errors(self, form, resources):
        form.populate_errors(resources.get('switchboard', {}))
        return form


class SwitchboardDestinationView(LoginRequiredView):

    def list_json(self):
        params = extract_select2_params(request.args)
        switchboards = self.service.list(**params)
        results = [{'id': sw['uuid'], 'text': sw['name']} for sw in switchboards['items']]
        return jsonify(build_select2_response(results, switchboards['total'], params))
