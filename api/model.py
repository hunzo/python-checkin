from pydantic import BaseModel

class CheckIn(BaseModel):
    Fname: str
    Lname: str
    Bld: str
    Floor: int
    PhoneNum: int

class CheckOut(BaseModel):
    PhoneNum: int

class IsCheckin(BaseModel):
    PhoneNum: int

