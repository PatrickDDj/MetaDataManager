import pandas as pd
import os


def exists_table(table_name):
    file_name = table_name + '.csv'
    return file_name in os.listdir('tables')


def create_table(table_name, columns):
    if exists_table(table_name):
        print("Table '%s' exists!" % table_name)
    else:
        df = pd.DataFrame(columns = columns)
        df.to_csv('tables/%s.csv' % table_name, index=False)


def get_all_tables():
    return [i.replace('.csv', '') for i in os.listdir('tables')]


def delete_table(table_name):
    file_name = 'tables/' + table_name + '.csv'
    os.remove(file_name)


def show_table(table_name):
    file_name = 'tables/' + table_name + '.csv'
    df = pd.read_csv(file_name)
    columns = df.columns
    records = [row.to_list() for i, row in df.iterrows()]
    index = df.index.to_list()
    return columns, zip(records, index)


def add_record(table_name, record):
    file_name = 'tables/' + table_name + '.csv'
    df = pd.read_csv(file_name)
    i = max(df.index)+1 if df.index!=None else 0
    df.loc[i] = record
    df.to_csv(file_name, index=False)


def delete_record(table_name, index):
    file_name = 'tables/' + table_name + '.csv'
    df = pd.read_csv(file_name)
    df = df.drop(index)
    df.to_csv(file_name, index=False)


def get_record(table_name, index):
    file_name = 'tables/' + table_name + '.csv'
    df = pd.read_csv(file_name)
    return df.columns, df.loc[index]


def edit_record(table_name, index, record):
    file_name = 'tables/' + table_name + '.csv'
    df = pd.read_csv(file_name)
    df.loc[index] = record
    df.to_csv(file_name, index=False)