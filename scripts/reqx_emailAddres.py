import re

text= "random String myname@123.com 1212eqweqe abcd123@sed.com  abc_edr-qwe.1.2.3@ancd.com"

pattern = re.compile("[a-zA-Z0-9\.\_\-]+@[a-zA-Z0-9]+\.[a-zA-Z]+")

result= pattern.search(text)
res=pattern.findall(text)
print (result)
print(res)