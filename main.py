#  coding: utf-8

from twittenizer.tokenizer import Tokenizer
from twittenizer.mongo_mng import MongoMng
from pprint import pprint


def main():
    connect = MongoMng.connect_db()
    insert_tokens = MongoMng.connect_db(collection="tokens")
    while True:
        cursor = connect.watch()
        document = next(cursor)["fullDocument"]
        tweet_id, date, text = (
            document["id_str"],
            document["created_at"],
            document["text"],
        )
        tokens = Tokenizer().tokenize(text)
        tags = len(tokens) * ["MISC"]
        insert = {
            "tweet_id_str": tweet_id,
            "tweet_date": date,
            "tokens": tokens,
            "tags": tags,
        }
        insert_tokens.insert_one(insert)
        print(text)
        print(tokens, end="\n\n")


if __name__ == "__main__":
    main()

# Valid JSON data format for tokenization


# sudo service mongod stop
# sudo rm -rf /tmp/mongodb-27017.sock
# mongod --port 27017 --dbpath /data/db0 --replSet foo&
# mongod --port 27018 --dbpath /data/db1 --replSet foo&
# mongod --port 27019 --dbpath /data/db2 --replSet foo&
