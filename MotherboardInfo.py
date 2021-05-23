import os

print(str(os.system("wmic baseboard get Manufacturer, Model, Name, PartNumber, serialnumber")) + "\n")
