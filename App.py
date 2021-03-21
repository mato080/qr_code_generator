import pyqrcode
import pandas as pd

def createQRCode():

    df = pd.read_csv("Data.csv")

    for index, values in df.iterrows():

        app_verif = values["app_verif"]
        app_name = values["app_name"]
        app_address = values["app_address"]
        app_logo = values["app_logo"]
        app_value = values["app_value"]

        data = f'''{app_verif};{app_name};{app_address};{app_logo};{app_value}'''
    #    data = print(f'''{app_verif};{app_name};{app_address};{app_logo};{app_value}''')

        image = pyqrcode.create(data)
        image.svg(f"{app_name}_{app_value}.svg", scale="5")

createQRCode()
