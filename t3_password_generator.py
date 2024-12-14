import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    
   
    all_characters = lowercase + uppercase + digits 
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 1): "))
            if length < 1:
                print("Please enter a valid length (1 or more).")
                continue
            
            password = generate_password(length)
            print(f"\nGenerated Password: {password}")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        play_again = input("\nDo you want to generate another password? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for using the Password Generator!")
            break

if __name__ == "__main__":
    main()
