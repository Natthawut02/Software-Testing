def caesarCipher(s, k):
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            result.append(chr(((ord(char) - ord('a') + k) % 26) + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr(((ord(char) - ord('A') + k) % 26) + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    fptr.write(result + '\n')
    fptr.close()
