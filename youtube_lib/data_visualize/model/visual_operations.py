import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from dotenv import load_dotenv

load_dotenv()

#Load the csv file for visualization of required data 
IMAN_GADZHI_MOMENTS = os.getenv('IMAN_GADZHI_MOMENTS')

class VisualOperations:

    def __init__(self):
        self.df = self.init()

    def init(self):
        df = pd.read_csv(IMAN_GADZHI_MOMENTS)
        return df

    def barchart_visulization(self):
        ax = sns.barplot(x = 'title', y = 'viewCount', data = self.df.sort_values('viewCount', ascending=False)[0:5])
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos:'{:,.0f}'.format(x/1000) + 'K'))
        plt.xticks(fontsize=8)
        plt.subplots_adjust(bottom=0.387, top=1)
        plt.show()

    def compare_plot(self):
        fig, ax = plt.subplots(1,2)
        sns.scatterplot(data = self.df, x = 'commentCount', y = 'viewCount', ax = ax[0])
        sns.scatterplot(data = self.df, x = 'likeCount', y = 'viewCount', ax = ax[1])
        plt.show()



'''
Testing visualization of data

'''

if __name__ == '__main__':
    visualization_obj = VisualOperations()
    # visualization_obj.barchart_visulization()
    visualization_obj.compare_plot()