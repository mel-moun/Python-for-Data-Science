from load_csv import load
import matplotlib.pyplot as plt


def main():
    df = load("../life_expectancy_years.csv")
    print(df)

if __name__ == '__main__':
    main()
 