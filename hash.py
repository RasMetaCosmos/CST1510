import bcrypt

# This module provides functions for hashing passwords and checking hashed passwords using bcrypt.

# Hashing a plain text password
def hash_password(plain_text_password):
    password_bytes = plain_text_password.encode("utf-8")
    salt = bcrypt.gensalt()
    bcrypted_password = bcrypt.hashpw(password_bytes, salt)
    return (bcrypted_password).decode("utf-8")

# Checking a plain text password against a hashed password  
def check_password(plain_text_password, hash_password):
    password_bytes = plain_text_password.encode("utf-8")
    hash_password_bytes = hash_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hash_password_bytes)


