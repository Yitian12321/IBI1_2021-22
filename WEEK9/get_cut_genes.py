import re
#import the file
code = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
file = code.read()

#remove all \n
file=re.sub(r'\n','',file)

#split all genes and make a list to store them one by one.
orig_list=re.split(r'>',file)
#creat a new list called list and selected genes with 'GAATTC' sequence
list=[]
for i in range(0,len(orig_list)):
    if re.findall(r'GAATTC',orig_list[i]):
        list.append(orig_list[i])

#As the length of gene ID is the same, extract all gene ID 
gene_ID = re.findall(r'gene:(.......)',str(list))
#extract all sequence
sequence = re.findall(r'[A-Z]{10,}', str(list))

#create a list to store the length of each sequence
length=[]
for i in range(0,len(sequence)):
    count=str(len(sequence[i]))
    length.append(count)

#combine all infomation together, thus output a list that each element is the gene that remains all required infomations
final=[]
for i in range(0,len(list)):
    final.append(str('>'+gene_ID[i]+'   '+length[i]+'\n'+sequence[i]+'\n'))
#change the list into the string variant and store it in variable called 'final'
final=''.join(final)

#creat a file called 'cut_genes.fa' and write in with 'final'
file=open('cut_genes.fa', 'w')
file=file.write(final)
