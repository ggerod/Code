#!/usr/bin/python3
from Crypto.Hash import SHA256

# (1024 * 16530) + 593
# os.fstat(f.fileno()).st_size
with open('6.2.birthday.mp4_download','rb') as f:

    # do the last block hash first
    pos = (1024 * 16530)
    f.seek(pos)
    rawbytes = f.read(593)
    h = SHA256.new()
    h.update(rawbytes)
    shahash = bytes.fromhex(h.hexdigest())
    #print(shahash)

    # loop over the file bytes
    for i in range(16529,-1,-1):
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
