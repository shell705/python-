# 法1
name="南昌二中"
message="坐牢就来%s"%name
print(message)
#将数字以字符串形式占位拼接（%s）
score=619
rank=3990
English_score=136.50
message="我高考%s分,%s名,英语%s分"%(score,rank,English_score)
print(message)
# %s占位字符串 %d占位整数 %f占位浮点数 %和f之间的.n代表保留n位小数
message="我高考%s分,%d名,英语%.2f分"%(score,rank,English_score)
print(message)
# 法2(快速格式化)不能控制精度
print(f"我高考{score}分,{rank}名,英语{English_score}分")