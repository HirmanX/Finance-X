# create graphics user inter face here
from Module import CSV
import tkinter as tk


class Window:

    def home():
        # windows settings :
        root = tk.Tk()
        root.title('PyFinance')
        root.geometry("1200x700")

        # Button box ->
        frame = tk.Frame(
            root,
            highlightbackground='white',
            highlightthickness=2,
            bd=0,
            width=150,
            height=330,
            background='blue'
        )
        frame.place(
            x=7,
            y=30
        )

        add = tk.Button(
            root,
            text="Add",
            width=15,
            height=2
        )
        add.place(
            x=25,
            y=50
        )
        search = tk.Button(
            root,
            text="Search",
            width=15,
            height=2
        )
        search.place(
            x=25,
            y=100
        )
        edit = tk.Button(
            root,
            text="Edit",
            width=15,
            height=2
        )
        edit.place(
            x=25,
            y=150
        )
        delete = tk.Button(
            root,
            text="Delete",
            width=15,
            height=2
        )
        delete.place(
            x=25,
            y=200
        )
        open_excel = tk.Button(
            root,
            text="Open Excel",
            width=15,
            height=2
        )
        open_excel.place(
            x=25,
            y=250
        )
        export_excel = tk.Button(
            root,
            text="Export Excel",
            width=15,
            height=2
        )
        export_excel.place(
            x=25,
            y=300
        )
        # end button box <-

        # total boc -> 
        m_frame = tk.Frame(
            root,
            width=150,
            height=200,
            bd=0,
            background='blue'
        )
        m_frame.place(
            x=7,
            y=450
        )
        months = tk.Label(
            root,
            text="this months",
            background='white',
            width=12,
            height=1
        )
        months.place(
            x=40,
            y=460
        )
        buy = tk.Label(
            root,
            text="Buy :",
            width=10,
            height=1
        )
        buy.place(
            x=5,
            y=500
        )
        buy_number = tk.Label(
            root,
            text="99999",
            width=10,
            height=1
        ) 
        buy_number.place(
            x=85,
            y=500
        )
        sell = tk.Label(
            root,
            text="Sell :",
            width=10,
            height=1
        )
        sell.place(
            x=5,
            y=530
        )
        sell_number = tk.Label(
            root,
            text="99999",
            width=10,
            height=1
        ) 
        sell_number.place(
            x=85,
            y=530
        )
        tax = tk.Label(
            root,
            text="Tax :",
            width=10,
            height=1
        )
        tax.place(
            x=5,
            y=560
        )
        tax_number = tk.Label(
            root,
            text="99999",
            width=10,
            height=1
        ) 
        tax_number.place(
            x=85,
            y=560
        )
        profit = tk.Label(
            root,
            text="Profit",
            width=10,
            height=1,
            background='green'
        ) 
        profit.place(
            x=5,
            y=590
        )
        profit_number = tk.Label(
            root,
            text="99999",
            width=10,
            height=1,
            background='green'
        ) 
        profit_number.place(
            x=85,
            y=590
        )
        # end tottal box <-

        # table view box -> 

        home_list_buy = tk.Listbox(
            root,
            width=70,
            height=36,
            background='red'
        )
        home_list_buy.place(
            x=200,
            y=68
        )
        home_list_sell = tk.Listbox(
            root,
            width=70,
            height=36,
            background='green'
        )
        home_list_sell.place(
            x=700,
            y=68
        )

        # home list label ->
        cloums_buy = tk.Label(
            root,
            width=52,
            height=3,
            text=CSV.COLUMS,
            font=('Arial',10),
            background='red'
        )
        cloums_buy.place(
            x=200,
            y=5
        )
        cloums_sell = tk.Label(
            root,
            width=52,
            height=3,
            text=CSV.COLUMS,
            font=('Arial',10),
            background='green'
        )
        cloums_sell.place(
            x=700,
            y=5
        )

        # end home list label <-
        
        # end menu box <- 

        # show window
        root.mainloop()


Window.home()
