# -*- coding=UTF-8 -*-

import pandas as pd


def read_excel():
    df1 = pd.read_excel("D:\\ml-data\\fndx-p0-example.xlsx")
    print("excel data: \n{}".format(df1.dropna()))


def read_excel_dropna():
    df1 = pd.read_excel("D:\\ml-data\\fndx-p0-example.xlsx")
    print("excel data: \n{}".format(df1.dropna()))


def read_excel_fillna():
    df1 = pd.read_excel("D:\\ml-data\\fndx-p0-example.xlsx")
    print("excel data: \n{}".format(df1.fillna(1)))


def read_csv():
    df1 = pd.read_csv("D:\\ml-data\\cvs-test.csv", sep=",")
    print("cvs data: \n{}".format(df1))


if __name__ == '__main__':
    # read_excel()
    # read_excel_dropna()
    read_excel_fillna()
    # read_csv()
