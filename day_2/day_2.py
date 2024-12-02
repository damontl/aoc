#opens and reads input.txt as file
#creates variable called reports which is every new line in the input file
#creates a list of reports with a list of levels in each report stored as integers
with open("input.txt", "r") as file:
    reports = [list(map(int, line.strip().split())) for line in file]

#safety function which works out if there is a positive or negative trend within the range of + or - 3 per gap between levels
#we subtract the first integer FROM the next integer because then if the subtracted difference is positive, it is a positive increase
def safety(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    grad_inc = all(1 <= diff <= 3 for diff in differences)
    grad_dec = all(-3 <= diff <= -1 for diff in differences)
    return grad_inc or grad_dec

#PART 2
#second function to remove every level within an unsafe report and test if it is safe after the level has been removed
def dampener(report):
    if safety(report):
        return report
    
    for i in range(len(report)):
        dampened_report = report[:i] + report[i+1:]
        if safety(dampened_report):
            return dampened_report
            
    #if report is still not made safe, it is returned as an unsafe report        
    return report

#variable to store a list of safe reports
safe_reports = [dampener(report) for report in reports]

#adds up the total number of safe reports in the list of safe reports
safety_num = sum(safety(report) for report in safe_reports)
print("The total number of reports that are safe is {}.".format(safety_num))
