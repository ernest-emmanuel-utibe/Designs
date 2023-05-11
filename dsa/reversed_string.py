sentences = input("Enter a string: ")


def palindrome(string):
    empty_string = " "
    for every_letters_entered_by_the_user in string:
        empty_string = every_letters_entered_by_the_user + empty_string

    return empty_string


print(palindrome(sentences))
