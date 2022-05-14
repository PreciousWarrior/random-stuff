import random


def get_words(filename="words.txt"):
    file_object = open(filename, "r")
    return file_object.read().splitlines()


def get_number_extension(number):
    number = str(number)
    if len(number) >= 2:
        second_last_digit = number[len(number)-2]
        if second_last_digit == "1":
            return "th"
    last_digit = number[len(number)-1]

    digits_and_extensions = {
        "1": "st",
        "2": "nd",
        "3": "rd"
    }
    if last_digit not in digits_and_extensions.keys():
        return "th"
    return digits_and_extensions[last_digit]


def get_user_settings():
    while True:
        i = input("Enter your maximum word character length (Press enter for no max length)")
        if i == "":
            max_char_lim = None
            break
        try:
            max_char_lim = int(i)
            break
        except ValueError:
            pass
    while True:
        i = input("Enter the number of words you want in your password (Press enter for 4)")
        if i == "":
            number_of_words = 4
            break
        try:
            number_of_words = int(i)
            if number_of_words <= 20:
                break
        except ValueError:
            pass
    return max_char_lim, number_of_words


def make_password():
    settings = get_user_settings()
    words = get_words()
    password = []

    for word_number in range(1, settings[1]+1):
        while True:
            while True:
                random_word = random.choice(words)
                if random_word not in password:
                    if settings[0] is None:
                        break
                    if settings[0] > len(random_word):
                        break
            i = input(f"Would you like {random_word} as the {word_number}{get_number_extension(word_number)} word in "
                      f"your password? (y for yes, n or enter for no)")
            if i == "y":
                password.append(random_word)
                break

    print(f"Your password is -: ({''.join(password)}).")


while True:
    make_password()
    i = input("Press enter to exit the program or type anything to start it again.")
    if i == "":
        break


