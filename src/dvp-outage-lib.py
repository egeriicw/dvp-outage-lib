import numpy as np
import pysal


file = "C:/Users/bill.eger/Desktop/Outage Data/Data Files/Alexandria__1208011130.dbf"

db = pysal.open(file, 'r')
print db.header
data = np.array(db.read())

print data[0]
