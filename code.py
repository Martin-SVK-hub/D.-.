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
