import leveldb


def say_howdy():
    db = leveldb.LevelDB('./db')
    key = bytes("Howdy", "utf-8")
    value = bytes("There", "utf-8")
    db.Put(key, value)
    print(db.Get(key))


def give_keys():
    db = leveldb.LevelDB('./db')

    key = bytes("Howdy", "utf-8")
    value = bytes("There", "utf-8")
    db.Put(key, value)

    key = bytes("Hello", "utf-8")
    value = bytes("There", "utf-8")
    db.Put(key, value)

    for k in db.RangeIter(include_value=False):
        print('K: ', k)
