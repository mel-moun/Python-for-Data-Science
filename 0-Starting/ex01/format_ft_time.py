import time
import datetime

curr = time.time()
scientific = f"{curr:.4e}"
curr_date = datetime.datetime.fromtimestamp(curr)
date = curr_date.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {curr:,.4f} or {scientific} in scientific notation")
print(date)



