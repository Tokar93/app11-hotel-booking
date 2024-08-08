import pandas as pd
from fpdf import FPDF

df = pd.read_csv('articles.csv', sep=',', dtype={'id': str})
df['name'] = df['name'].str.title()


class Product:
    def __init__(self, product_id):
        self.product_id = product_id
        self.name = df.loc[df['id'] == self.product_id, 'name'].squeeze().title()
        self.price = df.loc[df['id'] == self.product_id, 'price'].squeeze()

    def available(self):
        in_stock = df.loc[df['id'] == self.product_id, 'in stock'].squeeze()
        return in_stock


class Invoice:
    def __init__(self, article):
        self.article = article

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.product_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")


print(df)

product_ID = input('Choose an ID of the product: ')
product = Product(product_ID)
if product.available():
    invoice = Invoice(product)
    invoice.generate()
else:
    print('Product not available')
