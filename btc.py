
# needed python libs
import sys
import binascii
from bitcoinlib.keys import HDKey
from Crypto.Hash import SHA256

pwd = sys.argv[1]+sys.argv[2]

h = SHA256.new()
h.update(pwd.encode('utf-8'))

# generate a password based BTC private key
private_key = h.hexdigest()
key = HDKey(private_key)

# get the BTC address
address = key.address()

print('{0}, {1}, {2}, {3}'.format(sys.argv[2],pwd,private_key,address))