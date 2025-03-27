import pyotp
import time 
def generate_secret(): 

    totp = pyotp.TOTP(pyotp.random_base32()) 
    secret = totp.secret 
    print(f"Your secret key is: {secret}") 
    return secret 
 
def generate_otp(secret): 
    totp = pyotp.TOTP(secret) 
    otp = totp.now()  
    print(f"Generated OTP: {otp}") 
    return otp 
def verify_otp(secret, otp): 
    totp = pyotp.TOTP(secret) 
    if totp.verify(otp): 
        print("OTP Verified Successfully!") 
    else: 
        print("Invalid OTP! Verification Failed.") 
 
# Main function 
def main(): 
    print("Two-Factor Authentication (2FA) Demo") 
 
    secret = generate_secret() 
    otp = generate_otp(secret) 
    entered_otp = input("Enter the OTP: ") 
    verify_otp(secret, entered_otp) 
 
if __name__ ==  "__main__": 
   main()
