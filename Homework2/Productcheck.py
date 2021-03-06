products = {"candy": 10, "juice": 5, "pen": 50}

def check(product,num):
    return products.get(product,0) >= num
