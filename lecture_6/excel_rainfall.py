from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference

wb = Workbook()
ws = wb.active

rainfall_data = [["Month", "Precipitation Amount (nm)"], ["January", "81.2"],
                 ["February", "63.2"], ["March", "70.3"], ["April", "55.7"],
                 ["May", "53.0"], ["June", "36.4"], ["July", "17.5"], ["August", "27.5"],
                 ["September", "60.9"], ["October", "117.7"], ["November", "111.0"], ["December", "792.9"]]

for row in rainfall_data:
    ws.append(row)

ft = Font(bold=True)

for row in ws["A1:B1"]:
    for cell in row:
        cell.font = ft

chart = BarChart()
chart.type = "col"
chart.title("Average Rainfall in Rome: 1188 months between 1782 and 1970")
chart.y_axis.title = 'Height (nm)'
chart.x_axis.title = "Month"
chart.legend = None

