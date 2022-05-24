import re
seq ='ATGCAATCGACTACGATCAATCGAGGGCC'
#use findall to creat a list that record all sites
counts=re.findall('GAATTC',seq)
#use len() to calculate the number of sites 
print('There is',len(counts),'site(s) that can be identified by enzyme.')
