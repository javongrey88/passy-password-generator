import random

# Define character pools
letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!#$%&()*+')

def generate_secure_password(nr_letters, nr_symbols, nr_numbers):
    password_chars = []

    # Add random letters, symbols, and numbers to the list
    password_chars += random.choices(letters, k=nr_letters)
    password_chars += random.choices(symbols, k=nr_symbols)
    password_chars += random.choices(numbers, k=nr_numbers)

    # Shuffle the characters for unpredictability
    random.shuffle(password_chars)

    # Join them into a single string
    return ''.join(password_chars)

if __name__ == '__main__':
    print("Welcome to Passy – your AI-generated password wizard 🧙‍♂️🔐")
    try:
        nr_letters = int(input("How many letters? "))
        nr_symbols = int(input("How many symbols? "))
        nr_numbers = int(input("How many numbers? "))

        password = generate_secure_password(nr_letters, nr_symbols, nr_numbers)
        print(f"Here is your strong password: {password}")
    except ValueError:
        print("⚠️ Please enter valid numbers only!")



