from collections import Counter

def check_perm(a:str,b:str):
    sa = sorted(a)
    sb = sorted(b)

    return sa == sb

def check_perm_ctr(a:str,b:str):
    ca = Counter(a)
    cb = Counter(b)
    print(ca)
    # print(type(ca))
    # print(cb)

    for k,v in ca.items():
        print(ca.items())
        print(k,v)
        if k not in cb:
            return False
        elif v != cb[k]:
            return False

    if any(k not in ca for k in cb):
        return False

    return True

if __name__ =="__main__":
    inputs = [("aa", "ac"), ("", "")]

    for a,b in inputs:
        print(
            # f"Bot input {a} and {b}, result: {check_perm(a,b)}"+ "\n"
            f"Go input {a} and {b}, result=={check_perm_ctr(a,b)}"
        )
