import numpy as np

t = np.arange(0., 5., 0.2)

# 각 데이터에 대한 색상과 모양을 지정한 plot 그래프를 출력합니다.
plt.plot(t, t, 'r--', label='red dashes')
plt.plot(t, t**2, 'bs', label='blue squares')
plt.plot(t, t**3, 'g^', label='green triangles')

# 그래프에 제목(title)과 x, y 축 레이블(label)을 추가하고 범례(legend)를 출력합니다.
plt.title("Example Graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()

plt.show()