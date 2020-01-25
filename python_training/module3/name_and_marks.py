data=input("Enter the string :")
str=data.split(",")
theory=practical=0
for i in range(1,6):
    theory+=int(str[i])
    for j in range(6,8):
        practical+=int(str[j])

per=(theory+practical)*.2
print(str[0],"obtained",theory," marks out of 460 in theory and",practical,"marks out of 50 in practical and successfully passed the exam with",per,"in aggregrate . Many congratulations to Robert")


