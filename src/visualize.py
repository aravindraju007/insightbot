import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style="whitegrid")

def plot_histogram(df, column, bins=20):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], bins=bins, kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def plot_bar(df, column):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x=column, order=df[column].value_counts().index)
    plt.title(f'Bar Plot of {column}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(df):
    plt.figure(figsize=(10, 8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", square=True)
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.show()

def plot_boxplot(df, column, by=None):
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x=by, y=column) if by else sns.boxplot(y=df[column])
    title = f'Boxplot of {column}' + (f' by {by}' if by else '')
    plt.title(title)
    plt.tight_layout()
    plt.show()

def plot_pairplot(df, columns=None, hue=None):
    if columns is None:
        columns = df.select_dtypes(include='number').columns[:4]  # Limit to first 4
    sns.pairplot(df[columns], hue=hue)
    plt.suptitle("Pair Plot", y=1.02)
    plt.show()
