# -*- coding: utf-8 -*-
import json
import os

from authlib.jose import jwk

key_dict = jwk.dumps(os.environ["LOGIN_GOV_SECRET_KEY"], kty="RSA")
key_dict["use"] = "sig"
key_dict["alg"] = "RS256"
key_dict["kid"] = os.environ["LOGIN_GOV_KID_JWK"]

key_set_dict = {"keys": [key_dict]}

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
keys_dir = os.path.join(project_dir, "app", "keys")
key_set_path = os.path.join(keys_dir, os.environ["LOGIN_GOV_JWK_SET_FILENAME"])

os.makedirs(keys_dir, exist_ok=True)

with open(key_set_path, "w") as fp:
    json.dump(key_set_dict, fp, indent=2, sort_keys=True)
