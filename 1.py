#Лаб 4 - Строки
s = input('Введите строку, для определения наличия в ней латинских букв:\n\t')
count = 0
for c in s:
	if ((ord(c) >= ord('a')) and (ord(c) <= ord('w'))) or (ord(c) >= ord('A')) and (ord(c) <= ord('W')):
		count += 1
if count > 0:
	print ('Да есть в этой строке латинские буквы. (Их там {})'.format(count))
elif count == 0:
	print ('Нет в этой строке латинских букв')
input()