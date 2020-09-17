# 余弦相似度，一种相似度计算方法。基于用户的协同过滤算法是推荐系统中最古老的算法。
import numpy as np


def bit_product_sum(x, y):
    return sum([item[0] * item[1] for item in zip(x, y)])


def cosine_similarity(x, y, norm=False):
    """计算两个向量x和y的余弦相似度"""
    assert len(x) == len(y), "len(x) != len(y)"
    # Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
    # 确保两向量维度一致
    zero_list = [0] * len(x)
    if x == zero_list or y == zero_list:
        return float(1) if x == y else float(0)

    # method 1
    res = np.array([[x[i] * y[i], x[i] * x[i], y[i] * y[i]] for i in range(len(x))])
    cos = sum(res[:, 0]) / (np.sqrt(sum(res[:, 1])) * np.sqrt(sum(res[:, 2])))

    return 0.5 * cos + 0.5 if norm else cos  # 归一化到[0, 1]区间内

    # method 2
    # def cosine_similarity(x,y):
    #     num = x.dot(y.T)
    #     denom = np.linalg.norm(x) * np.linalg.norm(y)
    #     return num / denom

if __name__ == "__main__":
    print(cosine_similarity([0, 0], [0, 0]))  # 1.0
    print(cosine_similarity([1, 1], [0, 0]))  # 0.0
    print(cosine_similarity([1, 1], [-1, -1]))  # -1.0
    print(cosine_similarity([1, 1], [2, 2]))  # 1.0
    print(cosine_similarity([3, 3], [4, 4]))  # 1.0
    print(
        cosine_similarity([1, 2, 2, 1, 1, 1, 0], [1, 2, 2, 1, 1, 2, 1])
    )  # 0.938194187433
