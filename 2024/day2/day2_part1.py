
count = 0

with open("2024/inputs/day2.txt", 'r') as file:
    for line in file:
        report = list(map(int,line.strip().split()))
        
        if len(report) == 1:
            count += 1
        elif len(report) == 2:
            if report[0] != report[1]:
                count += 1
        else:
            safe = True
            increasing = report[0] < report[1]

            for i in range(1, len(report)):
                diff = report[i] - report[i-1]
                if increasing and (diff < 1 or diff > 3):
                    safe = False
                    break
                elif not increasing and (-diff < 1 or -diff > 3):
                    safe = False
                    break

            if safe:
                count += 1
            
print(count)
            
            
            
    