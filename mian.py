import ntplib
from datetime import datetime
import os
# from time import ctime # 如需要原始时间格式需导入


ntp_servers = [
    "time.izatcloud.net",  # 高通中国 NTP服务器
    "time.gpsonextra.net",  # 高通中国 NTP服务器
    "time.google.com",  # Google NTP服务器
    "time.windows.com",  # 微软 NTP服务器
    "time.apple.com",  # 苹果 NTP服务器
    "time.nist.gov",  # 美国国家标准与技术研究所 NTP服务器
    "edu.ntp.org.cn",  # 中国教育网 NTP服务器
]


def get_ntp_time():

    for server in ntp_servers:
        try:
            # print(f"尝试连接NTP服务器: {server}")
            client = ntplib.NTPClient()
            response = client.request(server, timeout=1)

            # 获取NTP时间戳并转换为datetime对象
            ntp_time = datetime.fromtimestamp(response.tx_time)

            # 格式化为所需的字符串格式
            date_str = ntp_time.strftime("%Y/%m/%d")  # 格式: 2025/07/03
            time_str = ntp_time.strftime("%H:%M:%S.%f")[:-4]  # 格式: 17:26:58.04

            return {
                "date": date_str,
                "time": time_str,
                # "raw_time": ctime(response.tx_time),  # 保留原始格式
            }

        except ntplib.NTPException:
            print(f"服务器 {server} NTP异常")
        except Exception:
            print(f"连接服务器 {server} 失败:")

    # 所有服务器都失败时返回本地时间
    local_time = datetime.now()
    return {
        "date": local_time.strftime("%Y/%m/%d"),
        "time": local_time.strftime("%H:%M:%S.%f")[:-4],
        # "raw_time": ctime(),
    }


if __name__ == "__main__":
    # 获取时间结果
    time_result = get_ntp_time()

    # 调用cmd命令更新系统时间
    text = os.system(f"date {time_result['date']} && time {time_result['time']}")
    if text == 0:
        print("系统时间更新成功")
    else:
        print("系统时间更新失败，请使用管理员权限运行")

    # 输出格式化后的时间
    print(f"日期: {time_result['date']}")
    print(f"时间: {time_result['time']}")
    # print(f"原始格式: {time_result['raw_time']}")
