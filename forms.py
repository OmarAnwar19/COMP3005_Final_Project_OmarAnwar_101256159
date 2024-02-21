from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class MemberProfileForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Update Profile")


class TrainerScheduleForm(FlaskForm):
    availability = StringField("Availability", validators=[DataRequired()])
    submit = SubmitField("Update Schedule")


class AdminBillingForm(FlaskForm):
    submit = SubmitField("Process Payment")
