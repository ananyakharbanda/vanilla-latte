def reverse(input_string):
    answer = ''
    for i in range(len(input_string)):
        answer = answer + input_string[len(input_string) - i -1]
    return answer

def join(list_strings):
    joined = ''
    for i in list_strings:
        joined = joined + i
    return joined

def strcmp(s1, s2):
    if (len(s1) != len(s2)):
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

if __name__ == '__main__':

# reverse the string
# join the list of strings
# string compare (strcmp), compare the strings to see if they are the same

    print(reverse('neha malik'))

    print(join(['ananya', ' kharbanda', ' is', ' a', ' good', ' girl']))

    print(strcmp('ananyap', 'ananyax'))