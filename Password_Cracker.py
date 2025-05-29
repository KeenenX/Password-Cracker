import hashlib
import urllib.request

url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/Ashley-Madison.txt"
response = urllib.request.urlopen(url)

password = "booomer"
enc_password = password.encode("utf-8")
password_hash = hashlib.md5(enc_password.strip()).hexdigest()

for line in response:
    word = line.decode("utf-8")
    enc_word = word.encode("utf-8")
    enc_hash = hashlib.md5(enc_word.strip()).hexdigest()

    if password_hash == enc_hash:
        print("This agency has been compromised! Password found: " + word)
        quit()

print("This agency has a strong password.")
