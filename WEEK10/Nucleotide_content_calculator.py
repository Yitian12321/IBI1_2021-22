import re
print('please input the gene sequence')
#ask for input the sequence under test
seq=input('seq=')
#calculate the length of sequence
all=len(seq)
a=['A','C','T','G']
#use a 'for' loop to calculate each kind of nucleotides by turn.
#use findall function to turn all nucletides to a list
#use len function to calculate the number of each kind of nucleotides.
print('The content of each base :')
for i in a:
    x=len(re.findall(i,seq))
    content=x/all
    print(i,'percentage:{:.2%}'.format(content))         #print the result in percent and keeps two significant digits 
#adopted from https://www.cnblogs.com/changbaishan/p/8454511.html

