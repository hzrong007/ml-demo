# -*- coding=UTF-8 -*-

import numpy as  np


def test_np_base():
    arr = np.array([1, 2, 3])
    print("arr data：\n {}".format(arr))
    print("type:\n {}".format(type(arr)))
    print("shape:\n {}".format(arr.shape))

    arr = arr.reshape(1, -1)
    print("reshape:\n {}".format(arr.shape))
    print("reshape arr data：\n {}".format(arr))

    arr[0][1] = 22
    print("reset arr data：\n {}".format(arr))

    print("uniform: \n{}".format(np.random.uniform(0, 1, 5)))


def test_np_matrix():
    a = np.zeros((3, 3))
    print("arr data：\n {}".format(a))
    print("type:\n {}".format(type(a)))
    print("shape:\n {}".format(a.shape))

    one = np.ones((2, 3))
    print("one data：\n {}".format(one))

    s = np.full((2, 4), 0.5)
    print("s data：\n {}".format(s))

    e = np.eye(3, 3)
    print("e data：\n {}".format(e))

    r = np.random.random((4, 4))
    print("r data：\n {}".format(r))


def test_np_dtype():
    a = np.array([1, 2, 3])
    print("arr dtype：\n {}".format(a.dtype))

    f = np.array([1, 2, 3], dtype=np.float32)
    print("f dtype：\n {}".format(f.dtype))


def test_np_math():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    print("add result: \n{}".format(a + b))
    print("sub result: \n{}".format(a - b))
    print("times result: \n{}".format(a * b))
    print("divide result: \n{}".format(a / b))
    print("sqrt result: \n{}".format(np.sqrt(a)))
    print("矩阵相乘的结果: \n{}".format(a.dot(b)))


def test_np_func():
    a = np.array([[1, 2], [3, 4]])
    print("数组中所有元素的总和: \n{}".format(np.sum(a)))
    print("数组中列与列进行求和: \n{}".format(np.sum(a, axis=0)))
    print("数组中行与行进行求和: \n{}".format(np.sum(a, axis=1)))

    print("数组中所有元素的平均值: \n{}".format(np.mean(a)))
    print("数组中列与列求平均值: \n{}".format(np.mean(a, axis=0)))
    print("数组中行与行求平均值: \n{}".format(np.mean(a, axis=1)))

    print("矩阵转置操作（行变列，列变行）: \n{}".format(a.T))


if __name__ == '__main__':
    # test_np_base()
    # test_np_matrix()
    # test_np_dtype()
    # test_np_math()
    test_np_func()
