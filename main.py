#  coding: utf-8

from twittenizer.tokenizer import Tokenizer
from pymongo import MongoClient
from pprint import pprint

config = {
    "_id": "foo",
    "members": [
        {"_id": 0, "host": "localhost:27017"},
        {"_id": 1, "host": "localhost:27018"},
        {"_id": 2, "host": "localhost:27019"},
    ],
}


def config_replica(config, host="localhost", port=27017) -> None:
    client = MongoClient(host, port)
    response = client.admin.command("replSetInitiate", config)
    print(response)


def connect_db(
    host="localhost", port=27017, replicaset="foo", name="twitter", collection="tweet"
):
    client = MongoClient(host, port)
    db = client[name]
    connect = db[collection]
    return connect


def main():
    connect = connect_db()
    while True:
        cursor = connect.watch()
        document = next(cursor)
        text = document["fullDocument"]["text"]
        res = Tokenizer().tokenize(text)
        print(text)
        print(res, end="\n\n")


if __name__ == "__main__":
    main()
