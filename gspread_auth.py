import gspread
import os
import gspread.auth as ga
import pandas as pd
'''

def gspread_paths(dir):
    ga.DEFAULT_CONFIG_DIR = dir
    ga.DEFAULT_CREDENTIALS_FILENAME = os.path.join(
        ga.DEFAULT_CONFIG_DIR, 'credentials.json')
    ga.DEFAULT_AUTHORIZED_USER_FILENAME = os.path.join(
        ga.DEFAULT_CONFIG_DIR, 'authorized_user.json')
    ga.DEFAULT_SERVICE_ACCOUNT_FILENAME = os.path.join(
        ga.DEFAULT_CONFIG_DIR, 'service_account.json')
    ga.load_credentials.__defaults__ = (ga.DEFAULT_AUTHORIZED_USER_FILENAME,)
    ga.store_credentials.__defaults__ = (ga.DEFAULT_AUTHORIZED_USER_FILENAME, 'token')
gc = gspread.oauth()
sh = gc.open('Example spreadsheet')
print(sh.sheet1.get('A1'))
gspread_paths('/Users/gokmen/PycharmProjects/TwoZero_TeamScore/venv/lib/python3.9/site-packages/gspread')
'''

top_100_read = pd.read_csv('/Users/gokmen/Desktop/top_1000.csv', sep=',')
top_100_list = list(top_100_read['universities'])
print(top_100_list)