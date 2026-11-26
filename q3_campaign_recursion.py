def cumulative_spend(daily_spend, n):
    """使用遞迴計算前 n 天的累計廣告花費"""
    if n == 0:
        return 0
    return cumulative_spend(daily_spend, n - 1) + daily_spend[n - 1]


# 共同設定：讀取完整學號
student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c

# 建立個人測試資料
daily_spend = [100 + 10 * a, 150 + 10 * b, 0, 200 + 10 * c, 50 + 10 * s]
n = 3 + c % 3

print(f"學號：{student_id}")
print(f"每日費用：{daily_spend}")
print(f"指定n：{n}")
print(f"指定前{n}天累計：{cumulative_spend(daily_spend, n)}元")

for day in range(6):
    print(f"前{day}天：{cumulative_spend(daily_spend, day)}元")

print(f"空資料：{cumulative_spend([], 0)}元")