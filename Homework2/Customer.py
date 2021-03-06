from Productcheck import products,check

def buy(product, num, price):
    if check(product,num):
        products[product] = products[product] - num
        print('You bought',product,'and spent', num*price)
    else:
        print('Sorry! We are out of this product.')

def main():
    buy('candy',5,10)
    buy('juice',9,5)
    buy('pen',50,2)
    buy('candy',1,10)

main()

