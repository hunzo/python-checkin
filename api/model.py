from pydantic import BaseModel

class UserReg(BaseModel):
    Fname: str
    Lname: str
    Bld: str
    Floor: int
    PhoneNum: int
    isCheckin: bool

class ChkPhoneNum(BaseModel):
    PhoneNum: int
    Bld: str
    Floor: int

