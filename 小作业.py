import numpy as np
import matplotlib.pyplot as plt

# 创建一个包含1行和2列的子图
fig, axes = plt.subplots(2, 3, figsize=(15, 8))  # figsize可根据需要设置图形的大小

# 数据准备
lambda_param = 2

sample_sizes = [10, 30, 50, 70, 100, 1000]
for i in range(2):
    for j in range(3):
        sample_size = sample_sizes[i * 3 + j]
        random_samples = np.random.poisson(lambda_param, sample_size)

        mean_value = np.mean(random_samples)  # 计算平均值
        variance_value = np.var(random_samples)  # 计算方差

        print(f"{str(sample_sizes[i*3+j])}个数据的平均值: {mean_value}")
        print(f"{str(sample_sizes[i*3+j])}个数据的方差: {variance_value}")
        
        axes[i, j].set_xlim(0, 10)
        axes[i, j].set_ylim(0, 4)
        axes[i, j].hist(random_samples, bins=50, density=True, alpha=0.6, color='b', edgecolor='black')
        axes[i, j].set_xlabel('value of the random variable')
        axes[i, j].set_ylabel('frequency')
        axes[i, j].set_title(f'Frequency Histogram (Sample Size: {sample_size})')

# 调整子图布局
plt.tight_layout()

# 显示图形
plt.show()