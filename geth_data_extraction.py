import leveldb


def get_keys():
    geth_ldb_path = "/home/web3success/full-node-volumes/volumes/eth-docker_geth-eth1-data/_data/geth/chaindata"
    db = leveldb.LevelDB(geth_ldb_path)

    print("Keys: ")
    for k in db.RangeIter(include_value=False):
        print(k)
