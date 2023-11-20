import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations



def main():
    df = pd.read_csv('resources/iris.csv', header='infer')

    property_df = df.loc[:, df.columns != "Class"] #todo replace class str to variable
    project_axis(df, range(1, len(property_df.columns)))

    # normalized_df = (property_df - property_df.min()) / (property_df.max() - property_df.min())
    normalized_df = (property_df-property_df.mean())/property_df.std()
    project_axis(normalized_df, range(1, len(normalized_df.columns)))

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
