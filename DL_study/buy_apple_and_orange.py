from layer import Mullayer, Addlayer

apple = 100
apple_num = 2

orange = 150
orange_num = 3

tax = 1.1

# forward
mul_apple_price = Mullayer()
mul_orange_price = Mullayer()
apple_price = mul_apple_price.forward(apple, apple_num)
orange_price = mul_orange_price.forward(orange, orange_num)

add_apple_and_orange_price = Addlayer()
apple_and_orange_price = add_apple_and_orange_price.forward(apple_price, orange_price)

mul_price = Mullayer()
price = mul_price.forward(apple_and_orange_price, tax)

print(price)

dprice = 1

# backward
dapple_and_orange_price, dtax = mul_price.backward(dprice)
dapple_price, dorange_price = add_apple_and_orange_price.backward(dapple_and_orange_price)
dapple, dapple_num = mul_apple_price.backward(dapple_price)
dorange, dorange_num = mul_orange_price.backward(dorange_price)

print(dtax, dapple_and_orange_price, dapple_price, dorange_price, dapple, dapple_num, dorange, dorange_num)
