import string
import random
all_characters = string.ascii_letters + string.digits + string.punctuation
length = int(input("আপনার কত ডিজিটের পাসওয়ার্ড চান তা লিখুন: "))
password = ''.join(random.choices(all_characters, k=length))
print("আপনার পাসওয়ার্ড:", password)
