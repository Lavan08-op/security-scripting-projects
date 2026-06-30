import re

def password_checker(pwd):
    score = 0
    feedback = []

    # length check
    if len(pwd) < 8:
        return "WEAK", ["Password too short, needs at least 8 characters"]
    elif len(pwd) >= 12:
        score += 2
    else:
        score += 1

    # character checks using regex instead of any()
    if re.search(r'[A-Z]', pwd):
        score += 1
    else:
        feedback.append("Add an uppercase letter")

    if re.search(r'[a-z]', pwd):
        score += 1
    else:
        feedback.append("Add a lowercase letter")

    if re.search(r'[0-9]', pwd):
        score += 1
    else:
        feedback.append("Add a number")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd):
        score += 1
    else:
        feedback.append("Add a special character like @ # $ %")

    # common password check
    weak_list = ["password", "12345678", "qwerty123", "admin123", "letmein"]
    if pwd.lower() in weak_list:
        return "WEAK", ["This is a commonly leaked password, choose something else"]

    # repeated character check (like aaaa1111)
    if re.search(r'(.)\1{2,}', pwd):
        score -= 1
        feedback.append("Avoid repeating the same character too many times")

    # final verdict
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, feedback


while True:
    user_pwd = input("\nEnter your password (or type 'exit' to quit): ")
    if user_pwd.lower() == "exit":
        print("Closing password checker...")
        break

    result, tips = password_checker(user_pwd)
    print(f"Strength: {result}")
    if tips:
        print("Suggestions:")
        for t in tips:
            print(" -", t)
