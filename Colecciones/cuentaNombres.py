exit = False
words_len_5 = 0
list = []
while (not exit) :
    
    print("Input a word (\"exit\" if you want to stop)")
    user_input = input()
    
    if (user_input != "exit") :
        list.append(user_input)
        if (len(user_input) >=5) :
            words_len_5 += 1
    else :
        exit = True
    print("There are " + str(words_len_5) + " words with more than 5 characters")
    print(list)
