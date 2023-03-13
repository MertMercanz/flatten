def count_substring(string,sub_string):

    while True:
        for i in range(0,len(string)):
            if string[i] == sub_string[i]:
                



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)