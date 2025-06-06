import matplotlib.pyplot as plt

years = [
2000, 2001, 2002, 2003, 2004,2005, 2006,2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
2015, 2016, 2017, 2018, 2019
]

violent_crime_rate = [
506.5, 504.5, 494.4, 475.8, 463.2, 469.0, 479.3, 471.8, 458.6, 431.9,
404.5, 387.1, 387.8, 369.1, 361.6,373.7, 386.6, 383.8, 370.4, 366.7
]

murder_rate = [
5.5, 5.6, 5.6, 5.7, 5.5, 5.6, 5.8, 5.7, 5.4, 5.0,
4.8, 4.7, 4.7, 4.5, 4.4, 4.9, 5.4, 5.3, 5.0, 5.0
]


property_crime_rate = [
3658.1, 3658.1, 3630.6, 3591.2, 3514.1, 3431.5, 3346.6, 3276.4, 3214.6, 3041.3,
2945.9, 2945.9, 2905.4, 2868.0, 2733.6, 2574.1, 2500.5, 2451.6, 2362.9, 2209.8, 2109.9
]

plt.plot(years, violent_crime_rate, label="violent crime rate")
plt.plot(years, murder_rate, label= "murder rate")
plt.plot (years, property_crime_rate, label= "property crime rate")

plt.xlabel("years")
plt.ylabel("rate perr 100,000 people")
plt.title("crime rates in the US 2000-2019")
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()
