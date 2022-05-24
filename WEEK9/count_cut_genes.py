import re
#ask input for the open directory
file = input('Input the file:')
#open the file
input=open(file, 'r') 
genes = input.read()

file=open(r'count_fragments.fa', 'w') 

#divide all genes into a list 
list = genes.split('>') 
# remove ' ' 
list.remove('')   
cut_site = 'GAATTC'
for i in list:  # extract sequence of each gene without \n in to a list
        sequence = re.findall(r'^[ATGC]+',i , re.M)  # re.M: ignore
        seq = ''.join(sequence)  
        if re.search(cut_site, seq)==None:  #if there is no recognition site
            continue
        else:  # if recognition site found in the sequence
            number = len(cut_site.findall(seq))  # number of recognition sites
            name = re.findall(r'gene:([^ ]+)', i)  # extract gene ID
            add = f'>{name[0]}  {number + 1}\n{seq}\n'  # count fragments
            file.write(add)  # write the information into the file
#the number of fragments are shown in the file
#In this part, I got help from my classmate Mr.Deng
