import pandas as pd

def preprocess(file_name):
    # read csv
    df = pd.read_csv(file_name)

    # index,product,category,sub_category,brand,sale_price,market_price,type,rating,description

    # drop index
    df = df.drop(columns=['index'])

    # drop duplicates products
    df = df.drop_duplicates(subset=['product'])

    # drop null values
    df = df.dropna()

    # drop rows with sale_price = 0
    df = df[df.sale_price != 0]

    # drop rows with market_price = 0
    df = df[df.market_price != 0]

    # reset index
    df = df.reset_index(drop=True)

    # merge colums to create a new column 'context'
    df['context'] = 'Category: ' + df['category'] + ' Sub Category: ' + df['sub_category'] + ' Brand: ' + df['brand'] + ' Sale Price: ' + df['sale_price'].astype(str) + ' Market Price: ' + df['market_price'].astype(str) + ' Type: ' + df['type'] + ' Rating: ' + df['rating'].astype(str) + ' Description: ' + df['description']
    
    # remove columns
    df = df.drop(columns=['category', 'sub_category', 'brand', 'sale_price', 'market_price', 'type', 'rating', 'description'])

    # remove special characters
    # df['context'] = df['context'].str.replace('[^\w\s]','')

    # print metadata
    print('Total number of records: ', len(df))
    print('Columns: ', df.columns)

    return df