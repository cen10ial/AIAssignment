import random
import string

# ---------------- CAPTCHA ----------------

def generate_captcha(length=6):
    chars = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(chars) for _ in range(length))
    return captcha

def captcha_system():
    captcha = generate_captcha()

    print("\n===== CAPTCHA Verification =====")
    print("Enter the CAPTCHA below:")

    # simple distortion
    distorted = " ".join(captcha)
    print(distorted)

    user_input = input("Captcha: ")

    if user_input == captcha:
        print("Access Granted (Human Verified)")
    else:
        print("Verification Failed")


# ---------------- TURING TEST ----------------

def ai_response(question):
    responses = [
        "That's interesting.",
        "I think it depends on the situation.",
        "Can you explain more?",
        "I'm not sure about that.",
        "That sounds good."
    ]
    return random.choice(responses)

def turing_test():
    print("\n===== Turing Test Simulation =====")

    question = input("Judge asks a question: ")

    human_answer = input("Human participant answer: ")
    ai_answer = ai_response(question)

    participants = [("A", human_answer), ("B", ai_answer)]
    random.shuffle(participants)

    print("\nResponses:")
    for label, ans in participants:
        print(label + ": " + ans)

    guess = input("\nJudge: Which one is AI? (A/B): ")

    for label, ans in participants:
        if ans == ai_answer:
            ai_label = label

    if guess.upper() == ai_label:
        print("Correct! AI identified.")
    else:
        print("Wrong! AI fooled the judge.")


# ---------------- MAIN PROGRAM ----------------

while True:
    print("\n===== MENU =====")
    print("1. CAPTCHA System")
    print("2. Turing Test Simulation")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        captcha_system()
    elif choice == "2":
        turing_test()
    elif choice == "3":
        print("Program Ended")
        break
    else:
        print("Invalid choice")
