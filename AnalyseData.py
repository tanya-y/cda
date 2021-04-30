import pandas as pd

class Analyse():

    def __init__(self, path):
        self.df = pd.read_csv(path)

        if path.endswith('apps.csv'):
            self.cleanAppsData()
        else:
            self.cleanReviewsData()

    def cleanAppsData(self):
        chars_to_remove = ['+', ',', 'M', '$']
        cols_to_clean = ['Installs', 'Size', 'Price']

        for col in cols_to_clean:
            for char in chars_to_remove:
                self.df[col] = self.df[col].str.replace(char, '')
            self.df[col] = pd.to_numeric(self.df[col])

    def cleanReviewsData(self):
        pass

    def getDataset(self):
        return self.df

    def getTopCategories(self, n=10):
        return self.df.groupby('Category').count().sort_values('App')['App'][::-1]

    def getAppRatings(self):
        return self.df['Rating']

    def getFreeApps(self):
        return self.df['Installs'][self.df['Type'] == 'Paid']

    def getPaidApps(self):
        return self.df['Installs'][self.df['Type'] == 'Free']

    def getExpensive(self):
        popular_cat = ['FAMILY', 'GAME', 'TOOLS', 'BUSINESS', 'MEDICAL', 'PERSONALIZATION',
       'PRODUCTIVITY', 'LIFESTYLE']
        popular_apps = apps[apps.Category.isin(popular_cat)]
        return popular_apps[['Category', 'App', 'Price']][popular_apps['Price'] > 200]