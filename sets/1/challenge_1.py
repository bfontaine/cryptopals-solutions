# -*- coding: UTF-8 -*-

import base64

# https://cryptopals.com/sets/1/challenges/1
def hex_to_base64(h):
    return base64.b64encode(bytearray.fromhex(h))
