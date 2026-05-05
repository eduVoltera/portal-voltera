import pandas as pd

file_path = "data/base.xlsx"

df = pd.read_excel(file_path, engine="openpyxl")

html = f"""
<html>
<head>
    <title>Portal Voltera</title>
</head>
<body>
    <h1>Datos</h1>
    {df.to_html(index=False)}
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("OK")
