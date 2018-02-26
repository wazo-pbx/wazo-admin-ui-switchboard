# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import jsonify, request
from flask_babel import lazy_gettext as l_
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView, LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response

from .form import SwitchboardForm


class SwitchboardView(BaseView):
    form = SwitchboardForm
    resource = 'switchboard'

    @classy_menu_item('.switchboards', l_('Switchboards'), order=3, icon="desktop")
    def index(self):
        return super(SwitchboardView, self).index()

    def _map_resources_to_form(self, resource):
        users = [user['uuid'] for user in resource['members']['users']]
        resource['members']['user_uuids'] = users
        form = self.form(data=resource)
        return form

    def _populate_form(self, form):
        form.members.user_uuids.choices = self._build_set_choices_users(form.members.users)
        return form

    def _build_set_choices_users(self, users):
        results = []
        for user in users:
            if user.lastname.data:
                text = '{} {}'.format(user.firstname.data, user.lastname.data)
            else:
                text = user.firstname.data
            results.append((user.uuid.data, text))
        return results

    def _map_form_to_resources(self, form, form_id=None):
        resource = super(SwitchboardView, self)._map_form_to_resources(form, form_id)
        resource['members']['users'] = [{'uuid': user_uuid} for user_uuid in form.members.user_uuids.data]
        return resource

    def _map_resources_to_form_errors(self, form, resources):
        form.populate_errors(resources.get('switchboard', {}))
        return form


class SwitchboardDestinationView(LoginRequiredView):

    def list_json(self):
        params = extract_select2_params(request.args)
        switchboards = self.service.list(**params)
        results = [{'id': sw['uuid'], 'text': sw['name']} for sw in switchboards['items']]
        return jsonify(build_select2_response(results, switchboards['total'], params))
