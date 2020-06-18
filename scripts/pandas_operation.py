import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

df =pd.DataFrame({"Day":[1,2,3,4,5], "Visitor":[100,200,300,400,500], "Bounce":[20,30,50,41,20]})
print("<----------> \n", df)

# df1= df.set_index("Day", inplace=True)
# print("Change the Index by Column <----------> \n", df1)

# df.plot()
# plt.show()

df=df.rename(columns={"Bounce":"User"})
print("Change the Column Header <----------> \n", df)


#Converting data from one format to another like csv to html
print("Data Munging")

weather=pd.read_csv("/result.csv", index_col=0)
weather.to_html("weat.html")
