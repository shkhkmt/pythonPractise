from sys import argv

script, userName, pseudonym = argv
prompt = '> '

print(f"Hi {userName}, I'm the {script} script.")
print(f"Do you have a nickname?")
nickName = input(prompt)
print(f"{nickName}? that's cool. I wonder how you got it?")
backStory = input(prompt)

print(f"Do you like me {userName}?")
likes = input(prompt)

print(f"Where do you live {userName}?")
lives = input(prompt)

print("What kind of computer do you have?")

computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me. You said you go by, {nickName}.
And that you got this name from {backStory}.
You live in {lives}. South Africa's biggest city.
And you have a {computer} computer. Which isn't relevant to anything.
""")

