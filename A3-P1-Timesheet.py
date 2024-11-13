#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
# get input for for daily hours worked 
    
    hoursWorked= []
    def hours():
        for counter in range(5):
            hoursWorked.append(int(input(f"Enter Hours Worked on Day # {counter + 1}: ")))
        return hoursWorked
    hours()
# seperate longest day(s) worked from list 
    longestDay=[]
    for i in range(len(hoursWorked)):
        if hoursWorked[i] == max(hoursWorked):    
            longestDay.append(i)                  #had it as listing the values but changed to list the indexs so I could call back to the day from hours worked.
#print longest day(s) 
    print("----------------------------------------------------------")
    print("The most hours worked was on:")
    for i in range(len(longestDay)):    #turned this into a loop to make up for multiple days with the same max hours
        print(f"Day{longestDay[i]+1} when you worked {hoursWorked[longestDay[i]]} hours")
    print("----------------------------------------------------------")
    print(f"The total number or hours worked was: {sum(hoursWorked)}")
    averageHours=sum(hoursWorked)/len(hoursWorked)
    print(f"The average number of hours worked each day was: {averageHours:.1f}")
    print("----------------------------------------------------------")
# seperate Slack Days ( less than 7 hours)
    slackDays=[]
    for i in range(len(hoursWorked)):
         if hoursWorked[i]<7:
             slackDays.append(i)
    print("Days you slacked off (i.e. worked less than 7 hours): ")
    for i in range(len(slackDays)):
        print(f"Day #{slackDays[i]+1}:  {hoursWorked[slackDays[i]]}")


# CODE WORKS WOOOOO now to add functions 
    # YOUR CODE ENDS HERE
    hours()
main()
