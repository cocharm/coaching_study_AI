import pandas as pd

idx = ["Sue", "Ryan", "Jay", "Jane", "Anna"]
col = ["round_1", "round_2", "round_3", "round_4", "round_5"] 
data= [[55, 65, 60, 66, 57],
            [64, 77, 71, 79, 67],
            [88, 81, 79, 89, 77],
            [45, 35, 30, 46, 47],
            [91, 96, 90, 97, 99]]

#위 데이터를 이용해 dataframe을 구성해보세요.
df = pd.DataFrame(data, columns=col, index=idx)

#df에 새로운 column인 round_6의 데이터 [11, 15, 13, 17, 19]를 추가해보세요. 
col_round_6 = [11, 15, 13, 17, 19]
df["round_6"] = col_round_6

print(df)
print(df.describe().loc[["mean", "max", "min"]])