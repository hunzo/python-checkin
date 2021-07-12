from flask import Flask, render_template, request
from dotenv import load_dotenv
import model as form

import services

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret'

s = services.SERVICES()

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/checkin', methods=['GET', 'POST'])
def checkin():
    f = form.CheckinForm()
    print(f.firstname)

    if f.validate_on_submit():
        rs = s.checkin(f.firstname.data, f.lastname.data, int(f.phonenumber.data), f.building.data, int(f.floor.data))

        info = s.getinfo(f.phonenumber.data) 
        ret = {
            "result": rs,
            "info": info
        }
        return render_template('result.html', data=ret)
    return render_template('checkin.html', form=f)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    f = form.CheckoutForm()

    if f.validate_on_submit():

        info = s.getinfo(f.phonenumber.data)
        ret = {
            "result": 'test',
            "info": info
        }

        s.checkout(f.phonenumber.data)

        return render_template('result.html', data=ret)
    return render_template('checkout.html', form=f)
