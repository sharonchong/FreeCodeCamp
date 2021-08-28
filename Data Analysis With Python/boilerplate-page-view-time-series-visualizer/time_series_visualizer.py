import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True, index_col="date")

# print(df.info())

# Clean data
df = df[(df["value"] > df["value"].quantile(0.025))
        & (df["value"] < df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(10, 4))
    plt.plot(df.index, df["value"], color="red")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    # df_bar["date1"] = pd.to_datetime(df_bar.index)
    # df_bar = df_bar.groupby([df_bar["date1"].dt.year, df_bar["date1"].dt.month]).mean("value")

    df_pivot = pd.pivot_table(df_bar,
                              values=["value"],
                              index=["year"],
                              columns=["month"],
                              aggfunc=np.mean)

    # print(df_pivot)

    # Draw bar plot
    ax = df_pivot.plot(kind="bar")
    fig = ax.get_figure()
    fig.set_size_inches(7, 6)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    plt.legend([
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ],
               title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(20, 7))

    sns.boxplot(x="year", y="value", data=df_box, orient='v',
                ax=ax[0]).set(title="Year-wise Box Plot (Trend)",
                              xlabel="Year",
                              ylabel="Page Views")
    sns.boxplot(x="month",
                y="value",
                data=df_box,
                orient='v',
                ax=ax[1],
                order=[
                    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                    'Sep', 'Oct', 'Nov', 'Dec'
                ]).set(title="Month-wise Box Plot (Seasonality)",
                       xlabel="Month",
                       ylabel="Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
