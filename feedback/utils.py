import json
import os
from .db import getAllData
import pandas as pd


def getQuestions() -> list:
    filepath = os.path.realpath(os.path.dirname(__file__))
    realfile = os.path.join(filepath, "static/data", "question.json")
    file = open(realfile)
    question = json.load(file)
    file.close()
    return question


async def createCSV() -> tuple:
    dictdata = {
        "name": [],
        "email": [],
        "age": [],
        "rating": [],
        "suggestion": [],
        "How satisfied are you with the product's performance ?": [],
        "Would you recommend this product to others ?": [],
        "How would you rate the product's ease of use ?": [],
        "Did the product meet your expectations ?": [],
        "How responsive was the customer support for the product ?": []
    }

    alldata = getAllData()
    for data in alldata:
        dictdata["name"].append(data["name"])
        dictdata["age"].append(data["age"])
        dictdata["email"].append(data["email"])
        dictdata["rating"].append(data["rating"])
        dictdata["suggestion"].append(data["suggestion"])
        dictdata["How satisfied are you with the product's performance ?"].append(
            data["ques1"])
        dictdata["Would you recommend this product to others ?"].append(
            data["ques2"])
        dictdata["How would you rate the product's ease of use ?"].append(
            data["ques3"])
        dictdata["Did the product meet your expectations ?"].append(
            data["ques4"])
        dictdata["How responsive was the customer support for the product ?"].append(
            data["ques5"])
    df = pd.DataFrame(dictdata)
    filepath = os.path.realpath(os.path.dirname(__file__))
    realfile = os.path.join(filepath, "static/data", "data.csv")
    try:
        os.remove(realfile)
    except FileNotFoundError as e:
        pass
    df.to_csv(realfile)
    return (True, realfile)
