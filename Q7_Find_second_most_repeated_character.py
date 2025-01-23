# string = "aabbbbbccddddd"
# Find me the most repeated char in the string
# Find me the second most repeated char in the string

# Solution for most repeated Character in the string
def repeatedChar(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    
    frequency = list(set(char_count.values()))
    frequency.sort(reverse=True)
    
    second_most_frequency = frequency[1]
    
    second_highest =[]
    for char, count in char_count.items():
        if count == second_most_frequency:
            second_highest.append(char)
        
    return second_highest


string = "aabbbbbccddddd"
print(repeatedChar(string)) 