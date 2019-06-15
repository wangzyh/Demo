import numpy as np


class StandarScaler:

    def __index__(self):
        self.mean_ = None
        self.scale_ = None

    def fit(self, X):
        """根据训练数据集X获取数据的均值和方差"""
        assert X.ndim == 2, "The dimension of X must be 2"

        self.mean_ = np.array([np.mean(X[:, i]) for i in range(X.shape[1])])
        self.scale_ = np.array([np.std(X[:, i]) for i in range(X.shape[1])])

        return self

    def tranform(self, X):
        """将X根据这个StandardScaler根据均值方差归一化处理"""
        assert X.ndim == 2, "The dimension of X must be 2"
        assert self.mean_ and self.scale_ is not None, "must fit before transform"
        assert X.shape[1] == len(self.mean_), "the feature number of X must be equal to mean_ and std_"

        resX = np.empty(shape=X.shape, dtype=float)
        for col in range(X.shape(X)):
            resX[:, col] = (X[:, col] - self.mean_[col] / self.scale_[col])
        return resX

