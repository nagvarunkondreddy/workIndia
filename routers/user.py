from fastapi import APIRouter, HTTPException, Request
from config.db import conn
from models.usertable import users
from models.models import User
# from cryptography.fernet import Fernet
# key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
# cipher_suite = Fernet(key)
   

router = APIRouter()

@router.post("/")
def register_user( user: User):
    try:
        conn.execute(users.insert().values(
            username=user.username,
            # password=cipher_suite.encrypt(b""+user.password+"")
            password=user.password
        ))
        return conn.execute(users.select()).fetchall()

    except Exception as e:
        print(e)

@router.post("/auth/")
def authenticate_user(user: User):
    try:

        # if(conn.execute(users.select().where((users.c.username == user.username) and (users.c.password) == cipher_suite.encrypt(b""+user.password+"") )).fetchall()):
        if(conn.execute(users.select().where((users.c.username == user.username) and (users.c.password) == user.password )).fetchall()):
            user_data=conn.execute(users.select().where((users.c.username == user.username) and (users.c.password) == user.password )).fetchall()
            return {"status":'success', 'userId':user_data[0]["id"]}

    except Exception as e:
        print(e)