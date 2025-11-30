#from magika import Magika
import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'python', 'src'))

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