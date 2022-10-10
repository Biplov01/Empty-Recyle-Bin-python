# pip install winshell
import winshell
try:
winshell.recyclebin().empty(confirm=False, show_progress=False, sound=True)
print("Recycle bin is emptiedNow")
except:
print("Recycle bin is emptied now")
except:
print("recycle bin alreadyempty")

© copyright @Biplov2022
#Recycle bin is emptied now