#Auto Nickname Combiner.....

import random
first = input("Enter your first name: ").strip().capitalize()
last = input("Enter your last name: ").strip().capitalize()

nicknames = [
    first[:3] + last[-3:],
    last[:3] + first[-3:],
    first + last,
    last + first,
    first[0] + last,
    first + last[0],
    first[:2] + last[:2],
    first[::-1] + last[::-1],
]
symbols = ['_', '.', '-', '']
numbers = [str(random.randint(10, 99)) for _ in range(5)]

for _ in range(5):
    part1 = random.choice([first, last, first[:3], last[-3:]])
    part2 = random.choice([first[::-1], last[::-1], last[:2], first[-2:]])
    sym = random.choice(symbols)
    num = random.choice(numbers)
    nickname = part1 + sym + part2 + num
    nicknames.append(nickname)

style = input("Do you want (short/fun/formal) style nicknames? ").lower()

styled_nicknames = []
for name in nicknames:
    if style == "short" and len(name) <= 8:
        styled_nicknames.append(name)
    elif style == "fun" and any(char.isdigit() or char in symbols for char in name):
        styled_nicknames.append(name)
    elif style == "formal" and name.isalpha():
        styled_nicknames.append(name)

if not styled_nicknames:
    styled_nicknames = nicknames

print("\n🎉 Your generated nicknames:")
for i, name in enumerate(set(styled_nicknames), start=1):
    print(f"{i}. {name}")

save = input("\nDo you want to save these nicknames to a file? (yes/no): ").lower()
if save == "yes":
    with open("nicknames.txt", "w") as f:
        for name in styled_nicknames:
            f.write(name + "\n")
    print("✅ Nicknames saved to 'nicknames.txt'")
