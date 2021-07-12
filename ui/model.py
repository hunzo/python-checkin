from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, InputRequired

choices = [
    ('siam', 'อาคารสยาม'),
    ('boonchana', 'อาคารบุญชนะ'),
    ('choop', 'อาคารชุบ'),
    ('navamin', 'อาคารนวมินทร์'),
    ('lib', 'ห้องสมุด'),
]


class CheckinForm(FlaskForm):
    firstname = StringField(label="ชื่อ", validators=[DataRequired()])
    lastname = StringField(label="นามสกุล", validators=[DataRequired()])
    phonenumber = IntegerField(label="เบอร์โทรศัพท์", validators=[DataRequired()])
    building = SelectField(label="อาคาร", choices=choices)
    floor = IntegerField(label="ชั้น", validators=[DataRequired()])
    submit = SubmitField('ลงชื่อเข้าอาคาร')


class CheckoutForm(FlaskForm):
    phonenumber = StringField(label="เบอร์โทรศัพท์", validators=[DataRequired()])
    submit = SubmitField('ลงชื่อออก')
