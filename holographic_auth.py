import pyotp #generate time based otps in every 30 sec
import random  #used to generate ascii art pattern
import time
import os #used here to clear the previous outputs


# Function to generate a TOTP (Time-Based One-Time Password)
def generate_totp(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()


# Function to create a dynamic holographic pattern (ASCII art)
def generate_holographic_pattern(data):
    # Characters for ASCII art
    chars = ['@', '#', '*', '%', '=', '+', '-', ':', '.', ' ']
    random.seed(data)  # Seed randomness with the data (TOTP)

    # Generate a 10x30 grid of random characters based on the seed
    pattern = ""
    for _ in range(10):  # 10 rows
        line = "".join(random.choices(chars, k=30))  # 30 characters per row
        pattern += line + "\n"
    return pattern


def display_holographic_pattern(secret):
    for i in range(3):  # Display 3 dynamic patterns
        os.system("clear" if os.name == "posix" else "cls")
        print("Dynamic Holographic Authentication System\n")
        
        # Combine TOTP with current time to ensure a different pattern
        current_totp = generate_totp(secret)
        dynamic_seed = current_totp + str(time.time())  # Adding current time for randomness
        holographic_pattern = generate_holographic_pattern(dynamic_seed)
        
        print("Holographic Pattern:\n")
        print(holographic_pattern)
        time.sleep(1.5)  # Pause before generating the next pattern

# Authentication flow
def authenticate_user(secret):
    os.system("clear" if os.name == "posix" else "cls")  #posix used for linux or macOS os  and cls used for windows
    print("Welcome to the Holographic Authentication System (CLI)\n")

    # Display dynamic holographic patterns
    display_holographic_pattern(secret)

    # Prompt user to enter the decoded TOTP
    user_input = input("\nEnter the decoded TOTP from your companion app: ")

    # Validate the user's input
    if user_input == generate_totp(secret):
        print("\nAuthentication Successful!")
    else:
        print("\nAuthentication Failed. Please try again.")


# Main function
if __name__ == "__main__":
    # Generate a shared secret (unique per user)
    SECRET_KEY = pyotp.random_base32()

    # Display shared secret for demonstration purposes
    print(f"Shared Secret (Save this in your authenticator app): {SECRET_KEY}\n")
    time.sleep(6)

    # Start the authentication process
    authenticate_user(SECRET_KEY)
