from collections import defaultdict
def permutation_is_palindrome(user_input):
    character_map = defaultdict(lambda: 0)
    odd_occurrence = 0
    for character in user_input:
        character_map[character] += 1

    for count in character_map.values():
        if count % 2 == 0:
            continue
        else:
            odd_occurrence += 1
    if odd_occurrence <= 1:
        return True
    else:
        return False

def print_result(result, user_input):
    if result:
        print(user_input, ' is a palindrome')
    else:
        print(user_input, ' is not a palindrome')

if __name__ == '__main__':
    user_input = input('Enter the string which is to be identified as a palindrome')
    print_result(permutation_is_palindrome(user_input), user_input)
