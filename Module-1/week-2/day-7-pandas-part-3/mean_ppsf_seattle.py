"""Find the mean price per square foot for a house sold in Seattle in 2019"""
import pandas as pd

"""Import csv files"""
sales_df = pd.read_csv('data/EXTR_RPSale.csv')
bldg_df = pd.read_csv('data/EXTR_ResBldg.csv')

"""Specify interests"""
sales_df = sales_df[['Major', 'Minor', 'DocumentDate', 'SalePrice']]
bldg_df = bldg_df[['Major', 'Minor', 'SqFtTotLiving', 'ZipCode']]

"""Merge files"""
sales_data = pd.merge(sales_df, bldg_df, on=['Major', 'Minor'])

"""Change data type"""
sales_data['Major'] = pd.to_numeric(sales_df['Major'], errors = 'coerce')
sales_data['Minor'] = pd.to_numeric(sales_df['Minor'], errors = 'coerce')

"""Drop the missing values in ZipCode"""
sales_data = sales_data[~sales_data['ZipCode'].isna()]

"""Remove invalid values"""
cleaned_data = sales_data[(sales_data['SalePrice'] > 0) & (sales_data['SqFtTotLiving'] > 0)]

"""Convert Zipcode data type to str to return 5 digit ZipCode"""
cleaned_data['ZipCode'] = cleaned_data['ZipCode'].map(lambda x:str(x))
cleaned_data['ZipCode'] = cleaned_data.['ZipCode'].map(lambda x:x[0:5])

"""Add new variable PricePerSqFt"""
cleaned_data['PricePerSqFt'] = round(cleaned_data.SalePrice / cleaned_data.SqFtTotLiving, 2)

"""Subset the data to 2019"""
data_2019 = cleaned_data.loc[cleaned_data.DocumentDate.str[-4:] == "2019"]

"""Import a list of Seattle City ZipCode"""
seattle_zipcode = [98101, 98102, 98103, 98104, 98105, 98106, 98107, 98108, 98109, 98112, 98115, 98116, 98117, 98118, 98119, 98121, 98122, 98125, 98126, 98133, 98134, 98136, 98144, 98146, 98154, 98164, 98174, 98177, 98178, 98195, 98199]

"""Convert the Seattle City ZipCode--Object to Seattle City ZipCode Numeric--Float"""
data_2019['ZipCode'] = pd.to_numeric(cleaned_data.ZipCode, errors = 'coerce')

"""Create new dataframe seattle_city_2019 and find the data_2019 ZipCode that mathches Seattle City ZipCode"""
seattle_city_2019= data_2019[data_2019.ZipCode.isin(seattle_zipcode)]

"""Convert the Seattle City ZipCode--Float back to Seattle City ZipCode--Object and slice it to 5 digits"""
seattle_city_2019.ZipCode = seattle_city_2019.ZipCode.astype(object)
seattle_city_2019.ZipCode = seattle_city_2019.ZipCode.map(lambda x:x[0:5])

"""Get the price per square foot of Seattle City in 2019"""
seattle_price_per_sqft_2019 = seattle_city_2019.PricePerSqFt.mean()
seattle_price_per_sqft_2019