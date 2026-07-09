# Import the regular expression module.
# Purpose: Used to search for patterns like uppercase letters, numbers, etc.
import re


# Function to check the password strength.
# Purpose: Keeps the code organized and reusable.
def check_password(password):

    # Variable to store the password score.
    # Purpose: Higher score means a stronger password.

    score = 0

    # Check if the password length is at least 8 characters.
    # Why: Longer passwords are harder for attackers to guess.
    if len(password) >= 8:
        score += 1
    else:
        print("❌ Password should be at least 8 characters long.")

    # Check for at least one uppercase letter.
    # Why: Adds complexity and improves security.
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        print("❌ Add at least one uppercase letter.")

    # Check for at least one lowercase letter.
    # Why: Mixing uppercase and lowercase makes passwords stronger.
    if re.search(r"[a-z]", password):
        score += 1
    else:
        print("❌ Add at least one lowercase letter.")

    # Check for at least one digit.
    # Why: Numbers increase the number of possible password combinations.
    if re.search(r"[0-9]", password):
        score += 1
    else:
        print("❌ Add at least one number.")

    # Check for at least one special character.
    # Why: Special characters make passwords more difficult to crack.
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        print("❌ Add at least one special character.")

    # List of common passwords.
    # Purpose: These passwords are easily guessed by attackers.
    common_passwords = ["password", "123456", "admin", "qwerty"]

    # Check whether the entered password is in the common password list.
    # lower() converts the password to lowercase for case-insensitive comparison.
    if password.lower() in common_passwords:
        print("❌ This is a commonly used password.")
        score -= 1 # Reduce the score because it is insecure.

    # Display the final score.
    print("\nPassword Score:", score, "/5")

    # Decide the password strength based on the score.
    # Why: Gives the user an easy-to-understand result.
    if score == 5:
        print("✅ Password Strength: Strong")
    elif score >= 3:
        print("⚠️ Password Strength: Moderate")
    else:
        print("❌ Password Strength: Weak")


# Ask the user to enter a password.
# input() reads the password entered by the user.
password = input("Enter your password: ")

# Call the function to check the password.
# Purpose: Starts the password strength checking process.
check_password(password)