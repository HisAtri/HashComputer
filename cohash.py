import hashlib
import base64

def compute(string, mode):

    co_string = string.encode("utf-8")
    co_dict = {
        "md5":hashlib.md5(),
        "sha1":hashlib.sha1(),
        "sha244":hashlib.sha224(),
        "sha256":hashlib.sha256(),
        "sha384":hashlib.sha384(),
        "sha512":hashlib.sha512(),
    }
    result = co_dict[mode]
    result.update(co_string)
    result = result.hexdigest()

    return result