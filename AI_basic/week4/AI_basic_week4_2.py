import pandas as pd

data1 = {"Name" : ["cherry", "mango", "potato", "onion"], 
      "Type" : ["Fruit", "Fruit", "Vegetable", "Vegetage"],
      "Price" : [100,110, 60, 80]}
data2 = {"Name" : ["pepper", "carrot", "banana", "kiwi"],
      "Type" : ["Vegetable", "Vegetabe", "Fruit", "Fruit"],
      "Price" : [50, 70, 90, 120]}

df1 = pd.DataFrame(data1, columns=["Name", "Type", "Price"])
df2 = pd.DataFrame(data2, columns=["Name", "Type", "Price"])

# 두 데이터프레임을 합치기
df3 = pd.concat([df1, df2], ignore_index=True)

# Fruit와 Vegetable의 type에 따라 정렬하고, 가격을 내림차순으로 정리
df_fruit = df3[df3["Type"] == "Fruit"].sort_values("Price", ascending=False)
df_veg = df3[df3["Type"] == "Vegetable"].sort_values("Price", ascending=False)

# Fruit와 Vegetable 상위 2개의 가격의 합을 출력
sum_fruit = df_fruit["Price"].iloc[:2].sum()
sum_veg = df_veg["Price"].iloc[:2].sum()

print("Sum of Top 2 Fruit Price: ", sum_fruit)
print("Sum of Top 2 Vegetable Price : ", sum_veg)