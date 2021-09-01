import pandas as pd

# Read the csv file in
df = pd.read_csv('Resources/cities.csv')

# Save to file
#df.to_html('myTable.htm')

# Assign to string
#htmTable = df.to_html()

for rowIndex, row in df.iterrows(): #iterate over rows
    print("<tr>")
    for columnIndex, value in row.items():
        print(f"<td>{value}</td")
    print("</tr>")