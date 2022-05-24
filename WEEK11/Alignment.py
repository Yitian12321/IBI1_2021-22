#import functions
import re
import numpy as np

#Import the data. 
open1=open("D:\\python\\box\\DLX5_human.fa")
open2=open("D:\\python\\box\\DLX5_mouse.fa")
open3=open("D:\\python\\box\\RandomSeq.fa") 

#open the .fa file and make each of them become a string
human = open1.read()
mouse = open2.read()
random = open3.read()

#Extract the amino acid sequence.
human = re.sub(r'>(.+)\n','',human)
human=re.sub(r'\n','',human)
mouse = re.sub(r'>(.+)\n','', mouse)
mouse=re.sub(r'\n','',mouse)
random = re.sub(r'>(.+)\n','',random)
random=re.sub(r'\n','',random)




#Define the variables to record the number of different acids and initialize them as 0
distance_human_mouse = 0
distance_human_random = 0
distance_mouse_random = 0

#calculate the number of different amino acid
for i in range(len(mouse)):       
    if mouse[i]!=human[i]:
        distance_human_mouse += 1
#check if each amino acid is different. If so,add a score 1 in corresponding variable.

for i in range(len(human)):       
    if random[i]!=human[i]:
        distance_human_random += 1 

for i in range(len(random)):    
    if random[i]!=mouse[i]:
        distance_mouse_random += 1


#calculate the percentage of identical amino acid in the three comparisons
human_mouse= distance_human_mouse/len(mouse)    
human_mouse= (1-human_mouse)*100
human_random= distance_human_random/len(human)
human_random=(1-human_random)*100
mouse_random= distance_mouse_random/len(random)
mouse_random=(1-mouse_random)*100

#print the number of different amino acids and percentage of similarity.
print ('The number of different amino acids between human and mouse is',distance_human_mouse)
#There is 10 different amino acids between human and mouse 
print ('The percentage of identical amino acids between human and mouse is',human_mouse,'%')
#The percentage of identical amino acids between human and mouse is 96.53979238754326 %
print ('The number of different amino acids between human and random is',distance_human_random)
#There is 281 different amino acids between human and random
print ('The percentage of identical amino acids between human and random is',human_random,'%')
#The percentage of identical amino acids between human and random is 2.768166089965396 %
print ('The number of different amino acids between mouse and random is',distance_mouse_random)
#There is 280 different amino acids between mouse and random
print ('The percentage of identical amino acids between mouse and random is',mouse_random,'%')
#The percentage of identical amino acids between mouse and random is 3.114186851211076 %






#Create a amino_acidtionary and type in the amino acid list following the range of BLOSUM62 score matrix axis.

amino_acid={'A':0,'R':1,'N':2,'D':3,'C':4,'Q':5,'E':6,'G':7,'H':8,'I':9,'L':10,'K':11,'M':12,'F':13,'P':14,'S':15,'T':16,'W':17,'Y':18,'V':19,'B':20,'Z':21,'X':22,'*':23}

BLOSUM62 = np.matrix([
            [ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
            [-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
            [-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
            [-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
            [ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
            [-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
            [-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
            [ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
            [-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
            [-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
            [-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
            [-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
            [-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
            [-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
            [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
            [ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
            [ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
            [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
            [-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
            [ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
            [-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
            [-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
            [ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
            [-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1]])



# Sum scores
def BLOSUM62_score(seq1,seq2):  
    score=0
    list1=list(seq1)
    list2=list(seq2)
    for i in range(len(seq1)):
        score+=BLOSUM62[amino_acid[list1[i]],amino_acid[list2[i]]]
    return score

#calculate the BLOSUM score
score_human_mouse=BLOSUM62_score(mouse,human)
score_human_random=BLOSUM62_score(human,random)
score_mouse_random=BLOSUM62_score(mouse,random)

#print out the BLOSUM score
print('The BLOSUM score between human and mouse is',score_human_mouse)
#The BLOSUM score between human and mouse is 1490
print('The BLOSUM score between human and random is',score_human_random)
#The BLOSUM score between human and random is -351
print('The BLOSUM score between mouse and random is:',score_mouse_random)
#The BLOSUM score between mouse and random is -348

#From the progamme above, I can get the BLOSUM score, percentage of identical amino acid, and number of different amino acid.
#The percentage of identical amino acids between human and mouse is 96.53 %, between human and random is 2.76 %, between mouse and random is 3.11 %
#We can conclude that there is a little similarity (less that 5%) between a amino_acid sequence and a random sequence. And there is a high sequence similarity between the human and mouse.
#The BLOSUM score between human and mouse is 1490, between human and random is -351, between mouse and random is -348.
#The score of human-to-mouse is the only one that over 0. And it shows a relative high score. It means conserved regions in a number of protein families between human and mouse takes a very high percentage. During the evolution process, variations, which presents as the difference in amino acid sequences happened and thus forming different species. However, the difference between species is quite low. It can be imagined that there will be higher similarity between human and ape.
