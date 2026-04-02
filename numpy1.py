import numpy as np
# 1维矩阵
ary = np.array([1, 2, 3, 4])
# print(ary)
# 2维矩阵
points = np.array([[1, 4], [2, 6], [3, 17], [4, 21], [5, 30]])
# print(points)

# 绘制点图
import matplotlib.pyplot as plt
plt.plot(points[:, 0], points[:, 1])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('YX Plot')
plt.show()

# 计算线性回归系数
x = points[:, 0]
y = points[:, 1]
coeff = np.polyfit(x, y, 1)
print(f"Y = {coeff[0]}X + {coeff[1]}")

# 计算残差方差
y_pred = np.polyval(coeff, x)
residuals = y - y_pred
variance = np.var(residuals)
print(f"Variance of residuals: {variance}")

# Calculate Y for X=33
y_at_33 = np.polyval(coeff, 33)
print(f"For X=33, Y = {y_at_33}")