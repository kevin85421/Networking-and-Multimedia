import gmpy
from Crypto.PublicKey import RSA
from base64 import b64decode

public_key = b'MGwwDQYJKoZIhvcNAQEBBQADWwAwWAJRAK5btPJmADJZz5pvUhw8A0EBds8W31OVNHbq47Ie3mw8ewO9yiCzHABn/6eX5OkQWXhz7vETpg/szZXetbK/EAZr4iJKzinVMtwLWnTS0AbxAgMBAAE='

# 讀取 public-key 得 n,e
keyDER = b64decode(public_key)
keyPub = RSA.importKey(keyDER)

print("n = ")
print(keyPub.n)
print("e = ")
print(keyPub.e)
# 把 n 丟去factorDB 得 p,q

p = 1634733645809253848443133883865090859841783670033092312181110852389333100104508151212118167511579
q = 1900871281664822113126851573935413975471896789968515493666638539088027103802104498957191261465571

# 求r
r = (p-1)*(q-1)
# 求d 
d = int(gmpy.invert(keyPub.e,r))
print("d = ")
print(d)

# 用 rsatool 製作private key
# python3 rsatool-master/rsatool.py -f PEM -o key.pem -n 3107418240490043721350750035888567930037346022842727545720161948823206440518081504556346829671723286782437916272838033415471073108501919548529007337724822783525742386454014691736602477652346609 -d 2464047959500535454951489660269116654533786992311074127530789876809197740220694563815619147113537879811295339427915163213618715392333280036495568759211274464407731279798672759722961973941926913

# 用 openssl 搭配private key 解密文（flag.txt）得明文
# openssl rsautl -decrypt -inkey key.pem -in flag.txt -out flag