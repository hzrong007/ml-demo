# -*- coding=UTF-8 -*-

import numpy as np
import pandas as pd


def test_series():
    series = pd.Series([1, 2, 3, 4])
    print("series:\n{}".format(series))
    print("keys;{}".format(series.index))
    print("values;{}".format(series.values))


def test_series_index():
    series = pd.Series([1, 2, 3, 4, 5, 6],
                       index=['C', 'D', 'E', 'F', 'G', 'H'])
    print("series:\n{}".format(series))
    print("getValueByKey: key={}, value={}".format("G", series["G"]))


def test_data_frame():
    df = pd.DataFrame(np.arange(16).reshape(4, 4))
    print("dataFrame: \n{}".format(df))


def test_df_index_column():
    df = pd.DataFrame(np.arange(16).reshape(4, 4), index=['A', 'B', 'C', 'D'], columns=["col1", "col2", "col3", "col4"])
    print("dataFrame: \n{}".format(df))


def test_df_detailed_data():
    df = pd.DataFrame(
        {"name": ["Lily", "Lucy", "Bill"], "Math": [90.5, 89, 59]}
    )
    print("dataFrame: \n{}".format(df))


def test_series2df():
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series(["加班", "周二发版日", "分享", "周四发版日", "在加班"])
    df = pd.DataFrame([s1, s2])
    print("dataFrame: \n{}".format(df))


def test_series_del_item():
    series = pd.Series([1, 2, 3, 4, 5, 6], index=['C', 'D', 'E', 'F', 'G', 'H'])
    print("series:\n{}".format(series))
    del series["D"]
    print("series del result:\n{}".format(series))


def test_df_add_del_item():
    df = pd.DataFrame(
        {"Name": ["Lily", "Lucy", "Bill"], "Math": [90.5, 89, 59]}
    )
    df["Science"] = pd.Series([90.5, 89, 59])
    print("DataFrame add result::\n{}".format(df))
    del df["Math"]
    print("DataFrame del result:\n{}".format(df))


def test_df_index_column2():
    df = pd.DataFrame(
        {"Name": ["Lily", "Lucy", "Bill"], "Math": [90.5, 89, 59]}
    )
    print(df.columns)
    print(df.index)


def test_df_loc():
    df = pd.DataFrame(
        {"Name": ["Lily", "Lucy", "Bill"], "Math": [90.5, 89, 59]}
    )
    print("loc: {}".format(df.loc[[1, 2], "Name"]))
    print("iloc: {}".format(df.iloc[[2, 2], 1]))


if __name__ == '__main__':
    # test_series()
    # test_series_index()
    # test_data_frame()
    # test_df_index_column()
    # test_df_detailed_data()
    # test_series2df()
    # test_series_del_item()
    # test_df_add_del_item()
    # test_df_index_column()
    test_df_loc()
