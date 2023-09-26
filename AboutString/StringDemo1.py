import random
import string

#numbers = [12, 34, 203, 1112, 31, 7]
heading = ['firstName', 'lastName', 'Gender', 'Age']
#result1 = ', '.join(f"'{num1}'" for num1 in numbers)
result2 = ','.join(f"{num2}" for num2 in heading)
#print(result1)
print(result2)


'''
def generate_random_name(length=5):
    """Generate a random name with a given length."""
    return ''.join(random.choice(string.ascii_uppercase if i == 0 else string.ascii_lowercase)
                   for i in range(length))

# Generate 20 random first names and last names
random_names = [(generate_random_name(), generate_random_name()) for _ in range(20)]

for first, last in random_names:
    print(f"{first} {last}")



# Define some common name parts
prefixes = ['Ja', 'Mi', 'El', 'Ri', 'Al', 'So', 'Le', 'Da', 'Ro']
middle = ['vier', 'mi', 'bel', 'ton', 'lyn', 'na', 'ri', 'sia', 'la', 'nie']
suffixes = ['son', 'la', 'y', 'lee', 'lie', 'th', 'na', 'lie']

def generate_name():
    """Generate a semi-realistic name."""
    return random.choice(prefixes) + random.choice(middle) + random.choice(suffixes)

# Generate and print 20 names
for _ in range(100):
    print(generate_name())

'''

# Define some common name parts for first names and last names
first_prefixes = ['Ja', 'Mi', 'El', 'Ri', 'Al', 'So', 'Le', 'Da', 'Ro']
first_middle = ['vier', 'mi', 'bel', 'ton', 'lyn', 'na', 'ri', 'sia', 'la', 'nie']
first_suffixes = ['son', 'la', 'y', 'lee', 'lie', 'th', 'na', 'lie']

last_prefixes = ['And', 'Car', 'Ben', 'Har', 'Dal', 'Sta', 'Rod', 'Jen']
last_middle = ['der', 'ri', 'son', 'ter', 'man', 'ver', 'sen', 'kins']
last_suffixes = ['son', 'way', 'lan', 'by', 'ton', 'field', 'berg', 'stein']
gender = ['male', 'female', 'other']

def generate_first_name():
    """Generate a semi-realistic first name."""
    return random.choice(first_prefixes) + random.choice(first_middle) + random.choice(first_suffixes)

def generate_last_name():
    """Generate a semi-realistic last name."""
    return random.choice(last_prefixes) + random.choice(last_middle) + random.choice(last_suffixes)

def generate_gender():
    return random.choice(gender)

# Generate and print 20 first names and last names
for _ in range(20):
    print(generate_first_name()+","+generate_last_name()+","+generate_gender()+","+ str(random.randint(18, 65)))
