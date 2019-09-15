#  coding: utf-8

from twittenizer.tokenizer import Tokenizer
from twittenizer.mongo_mng import MongoMng
from pprint import pprint


def main():
    MongoMng.config_replica()
    connect = MongoMng.connect_db()
    while True:
        cursor = connect.watch()
        document = next(cursor)
        text = document["fullDocument"]["text"]
        res = Tokenizer().tokenize(text)
        print(text)
        print(res, end="\n\n")


if __name__ == "__main__":
    main()
