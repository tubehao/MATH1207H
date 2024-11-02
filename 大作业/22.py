import numpy as np
import matplotlib.pyplot as plt

# 生成混合高斯分布样本的函数
def generate_mixed_gaussian(n, miu1 = -2, std1 = 1, miu2 = 2, std2 = 1, yitap = 0.5):
    X = np.random.normal(miu1, std1, n)  # 生成第一个高斯分布的样本
    Y = np.random.normal(miu2, std2, n)  # 生成第二个高斯分布的样本
    yita = np.random.binomial(1, yitap, n)  # 生成混合的伯努利试验
    Z = X + Y * yita  # 混合两个分布
    return Z

# 创建一个3行3列的子图布局
fig, axes = plt.subplots(3, 3, figsize=(15, 8))

# 用于模拟不同样本量下的分布并绘图的函数
def problem2(n, seq, miu1, std1, miu2, std2, yitap, title):
    # 计算混合分布的期望值和方差
    EZ = miu1 + miu2 * yitap
    DZ = (std1 ** 2 + miu1 ** 2) + yitap * (std2 ** 2 + miu2 ** 2) - EZ ** 2

    U = []

    # 生成1000个样本并计算每个样本的Ui
    for i in range(1000):
        samples = generate_mixed_gaussian(n=n, miu1=miu1, std1=std1, miu2=miu2, std2=std2, yitap=yitap)
        Ui = (samples.mean() * n - n * EZ) / np.sqrt(n * DZ)
        U.append(Ui)
    
    # 绘制Ui值的直方图
    axes[seq // 3, seq % 3].hist(U, bins=50, density=True, alpha=0.6, color='blue')
    axes[seq // 3, seq % 3].set_title(f"{title} (n={n})")
    axes[seq // 3, seq % 3].set_xlabel('值')
    axes[seq // 3, seq % 3].set_ylabel('密度')

# 不同的样本量进行测试
nlist = [2, 3, 4, 5, 10, 20, 50, 100, 5000]

# 对每个样本量运行模拟
for i in range(9):
    problem2(nlist[i], i, miu1=-10, std1=1, miu2=10, std2=2, yitap=0.8, title="变化的均值")

# 调整子图布局
plt.tight_layout()

# 展示图形
plt.show()
