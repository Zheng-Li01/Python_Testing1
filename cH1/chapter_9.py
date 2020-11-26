def chechrot(s1:str,s2:str):
    s22 = s1 + s2
    return isSubstr(s1,s22) and len(s1) == len(s2)

def isSubstr(s1:str, s2:str) ->bool:
    return s1 in s2


if __name__=="__main__":
    ex1 = ("abc", "cab")
    ex2 = ("panama", "ampaan")
    ex3 = ("ab", "abc")

    for a, b in (ex1,ex2,ex3):
        print(f"Is {a} rot of {b} ? {chechrot(a,b)}")