import string
from collections import Counter

# -> bool: Describe the return type; word:str : Input the correct perm's type
def is_palindrom_perm(word: str) ->bool:
    clean_w = proc(word)
    # print(clean_w)
    ctr = Counter(clean_w)
    # print(ctr)
    odd_c = sum(x %2 for x in ctr.values())
    # print(ctr.values())
    # print(odd_c)
    return not odd_c > 1

def is_palindrom_perm_better(word: str) -> bool:
    bs = {c: 0b0 for c in  string.ascii_lowercase}
    # print(string.ascii_lowercase)
    # print(bs)
    for c in proc(word):
        bs[c] ^= 0b1 
        # print(bs[c])
        print(bs.values())
    return not sum(x for x in bs.values()) >1

def proc(x:str) ->str:
    letter_iter = filter(lambda  c: c.isalpha(), x.strip())
    # print(letter_iter)
    return "".join(map(lambda x:x.lower(), letter_iter))

if __name__=="__main__":
    print(proc("a...!>!>!a<<>  <!!!aaa"))

    def printex(ex): 
        return print(
        f"For exammple: {ex} ==> {is_palindrom_perm(ex)} \
            same as {is_palindrom_perm_better(ex)}")

    # ex1 = "A man, a plan, a canal, panama"
    # printex(ex1)
    # ex2 = "This is not a plaindrome"
    # printex(ex2)
    ex3 = "AAaccbbbb   "
    printex(ex3)

