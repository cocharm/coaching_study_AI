import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c'] 
values = [1, 10, 100]


fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

axs[0].bar(names,values)
axs[0].set_title('Bar Plot')
axs[0].set_xlabel('Name')
axs[0].set_ylabel('Value')

axs[1].scatter(names, values)
axs[1].set_title('Dot Plot')
axs[1].set_xlabel('Name')
axs[1].set_ylabel('Value')

axs[2].plot(names, values)
axs[2].set_title('Line Plot')
axs[2].set_xlabel('Name')
axs[2].set_ylabel('Value')

plt.tight_layout()
plt.show
