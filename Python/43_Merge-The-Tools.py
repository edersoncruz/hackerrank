# Question Link
# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    def remove_duplicate(part):
        result = ''
        for c in part:
            if c not in result:
                result += c
        return result
        
    for i in range(0, len(string), k):
        part = string[i:i+k]
        print(remove_duplicate(part))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
