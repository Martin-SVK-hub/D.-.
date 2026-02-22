import requests

response = requests.get("https://boozeapi.com/api/v1/cocktails")

if response.status_code == 200:
    data = response.json()

    pocitadlo = {
        "Vodka": 0,
        "Gin": 0,
        "Rum": 0}

    for cocktail in data['data']:
        print(cocktail['image'])
        for ingredient in cocktail.get("ingredients", []):
            if ingredient['type'] == "Rum":
                pocitadlo["Rum"] += 1

    for alkohol, pocet in pocitadlo.items():
        print(f"{alkohol}: {pocet}")

else:
    print("Error", response.status_code, response.text)
   



   from flask import Flask

app = Flask(__name__)

@app.route("/")
def Dobrý():
    return "<p>Dobrý!</p>" """
<img src="https://www.tasteofhome.com/wp-content/uploads/2018/01/EXPS_TOHVP24_37188_MF_04_10_2.jpg" alt="Koktail">
"""









import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    try:
        response = requests.get("https://boozeapi.com/api/v1/cocktails")

        if response.status_code != 200:
            return f"Chyba pri načítaní API: {response.status_code}"

        data = response.json()

        pocitadlo = {
            "Vodka": 0,
            "Gin": 0,
            "Rum": 0
        }

        html = "<h1>Zoznam drinkov</h1>"

        for cocktail in data.get("data", []):
            nazov = cocktail.get("name", "Neznámy drink")
            obrazok = cocktail.get("image", "")

            html += f"<h3>{nazov}</h3>"
            html += f'<img src="{obrazok}" width="200"><br><br>'

            for ingredient in cocktail.get("ingredients", []):
                typ = ingredient.get("type")
                if typ in pocitadlo:
                    pocitadlo[typ] += 1

        html += "<h2>Počet podľa alkoholu:</h2>"
        for alkohol, pocet in pocitadlo.items():
            html += f"<p>{alkohol}: {pocet}</p>"

        return html

    except Exception as e:
        return f"Nastala chyba: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)





