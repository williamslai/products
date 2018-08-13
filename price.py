data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
# 請開始寫"寫入檔案"的程式碼
with open ('exam1.txt', 'w') as f :
	for d in data:
		f.write(str(d) + '\n')


