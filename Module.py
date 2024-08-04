# The code is preliminary and will be completed when the user interface is built

from datetime import datetime
import pandas as pd
import csv
import openpyxl as xl


class Product():

    """
    -> This class is a form for the product,
    we use this class to create the product object 
    every time we add the product

    Attributes of this object:
        - SN : Serial number or id -> int
        - Name : Product name -> str
        - Price : Price product -> float
        - Buy : The number of products purchased -> int
        - Sell : Some of this product has been sold -> int
        - Category : Product categories for filtering and better user access -> str
        - Date : date to add buy or sell -> %d-%m-%y
        - Time : Time to add buy or sell -> %H:%M:%S

    """

    def __init__(self, SN, name, price, category, date, time, buy_count=0, sell_count=0):

        if isinstance(SN, int):
            self.__serial_number = SN
        else:
            raise ValueError(
                'the value is not valid ! , plese inter the valid value')
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError(
                'the value is not valid ! , plese inter the valid value')

        if isinstance(price, float) or isinstance(price, int):
            self.__price = price
        else:
            raise ValueError(
                'the value is not valid ! , plese inter the valid value')
        if isinstance(buy_count, int):
            self.__buy_count = buy_count
        else:
            raise ValueError(
                'the value is not valid ! , plese inter the valid value')
        if isinstance(sell_count, int):
            self.__sell_count = sell_count
        else:
            raise ValueError(
                'the value is not valid ! , plese inter the valid value')
        if isinstance(category, str):
            self.__category = category
        else:
            raise ValueError(
                'the value is not valid ! , plese inter the valid value')
        if not date:
            self.__date = DateTime.date()
        else:
            self.__date = date

        if not time:
            self.__time = DateTime.time()
        else:
            self.__time = time

    def __str__(self) -> str:

        return f"SN\tName\tCategory\tPrice\n{self.__serial_number}\t{self.__name}\t{self.__category}\t{self.__price}"

    # Accessor methods ->

    def get_id(self):
        return self.__serial_number

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_buy_count(self):
        return self.__buy_count

    def get_sell_count(self):
        return self.__sell_count

    def get_category(self):
        return self.__category

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    # end Accessor methods <-

    # Mutator methods ->

    def set_id(self, new_serial):
        self.__serial_number = new_serial

    def set_name(self, new_name):
        self.__name = new_name

    def set_price(self, new_price):
        self.__price = new_price

    def set_buy_count(self, new_buy_count):
        self.__buy_count = new_buy_count

    def set_sell_count(self, new_sell_count):
        self.__sell_count = new_sell_count

    def set_category(self, new_category):
        self.__category = new_category

    # end Mutator methods <-


class DateTime:

    import datetime

    TIMEFORMAT = "%H:%M:%S"
    DATEFORMAT = "%d-%m-%y"

    @classmethod
    def date(self):
        date = self.datetime.now().strftime(self.DATEFORMAT)
        return date

    @classmethod
    def time(self):
        time = self.datetime.now().strftime(self.TIMEFORMAT)
        return time


class CSV():

    FILENAME = 'pyfinance.csv'
    COLUMS = ['SN', 'Name', 'Price', 'Buy', 'Sell', 'Category', 'Date', 'Time']
    FORMAT = '%d-%m-%y'
    EXCEL = 'Book1.xlsx'

    @classmethod
    def init_file(cls):

        # cls -> self

        try:
            df = pd.read_csv(cls.FILENAME)
            return df
        except FileNotFoundError:

            df = pd.DataFrame(columns=cls.COLUMS)
            df.to_csv(cls.FILENAME, index=False)

    @classmethod
    def add(cls, SN, Name, Price, Buy, Sell, Category):
        new_Product = Product(
            SN=SN,
            name=Name,
            price=Price,
            buy_count=Buy,
            sell_count=Sell,
            category=Category
        )

        df = pd.DataFrame(
            columns=[
                {
                    'SN': new_Product.get_id(),
                    'Name': new_Product.get_name(),
                    'Price': new_Product.get_price(),
                    'Buy': new_Product.get_buy_count(),
                    'Sell': new_Product.get_sell_count(),
                    'Category': new_Product.get_category(),
                    'Date': new_Product.get_date(),
                    'Time': new_Product.get_time()
                }
            ]
        )

        with open(cls.FILENAME, 'a', newline="") as csvfile:
            wrirter = csv.DictWriter(csvfile, fieldnames=cls.COLUMS)
            wrirter.writerows(df)
        print("entry added successfully...")

    @classmethod
    def search(cls, start, end):

        df = cls.init_file()
        df['Date'] = pd.to_datetime(df['Date'], format=cls.FORMAT)
        start_date = datetime.strptime(start, cls.FORMAT)
        end_date = datetime.strptime(end, cls.FORMAT)
        mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
        filtred_df = df.loc[mask]
        print(filtred_df.to_string(index=False, formatters={
              'Date': lambda x: x.strftime(cls.FORMAT)}))

        # todo: When the GUI is created, it will be completed

    @classmethod
    def edit(cls, id):
        df = cls.init_file()
        sdf = df.loc[df['SN'] == id]

        edited = []

        for coulm in CSV.COLUMS:
            if coulm == 'Date':
                result = input(f'\\ inter the edited Date "(dd-mm-yyyy)": ')
            elif coulm == 'Time':
                result = input(f'\\ inter the edited Time "(HH:MM:SS)": ')
            else:
                result = input(f'\\ inter the edited {coulm} : ')
            edited.append(result)
        # use zip function
        # todo : When the GUI is created, it will be completed

    def delete(cls):
        pass

    @classmethod
    def input_exel(cls):
        excel = xl.load_workbook(cls.EXCEL)
        sheet = excel.active
        col = csv.writer(open(cls.FILENAME, 'a', newline=""))

        for r in sheet.rows:
            col.writerow([cell.value for cell in r])

        df = pd.DataFrame(pd.read_csv(cls.FILENAME))
        # todo : When the GUI is created, it will be completed
        # When the user approves, it will be saved in the csv file

    def output_exel(cls):

        # Reading the csv file
        df_new = pd.read_csv('Names.csv')

        # saving xlsx file
        GFG = pd.ExcelWriter('Names.xlsx')
        df_new.to_excel(GFG, index=False)

        GFG.save()
        
        # todo : When the GUI is created, it will be completed
        # todo : When the user approves, it will be saved in the csv file and input excel name from user 
