# Question Link https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def count_substring(string, sub_string):
        count = 0
        for i in range(len(string)):
            if string[i:i+len(sub_string)] == sub_string:
                count += 1
        return count

string = 'ABCDCDC'
sub_string = 'CDC'

count = count_substring(string, sub_string)
print(count)