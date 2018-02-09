#!/usr/bin/env python
# -*- coding: utf-8 -*-
import M2Crypto
import base64


# msg = 'Hqgt6U5ks1RmoGg6NyEf3auy3KhVdSf1jJWGZwxMzYCdPe16efkI3bFdqxgOwUb5hqQBsj0EocAFldQqO2r4/hyN5hrRtW2QdYlxPc8yyeWrhPtFV5a9ddf39SF/N1dWS4c5mg3RYaCJBZj05ZfjtKV9vPHd2hrsaG9GTDT/Z1sitQH4ZTyxro8FzFIyxqiPe4OczZR3Vm0lpVTxKBm+NH3qIRuNHNe0pe69t8pqjoJI/+BOxTPHOCYBxkYwI5+bK8Nz2eBOdKis8HWfHXQUtYYWyl009kegJhaWbRCNJZj8RsLpjJ3DiA2Qx8Y9gRBPK80oZNuwFjCFzHSmw2KXf8jWsX5jB6ZkprDxg6+KL9dRDC5HebS6jOljPuXwtZYX448OBAJ5T/4kuR+NRlNaR63xg7h57LNzhLU7ICgBaTCIkvS3UKaTbdJgI47vuSjSe435MOj91k9bOZflyWy9Re5n0BbH9sSNJxWH4i0ahIEh6C+/MASdzKXRq0VP'

msg = 'Hqgt6U5ks1RmoGg6NyEf3auy3KhVdSf1jJWGZwxMzYCdPe16efkI3bFdqxgOwUb5hqQBsj0EocAFldQqO2r4/hyN5hrRtW2QdYlxPc8yyeWrhPtFV5a9ddf39SF/N1dWS4c5mg3RYaCJBZj05ZfjtKV9vPHd2hrsaG9GTDTfQ0V/Z1sitQH4ZTyxro8FzFIyxqiPe4OczZR3Vm0lpVTxKBm+NH3qIRuNHNe0pe69t8pqjoJI/+BOxTPHOCYBxkYwI5+bK8Nz2eBOdKis8HWfHXQUtYYWyl009kegJhaWbRCNJZj8RsLpjJ3DiA2Qx8Y9gRBPK80oZNuwFjCFzHSmw2KXf8jWsX5jB6ZkprDxg6+KL9dRDC5HebS6jOljPuXwtZYX448OBAJ5T/4kuR+NRlNaR63xg7h57LNzhLU7ICgBaTCIkvS3UKaTbdJgI47vuSjSe435MOj91k9bOZflyWy9Re5n0BbH9sSNJxWH4i0ahIEh6C+/MASdzKXRq0VP'

# privkey = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKwaNzgekeP5Ma7fnAER63uqVmu7kWlCLuU03r/33j9CeWJ0Unkxe0mnG8CRDizduZu/zpnvbHHRmdEx+ZDuudUCAwEAAQ=="
pub_key = """
-----BEGIN PRIVATE KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKwaNzgekeP5Ma7fnAER63uqVmu7kWlC
LuU03r/33j9CeWJ0Unkxe0mnG8CRDizduZu/zpnvbHHRmdEx+ZDuudUCAwEAAQ==
-----END PRIVATE KEY-----
"""

# pub_key = base64.b64decode(pub_key)
ctxt_pri = base64.b64decode(msg)

maxlength = 64
output = ''
# 方法一
rsa_pub = M2Crypto.RSA.load_pub_key('my_rsa_pubkey.pem')

# 方法二
bio = M2Crypto.BIO.MemoryBuffer(pub_key)
rsa_pub = M2Crypto.RSA.load_pub_key_bio(bio)
while ctxt_pri:
    input = ctxt_pri[:64]
    ctxt_pri = ctxt_pri[64:]
    out = rsa_pub.public_decrypt(input, M2Crypto.RSA.pkcs1_padding) #解密
    output = output + out
print('明文:%s'% output)

