import pandas as pd
from fpdf import FPDF

df = pd.read_csv('articles.csv', sep=',', dtype={'id': str})
df['name'] = df['name'].str.title()


class Product:
    def __init__(self, product_id):
        self.product_id = product_id
        self.name = df.loc[df['id'] == self.product_id, 'name'].squeeze().title()
        self.price = df.loc[df['id'] == self.product_id, 'price'].squeeze()
        self.stock = df.loc[df['id'] == self.product_id, 'in stock'].squeeze()

    def buy(self):
        stock = self.stock
        if stock > 0:
            stock = stock - 1
            df.loc[df['id'] == self.product_id, 'in stock'] = stock
            df.to_csv('articles.csv', index=False)

    def invoice(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.product_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.price}", ln=1)

        pdf.output("receipt.pdf")


print(df)

product_ID = input('Choose an ID of the product: ')

product = Product(product_ID)
product.invoice()
product.buy()
