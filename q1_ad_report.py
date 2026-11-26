def ad_report(impressions, clicks, target=3.0):
    """計算廣告點擊率 (CTR) 並判斷是否達到目標門檻"""
    if impressions == 0:
        return (None, False)
    ctr = clicks / impressions * 100
    passed = ctr >= target
    return (ctr, passed)


# 共同設定：讀取完整學號
student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c

# 建立個人測試資料
ads = [
    ("搜尋廣告", 1000 + 100 * a, 30 + 5 * b),
    ("社群廣告", 1200 + 100 * b, 24 + 4 * c),
    ("影音廣告", 0, 0),
]
target = 2.5 + 0.1 * c

print(f"學號：{student_id}")
print(f"CTR門檻：{target:.2f}%")

passed_count = 0
for name, imp, clk in ads:
    ctr, passed = ad_report(imp, clk, target=target)
    if passed:
        passed_count += 1
    ctr_text = "無曝光資料" if ctr is None else f"{ctr:.2f}%"
    print(f"{name}：曝光={imp}，點擊={clk}，CTR={ctr_text}，達標={passed}")

print(f"達標廣告數：{passed_count}")
print(f"預設門檻測試：{ad_report(1000, 30)}")
print(f"零點擊測試：{ad_report(1000, 0)}") 