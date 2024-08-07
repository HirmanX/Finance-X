# main function to run programm

from GUI import Window
from Module import CSV, Product

def main():
    
    def file_load():
        file = CSV.init_file()
        if file == None:
            Window.Error("data file not found!")
           
    def home_page():
        buy_data = CSV.list_view('buy')
        sell_data = CSV.list_view('sell') 
        Window.home(buy_innsert=buy_data,sell_insert=sell_data) # TODO : move to inner class

    home_page()

main()