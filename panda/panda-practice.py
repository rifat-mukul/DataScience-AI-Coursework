import pandas

mydata = {
    "cars": ["BMW", "Audi"],
    "passing": [2,3]
}

myvar = pandas.DataFrame(mydata)
print(myvar)
print(pandas.__version__)