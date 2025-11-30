#from magika import Magika
import sys
import os

# Get the absolute path to the folder containing magika.py
# We go: current dir -> python -> src -> magika
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'python', 'src'))

# --- THE FIX ---
# Use insert(0, path) instead of append(path)
# This puts your folder at the TOP of the search list
if module_path not in sys.path:
    sys.path.insert(0, module_path)

import magika
#m = Magika()
m = magika.Magika()
#res = m.identify_path('./tests_data/basic/python')
res = m.scan_directory('./tests_data/scan_directory')
print("------------------ PREDICTIONS ------------------")
for result in res:
    print(result)
    print()
#print(res)