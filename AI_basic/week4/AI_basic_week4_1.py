import pandas as pd

idx = ["HDD", "SSD", "USB", "CLOUD"]
data = [19, 11, 5, 97]


# 위 데이터로 Series를 구현해보세요.
series = pd.Series(data, index=idx)

# 10 이상 20 이하를 가지는 데이터만 이용해 다시 series를 정의하세요.
series = series[(series >= 10) & (series <= 20)]
print(series)