# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Base case
    if len(string) <= 1:
        return string
    small_ans = removeConsecutiveDuplicates(string[1:])
    if small_ans and string[0] == small_ans[0]:
        return small_ans
    return string[0] + small_ans
# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
