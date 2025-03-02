def funnyString(s):
    reversed_s = s[::-1]
    diff_s = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1)]
    diff_reversed = [abs(ord(reversed_s[i]) - ord(reversed_s[i+1])) for i in range(len(reversed_s)-1)]
    
    if diff_s == diff_reversed:
        return "Funny"
    else:
        return "Not Funny"
    
if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        fptr.write(result + '\n')
        
    fptr.close()