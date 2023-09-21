string = str(input("Enter a string "))
position = int(input("Enter the index "))
new_char = input("Enter the character ")



def mutate_string(string,position,new_char):
    string_list = list(string)
    string_list[position] = new_char
    new_string = "".join(string_list)
    print(new_string)


mutate_string(string,position,new_char)