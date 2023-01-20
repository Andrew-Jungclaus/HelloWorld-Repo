#Part 1. 
seconds = int(input("Enter a number of seconds between 0 and 86,400:"))
hours = seconds //3600
minutes = seconds%3600//60
Seconds = seconds%60

print(seconds ,"seconds is about", hours, "hours", minutes,"minutes",Seconds,"seconds.")


#part 2 
time = 1685720
births = time//7
deaths = time//13
immigrants = time//35

a = births + immigrants - deaths

oldpop = 334205119

newpop = oldpop + a 

print("On January 20, 2022 at 12:15:20, the US population was", newpop)


#part 3 
secondsInput = int(input("Enter seconds since the beginning of the year:"))
days = (((secondsInput//60)//60)//24)

hour = ((secondsInput//3600)%60)//3
minute = ((secondsInput%3600)//60)
secs = secondsInput%60

print(days,"days,",hour,"hours,",minute,"minutes",secs,"seconds after the start of 2022")

times = secondsInput
birth = times//7
death = times//13
immigrant = times//35

L = birth + immigrant - death

newpopsince2022 = oldpop + L

print("Total population was", newpopsince2022)

#part 4 

p = int(newpopsince2022 + 350)
i = p**2-12
q = i/50
w = int(q**.2)

print("The average number of flapjacks eaten is",w)