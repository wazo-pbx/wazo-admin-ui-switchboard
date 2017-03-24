# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_wtf import FlaskForm

from wtforms.fields import (SubmitField,
                            StringField,
                            SelectField,
                            SelectMultipleField)
from wtforms.validators import InputRequired

from wazo_admin_ui.helpers.destination import DestinationHiddenField


class SwitchboardForm(FlaskForm):
    name = StringField('Name', [InputRequired()])
    users = SelectMultipleField('Users', choices=[])
    submit = SubmitField('Submit')


class SwitchboardDestinationForm(FlaskForm):
    setted_value_template = '{switchboard_name}'

    switchboard_uuid = SelectField('Switchboard', choices=[])
    switchboard_name = DestinationHiddenField()
