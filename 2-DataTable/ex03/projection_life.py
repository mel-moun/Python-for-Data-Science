from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def suffix(x):
    try:
        x = str(x).replace('M', 'e+06').replace('k', 'e+03')
    except AttributeError:
        pass
    return x


def change_x(x, pos):
    return str(int(round(x / 1e3, 0))) + "k"


def main():
    try:
        gdp = load(
            "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        expectancy = load("../life_expectancy_years.csv")

        gdp_1900 = gdp.loc[:, '1900'].apply(suffix).astype('float64')
        life_expectancy_1900 = expectancy.loc[:, '1900'].astype('float64')

        combined_data = pd.DataFrame({
            'GDP per Capita (PPP, 1900)': gdp_1900,
            'Life Expectancy (1900)': life_expectancy_1900
        }).dropna()

        plt.figure(figsize=(6.4, 4.8))
        ax = sns.scatterplot(
            x='GDP per Capita (PPP, 1900)',
            y='Life Expectancy (1900)',
            data=combined_data,
            s=100,
            alpha=0.7,
            edgecolor='k'
        )

        plt.title('1900', fontsize=16)
        plt.xlabel('Gross domestic product', fontsize=14)
        plt.ylabel('Life Expectancy', fontsize=14)
        plt.xscale('log')
        ax.xaxis.set_major_formatter(change_x)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend(['Country'], loc='upper left')
        plt.show()

    except Exception as e:
        print(type(e).__name__, ":", e)


if __name__ == "__main__":
    main()
