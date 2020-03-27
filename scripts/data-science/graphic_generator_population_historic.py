#-*- coding: utf-8 -*-
import matplotlib.pyplot as pyplot

x_assis = []
y_assis = []
data = open("files/brasilian_population_historic.csv").readlines()

for i in range(len(data)):
	if i > 0:
		line = data[i].split(";")
		x_assis.append(int(line[0]))
		y_assis.append(int(line[1]))

pyplot.bar(x_assis, y_assis, color="#324ea8");
pyplot.plot(x_assis, y_assis, color="k", linestyle="--")

pyplot.title("Crescimento da populacao brasileira 1980-2016")
pyplot.xlabel("Ano")
pyplot.ylabel("Populacao x100.000.000")
pyplot.show()