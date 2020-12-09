from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 

# dd/mm/YY H:M:S
rb_brain = now.strftime("%d/%m/%Y %H:%M:%S")