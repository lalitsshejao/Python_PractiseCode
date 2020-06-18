from matplotlib import pyplot as plt

data1=[1,2,3,4,5],[5,6,7,8,9]
data2=[2,4,6,8,10],[1,3,6,9,12]

plt.bar([1,2,3,4,5],[5,6,7,8,15],label="Ex one")
plt.bar([2,4,6,8,10],[1,3,6,9,12],label="Ex two", color='r')
plt.legend()
plt.title ("Info")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.show()
