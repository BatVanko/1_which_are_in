substring_line = input().split(", ")
string_line = input()
subs_in_string = [el for el in substring_line if el in string_line]
print(subs_in_string)