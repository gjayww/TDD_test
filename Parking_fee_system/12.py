import random
import datetime
import unittest
import sys
from unittest.mock import patch

def calculate_parking_fee(date, time):
    # 判斷是否為假日

    if date.weekday() >= 5:
        unit = 20
        max_fee = 420  # 假日最高收費金額
    else:
        unit = 15
        max_fee = 300  # 平日最高收費金額

    # 計算停車時間的區間數量
    several = time // 30

    # 計算停車費用
    fee = unit * several

    # 若超過最高收費金額，將費用調整為最高收費金額
    if fee > max_fee:
        fee = max_fee

    return fee

Time = random.randint(1, 1440)
H = Time // 60  # 分鐘數轉換為小時數
M = Time % 60  # 取得剩餘的分鐘數


# 取得當前日期
today= datetime.date.today()
license_plate = input("請輸入車牌號碼：")

# 檢查車牌號碼長度
if len(license_plate) > 7:
    print("輸入錯誤！車牌號碼長度超過7位數")
else:
    # 計算停車費用
    print("停車時間為 " + str(H) + " 小時 " + str(M) + " 分鐘")
    money = calculate_parking_fee(today, Time)
    print("停車費用為:", money)
    confirm = input("請確認付款(y/n)：")
    if confirm.lower() != 'y':
        print("取消付款，請再進行一次")
        exit()
        
class PaymentTestCase(unittest.TestCase):
    def setUp(self):
        self.money = money  # 初始化停車費用

    def insert_coin(self, coin):
        valid_coins = [50, 10, 5]
        if coin in valid_coins and self.money != 0:
            while self.money > 0:
                try:
                    amount = input("請輸入金額（或按下 'Q' 取消付款）：")
                    if amount == 'Q':
                        raise KeyboardInterrupt
                    amount = int(amount)
                    if amount in valid_coins:
                        if amount <= self.money:
                            self.money -= amount
                            print("投入硬幣：", amount)
                            print("剩餘金額：", self.money, "元")
                        else:
                            print("金額不足，請重新輸入！")
                    else:
                        print("無效的硬幣！")
                except ValueError:
                    print("無效的輸入！")
                except KeyboardInterrupt:
                    print("取消付款！")
                    return

            print("付款成功，列印單據中")
        elif self.money == 0:
            print("付款成功，列印單據中")
        else:
            print("無效的硬幣！")

    def test_insert_valid_coin(self):
        coin = 50
        self.insert_coin(coin)
        self.assertEqual(self.money, self.money)  # 檢查金額是否不變

    def test_insert_one_dollar_coin(self):
        coin = 1
        self.insert_coin(coin)
        self.assertEqual(self.money, money)  # 檢查金額是否不變





class HolidayTestCase(unittest.TestCase):
    def test_weekend_holiday(self):
        # 測試週末是否為假日
        date = datetime.date(2023, 6, 4)  # 週日
        self.assertEqual(calculate_parking_fee(date, 60), 40)  # 停車1小時，期望費用為20

    def test_weekday_not_holiday(self):
        # 測試工作日是否不是假日
        date = datetime.date(2023, 6, 6)  # 週二
        self.assertEqual(calculate_parking_fee(date, 60), 30)  # 停車1小時，期望費用為15

class ParkingFeeTestCase(unittest.TestCase):
    def test_weekday_over_10_hours(self):
        date = datetime.date(2023, 6, 7)
        time = 10 * 60 + 1  # 超過10小時1分鐘
        expected_fee = 300
        actual_fee = calculate_parking_fee(date, time)
        self.assertEqual(actual_fee, expected_fee)

    def test_weekend_over_10_hours(self):
        date = datetime.date(2023, 6, 10)
        time = 10.5 * 60 + 1  # 超過10.5小時1分鐘
        expected_fee = 420
        actual_fee = calculate_parking_fee(date, time)
        self.assertEqual(actual_fee, expected_fee)

    def test_parking_time_less_than_30_minutes(self):
        date = datetime.date(2023, 6, 7)
        time = 15  # 停车15分
        expected_fee = 0
        actual_fee = calculate_parking_fee(date, time)
        self.assertEqual(actual_fee, expected_fee)

    def test_maximum_fee(self):
        date = datetime.date(2023, 6, 7)
        time = 12 * 60  # 停車12小时
        expected_fee = 300  # 平日最高收費
        actual_fee = calculate_parking_fee(date, time)
        self.assertEqual(actual_fee, expected_fee)



if __name__ == '__main__':
    unittest.main()