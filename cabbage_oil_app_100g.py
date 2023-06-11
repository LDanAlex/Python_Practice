import tkinter as tk


class OilCalculator:

    def __init__(self, master):
        self.master = master
        master.title("Oil Calculator")

        # Create a PhotoImage object with the image file
        self.image = tk.PhotoImage(file="C:\\Users\\alutac\\Downloads\\grameprodus.png")

        # Create a Label widget to display the image
        self.image_label = tk.Label(master, image=self.image)
        self.image_label.pack()

        # Label for title
        self.title_label = tk.Label(master, text="Oil Calculator")
        self.title_label.pack()

        # Entry field for cabbage input
        self.cabbage_label = tk.Label(master, text="Cabbage (grams): ")
        self.cabbage_label.pack()
        self.cabbage_entry = tk.Entry(master)
        self.cabbage_entry.pack()

        # Button to calculate cabbage grams
        self.cabbage_button = tk.Button(master, text="Cabbage Grams", command=self.show_oil_entry)
        self.cabbage_button.pack()

    def show_oil_entry(self):
        # Hide cabbage elements
        self.cabbage_label.pack_forget()
        self.cabbage_entry.pack_forget()
        self.cabbage_button.pack_forget()

        # Show oil elements
        self.oil_label = tk.Label(self.master, text="Oil (grams): ")
        self.oil_label.pack()
        self.oil_entry = tk.Entry(self.master)
        self.oil_entry.pack()

        self.oil_button = tk.Button(self.master, text="Oil Grams", command=self.calculate_oil_grams)
        self.oil_button.pack()

    def calculate_oil_grams(self):
        cabbage_grams = int(self.cabbage_entry.get())
        oil_grams = int(self.oil_entry.get())
        oil_per_100_grams_cabbage = (oil_grams / cabbage_grams) * 100
        result_label = tk.Label(self.master, text="Oil per 100g cabbage: {:.2f}g".format(oil_per_100_grams_cabbage))
        result_label.pack()


root = tk.Tk()
app = OilCalculator(root)
root.mainloop()
