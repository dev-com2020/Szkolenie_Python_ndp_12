num_days = int(input('Z ilu dni chcesz podać dane'))

sales_file = open('sales.txt', 'w')

for count in range(1, num_days + 1):
    sales = float(input('Podaj wartość sprzedaży w dniu nr' + str(count)))
    sales_file.write(str(sales) + '\n')

sales_file.close()
print('Dane zostały zapisane')

test = []
sales_file = open('sales.txt', 'r')
line = sales_file.readline()
while line != "":
    amount = float(line)
    print(format(amount, '.2f'))
    line = sales_file.readline()
    test.append(amount)
sales_file.close()
print(test)
