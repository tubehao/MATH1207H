import numpy as np
import matplotlib.pyplot as plt

# 创建一个4行2列的子图布局，第一行单独一个大图
fig = plt.figure(figsize=(10, 12))
gs = fig.add_gridspec(4, 2)  # 4 rows, 2 columns grid
axes = [fig.add_subplot(gs[0, :])]  # First row spans all columns
axes += [fig.add_subplot(gs[i, j]) for i in range(1, 4) for j in range(2)]  # Remaining rows

# 定义一个函数，用于生成混合高斯分布的样本并绘制直方图
def plot_mixed_gaussian(miu1, std1, miu2, std2, yitap, title, seq):
    samples = generate_mixed_gaussian(miu1=miu1, std1=std1, miu2=miu2, std2=std2, yitap=yitap, n=1000)
    plot(samples, title, seq)

# 定义绘制直方图的函数
def plot(samples, title, seq):
    # 绘制频率直方图
    axes[seq].hist(samples, bins=50, density=True, alpha=0.6, color='blue')
    axes[seq].set_title(title)
    axes[seq].set_xlabel('Value')
    axes[seq].set_ylabel('Density')

# 生成混合高斯分布样本的函数
def generate_mixed_gaussian(n, miu1, std1, miu2, std2, yitap):
    X = np.random.normal(miu1, std1, n)
    Y = np.random.normal(miu2, std2, n)
    yita_samples = np.random.binomial(1, yitap, n)
    Z = X + Y * yita_samples
    return Z

# 使用定义的函数绘制不同条件下的混合高斯分布
plot_mixed_gaussian(miu1=-10, std1=1, miu2=10, std2=2, yitap=0.8, title="Origin Data", seq=0)
plot_mixed_gaussian(miu1=-10, std1=1, miu2=20, std2=2, yitap=0.8, title="Varying Means", seq=1)
plot_mixed_gaussian(miu1=0, std1=1, miu2=10, std2=2, yitap=0.8, title="Varying Means", seq=2)
plot_mixed_gaussian(miu1=-10, std1=1, miu2=10, std2=4, yitap=0.8, title="Varying Standard Deviations", seq=3)
plot_mixed_gaussian(miu1=-10, std1=2, miu2=10, std2=2, yitap=0.8, title="Varying Standard Deviations", seq=4)
plot_mixed_gaussian(miu1=-10, std1=1, miu2=10, std2=2, yitap=0.5, title="Varying Weights", seq=5)
plot_mixed_gaussian(miu1=-10, std1=1, miu2=10, std2=2, yitap=1, title="Varying Weights", seq=6)

# 调整子图布局
plt.tight_layout()
# 显示图形
plt.show()
