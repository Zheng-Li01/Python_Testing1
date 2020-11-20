from collections import Counter

def all_uniqs(input_str: str):
    ctr = Counter(input_str)
    # print(ctr)
    # print(type(ctr))

    for k,v in ctr.items():
        # print(k,v)
        if v >1:
            return False
    return True


def all_uniqs_no_datastruct(x:str):
    sorted_x = sorted(x)
    # print(type(sorted_x))
    # print(sorted_x)
    n = len(x)
    for i in range(1,n):
        if sorted_x[i-1]==sorted_x[i]:
            return False
    return True

if __name__ == "__main__":
    # all_uniqs('12323')
    # all_uniqs_no_datastruct('12323')
    inputs =["","aaasodkc", "abbccdcss", "aaa", "b", "bdes"]

    for x in inputs:
        print(f"Input {x} result:{all_uniqs(x)} same as {all_uniqs_no_datastruct(x)}")

