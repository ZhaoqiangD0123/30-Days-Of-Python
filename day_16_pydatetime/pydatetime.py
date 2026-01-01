from datetime import datetime, timedelta
# 从datetime模块获取当前的日、月、年、小时、分钟和时间戳
now = datetime.now()
print(now)
# 使用此格式格式化当前日期："%m/%d/%Y, %H:%M:%S"
now_strf = now.strftime("%m/%d/%Y, %H:%M:%S")
print(now_strf)
# 今天是2019年12月5日。将此时间字符串转换为时间。
today = datetime(2019,12,5)
# 计算现在和新年之间的时间差。
now_timedelta = now-today
print(now_timedelta.days)
# 计算1970年1月1日和现在之间的时间差。
last = datetime(1970,1,1)
print((now-last))
# 任务 1：你是哪天出生的？
# 定义你的生日（例如：birthday = datetime(1995, 5, 20)）。
birthday = datetime(2004,1,23)
# 计算你在这个世界上活了多少天？（用 now - birthday）。
print(f'我已经在地球上生活了{(now-birthday).days}天了')
# 打印结果："我已经在地球上生活了 X 天了！"