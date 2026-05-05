import pandas as pd

df = pd.read_excel("data/base.xlsx")

html = f"""
<html>
<head>
    <title>Portal Voltera</title>
</head>
<body>
    <h1>Datos actualizados</h1>
    {df.to_html(index=False)}
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
