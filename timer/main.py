from Timer import Timer
from multiprocessing import Process


print("Set timer duration: ")
print("formats allowed are: ")
print("> hh:mm:ss")
print("> [hours]h[minutes]m[seconds]s")
print("> [seconds]")
timestamp = input()

indexes = [('', -1)]
for id in ['h', 'm', 's']:
    index = timestamp.find(id)
    if index > 0:
        indexes.append((id, index))

# 'h', 'm', 's' identifiers are present
if len(indexes) > 1:
    idValue = {'h': 3600, 'm': 60, 's': 1}
    indexes.sort(key=lambda x: x[1])
    seconds = 0
    for left, right in zip(indexes, indexes[1:]):
        seconds += int(timestamp[left[1]+1:right[1]])*idValue.get(right[0])
# 'h', 'm', 's' identifiers not present, the format is
# a hh:mm:ss timestamp
else:
    durations = timestamp.split(":")
    if len(durations) > 3:
        exit("Timestamp not recognised")
    seconds = int(durations[-1])
    if len(durations) >= 2:
        seconds += int(durations[-2])*60
    if len(durations) == 3:
        seconds += int(durations[-3])*3600

timer = Timer(seconds)
timer.start()

alarmProcess = Process(target=timer.playAlarm())
alarmProcess.start()
input()
alarmProcess.kill()
