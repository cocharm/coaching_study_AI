import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.],
               [3., 6., 9., 12., 15., 18.]])

x_train = xy[0,:]
y_train = xy[1,:]

beta_gd = np.random.rand(1)
bias = np.random.rand(1)

learning_rate = 0.01

for i in range(1000):
    y_predict = beta_gd * x_train + bias
    error = np.mean((y_train - y_predict)**2)

    beta_gd_diff = -2 * np.mean(x_train * (y_train - y_predict))
    bias_diff = -2 * np.mean(y_train - y_predict)

    beta_gd = beta_gd - learning_rate * beta_gd_diff
    bias = bias - learning_rate * bias_diff

if i % 100 == 0:
        print('Epoch ({:10d}/1000) error: {:10f}, beta_gd: {:10f}, bias:{:10f}'.format(i, error, beta_gd.item(), bias.item()))
