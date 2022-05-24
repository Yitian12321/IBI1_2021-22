#input the money you have and the price for each bar of chocolate
money=input('your total money =')
price=input('price for a chocolate bar =')
#use % function to calculate remainder
remainder=money%price
# reduce remainder to get the number of bars that can be bought
bar=(money-remainder)/price
#output the biggest number that you can buy and the money you will remain.
print('You can buy',bar,'bar/bars of chocolate.')
print('You still have',remainder,'left.')
