products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	#p = []
	#p.append(name)
	#p.append(price)
	p = [name, price]
	products.append(p)
	#products.append([name, price]) 上面兩行可以變成這一行。
print(products)