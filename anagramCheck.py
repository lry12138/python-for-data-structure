def anagram(st1,st2):
    st1 = st1.lower()
    st2 = st2.lower()
    check = []
    extra = []
    for letter in st1:
        if letter != " ":
            check.append(letter)
            
    for letter in st2:
        if letter in check:
            check.remove(letter)
        elif letter != " " and letter not in check:
            extra .append(letter)
            
    if not check and not extra:
        print(True)
    else:
        print(False)
            
            
anagram("dog","God")     
anagram("aa","bb")   
anagram("clint eastwood","old west action")   