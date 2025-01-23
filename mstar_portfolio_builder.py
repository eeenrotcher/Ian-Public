import os
import morningstar_data as md

print("Current working directory:", os.getcwd())

os.environ['MD_AUTH_TOKEN']="paste copied token here"

try:
    data_sets = md.direct.get_morningstar_data_sets()
    print("Successfully retrieved data
    
     sets:", data_sets)
except Exception as e:
    print("Error retrieving data sets:", e)
