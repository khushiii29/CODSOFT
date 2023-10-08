import random
import string
def generate_password(length, complexity):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    if complexity == 1:
        charset = lowercase + uppercase
    elif complexity == 2:
        charset = lowercase + uppercase + digits
    elif complexity == 3:
        charset = lowercase + uppercase + digits + special_chars
    else:
        print("Invalid complexity level")
        return None
    password = ''.join(random.choice(charset) for _ in range(length))
    return password
if __name__ == "__main__":
    try:
        length = int(input("Enter the password length: "))
        complexity = int(input("Enter the complexity level (1, 2, or 3): "))
        password = generate_password(length, complexity)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter valid numbers for length and complexity.")
