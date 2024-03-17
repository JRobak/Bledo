import random

LENGTH = 10

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
low_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
joined = numbers + low_letter + upper_letter

# for x in range(65, 91):
#     upper_letter.append(chr(x))
#
# for x in range(97, 123):
#     low_letter.append(chr(x))


def create_session_number(length):
    session_numbers = []
    for i in range(length):
        rand = random.randint(0, len(joined)-1)
        session_numbers.append(str(joined[rand]))
    return ''.join(session_numbers)


