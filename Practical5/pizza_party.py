#for this problem, maybe for loop is useful.I can set it as (1,65) 
#no.the range shouldn't be (1,65),but the result should be larger than 64.
n=0
p=1
#define n and p,value here is not important.
while p<64:
#give range of p
 n+=1
 p=(n**2+n+2)/2
#when p>=64,the loop will break
else:
 print("We need at least",n,"cuts")




