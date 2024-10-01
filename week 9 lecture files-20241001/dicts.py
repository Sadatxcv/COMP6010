# dictionaries
#
#
print("")

l = [1,  3,  5,   9]
#  l[0] l[1] l[2] l[3]


my_dict = {}          # <- squiggly braces (shift+[] on most keyboards)
my_dict["apple"] = "a type of fruit"
my_dict["pi"] = 22/7

# dictionaries have KEYs and VALUEs
# "keys" are what we use to look up entries, e.g. "apple", "pi"
# "values" are the information inside the entries

print(my_dict["apple"])
my_dict["apple"] = "a type of fruit that is sometimes red"
print(my_dict["apple"])
print(my_dict["pi"])

my_dict["chair"] = "a quadruped"
my_dict["horse"] = "a quadruped"

print(my_dict)


# print out the keys one by one
for word in my_dict.keys():
    print("next entry: " + word)
    print(my_dict[word])


print("my_dict.keys = " + str(my_dict.keys()))
print(my_dict.items())


### QUESTION 2
gpu_prices = {
    "NVIDIA GeForce RTX 3080": 799,
    "AMD Radeon RX 6900 XT": 999,
    "NVIDIA GeForce GTX 1660 Ti": 299,
    "AMD Radeon RX 6700 XT": 649,
    "NVIDIA GeForce RTX 3070": 499,
    "AMD Radeon RX 6600 XT": 349,
    "NVIDIA GeForce GTX 3050": 649,
    "NVIDIA GeForce GTX 1650 Super": 199,
}
#  APPROACH 1
TARGET_PRICE = 649

found = False

for gpu in gpu_prices.keys():
    if gpu_prices[gpu] == TARGET_PRICE:
        print(gpu)
        found = True

if not found:
    print("Value not found")

#  APPROACH 2

TARGET_PRICE = 649

found = False

for gpu, price in gpu_prices.items():
    if price == TARGET_PRICE:
        print(gpu)
        found = True


if not found:
    print("Value not found")

## QUESTION 3
song_times={} #  <--- so that the code runs

song = "Boogie Wonderland"

if song in song_times:
    print(song_times[song])
else:
    print("Key not found")


## QUESTION 4
def get_lap_times_lower(values, max_time):
    # Your code here
    names = []
    
    for their_name, their_time in values.items():
        if their_time < max_time:
            names.append(their_name)
    
    
    return names


print()
print()

# QUESTION 5


def convert_to_dict(listKeys, listValues):
    my_dict = {}
    for index in range(len(listKeys)):
        my_dict[listKeys[index]] = listValues[index]
    
    return my_dict

student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
exam_scores = [85, 92, 78, 96, 88]
print(convert_to_dict(student_names, exam_scores))


# QUESTION 6

name_counts = {}

for name in list_of_names:
    if name not in name_counts:
        name_counts[name] = 0
        
    name_counts[name] += 1

#for name in list_of_names:
#    if name not in name_counts:
#        name_counts[name] = 1
#    else:
#        name_counts[name] += 1