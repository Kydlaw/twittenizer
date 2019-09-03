#  coding: utf-8

from twittenizer.tokenizer import Tokenizer
from pymongo import MongoClient


def connect_db(host="localhost", port=27017, name="twitter", collection="tweet"):
    client = MongoClient(host, port)
    db = client[name]
    connect = db[collection]
    return connect


def main():
    connect = connect_db()
    cursor = connect.find({}, {"text": 1, "_id": 0})
    for item in cursor:
        res = Tokenizer().tokenize(item["text"])
        print(item["text"])
        print(res, end="\n\n")


if __name__ == "__main__":
    main()
