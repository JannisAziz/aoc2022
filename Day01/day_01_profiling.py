from datetime import datetime as dt
import day_01

start = dt.now().microsecond / 1000

steps = 1
for _ in range(steps):
    day_01.get_top_totals()

end = dt.now().microsecond / 1000
print(end - start)