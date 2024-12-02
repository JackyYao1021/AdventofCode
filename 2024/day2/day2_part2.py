
count = 0

def check(report):
    if report == sorted(report) or report == sorted(report, reverse=True):
        for i in range(1, len(report)):
            diff = abs(report[i] - report[i-1])
            if diff > 3 or diff < 1:
                return False
        return True                    

with open("2024/inputs/day2.txt", 'r') as file:
    for line in file:
        report = list(map(int,line.strip().split()))
        for i in range(len(report)):
            if check(report[:i]+report[i+1:]):
                count += 1
                break
        
print(count)
            
            
            
    