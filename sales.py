import matplotlib.pyplot as plt


file = open("SalesJan2009.csv", "r")

#skip the 1st line
file.readline()

salesPerCountry = {}

for line in file:
	line = line.strip().split(",")

	if line[7] not in salesPerCountry:
		salesPerCountry[line[7]] = int(line[2])   #change the 7 to see states, payment types
	else:
		salesPerCountry [line[7]] += int(line[2])

	#print(line[7], line[2])  #see only countries, sales


print(salesPerCountry)
file.close()

x = list(salesPerCountry.keys())
y = list(salesPerCountry.values())

y.sort()
y.reverse()


y10 = y[:10] #highest ten
x10 = []

for tmp in y10:
	for country in salesPerCountry:   #go over countries
		if tmp == salesPerCountry[country]:   #if the country's values are in y10 (top ten values)
			x10.append(country)       
			del salesPerCountry[country]
			break  #only looking for on match


plt.bar(x10,y10)
plt.xticks(rotation = "vertical")
plt.xlabel("Countries")
plt.ylabel("Sales per country($)")
plt.tight_layout()
plt.grid()
plt.savefig("sales.intro.pdf")

