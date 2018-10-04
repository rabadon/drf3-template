import datetime
import time
from django.utils import timezone

def nanhunmae(db_datetime,with_before=False):
    # パラメータ
    # db_time(DateTime) = DBのタイムスタンプ
    # with_before(Boolean) = 語尾に"前"という文字を付与するか

    # データのタイムスタンプをUNIX時間に変換
    db_datetime_unix = int(time.mktime(db_datetime.timetuple()))

    # 現在のタイムスタンプをUNIX時間に変換
    now_datetime = timezone.now()
    now_datetime_unix = int(time.mktime(now_datetime.timetuple()))

    # UNIX時間の差を求める
    diff = now_datetime_unix - db_datetime_unix

    # 成形
    if diff < 60 : result = str(int(diff)) + '秒'
    elif diff < 3600 : result = str(int(diff/60)) + '分'
    elif diff < 86400 : result = str(int(diff/3600)) + '時間'
    else : result = str(int(diff/86400)) + '日'

    if with_before == True :
        result += '前'

    return result
