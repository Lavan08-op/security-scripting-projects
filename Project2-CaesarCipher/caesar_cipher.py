import string
import os
from datetime import datetime

ALPHABET = string.ascii_uppercase
LOG_FILE = "cipher_log.txt"


def build_shift_map(shift):
    """Builds an encryption lookup table for a given shift value."""
    shift = shift % 26
    shifted = ALPHABET[shift:] + ALPHABET[:shift]
    return dict(zip(ALPHABET, shifted))


def transform(text, shift):
    """Applies the shift map to a string, preserving case and symbols."""
    enc_map = build_shift_map(shift)
    output = []
    for ch in text:
        if ch.isupper():
            output.append(enc_map[ch])
        elif ch.islower():
            output.append(enc_map[ch.upper()].lower())
        else:
            output.append(ch)
    return "".join(output)


def encrypt_text(text, shift):
    return transform(text, shift)


def decrypt_text(text, shift):
    return transform(text, -shift)


def log_action(action, original, shift, result):
    """Keeps a local audit trail of every encryption/decryption run."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {action} | shift={shift} | input='{original}' | output='{result}'\n")


def brute_force_demo(ciphertext):
    """
    Shows why Caesar cipher is weak: tries all 25 possible shifts
    and prints the result, since the key space is tiny.
    """
    print("\n--- Brute Force Demonstration (all 25 keys) ---")
    for key in range(1, 26):
        guess = decrypt_text(ciphertext, key)
        print(f"Shift {key:2}: {guess}")
    print("--- End of brute force scan ---\n")


def validate_shift(value):
    try:
        key = int(value)
        if not (1 <= key <= 25):
            raise ValueError
        return key
    except ValueError:
        return None


def save_to_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    print(f"Saved to {filename}")


def menu():
    print("\n===== Caesar Cipher Toolkit =====")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Encrypt + Decrypt + Verify")
    print("4. Brute-force demo (crack a ciphertext)")
    print("5. Exit")
    return input("Choose an option (1-5): ").strip()


def main():
    print("Welcome to the Caesar Cipher Tool — DecodeLabs Project 2")

    while True:
        choice = menu()

        if choice == "1":
            msg = input("Enter message to encrypt: ")
            key = None
            while key is None:
                key = validate_shift(input("Enter shift key (1-25): "))
                if key is None:
                    print("Invalid key. Must be a number between 1 and 25.")
            result = encrypt_text(msg, key)
            print(f"Encrypted: {result}")
            log_action("ENCRYPT", msg, key, result)
            if input("Save to file? (y/n): ").lower() == "y":
                save_to_file("encrypted_output.txt", result)

        elif choice == "2":
            msg = input("Enter message to decrypt: ")
            key = None
            while key is None:
                key = validate_shift(input("Enter shift key (1-25): "))
                if key is None:
                    print("Invalid key. Must be a number between 1 and 25.")
            result = decrypt_text(msg, key)
            print(f"Decrypted: {result}")
            log_action("DECRYPT", msg, key, result)

        elif choice == "3":
            msg = input("Enter message: ")
            key = None
            while key is None:
                key = validate_shift(input("Enter shift key (1-25): "))
                if key is None:
                    print("Invalid key. Must be a number between 1 and 25.")
            enc = encrypt_text(msg, key)
            dec = decrypt_text(enc, key)
            print(f"\nOriginal : {msg}")
            print(f"Encrypted: {enc}")
            print(f"Decrypted: {dec}")
            status = "PASSED" if dec == msg else "FAILED"
            print(f"Verification: {status}")
            log_action("VERIFY", msg, key, f"enc={enc}, dec={dec}, status={status}")

        elif choice == "4":
            ciphertext = input("Enter ciphertext to brute-force: ")
            brute_force_demo(ciphertext)
            log_action("BRUTE_FORCE", ciphertext, "ALL", "see console output")

        elif choice == "5":
            print("Exiting. Stay secure!")
            break

        else:
            print("Invalid choice, pick between 1-5.")


if __name__ == "__main__":
    main()
