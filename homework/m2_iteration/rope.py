# 6.	迴圏的練習-rope
# 若有一條繩子長3000公尺，每天剪去一半的長度，需多少天繩子的長度會短於5公尺。
rope_length = 3000
day = 0
print('若有一條繩子長{}公尺，每天剪去一半的長度，'.format(rope_length), end="")
while rope_length >= 5:
    rope_length /= 2
    day += 1
print('需要{}天繩子的長度會短於5公尺'.format(day))
print('此時繩長為{:.2f}公尺'.format(rope_length))
