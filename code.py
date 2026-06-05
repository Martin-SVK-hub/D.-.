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














gg
z = [5, 10, 15, 20, 25, 40, 1200]
z_sorted = []

def find_smallest(z):
    smallest = float("inf")
    for item in z:
        if item < smallest:
            smallest = item
    return smallest

while z:
    smallest = find_smallest(z)
    z_sorted.append(smallest)
    z.remove(smallest)

print(z_sorted)
















z = [5, 10, 15, 20, 25, 40, 1200]
z_sorted = []

def find_smallest(z):
    smallest = z[0]   
        if item < smallest:
        smallest = item
    return smallest

while len(z) > 0:
    smallest = find_smallest(z)
    z_sorted.append(smallest)
    z.remove(smallest)

print(z_sorted)



















TOTO JE STARY FRONTEND 

<!DOCTYPE html>
<html lang="sk">
<head>
    <meta charset="UTF-8">
    <title>Študenti</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f0f2f5;
            text-align: center;
        }

        h1 {
            margin: 20px;
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }

        .card {
            background: white;
            width: 220px;
            margin: 10px;
            padding: 10px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            transition: 0.2s;
        }

        .card:hover {
            transform: scale(1.05);
        }

        img {
            width: 100%;
            border-radius: 10px;
        }

        button {
            padding: 10px 20px;
            margin: 15px;
            border: none;
            border-radius: 8px;
            background: #007bff;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background: #0056b3;
        }
    </style>
</head>

<body>

<h1>Zoznam študentov</h1>

<button onclick="loadStudents()">Načítať študentov</button>

<div class="container" id="students"></div>

<script>
    const API_URL = "https://mojprvybackend-qjm9.onrender.com/api"; // 🔥 TU DÁŠ SVOJ BACKEND

    async function loadStudents() {
        const container = document.getElementById("students");
        container.innerHTML = "Načítavam...";

        try {
            const response = await fetch(API_URL);
            const data = await response.json();

            container.innerHTML = "";

            data.students.forEach(student => {
                const div = document.createElement("div");
                div.className = "card";

                div.innerHTML = `
                    <img src="${student.img}"
                    <h3>${student.name} ${student.surname}</h3>
                    <p><b>Prezývka:</b> ${student.nickname || "-"}</p>
                `;

                container.appendChild(div);
            });

        } catch (error) {
            container.innerHTML = "❌ Nepodarilo sa načítať dáta";
            console.error(error);
        }
    }
</script>

</body>
</html>
