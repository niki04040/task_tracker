import json
import datetime
from colorama import init,Fore,Back,Style
import tabulate

tasks = []
print("1.افزودن کار جدید😻\n"
          "2. نمایش لیست کارها📃\n"
          "3. حذف یک کار🤫\n"
          "4. علامت زدن به عنوان انجام شده😸\n"
          "5. خروج از برنامه🥺\n")


for choose in range(1000):
    choose = int(input("🙏لطفا از منو انتخاب کنید:"))
    if choose == 1:
            dict1 = {}
            dict1["work"] = input("کار جدید را اضافه کنید✍️")
            dict1["time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dict1["state"] = "انجام نشده"
            tasks.append(dict1)
    with open("tasks.json", "w") as f:
            json.dump(tasks, f)


    if choose == 2:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)

        tab = tabulate.tabulate(tasks, headers = "keys", tablefmt ="rounded_grid")
        print(tab)


    if choose == 3:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        del_work = int(input("برای حذف یک کار شماره کار مورد نظر را انتخاب کنید🔢"))
        del tasks[del_work]
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
        tab = tabulate.tabulate(tasks, headers = "keys", tablefmt = "rounded_grid")
        print(tab)

    if choose == 4:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        state_done = int(input("تغییر وضعیت به انجام شده✅\n شماره کار را وارد کنید"))
        tasks[state_done]["state"] = "انجام شده"
        tasks[state_done]["time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
        tab = tabulate.tabulate(tasks, headers = "keys", tablefmt = "rounded_grid")
        print(tab)

    if choose == 5:
        print("برنامه را تموم کن")
        break