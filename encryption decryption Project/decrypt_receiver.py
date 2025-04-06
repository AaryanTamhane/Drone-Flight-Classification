from Crypto.Cipher import AES
import base64

def decrypt_message(key, encrypted_message):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_message)).decode('utf-8')
    return decrypted.strip()

# Receiver side input
key = b'16charAESKey1234'  # Must match sender key

# Read encrypted message from file
with open("encrypted_command.txt", "r") as f:
    encrypted = f.read()

decrypted = decrypt_message(key, encrypted)
print("\n📬 Decrypted Message:", decrypted)