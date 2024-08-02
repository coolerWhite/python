def longest_consec(strarr, k):
    result = []
    res = ""
    if k > len(strarr) or k == 0 or k <= 0:
        return ""
    else:
        res += strarr[1:3]
        return res

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2))
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2))