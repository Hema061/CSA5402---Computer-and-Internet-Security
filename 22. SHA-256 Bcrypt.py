import hashlib 
import bcrypt 
import time 
 
# Function to hash using SHA-256 
def hash_sha256(data): 
    sha256 = hashlib.sha256() 
    sha256.update(data.encode('utf-8')) 
    return sha256.hexdigest() 
 
# Function to hash using bcrypt 
def hash_bcrypt(data): 
    salt = bcrypt.gensalt() 
    return bcrypt.hashpw(data.encode('utf-8'), salt) 
 
# Function to compare performance and security of SHA-256 and bcrypt 
def compare_hashing_algorithms(): 
    data = "supersecretpassword" 
     
    # SHA-256 hashing 
    start_time = time.time() 
    sha256_hash = hash_sha256(data) 
    sha256_time = time.time() - start_time 
    print(f"SHA-256 Hash: {sha256_hash}") 
    print(f"SHA-256 Time: {sha256_time:.6f} seconds") 
     
    # bcrypt hashing 
    start_time = time.time() 
    bcrypt_hash = hash_bcrypt(data) 
    bcrypt_time = time.time() - start_time 
    print(f"bcrypt Hash: {bcrypt_hash}") 
    print(f"bcrypt Time: {bcrypt_time:.6f} seconds") 
     
    # Comparing performance 
    print("\nPerformance Comparison:") 
    print(f"SHA-256 is faster than bcrypt by {bcrypt_time/sha256_time:.2f} times.") 
     
    # Security Considerations 
    print("\nSecurity Considerations:") 
    print("1. SHA-256 is fast, making it vulnerable to brute-force attacks and rainbow table attacks.") 
    print("2. bcrypt is designed to be slow, increasing the time for brute-force attacks and making it more secure.") 
    print("3. bcrypt also uses a salt to protect against rainbow table attacks.") 
    print("4. bcrypt hashes cannot be reversed, and it includes a work factor (cost factor) to make hashing more expensive.") 
 
# Main function to run the comparison 
if __name__ == "__main__": 
    compare_hashing_algorithms() 
