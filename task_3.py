import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."
    
    # Character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ] + random.choices(all_characters, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired length of the password (minimum 4): "))
        password = generate_password(length)
        print(f"Generated Password: {password}" if isinstance(password, str) else password)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()