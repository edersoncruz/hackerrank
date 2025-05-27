# Question Link https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

records = []
if __name__ == '__main__':

    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name,score])
        
scores = [score for name, score in records]
lowest = min(scores)
scores = [score for score in scores if score != lowest]
second = min(scores)

matching_records = [name for name, score in records if score == second]
matching_records.sort()
for i in matching_records:
    print(i)