import datetime

class Patient:
    def __init__(self, name, birthdate, main_issue):
        self.name = name  # 患者姓名
        self.birthdate = birthdate  # 生日
        self.visit_date = datetime.date.today()  # 自動記錄今日到訪日期
        self.main_issue = main_issue  # 主要問題

    def display_info(self):
        """顯示患者資訊"""
        return f"姓名: {self.name}\n生日: {self.birthdate}\n到訪日期: {self.visit_date}\n主要問題: {self.main_issue}"

# 測試建立患者資料
patient1 = Patient("王小明", "1990-05-12", "肩膀疼痛")
print(patient1.display_info())