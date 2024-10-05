import datetime
import struct
import extension.extensions_drive_now as ex
from prettytable import PrettyTable

def search_data(menu_number):
    if menu_number == 1:
        try:
            keep_going = True
            while keep_going:
                print("\t\t\tรายการเมนูค้นหาข้อมูล")
                print("---------------------------------------------------------")
                print("1. แสดงข้อมูลทั้งหมด")
                print("2. ค้นหาเฉพาะ")
                print("3. ออกจากเมนูการค้นหาข้อมูล")
                print("---------------------------------------------------------")
                search_data_menu = int(input("กรุณาเลือกรายการ : ")) 
                
                if search_data_menu == 1:
                    try:
                        with open("Doc/datas_drive_now.bin", "rb") as file:
                            records = []
                            record_size = struct.calcsize("i100s50s50s15s15sf")
                            
                            while True:
                                record_data = file.read(record_size)
                                if not record_data:
                                    print("ไม่พบข้อมูล")
                                    break
                                record = struct.unpack("i100s50s50s15s15sf", record_data)
                                records.append(record)

                            print("ข้อมูลทั้งหมดที่เช่ารถ:")
                            table = PrettyTable()
                            table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]
                            for record in records:
                                table.add_row([
                                    record[0],
                                    record[1].decode().strip(),
                                    record[2].decode().strip(),
                                    record[3].decode().strip(),
                                    record[4].decode().strip(),
                                    record[5].decode().strip(),
                                    record[6]
                                ])
                            print("ข้อมูลทั้งหมดที่เช่ารถ:")
                            print(table)
                    except Exception as e:
                        print(f"เกิดข้อผิดพลาดในการอ่านข้อมูล: {e}")
                        return None
                
                elif search_data_menu == 2:
                    try:
                        keep_going2 = True
                        while keep_going2:
                            print("\t\t\tรายการเมนูค้นหาข้อมูลเฉพาะ")
                            print("---------------------------------------------------------")
                            print("1. No.")
                            print("2. customer name")
                            print("3. car Model")
                            print("4. car type")
                            # print("5. rent date")
                            # print("6. return date")
                            print("7. ออกจากเมนูการค้นหาข้อมูล")
                            print("---------------------------------------------------------")
                            search_data_menu = int(input("กรุณาเลือกรายการ : ")) 
                            if search_data_menu == 1:
                                search_id = int(input("กรุณากรอกลำดับที่ที่ต้องการค้นหา: "))
                                try:
                                    with open("Doc/datas_drive_now.bin", "rb") as file:
                                        record_size = struct.calcsize("i100s50s50s15s15sf")
                                        found = False

                                        table = PrettyTable()
                                        table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]

                                        while True:
                                            record_data = file.read(record_size)
                                            if not record_data:
                                                break 
                                            
                                            record = struct.unpack("i100s50s50s15s15sf", record_data)
                                            if record[0] == search_id:
                                                found = True
                                                table.add_row([
                                                    record[0],
                                                    record[1].decode().strip(),
                                                    record[2].decode().strip(),
                                                    record[3].decode().strip(),
                                                    record[4].decode().strip(),
                                                    record[5].decode().strip(),
                                                    record[6]
                                                ])
                                                break
                                        if found:
                                            print("ข้อมูลทั้งหมดที่ของผู้เเช่ารถ:")
                                            print(table)
                                        else:
                                            print(f"ไม่พบข้อมูล No : {search_id}")

                                except Exception as e:
                                    print(f"เกิดข้อผิดพลาดในการค้นหาข้อมูล: {e}")
                            elif search_data_menu == 2:
                                search_name = input("กรุณากรอกชื่อที่ต้องการค้นหา: ")
                                try:
                                    with open("Doc/datas_drive_now.bin", "rb") as file:
                                        record_size = struct.calcsize("i100s50s50s15s15sf")
                                        found = False

                                        table = PrettyTable()
                                        table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]

                                        while True:
                                            record_data = file.read(record_size)
                                            if not record_data:
                                                break
                                            
                                            record = struct.unpack("i100s50s50s15s15sf", record_data)
                                            if search_name.lower() in record[1].decode().lower():
                                                found = True
                                                table.add_row([
                                                    record[0],
                                                    record[1].decode().strip(),
                                                    record[2].decode().strip(),
                                                    record[3].decode().strip(),
                                                    record[4].decode().strip(),
                                                    record[5].decode().strip(),
                                                    record[6]
                                                ])
                                        
                                        if found:
                                            print("ข้อมูลทั้งหมดที่ของผู้เช่ารถ:")
                                            print(table)
                                        else:
                                            print(f"ไม่พบข้อมูล Customer Name: {search_name}")

                                except Exception as e:
                                    print(f"เกิดข้อผิดพลาดในการค้นหาข้อมูล: {e}")
                            elif search_data_menu == 3:
                                search_model = input("กรุณากรอกรถรุ่นที่ต้องการค้นหา: ")
                                try:
                                    with open("Doc/datas_drive_now.bin", "rb") as file:
                                        record_size = struct.calcsize("i100s50s50s15s15sf")
                                        found = False
                                        
                                        table = PrettyTable()
                                        table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]

                                        while True:
                                            record_data = file.read(record_size)
                                            if not record_data:
                                                break
                                            
                                            record = struct.unpack("i100s50s50s15s15sf", record_data)
                                            if search_model.lower() in record[2].decode().lower():
                                                found = True
                                                table.add_row([
                                                    record[0],
                                                    record[1].decode().strip(),
                                                    record[2].decode().strip(),
                                                    record[3].decode().strip(),
                                                    record[4].decode().strip(),
                                                    record[5].decode().strip(),
                                                    record[6]
                                                ])
                                        
                                        if found:
                                            print("ข้อมูลทั้งหมดที่ของผู้เช่ารถ:")
                                            print(table)
                                        else:
                                            print(f"ไม่พบข้อมูล Car Moderl: {search_model}")

                                except Exception as e:
                                    print(f"เกิดข้อผิดพลาดในการค้นหาข้อมูล: {e}")
                            elif search_data_menu == 4:
                                search_type = input("กรุณากรอกประเภทของรถที่ต้องการค้นหา: ")
                                try:
                                    with open("Doc/datas_drive_now.bin", "rb") as file:
                                        record_size = struct.calcsize("i100s50s50s15s15sf")
                                        found = False
                                        
                                        table = PrettyTable()
                                        table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]

                                        while True:
                                            record_data = file.read(record_size)
                                            if not record_data:
                                                break
                                            
                                            record = struct.unpack("i100s50s50s15s15sf", record_data)
                                            if search_type.lower() in record[3].decode().lower():
                                                found = True
                                                table.add_row([
                                                    record[0],
                                                    record[1].decode().strip(),
                                                    record[2].decode().strip(),
                                                    record[3].decode().strip(),
                                                    record[4].decode().strip(),
                                                    record[5].decode().strip(),
                                                    record[6]
                                                ])
                                        
                                        if found:
                                            print("ข้อมูลทั้งหมดที่ของผู้เช่ารถ:")
                                            print(table)
                                        else:
                                            print(f"ไม่พบข้อมูล Car Type: {search_type}")

                                except Exception as e:
                                    print(f"เกิดข้อผิดพลาดในการค้นหาข้อมูล: {e}")        
                            # elif search_data_menu == 5:
                            #     search_rent_date = input("กรุณากรอกวันที่เช่าที่ต้องการค้นหา (YYYY/MM/DD): ")
                            #     try:
                            #         with open("Doc/datas_drive_now.bin", "rb") as file:
                            #             record_size = struct.calcsize("i100s50s50s15s15sf")
                            #             found = False

                            #             table = PrettyTable()
                            #             table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]

                            #             while True:
                            #                 record_data = file.read(record_size)
                            #                 if not record_data:
                            #                     break
                                            
                            #                 record = struct.unpack("i100s50s50s15s15sf", record_data)
                            #                 if search_rent_date == record[4].decode().strip():
                            #                     found = True
                            #                     table.add_row([
                            #                         record[0],
                            #                         record[1].decode().strip(),
                            #                         record[2].decode().strip(),
                            #                         record[3].decode().strip(),
                            #                         record[4].decode().strip(),
                            #                         record[5].decode().strip(),
                            #                         record[6]
                            #                     ])
                                        
                            #             if found:
                            #                 print("ข้อมูลทั้งหมดที่ของผู้เช่ารถ:")
                            #                 print(table)
                            #             else:
                            #                 print(f"ไม่พบข้อมูล Rent Date: {search_rent_date}")

                            #     except Exception as e:
                            #         print(f"เกิดข้อผิดพลาดในการค้นหาข้อมูล: {e}")
                            # elif search_data_menu == 6:
                                search_return_date = input("กรุณากรอกวันที่คืนที่ต้องการค้นหา (YYYY/MM/DD): ")
                                try:
                                    with open("Doc/datas_drive_now.bin", "rb") as file:
                                        record_size = struct.calcsize("i100s50s50s15s15sf")
                                        found = False

                                        table = PrettyTable()
                                        table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]

                                        while True:
                                            record_data = file.read(record_size)
                                            if not record_data:
                                                break
                                            
                                            record = struct.unpack("i100s50s50s15s15sf", record_data)
                                            if search_return_date == record[5].decode().strip():
                                                found = True
                                                table.add_row([
                                                    record[0],
                                                    record[1].decode().strip(),
                                                    record[2].decode().strip(),
                                                    record[3].decode().strip(),
                                                    record[4].decode().strip(),
                                                    record[5].decode().strip(),
                                                    record[6]
                                                ])
                                        
                                        if found:
                                            print("ข้อมูลทั้งหมดที่ของผู้เช่ารถ:")
                                            print(table)
                                        else:
                                            print(f"ไม่พบข้อมูล Return Date: {search_return_date}")

                                except Exception as e:
                                    print(f"เกิดข้อผิดพลาดในการค้นหาข้อมูล: {e}")
                            elif search_data_menu == 7:
                                print("ออกจากเมนูการค้นหาข้อมูลเฉพาะ")
                                keep_going2 = False
                            else:
                                print("เมนูที่เลือกไม่ถูกต้อง")
                    except Exception as e:
                        print(f"เกิดข้อผิดพลาด: {e}")
                elif search_data_menu == 3:
                    print("ออกจากเมนูการค้นหาข้อมูล")
                    keep_going = False
        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {e}") 

def rent_car(menu_number):
    detail_car = {
        "Nissan Altima": "Sedan",
        "Ford Mustang": "Coupe",
        "Honda CR-V": "SUV",
        "Toyota Corolla": "Sedan",
        "Audi A5": "Coupe",
        "Hyundai Sonata": "Sedan"
    }
    if menu_number == 2:
        try:
            keep_going = True
            while keep_going:
                print("\t\t\tรายการเมนูการเช่ารถ")
                print("---------------------------------------------------------")
                print("1. แสดงรายการรถที่มีให้เช่า")
                print("2. ทำรายการเช่ารถ")
                print("3. ออกจากเมนูการเช่ารถ")
                print("---------------------------------------------------------")
                rent_car_menu = int(input("กรุณาเลือกรายการ : "))
                
                if rent_car_menu == 1:
                    
                    print("รายการรถที่มีให้เช่า:")
                    for numer_id, (key, value) in enumerate(detail_car.items(), start=1):
                        print(f"{numer_id}. รถรุ่น: {key}, ประเภทรถ: {value}")
                        
                elif rent_car_menu == 2:
                    
                    date_rent = datetime.datetime.now()
                    print("...กรอกข้อมูลการเช่า...")
                    id_cus = ex.get_next_id()
                    print(f"ลำดับที่ (ID): {id_cus}")
                    cus_name = input("ชื่อ-นามสกุล : ")
                    car_model = input("รถรุ่น : ")
                    
                    if car_model not in detail_car:
                        print("รถรุ่นที่เลือกไม่มีในรายการ โปรดลองอีกครั้ง")
                        continue
                    
                    car_type = detail_car[car_model]
                    print(f"ประเภทรถ: {car_type}")  
                    return_date_input = int(input("จำนวนวันที่เช่า : "))
                    return_date = date_rent + datetime.timedelta(days=return_date_input)
                    cost_rent = float(input("ค่าเช่าวันละ : "))
                    total_cost_rent = cost_rent * return_date_input
                    
                    
                    with open("Doc/datas_drive_now.bin", "ab") as file:
                        data = struct.pack("i100s50s50s15s15sf", id_cus, cus_name.encode(), car_model.encode(), car_type.encode(), date_rent.strftime("%Y/%m/%d").encode(), return_date.strftime("%Y/%m/%d").encode(), total_cost_rent)
                        file.write(data)
                        
                    return {
                        "ลำดับที่": id_cus,
                        "ชื่อ-นามสกุล": cus_name,
                        "รถรุ่น": car_model,
                        "ประเภทรถ": car_type,
                        "วันที่เช่า": date_rent.strftime("%Y/%m/%d"),
                        "จำนวนวันที่เช่า": return_date_input,
                        "จำนวนเงิน": total_cost_rent,
                        "วันที่คืนรถ": return_date.strftime("%Y/%m/%d")  
                    }
                elif rent_car_menu == 3:
                    print("ออกจากเมนูการเช่ารถ")
                    keep_going = False
                else:
                    print("เมนูที่เลือกไม่ถูกต้อง")
        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {e}")
                   
import struct
from prettytable import PrettyTable

def edit_data_customer(menu_number):
    if menu_number == 3:
        try:
            keep_going = True
            while keep_going:
                print("\t\t\tรายการเมนูการเช่ารถ")
                print("---------------------------------------------------------")
                print("1. แสดงข้อมูลทั้งหมด")
                print("2. แก้ไขข้อมูลผู้เช่ารถ")
                print("3. ออกจากเมนูการเช่ารถ")
                print("---------------------------------------------------------")
                
                edit_car_menu = int(input("กรุณาเลือกรายการ : "))
                
                if edit_car_menu == 1:
                    try:
                        with open("Doc/datas_drive_now.bin", "rb") as file:
                            record_size = struct.calcsize("i100s50s50s15s15sf")
                            table = PrettyTable()
                            table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]
                            
                            while True:
                                record_data = file.read(record_size)
                                if not record_data:
                                    break 
                                
                                record = struct.unpack("i100s50s50s15s15sf", record_data)
                                table.add_row([
                                    record[0],
                                    record[1].decode().strip(),
                                    record[2].decode().strip(),
                                    record[3].decode().strip(),
                                    record[4].decode().strip(),
                                    record[5].decode().strip(),
                                    record[6]
                                ])
                            
                            print("ข้อมูลทั้งหมดของผู้เช่ารถทั้งหมด:")
                            print(table)

                    except Exception as e:
                        print(f"เกิดข้อผิดพลาดในการอ่านข้อมูล: {e}")
                
                elif edit_car_menu == 2:
                    edit_id = int(input("กรุณากรอกลำดับที่ผู้เช่ารถที่ต้องการแก้ไข: "))
                    records = []

                    try:
                        with open("Doc/datas_drive_now.bin", "rb") as file:
                            record_size = struct.calcsize("i100s50s50s15s15sf")
                            
                            while True:
                                record_data = file.read(record_size)
                                if not record_data:
                                    break
                                
                                record = struct.unpack("i100s50s50s15s15sf", record_data)
                                records.append(record)
                                if record[0] == edit_id:
                                    print("ข้อมูลที่พบ:")
                                    print(f"ชื่อ-นามสกุล: {record[1].decode().strip()}")
                                    
                                    new_name = input("กรุณากรอกชื่อใหม่: ").encode('utf-8')
                                    new_model = input("กรุณากรอกแบบรถใหม่: ")
                                    
                                    detail_car = {
                                        "Nissan Altima": "Sedan",
                                        "Ford Mustang": "Coupe",
                                        "Honda CR-V": "SUV",
                                        "Toyota Corolla": "Sedan",
                                        "Audi A5": "Coupe",
                                        "Hyundai Sonata": "Sedan"
                                    }
                                    
                                    if new_model not in detail_car:
                                        print("รถรุ่นที่เลือกไม่มีในรายการ โปรดลองอีกครั้ง")
                                        continue
            
                                    car_type = detail_car[new_model]
                                    print(f"ประเภทรถ: {car_type}") 
                                    
                                    new_type = car_type.encode('utf-8')  # ใช้ car_type ที่ได้จาก detail_car
                                    new_rent_date = input("กรุณากรอกวันที่เช่าใหม่ (YYYY/MM/DD): ").encode('utf-8')
                                    new_return_date = input("กรุณากรอกวันที่คืนใหม่ (YYYY/MM/DD): ").encode('utf-8')
                                    new_cost = float(input("กรุณากรอกจำนวนเงินใหม่: "))
                                    
                                    updated_record = (
                                        record[0], 
                                        new_name.ljust(100), 
                                        new_model.ljust(50).encode('utf-8'),  # แปลงเป็น bytes
                                        new_type.ljust(50), 
                                        new_rent_date.ljust(15), 
                                        new_return_date.ljust(15), 
                                        new_cost
                                    )
                                    
                                    records[-1] = updated_record  # แก้ไขข้อมูลในรายการ
                                    break  # ออกจากลูปถ้าพบข้อมูล
                            
                            else:
                                print("ไม่พบข้อมูลสำหรับ ID ที่ระบุ")

                    except FileNotFoundError:
                        print("ไม่พบไฟล์ข้อมูล โปรดตรวจสอบเส้นทางไฟล์")
                    except Exception as e:
                        print(f"เกิดข้อผิดพลาดในการอ่านข้อมูล: {e}")

                    # การบันทึกข้อมูล
                    try:
                        with open("Doc/datas_drive_now.bin", "wb") as file:
                            for rec in records:
                                file.write(struct.pack("i100s50s50s15s15sf", *rec))
                            print("ข้อมูลได้รับการอัปเดตเรียบร้อยแล้ว")
                    
                    except Exception as e:
                        print(f"เกิดข้อผิดพลาดในการบันทึกข้อมูล: {e}")
                
                elif edit_car_menu == 3:
                    print("ออกจากเมนูการเช่ารถ")
                    keep_going = False

                else:
                    print("เมนูที่เลือกไม่ถูกต้อง")

        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {e}")

def delet_data(menu_number):
    if menu_number == 4:
        print("ลบข้อมูล...")
        
def report_data(menu_number):
    if menu_number == 5:
        print("รายงานข้อมูล...")
