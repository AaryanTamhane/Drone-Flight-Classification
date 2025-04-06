from Crypto.Cipher import AES
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(message).encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

# Sender side input
key = b'16charAESKey1234'  # 16-byte key
message = input("Enter drone command to encrypt: ")

encrypted = encrypt_message(key, message)
print("\n🔒 Encrypted Message:", encrypted)

# Optionally save to file
with open("encrypted_command.txt", "w") as f:
    f.write(encrypted)
