
import re
def findtheindexes(names , find):
    k = re.findall(names , find)
print(findtheindexes('sadnesssad' , 'sad'))