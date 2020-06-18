import pandas as pd

xyz_web={"day":[1,2,3,4,5,6], "Visitor":[1000,700,600,500,1100,1200], "BounceRate":[10,20,30,40,10,20]}
df = pd.DataFrame(xyz_web)

print("<----> \n",df)

print("<----> \n",df.head(2))

print("<----> \n",df.tail(2))

df1=pd.DataFrame({"HPI": [70,80,90,40,50], "IntRate":[1,2,2,2.2,1], "GDP":[10,20,25,10,15]},
                 index = [2000,2001,2002,2003,2004])
df2=pd.DataFrame({"HPI": [70,80,90,40,50], "IntRate":[1,2,2,2.2,1], "GDP":[11,21,31,12,33]},
                 index = [2005,2006,2007,2008,2009])
merge = pd.merge (df1,df2)
print("<----> \n", merge)

merge = pd.merge (df1,df2 , on="HPI")
print("<----> \n", merge)

concat= pd.concat([df1,df2])
print("Concatination of DataFrame <------> \n", concat)

ddff1=pd.DataFrame({"IntRate":[1,2,2,2.2,1], "GDP":[3,6,9,12,15]},
                 index = [2000,2001,2002,2003,2004])
ddff2=pd.DataFrame({"IntRate_xxx":[1,2,2,2.2,1], "qqq_GDP":[5,10,15,20,25]},
                 index = [2001,2003,2007,2008,2002])

print("<----> \n", ddff1.join(ddff2))
# values present in ddff1 will be considered only, values present in
# ddff2 which does not present in ddff1 will be discarded like 2007,2008

