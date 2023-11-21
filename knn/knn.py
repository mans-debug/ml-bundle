import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
import numpy as np
import math


def split_df(df):
    if len(df) % 2 != 0:
        df = df.iloc[:-1, :]
    df1, df2 = np.array_split(df, 2)
    return df1, df2


def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def percent_mistakes(subject, example):
    return 1.0


def classify_and_add(row, df):
    df


def main():
    class_name = "Class"
    df = pd.read_csv('resources/iris.csv', header='infer')

    property_df = df.loc[:, df.columns != class_name]
    # project_axis(df, range(1, len(property_df.columns)))

    normalized_df = (property_df - property_df.min()) / (property_df.max() - property_df.min())
    # project_axis(df, range(1, len(property_df.columns)))
    normalized_df = normalized_df.join(df[class_name])
    subject, example = split_df(normalized_df)
    start_k = int(math.sqrt(len(df.index)))
    k_map = {}

    clean_df = pd.read_csv('resources/iris.csv', header='infer')
    for k in range(start_k, 1):
        for row in subject:
            classify_and_add(row, example, k, columns) # todo implement
        k_map[k] = percent_mistakes(example, clean_df) # todo implement

    print(k_map)
    # p = (rnd.uniform(0, 1), rnd.uniform(0, 1))
    # normalized_df['dist'] = normalized_df.apply(lambda row: dist(p, (row.A, row.B)), axis=1)
    # print(p)
    # print(normalized_df.sort_values('dist'))
    # project_axis(normalized_df, range(1, len(normalized_df.columns)))

    # todo split in half
    # def define_class --accept number of neighbors
    # def calculate_accuracy
    # implement creating new object


def project_axis(df, rng):
    axis = [df.iloc[:, i] for i in rng]
    axis_combinations = combinations(axis, 2)
    for x, y in axis_combinations:
        plt.scatter(x=x, y=y)
        plt.xlabel(x.name)
        plt.ylabel(y.name)
        plt.show()


if __name__ == '__main__':
    main()
