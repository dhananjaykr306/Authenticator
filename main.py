import time
import pyotp


key = "Mysecertsuperkey"

totp = pyotp.TOTP(key)

print(totp.now())

time.sleep(30)

print(totp.now())

input_code =input("Enter your 2FA Code:")

print(totp.verify(input_code))