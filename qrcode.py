import pyotp
import qrcode

key = "mysecretcode"
uri = pyotp.TOTP(key).provisioning_uri(name="Dhananjay123",issuer_name="Dhananjay")
print(uri)
qrcode.make(uri).save("total.png")

print('total.png')