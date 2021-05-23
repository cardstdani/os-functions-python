import os

print(str(os.system("""wmic path CIM_LogicalDevice where "Description like 'USB%'" get /value""")) + "\n")
