from flask import *
import pandas as pd
app = Flask(__name__)

@app.route("/")
def show_tables():
    data = pd.read_excel('fruit.xlsx')
    data.set_index(['Number'], inplace=True)
    data.index.name=None
    fruits = data.loc[data.Class=='f']
    vegs = data.loc[data.Class=='v']
    return render_template('view.html',tables=[fruits.to_html(classes='fruit'), vegs.to_html(classes='veg')],
    titles = ['na', 'Fruits', 'Veggies'])

@app.route("/json")
def show_json():
	# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
    data = pd.read_excel('fruit.xlsx')
    data.set_index(['Number'], inplace=True)
    data.index.name=None
    return data.to_json(orient='split')
	
if __name__ == "__main__":
    app.run(debug=True)