import struct
from datetime import datetime

# กำหนดรูปแบบสำหรับข้อมูลไบนารี
# i (Customer ID), 100s (Customer Name), 50s (Car Model), 50s (Car Type),
# 15s (Rent Date), 15s (Return Date), f (Total Cost)
format_str = "i100s50s50s15s15sf"

# รายชื่อลูกค้าและรถยนต์ตัวอย่าง
customers = [
    ("Jane Fate", "Ford Mustang", "Coupe", "2024/10/05", "2024/10/14", 900.0),
    ("Bill Wate", "Audi A5", "Coupe", "2024/10/10", "2024/10/15", 250.0),
    ("Mark Davin", "Nissan Altima", "Sedan", "2024/10/05", "2024/10/12", 630.0),
    ("Tom Brady", "BMW X5", "SUV", "2024/10/08", "2024/10/12", 650.0),
    ("Sara Lane", "Tesla Model 3", "Sedan", "2024/10/07", "2024/10/12", 777.0),
    ("Eve Adams", "Mercedes GLA", "SUV", "2024/10/11", "2024/10/15", 518.0),
    ("Mike Jordan", "Chevy Camaro", "Coupe", "2024/10/15", "2024/10/22", 528.0),
    ("Rachel Zane", "Toyota Corolla", "Sedan", "2024/10/09", "2024/10/18", 844.0),
    ("Chris Pine", "Honda Civic", "Sedan", "2024/10/06", "2024/10/16", 901.0),
    ("Diane Rowe", "Mazda CX-5", "SUV", "2024/10/13", "2024/10/23", 992.0),
    ("John Doe", "Subaru Impreza", "Sedan", "2024/10/12", "2024/10/17", 334.0),
    ("Linda Lee", "Porsche 911", "Coupe", "2024/10/08", "2024/10/13", 979.0),
    ("George Martin", "Lexus RX", "SUV", "2024/10/14", "2024/10/18", 714.0),
    ("Emma Brown", "Volvo XC90", "SUV", "2024/10/10", "2024/10/17", 296.0),
    ("Alex Jones", "Hyundai Sonata", "Sedan", "2024/10/12", "2024/10/20", 592.0),
    ("Lisa Green", "Jaguar F-Type", "Coupe", "2024/10/11", "2024/10/17", 563.0),
    ("Mark Terry", "Ford F-150", "Truck", "2024/10/15", "2024/10/18", 972.0),
    ("Paul Walker", "Dodge Challenger", "Coupe", "2024/10/13", "2024/10/21", 530.0),
    ("James Smith", "Kia Sorento", "SUV", "2024/10/11", "2024/10/16", 809.0),
    ("Megan Fox", "Volkswagen Passat", "Sedan", "2024/10/10", "2024/10/19", 339.0),
    ("Nina Simone", "Ford Explorer", "SUV", "2024/10/12", "2024/10/18", 760.0)
]

# เขียนข้อมูล 20 records ลงในไฟล์
with open("Doc/datas_drive_now.bin", "ab") as file:
    for idx, (cus_name, car_model, car_type, date_rent, return_date, total_cost) in enumerate(customers, start=1):
        # แปลงวันที่ให้เป็น datetime
        date_rent_dt = datetime.strptime(date_rent, "%Y/%m/%d")
        return_date_dt = datetime.strptime(return_date, "%Y/%m/%d")
        
        # จัดเก็บข้อมูลเป็นไบนารี
        data = struct.pack(
            format_str,
            idx,
            cus_name.encode('utf-8'),
            car_model.encode('utf-8'),
            car_type.encode('utf-8'),
            date_rent_dt.strftime("%Y/%m/%d").encode('utf-8'),
            return_date_dt.strftime("%Y/%m/%d").encode('utf-8'),
            total_cost
        )
        
        # เขียนข้อมูลลงในไฟล์
        file.write(data)

print("สร้าง 20 records เสร็จสิ้นแล้วในไฟล์ datas_drive_now.bin.")
