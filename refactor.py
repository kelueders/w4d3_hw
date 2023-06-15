# Split Strings 
# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/python
# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing 
# second character of the final pair with an underscore ('_').

def solution(s):    # overall is linear
    if s == "":  # constant time
        return []
    if len(s) % 2 != 0:   # constant time
        s += "_"
    # changed to a list comprehension instead of a for loop using .append inside it, which improves efficiency a little?
    answer = [s[i:i+2] for i in range(0, len(s), 2)]  # linear time complexity
#     for i in range(0, len(s), 2):
#         answer.append(s[i:i+2])
    return answer

# s = 'abc'
# print(solution(s))



# All Star Code Challenge #15
# https://www.codewars.com/kata/586560a639c5ab3a260000f3
# Create a function named rotate() that accepts a string argument and returns an array of 
# strings with each letter from the input string being rotated to the end.

def rotate(str_):    # entire solution is linear
    answer_array = []   # constant time
    strlist = list(str_)  # linear time
    while len(answer_array) != len(str_):    # linear time                         
        last_letter = strlist.pop(0)         
        strlist.append(last_letter)
        answer_array.append("".join(strlist))
    return answer_array

print(rotate("Hello"))

# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
# Simple, given a string of words, return the length of the shortest word(s).

def find_short(s):    # overall is linear
    shortest_word_length = float("inf")     # constant time
    word_list = s.split(" ")                # linear time (to iterate through entire string to find all occurrences of the delimiter)
    for word in word_list:                  # linear
        word_length = len(word)                         # constant time
        if word_length <= shortest_word_length:          # constant time
            shortest_word_length = word_length  
    return shortest_word_length