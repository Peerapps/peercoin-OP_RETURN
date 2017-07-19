from OP_RETURN import *

results = OP_RETURN_store("""{
  "hash" : "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
  "blockcount" : 0,
  "version" : 1,
  "merkleroot" : "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b",
  "time" : 1231006505,
  "nonce" : 2083236893,
  "difficulty" : 1.00000000,
  "tx" : [
    "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b"
  ],
  "hashnext" : "00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048"
}""", testnet=True)
print "results", results

for r in OP_RETURN_retrieve_fromblock(block_number=None, testnet=True):
    print r
    # {'heights': [0], 'data': " 1 {'hi'}", 'txids': ['108f6d5aa438fbd1eb0fbaece3af445b059137b7b5453caab5b3255ddb9b9a97']}
