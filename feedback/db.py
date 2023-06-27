from . import getdb
from .model import FeedBackData
from pymongo.cursor import Cursor

db = getdb()


def insertdata(Data: FeedBackData) -> bool:
    ins = {
        "name": Data.name,
        "email": Data.email,
        "age": Data.age,
        "rating": Data.rating,
        "suggestion": Data.suggestion,
        "ques1": Data.question1,
        "ques2": Data.question2,
        "ques3": Data.question3,
        "ques4": Data.question4,
        "ques5": Data.question5
    }
    db.data.insert_one(ins)
    return True


def getAllData() -> Cursor:
    return db.data.find()
