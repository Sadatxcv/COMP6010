"""
# Student Declaration
# I [48738085] declare that this is my own work and that
# I have not used any code or logic from other people or from sources outside of the unit.
# I understand that it is ok to look at COMP6010 videos and COMP6010 resources
# and that researching how certain python operators / functions work is ok.
# [x] <== put an x in here to indicate you have read and agree to the above statements.
"""


def main():
    print("--- encode ---")
    print(encode("Spiral helix"))  # expected answer: Sp1r4l h3l1x
    print(encode("CIAO adios ADIEU"))  # expected answer: C140 4d10s 4D13U
    print(encode("1a2b3c456"))  # expected answer: 142b3c456
    print(encode("Greetings, kids!"))  # expected answer: Gr33t1ngs, k1ds!
    print(
        encode("Time to learn about weather")
    )  # expected answer: T1m3 t0 l34rn 4b0ut w34th3r
    print(encode(123))  # expected answer: None

    print("--- has_same_encoding ---")
    print(has_same_encoding("11", "2"))  # expected answer: False
    print(has_same_encoding(11, 2))  # expected answer: None
    print(has_same_encoding("4e", "43"))  # expected answer: True
    print(has_same_encoding("4e", 43))  # expected answer: None
    print(has_same_encoding("sunny", "5unny"))  # expected answer: False
    print(has_same_encoding("CI4O", "C1A0"))  # expected answer: True

    print("--- count_daynight_pairs ---")
    print(count_daynight_pairs([8, 2, 4, 5, 9, 3]))  # expected answer: 2
    print(count_daynight_pairs([10, 3, 10, 3, 9, 9, 10, 2]))  # expected answer: 4
    print(count_daynight_pairs([10, 3, 10, 3, 10]))  # expected answer: None
    print(count_daynight_pairs([1, 2, 3, 4, 5, 6]))  # expected answer: 0
    print(count_daynight_pairs([6, 5, 4, 3, 2, 1]))  # expected answer: 3

    print("--- classify_temperatures ---")
    print(
        classify_temperatures(20, 45, [28, 20, 14, 18, 30, 45, 46])
    )  # expected answer: 2 days were colder than 20, 1 days were hotter than 45, and 4 days were normal.
    print(
        classify_temperatures(20, 45, [1, 2, 3])
    )  # expected answer: 3 days were colder than 20, 0 days were hotter than 45, and 0 days were normal.
    print(
        classify_temperatures(33, 32, [28, 20, 14, 18, 30, 45, 46])
    )  # expected answer: Warning: 33 is greater than 32.
    print(
        classify_temperatures(18, 18, [28, 20, 14, 18, 30, 45, 46])
    )  # expected answer: 1 days were colder than 18, 5 days were hotter than 18, and 1 days were normal.
    print(
        classify_temperatures(10, 25, [17, 19, 19, 18])
    )  # expected answer: 0 days were colder than 10, 0 days were hotter than 25, and 4 days were normal.

    print("--- filter_junk ---")
    print(filter_junk([20, 23, 24, None, 20]))  # expected answer: [20,23,24,20]
    print(filter_junk([40, 40, 4, 0, 40, 40]))  # expected answer: [40,40,4,40,40]
    print(filter_junk([0, "tuesday", 0, None]))  # expected answer: []
    print(filter_junk([3, 4, "wednesday", 0, True, 5]))  # expected answer: [3,4,5]

    print("--- find_biggest_chill ---")
    print(find_biggest_chill([30, 28, 30, 40]))  # expected answer: 2
    print(find_biggest_chill([30, 28, 40, 30]))  # expected answer: 10
    print(find_biggest_chill([40, 32, 30, 33, 26]))  # expected answer: 8
    print(find_biggest_chill([18, 19, 19, 20, 25]))  # expected answer: None
    print(find_biggest_chill([30]))  # expected answer: None
    print(find_biggest_chill([30, 30]))  # expected answer: None
    print(find_biggest_chill([30, 40, 35, 30, 40]))  # expected answer: 5
    print(find_biggest_chill([100, 1]))  # expected answer: 99
    print(find_biggest_chill([100, 0]))  # expected answer: 100

    print("--- find_biggest_chill_ignoring_junk ---")
    print(
        find_biggest_chill_ignoring_junk([30, "thirty one", 28, 30, 40])
    )  # expected answer: 2
    print(find_biggest_chill_ignoring_junk([100, 1]))  # expected answer: 99
    print(find_biggest_chill_ignoring_junk([100, 0]))  # expected answer: None
    print(find_biggest_chill_ignoring_junk([30, None, 0, 27]))  # expected answer: 3

    print("--- longest_heatwave ---")
    print(longest_heatwave(40, [40, 41, 40, 41, 41]))  # expected answer: 2
    print(longest_heatwave(38, [35, 36, 37, 38]))  # expected answer: 0
    print(longest_heatwave(38, [40, 42, 35, 41, 43, 32]))  # expected answer: 2
    print(longest_heatwave(38, [40, 38]))  # expected answer: 1
    print(longest_heatwave(35, [38]))  # expected answer: 1
    print(
        longest_heatwave(40, [38, 42, 43, 39, 43, 44, 45, 40, 41, 42])
    )  # expected answer: 3

    # TODO: (OPTIONAL) Add your own tests!


# WARNING:
# Do NOT modify any function headers (for example, do NOT modify the line "def encode(s):").


def encode(s):
    """
    Given a string, replace all 'i' and 'I' characters with '1',
    replace all 'e' and 'E' characters with '3',
    replace all 'a' and 'A' characters with '4', and
    replace all 'o' and 'O' characters with '0'.

    You must perform type checking to ensure the inputs are of correct type.
    If the input is not of correct type, your function should return None.
    """
    # TODO To be completed
    if type(s) != str:
        return None
    else:
        result = ""
        for letter in s:
            if letter == "i" or letter == "I":
                result += "1"
            elif letter == "e" or letter == "E":
                result += "3"
            elif letter == "a" or letter == "A":
                result += "4"
            elif letter == "o" or letter == "O":
                result += "0"
            else:
                result += letter
        return result


def has_same_encoding(a, b):
    """
    Given two strings, "encode" them according the the previous question.
    Return True if the resulting strings are the same, and False if the resulting strings are different.

    You must perform type checking to ensure the inputs are of correct type.
    If the input is not of correct type, your function should return None.
    """
    # TODO To be completed
    if type(a) == str and type(b) == str:
        encoded_str_a = encode(a)
        encoded_str_b = encode(b)
        if encoded_str_a == encoded_str_b:
            return True
        else:
            return False
    else:
        return None


def count_daynight_pairs(temps):
    """
    Given an list of numbers, 'temps',
    if 'temps' has an odd number of elements, return None.
    If 'temps' has an even number of elements, split it into adjacent pairs,
    count the number of pairs where the first >= the second,
    and return that count.

    E.g. if 'temps' = [8,2,4,5,9,3],
    split it into [8,2], [4,5], and [9,3].
    Now we count pairs. (8 >= 2): good. (4 < 5): bad. (9 >= 3): good.
    The function should return the number 2.

    E.g. if 'temps' = [10,3,10,3,9,9,10,2],
    split it into [10,3], [10,3], [9,9] and [10,2].
    Now we count pairs. (10 >= 3): good. (10 >= 3): good. (9 >= 9): good. (10 >= 2): good.
    The function should return the number 4.

    E.g. if 'temps' = [10,3,10,3,10],
    there is an odd number of elements.
    The function should return None.

    You may assume inputs are of correct type. (I.e., 'temps' is an list of numbers.)
    """
    # TODO To be completed

    if len(temps) % 2 != 0:
        return None
    count = 0
    for i in range(0, len(temps), 2):
        x = temps[i]
        y = temps[i + 1]
        if x >= y:
            count += 1
    return count


def classify_temperatures(coldest, hottest, temps):
    """
    Given two numbers, 'coldest' and 'hottest', and an list of numbers, 'temps',
    if 'coldest' is greater than 'hottest', then return a string formatted like below:
    Warning: ____ is greater than ____.

    Otherwise, count how many elements of 'temps' are *lower* than 'coldest',
    how many are *higher* than 'hottest',
    and how many are somewhere in between (inclusive).
    Return this information using the string format shown below:
    ____ days were colder than ____, ____ days were hotter than ____, and ____ days were normal.


    For example if coldest=20, hottest=45, and temps=[28, 20, 14, 18, 30, 45, 46], then the function should return this string:
    2 days were colder than 20, 1 days were hotter than 45, and 4 days were normal.

    For example if coldest=33, hottest=32, and temps=[28, 20, 14, 18, 30, 45, 46], then the function should return this string:
    Warning: 33 is greater than 32.

    For example if coldest=18, hottest=18, and temps=[28, 20, 14, 18, 30, 45, 46], then the function should return this string:
    1 days were colder than 18, 5 days were hotter than 18, and 1 days were normal.

    You may assume inputs are of correct type. (I.e., 'coldest' and 'hottest' are numbers, and 'temps' is an list of numbers.)
    """
    # TODO To be completed
    if coldest > hottest:
        return f"Warning: {coldest} is greater than {hottest}."
    cold_count = 0
    hot_count = 0
    normal_count = 0
    for i in temps:
        if i > hottest:
            hot_count += 1
        elif i < coldest:
            cold_count += 1
        else:
            normal_count += 1
    return f"{cold_count} days were colder than {coldest}, {hot_count} days were hotter than {hottest}, and {normal_count} days were normal."


def filter_junk(temps):
    """
    Given a list 'temps', remove every element that is neither a float nor an int,
    and remove every element that is equal to 0.
    Return the resulting list.

    You may assume that 'temps' is a list.
    """
    # TODO To be completed
    for i in temps[:]:
        if type(i) != int and type(i) != float or i == 0:
            temps.remove(i)
    return temps


def find_biggest_chill(temps):
    """
    Given a list 'temps',
    analyse 'temps' for elements that are *lower* than their previous element.
    This is called a 'chill', and the size of the chill is the difference between the elements.
    Return the size of the biggest chill, or if there are no chills, return None.

    For example if 'temps' is [40,32,30,33,26], the chills are
    40 -> 32 (size 8), 32 -> 30 (size 2), 33 -> 26 (size 7).
    The function should return 8.

    You may assume inputs are of correct type. (I.e., 'temps' is an list of numbers.)
    """
    # TODO To be completed
    biggest_chill = None

    for i in range(1, len(temps)):
        if temps[i] < temps[i - 1]:
            chill_size = temps[i - 1] - temps[i]
            if biggest_chill == None or chill_size > biggest_chill:
                biggest_chill = chill_size

    return biggest_chill


def find_biggest_chill_ignoring_junk(temps):
    """
    Given a list 'temps', remove every element that is neither a float nor an int,
    and remove every element that is equal to 0.

    *Then*, return the size of the biggest chill, or if there are no chills, return None.

    You may assume that 'temps' is a list.
    """
    # TODO To be completed
    for i in temps[:]:
        if type(i) != int and type(i) != float or i == 0:
            temps.remove(i)
    return find_biggest_chill(temps)


def longest_heatwave(threshold, temps):
    """
    Given a number 'threshold', and an list of numbers, 'temps',
    analyse 'temps' for elements that are *higher* than 'threshold'.
    Return the maximum number of *consecutive* elements that are higher than 'threshold'.

    You may assume inputs are of correct type. (I.e., 'threshold' is a number, and 'temps' is an list of numbers.)
    """
    # TODO To be completed
    max_len = 0
    current_len = 0

    for temp in temps:
        if temp > threshold:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 0
    return max_len


if __name__ == "__main__":
    main()
