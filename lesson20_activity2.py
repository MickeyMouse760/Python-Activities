def words_finder(words):
    cnt=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            cnt+=1
            lst.append(word)
    print("number of words with first and last characters matching\n", lst)
    return cnt
count=words_finder(["12", "11", "alla", "bmx", "i like salami"])
print("number of words with 2 or more letters:", count)