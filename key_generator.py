import random
#make list of 10 ones
length = int(input("Length of string: "))
x="1"*length
#for loop to pick 9 spots for 0s
for i in range(0,length-1):
  #generate randome spot until a valid spot is found
  while True:
	#pick a place to put a 0
    index= random.randint(1,len(x)+1)
    #check if the number of zeros preceding the selected index is less than the number of ones. Additionally, if the index is a spot where there is already a zero
    if(x[:index].count("0")+1<x[:index-1].count("1")):
      x=x[:index]+"0"+x[index:]
      break
x+='0'
print(x)
