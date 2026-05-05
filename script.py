import pandas as pd

df = pd.read_excel("data/base.xlsx")

html = f"""
<html>
<head>
    <title>Portal Voltera</title>
    <style>
        body {{ font-family: Arial; padding: 20px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; }}
        th {{ background-color: #0f172a; color: white; }}
    </style>
</head>
<body>
    <h1>Recaudación y Cobranza</h1>
    {df.to_html(index=False)}
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML generado")
