import pandas as pd

climate_table = pd.read_excel("climate-table.xlsx")
mean_temp = climate_table["Avg. Temp (°F)"].mean()
mean_rainfall = climate_table["Rainfall (in)"].mean()
mean_sunshine = climate_table["Sunshine hours"].mean()

print(climate_table)
print(f"The yearly temperature average is {mean_temp} (°F), the average yearly rainfall is {mean_rainfall} inches. "
      f"The yearly sunshine is {mean_sunshine} hours.")