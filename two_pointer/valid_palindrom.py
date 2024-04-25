def valid_palindrome(s):
    p =  s.strip().lower().replace(' ','')
    f = ''.join(e for e in p if e.isalnum())
    print(f)
    left = 0
    right = len(f) -1
    for left in range(len(f)):
        if f[left] != f[right]:
            return False
        right -= 1
    return True

print(valid_palindrome("A man, a plan, a canal: Panama"))