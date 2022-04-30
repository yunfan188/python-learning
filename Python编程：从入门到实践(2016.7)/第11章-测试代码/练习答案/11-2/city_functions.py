## 编写待测试函数

def city_country(city, country, population=0):
	ccp = city.title()+ ', '+ country.title()
	if population:
		ccp += ' - population '+ str(population)
	return ccp
