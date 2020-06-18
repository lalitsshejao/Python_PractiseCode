from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")

x=[1,2,3,4,5,6,7,8,9]
y=[10,20,30,10,30,60,50,80,90]

#plain graph
plt.plot(x,y)

#add style to graph
plt.plot(x,y,'g', label="LineOne", linewidth=5)
plt.title ("Infor")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.legend()

plt.show()
