import requests
import json

class SERVICES:
    def checkin(self, fname: str, lname: str, phone: int, building: str, floor: int):
        url = "http://localhost:8080/checkin"
        body = {
            "Fname": fname,
            "Lname": lname,
            "Bld": building,
            "Floor": floor,
            "PhoneNum": phone
        }
        headers = {
            "content-type": "application/json"
        }
        ret = requests.post(url=url, data=json.dumps(body), headers=headers)
        return ret.json()
    
    def getinfo(self, phone: int):
        url = f"http://localhost:8080/info?phone={phone}"
        headers = {
            "content-type": "application/json"
        }
        ret = requests.get(url=url, headers=headers)
        return ret.json()
    
    def checkout(self, phone: int):
        url = f"http://localhost:8080/checkout"
        headers = {
            "content-type": "application/json"
        }
        body = {
            "PhoneNum": phone
        }
        ret = requests.delete(url=url, data=json.dumps(body), headers=headers)
        return ret.json()


