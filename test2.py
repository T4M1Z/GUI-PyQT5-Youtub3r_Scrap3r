import pandas as pd
lstA = [1,2,3,4,5]
lstB = [6,7,8,9,10]

df = pd.DataFrame(list(zip(lstA, lstB)), columns=["holer","df"])
print(df)