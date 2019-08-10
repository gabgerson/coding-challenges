#combo of my solution and official solution

def reverse_characters(message, left_index, right_index):
    """Reverse a letters in a list. Input will be a list because strings
        are immutable in python.
    """   
    # saved_letter = None

    while left_index < right_index:

        # saved_letter = message[left_index]
        message[left_index], message[right_index] = message[right_index], message[left_index]
        # message[end] = saved_letter

        left_index += 1
        right_index -= 1

    return message




def reverse_words(message):
    reverse_characters(message, 0, len(message) - 1)

    current_word_start_index = 0
    print(len(message))
    for i in range(len(message) + 1):

        print(i)

        if i == len(message) or message[i]== " ":
            reverse_characters(message, current_word_start_index, i - 1)

            current_word_start_index = i + 1
    # for i in range(len(message)):
    #     print(i)
    return message

    #  remember that the end bound of range is excluded so range(len(message))
    # len message is 16 so it excludes 16
    # so the range goes from 0 to 15 so have to add one  to make it loop 16 times
    # mesage being the one below



print(reverse_words([ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]))
