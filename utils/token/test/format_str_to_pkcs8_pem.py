#!/usr/bin/env python
# -*- coding: utf-8 -*-
print '-----BEGIN PRIVATE KEY-----'
liuliuyu_str = '''MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKwaNzgekeP5Ma7fnAER63uqVmu7kWlCLuU03r/33j9CeWJ0Unkxe0mnG8CRDizduZu/zpnvbHHRmdEx+ZDuudUCAwEAAQ=='''
liuliuyu_str = liuliuyu_str.strip().replace('\n', '').replace('\r', '')
counter = -1
content_list = []
for _ in liuliuyu_str:
    counter += 1
    if counter == 64:
        counter = 0
        a = ''.join(content_list)
        print a#, len(a)
        content_list = []
        content_list.append(_)
    else:
        content_list.append(_)
if content_list:
    a = ''.join(content_list)
    print a#, len(a)
print '-----END PRIVATE KEY-----'

'''PKCS8格式私钥转换为PKCS1（传统私钥格式） 加密最大长度53，解密最大长度64（pkcs1_padding）

openssl pkcs8 -in private_key_pkcs8.pem -nocrypt -out private_key.pem'''
