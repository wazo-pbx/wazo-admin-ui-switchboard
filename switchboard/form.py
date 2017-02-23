# -*- copyright 2017 by Sylvain Boily
# SPDX-License-Identifier: GPL-3.0+

from flask_wtf import FlaskForm

from wtforms.fields import SubmitField
from wtforms.fields import TextField

from wtforms.validators import InputRequired


class SwitchboardForm(FlaskForm):
    name = TextField('Name', [InputRequired()])
    submit = SubmitField('Submit')
