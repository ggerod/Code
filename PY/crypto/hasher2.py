#!/usr/bin/python3
from Crypto.Hash import SHA256

# (1024 * 12201) + 955
# os.fstat(f.fileno()).st_size
with open('6.1.intro.mp4_download','rb') as f:

    # do the last block hash first
    pos = (1024 * 12201)
    f.seek(pos)
    rawbytes = f.read(955)
    h = SHA256.new()
    h.update(rawbytes)
    shahash = bytes.fromhex(h.hexdigest())
    #print(shahash)

    # loop over the file bytes
    for i in range(12200,-1,-1):
        # position file object
        pos = (1024 * i)
        f.seek(pos)

        # read the bytes and append previous hash to the bytes
        rawbytes = f.read(1024)
        rawbytes += shahash

        # do the new hash on the bytes + previous hash
        h = SHA256.new()
        h.update(rawbytes)
        shahash = bytes.fromhex(h.hexdigest())

    print(shahash.hex())
