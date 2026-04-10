with open("D:/tools/python learning/test7/文件的读取测试.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(f"本行数据为：{line}") # 文件会自动关闭
import time
time.sleep(60)