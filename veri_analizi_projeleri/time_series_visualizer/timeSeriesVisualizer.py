import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_lineplot():
    fig, ax = plt.subplots(figsize=(15,8))
    
    ax.plot(df.index, df.value, 'r', linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

draw_lineplot()

def draw_bar_plot():
    df_bar =df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    
    df_bar = df_bar.groupby(["year", "month"])["value"].mean()
    df_bar = df_bar.unstack()
        
    df_bar.columns = ['January','February','March','April','May','June','July','August','September','October','November','December']
        
    fig = df_bar.plot(kind='bar', figsize=(15, 9)).figure
        
    plt.xlabel('Years', fontsize=16)
    plt.ylabel('Average Page Views', fontsize=16)

draw_bar_plot()

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax_1, ax_2) = plt.subplots(1, 2, figsize = (20, 10))
    
    sns.boxplot(data=df_box, ax=ax_1, x="year", y="value")
    ax_1.set_title("Year-wise Box Plot (Trend)")
    ax_1.set_xlabel("Year")
    ax_1.set_ylabel("Page Views")
    
    sns.boxplot(data=df_box, ax=ax_2, x="month", y="value")
    ax_1.set_title("Month-wise Box Plot (Trend)")
    ax_1.set_xlabel("Month")
    ax_1.set_ylabel("Page Views")

draw_box_plot()