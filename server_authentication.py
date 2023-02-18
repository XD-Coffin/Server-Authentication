import hashlib

realm = "random_string"
uri = "xyzcorporation.com/auth"
nonce = "random_string"
nonce_count = nonce.count("",1,100)
cnonce = "random_string"
qop = "auth"
# RFC 2069
def RFC2069(username, password):
    hash1_fm = f"{username}:{realm}:{password}"
    hash1 = hashlib.md5(hash1_fm.encode("utf-8")).hexdigest()
    hash2 = hashlib.md5(uri.encode("utf-8")).hexdigest()
    hash = f"{hash1}:{nonce}:{hash2}"
    result = hashlib.md5(hash.encode("utf-8")).hexdigest()
    print ("Server shows the hash: ",result)
    pass
def RFC2617(username,password):
    hash1_fm = f"{username}:{realm}:{password}"
    hash1 = hashlib.md5(hash1_fm.encode("utf-8")).hexdigest()
    hash2 = hashlib.md5(uri.encode("utf-8")).hexdigest()
    hash = f"{hash1}:{nonce}:{nonce_count}:{cnonce}:{qop}:{hash2}"
    result = hashlib.md5(hash.encode("utf-8")).hexdigest()
    print ("Server shows the hash: ",result)
    pass

username = input("Enter Username: ")
password = input("Enter Password: ")
auth = input("1 for RFC2069/2 for RFC2617 = ")
if auth == "1":
    RFC2069(username,password)
elif auth == "2":
    RFC2617(username,password)
else:
    print ("Invalid typo !")

