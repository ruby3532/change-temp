# 讓使用者輸入 攝氏
# 印出 華氏

temp = input('請輸入攝氏： ')
temp = float(temp)
Ctempt = (temp - 32)* 5/9
Ctempt = float(Ctempt)
# F = C*9/5+32
print('攝氏為' , temp , '。' , '華氏為' , Ctempt)
