dict_str = {}
def removedup(string):
    dup = ''
    for char in string :
        if char in dict_str.keys() :
            dict_str[char] = dict_str[char]+1
        else:
            dict_str[char] = 1
            dup = dup+char

            
    print(dup)


string = str(input("enter string"))
print(string)
removedup(string)