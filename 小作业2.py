import numpy as np
import matplotlib.pyplot as plt

# 设置泊松分布的λ参数
lambda_param = 2
# 定义样本容量
sample_sizes = [10, 30, 50, 70, 100, 1000]
# 为每个样本容量生成50个样本均值
sample_means = {size: [np.mean(np.random.poisson(lambda_param, size)) for _ in range(50)] for size in sample_sizes}

# 创建画布，设置大小
plt.figure(figsize=(15, 12))

# 遍历样本容量，为每个容量绘制样本均值的频率直方图
for i, size in enumerate(sample_sizes):
    plt.subplot(3, 2, i+1)
    plt.xlim(0, 8)
    plt.hist(sample_means[size], bins=10, color='blue', edgecolor='black', alpha=0.7)
    plt.title(f'Sample Size: {size}')
    plt.xlabel('Sample Mean')
    plt.ylabel('Frequency')
    plt.tight_layout()
plt.title("Possion distribution")

plt.savefig("./Possion distribution.png",dpi=64)

plt.show()
