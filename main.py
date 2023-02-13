import numpy as np
x = np.array([1,2,3,4,5])
y = x*2
y = list(y)
with open('test.txt','w') as txt:
    txt.writelines(y)
