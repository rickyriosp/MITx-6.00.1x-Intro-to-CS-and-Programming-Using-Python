index = [0, 0]
max_s = 0
for i in range(len(s)-1):
    for j in range(i+1, len(s)):
        if s[j] < s[j-1]:
            if j-i > max_s:
                max_s = j-i
                index = [i, i+max_s-1]
            break
    if j-i > max_s:
        max_s = j-i
        index = [i, i+max_s]
                
print('Longest substring in alphabetical order is:', s[index[0]:index[1]+1])
