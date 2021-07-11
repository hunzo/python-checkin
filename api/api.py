from fastapi import FastAPI
import model as m
import csv_services as csv
import redis 

c = csv.CSV_SERVICES()

api = FastAPI()


@api.post('/register')
def register(req: m.UserReg):
    '''
    register session 
    '''
    print(req)
    c.get_csv(req)
    return req

@api.post('/session')
def check_session(sess: m.ChkPhoneNum):
    '''
    ckeck session in redis 
    '''
    return sess

@api.delete('/logout')
def disconnect_session(sess: m.ChkPhoneNum):
    '''
    set session expire 
    '''
    return sess

