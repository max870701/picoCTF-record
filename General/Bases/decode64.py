from base64 import b64decode

target = "bDNhcm5fdGgzX3IwcDM1"
flag = b64decode(target)
print(flag)