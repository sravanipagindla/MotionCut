#Fake Job Title Generator

import random
adjectives = ["Certified", "Global", "Virtual", "Dynamic", "Senior", "Lead", "Quantum", "Invisible", "Eco-friendly", "Futuristic"]
roles = ["Meme", "Unicorn", "AI", "Blockchain", "Vibes", "Cloud", "Emoji", "Crypto", "WiFi", "Energy", "Robot"]
suffixes = ["Strategist", "Engineer", "Manager", "Guru", "Architect", "Consultant", "Ninja", "Overlord", "Whisperer", "Wizard"]
def generate_job_title():
    adj = random.choice(adjectives)
    role = random.choice(roles)
    suffix = random.choice(suffixes)
    job_title = f"{adj} {role} {suffix}"
    return job_title
print("Welcome to the Fake Job Title Generator!\n")
while True:
    print("Your Fake Job Title is:", generate_job_title())
    again = input("Do you want another title? (yes/no): ").strip().lower()

    if again != 'yes':
        print("Thanks for using the Fake Job Title Generator! Keep being awesome! 😄")
        break
    print("-" * 50)
