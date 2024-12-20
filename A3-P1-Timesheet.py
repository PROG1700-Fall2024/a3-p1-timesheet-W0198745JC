#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     W0198745
#Student Name:  Jenille Cheney 

# took me forever to remember that functions go OUTSIDE the main function 
# gave them an underscore to create an empty perameter knowing within the main function it would refer to the list of the same name 
def calculateAverageDay(_hoursWorked):
        return sum(_hoursWorked)/len(_hoursWorked)
    
def printAvgDay(_hoursWorked):
    print("----------------------------------------------------------")
    print(f"The total number or hours worked was: {sum(_hoursWorked)}")
    averageHours = calculateAverageDay(_hoursWorked)
    print(f"The average number of hours worked each day was: {averageHours:.1f}")
    print("----------------------------------------------------------")

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # get input for for daily hours worked / make it a loop 
    slackHours=7  #orginally hardcoded but read the rubric and turned it into a local variable 
    hoursWorked= []

    for counter in range(5):
            while (True):
                  try:
                    string=(int(input(f"Enter Hours Worked on Day # {counter + 1}: "))) #love this elegant way to use format
                    if (int(string)<=0) or (int(string)>24):                       #recursive loop for hourly error checking 
                        print("invalid hours added please try again")
                        main()
                    else:
                        hoursWorked.append(string)
                        break                                               # took me forever to figure out why it just returned to day 1 every error all i needed was a BREAK!
                  except ValueError:
                       print("Invalid entry please use a number between 1 and 24!")
                         
    #   seperate longest day(s) worked from list 
    longestDay=[]
   
    for i in range(len(hoursWorked)):
             if hoursWorked[i] == max(hoursWorked):    
                longestDay.append(i)  #had listing the values changed to list the indexs so I could call back to the day from hours worked.
    #print longest day(s) 
    print("----------------------------------------------------------")
    print("The most hours worked was on:")
    for i in range(len(longestDay)):    #turned this into a loop to make up for multiple days with the same max hours
        print(f"Day{longestDay[i]+1} when you worked {hoursWorked[longestDay[i]]} hours")
            
    
    printAvgDay(hoursWorked)  # FUNCTION with A RETURN !!!!!!!
 
    # seperate Slack Days ( less than 7 hours)
    slackDays=[]
    
    for i in range(len(hoursWorked)):
            if hoursWorked[i]<(slackHours):
             slackDays.append(i)
    print("Days you slacked off (i.e. worked less than 7 hours): ")
    for i in range(len(slackDays)):
            print(f"Day #{slackDays[i]+1}:  {hoursWorked[slackDays[i]]}")
   

  

# CODE WORKS WOOOOO now to add functions 
    # YOUR CODE ENDS HERE

main()
