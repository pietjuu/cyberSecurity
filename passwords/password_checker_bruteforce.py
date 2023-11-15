import hashlib
import getpass

# Word to hash
password = getpass.getpass("Enter the word to hash: ")

# Hashing using MD5
md5_hash = hashlib.md5(password.encode()).hexdigest()
print(f"MD5 Hash: {md5_hash}")

# Hashing using SHA-256
sha256_hash = hashlib.sha256(password.encode()).hexdigest()
print(f"SHA-256 Hash: {sha256_hash}")

# Path to a dictionary file containing potential passwords
dictionary_file = "wordlist/wordlist.txt"


def crack_password(hash_to_crack, dictionary_file):
    try:
        with open(dictionary_file, 'r') as file:
            for line in file:
                password = line.strip()
                password_hash = hashlib.md5(password.encode()).hexdigest()

                # Compare the calculated hash to the target hash
                if password_hash == hash_to_crack:
                    return f"Password cracked: {password}"
        return "Password not found in the dictionary."
    except FileNotFoundError:
        return "Dictionary file not found."


result_md5 = crack_password(md5_hash, dictionary_file)
result_sha256 = crack_password(sha256_hash, dictionary_file)

print(result_md5)
print(result_sha256)