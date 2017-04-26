# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wtforms.fields import (SubmitField,
                            StringField,
                            SelectField,
                            SelectMultipleField)
from wtforms.validators import InputRequired, Length

from wazo_admin_ui.helpers.destination import DestinationHiddenField
from wazo_admin_ui.helpers.form import BaseForm


class SwitchboardForm(BaseForm):
    name = StringField('Name', [InputRequired(), Length(max=128)])
    users = SelectMultipleField('Users', choices=[])
    submit = SubmitField('Submit')


class SwitchboardDestinationForm(BaseForm):
    setted_value_template = u'{switchboard_name}'

    switchboard_uuid = SelectField('Switchboard', [InputRequired()], choices=[])
    switchboard_name = DestinationHiddenField()
