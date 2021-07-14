from fastapi import FastAPI
from dotenv import load_dotenv
import model as m
import csv_services
import redis
import json
import os

load_dotenv()

api = FastAPI()

REDIS_SERVER = os.getenv('REDIS_SERVER')

r = redis.Redis(host=REDIS_SERVER, port=6379, charset="utf-8", db=0)
c = csv_services.CSV_SERVICES()


@api.post('/checkin')
def checkin(req: m.CheckIn):
    '''
    register redis sessions
    '''
    if r.get(req.PhoneNum):
        ret = dict(json.loads(
            r.get(req.PhoneNum).decode('utf-8').replace("'", '"')))

        print('Check in Redis Session and Set CheckOut')

        if ret['Bld'] != req.Bld:
            c.logging_csv(ret['Fname'], ret['Lname'], ret['PhoneNum'], ret['Bld'], ret['Floor'], False)
            r.delete(req.PhoneNum)

            # c.logging_csv(ret[, ret['Lname'], ret['PhoneNum'], req.Bld, ret['Floor'], True)
            c.logging_csv(req.Fname, req.Lname, req.PhoneNum, req.Bld, req.Floor, True)
            r.set(req.PhoneNum, str(req.dict()), ex=300)

            return 're-checkin-switch-building logging'

        if ret['Bld'] == req.Bld:
            if ret['Floor'] != req.Floor:
                c.logging_csv(ret['Fname'], ret['Lname'], ret['PhoneNum'], ret['Bld'], ret['Floor'], False)
                r.delete(req.PhoneNum)

                c.logging_csv(req.Fname, req.Lname, req.PhoneNum, req.Bld, req.Floor, True)
                r.set(req.PhoneNum, str(req.dict()), ex=300)

                return 're-checkin-switch-Floor logging'

            return 're-checkin-same-building nolog'

    r.set(req.PhoneNum, str(req.dict()), ex=300)
    c.logging_csv(req.Fname, req.Lname, req.PhoneNum, req.Bld, req.Floor, True)

    return 'new-checkin'


@api.post('/ischeckin')
def is_checkin(p: m.IsCheckin):
    '''
    check phone in redis sessions
    '''
    return True if r.get(p.PhoneNum) else False


@api.get('/info')
def get_info(phone: int):
    if r.get(phone):
        ret = r.get(phone).decode('utf-8').replace("'", '"')
        return {
            "status": "inSession",
            "data": json.loads(ret)
        }
    return {
        "status": "notInSession"
    }


@api.delete('/checkout')
def checkout(sess: m.CheckOut):
    '''
    delete redis session
    '''
    if r.get(sess.PhoneNum):
        ret = dict(json.loads(
            r.get(sess.PhoneNum).decode('utf-8').replace("'", '"')))
        print(ret)
        c.logging_csv(ret['Fname'], ret['Lname'], ret['PhoneNum'], ret['Bld'], ret['Floor'], False)
        r.delete(sess.PhoneNum)
        return {
            "status": "success",
            "data": ret
        }

    # r.delete(sess.PhoneNum)
    return {
        "status": "failed",
        "data": "notInSession"
    }
