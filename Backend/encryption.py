from cryptography.fernet import Fernet

# Generate or load encryption key
def generate_key():
    """
    Generates a new encryption key and saves it to a file.
    This key is required for encryption and decryption.
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the encryption key from a file.
    This key must be the same for encryption and decryption.
    """
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Key file not found! Generating a new one...")
        generate_key()
        return load_key()

# Load the encryption key
key = load_key()
cipher = Fernet(key)

def encrypt_data(message: str) -> str:
    """
    Encrypts the given message using Fernet symmetric encryption.

    Args:
        message (str): The plaintext message to encrypt.

    Returns:
        str: The encrypted message in base64 format.
    """
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message.decode()  # Convert bytes to string

def decrypt_data(encrypted_message: str) -> str:
    """
    Decrypts an encrypted message using the stored key.

    Args:
        encrypted_message (str): The encrypted message in base64 format.

    Returns:
        str: The original decrypted message.
    """
    decrypted_message = cipher.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

if __name__ == "__main__":
    # Example Usage
    message = "Emergency vehicle detected at Sector 45"
    encrypted = encrypt_data(message)
    print(f"Encrypted Message: {encrypted}")

    decrypted = decrypt_data(encrypted)
    print(f"Decrypted Message: {decrypted}")
