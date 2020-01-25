str='English=78 Science=83 Math=68 History=65'  # sum =294 Percentage=73.5
spp=str.split(" ")
print(spp)
sum=0
for i in range(0,len(spp)):
    a=spp[i].split("=")

    for j in a:
        if j.isnumeric():
            print(j)
            sum=sum+int(j)
per=(sum*100)/400
print("Sum=",sum)
print("Percentage =",per)
