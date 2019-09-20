# 1 Check to see if directory is empty

import os, sys

if len(os.listdir('/Users/bull/Documents/AutoFolder') ) == 0:
    print("Directory is empty")
else:    
    print("next step")

