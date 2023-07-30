import numpy as np

xy = np.array([[1.,2.,3.,4.,5.,6.], [10.,20.,30.,40.,50.,60.]])

x_train = xy[0,:]
y_train = xy[1,:]

print(x_train, x_train.shape)
print(y_train, y_train.shape)
