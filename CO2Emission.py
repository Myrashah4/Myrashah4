import pandas as pd
import matplotlib.pyplot as plt

# Read CO2 emission data from Excel file
file_path = "CO2 emission.xlsx"
try:
    df = pd.read_excel(file_path)
except FileNotFoundError:
    print(f"File '{file_path}' not found. Please make sure the file exists.")
    exit()

# Data visualization
plt.figure(figsize=(10, 6))

# Bar chart
plt.subplot(2, 1, 1)
plt.bar(df['Year'], df['CO2 Emission'])
plt.title('CO2 Emission Over the Years (Bar Chart)')
plt.xlabel('Year')
plt.ylabel('CO2 Emission (Million Metric Tons)')

# Line chart
plt.subplot(2, 1, 2)
plt.plot(df['Year'], df['CO2 Emission'], marker='o', linestyle='-', color='b')
plt.title('CO2 Emission Over the Years (Line Chart)')
plt.xlabel('Year')
plt.ylabel('CO2 Emission (Million Metric Tons)')

# Save charts in different formats
plt.savefig('CO2_Emission_Bar_Chart.png', format='png')
plt.savefig('CO2_Emission_Line_Chart.jpeg', format='jpeg')
plt.savefig('CO2_Emission_Charts.svg', format='svg')

# Display the charts
plt.show()
