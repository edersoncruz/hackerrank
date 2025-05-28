# Question Link https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true


if __name__ == '__main__':
    s = input()
    
def string_validators(string):
        alnum = any(c.isalnum() for c in string)
        alpha = any(c.isalpha() for c in string)
        digit = any(c.isdigit() for c in string)
        lower = any(c.islower() for c in string)
        upper = any(c.isupper() for c in string)
        
        return alnum, alpha, digit, lower, upper
        
for result in string_validators(s):
    print(result)