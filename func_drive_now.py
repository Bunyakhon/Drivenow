import datetime  # นำเข้าโมดูล datetime ซึ่งเป็นเครื่องมือที่ใช้สำหรับการจัดการและรูปแบบของวันเวลา เช่น การดึงวันเวลาปัจจุบัน, การคำนวณวันเวลา หรือการฟอร์แมตวันที่และเวลาตามที่ต้องการ
import struct  # นำเข้าโมดูล struct ซึ่งใช้ในการทำงานกับข้อมูลแบบไบนารี เช่น การแปลงข้อมูลระหว่างรูปแบบ Python และข้อมูลแบบ C-struct หรือการอ่าน/เขียนข้อมูลจากไฟล์ในรูปแบบไบนารี
import extension.extensions_drive_now as ex  # นำเข้าโมดูล extensions_drive_now จากโฟลเดอร์ extension โดยตั้งชื่อย่อว่า 'ex' ซึ่งเป็นโมดูลที่น่าจะมีฟังก์ชันเพิ่มเติมที่เกี่ยวข้องกับการทำงานของระบบเช่ารถ (Drive Now)
from prettytable import PrettyTable  # นำเข้า PrettyTable จากโมดูล prettytable ซึ่งช่วยในการสร้างตารางข้อมูลในรูปแบบ ASCII table เพื่อให้การแสดงผลข้อมูลมีความชัดเจนและอ่านง่ายมากขึ้น

def search_data(menu_number):
    # ตรวจสอบว่า menu_number เป็น 1 หรือไม่
    if menu_number == 1:
        try:
            keep_going = True  # ตัวแปรเพื่อควบคุมลูปหลัก
            while keep_going:
                print("\t\t\tรายการเมนูค้นหาข้อมูล")
                print("-"*100)
                print("1. แสดงข้อมูลทั้งหมด")
                print("2. ค้นหาเฉพาะ")
                print("3. ออกจากเมนูการค้นหาข้อมูล")
                print("-"*100)
                search_data_menu = int(input("กรุณาเลือกรายการ : ")) 
                
                # ถ้าผู้ใช้เลือกแสดงข้อมูลทั้งหมด
                if search_data_menu == 1:
                    try:
                        # เปิดไฟล์สำหรับอ่านข้อมูล
                        with open("Doc/datas_drive_now.bin", "rb") as file:
                            records = []  # รายการเก็บข้อมูลที่อ่านจากไฟล์
                            record_size = struct.calcsize("i100s50s50s15s15sf")  # ขนาดของข้อมูลแต่ละระเบียน
                            
                            while True:
                                record_data = file.read(record_size)  # อ่านข้อมูลจากไฟล์
                                if not record_data:  # ถ้าไม่มีข้อมูล
                                    break
                                record = struct.unpack("i100s50s50s15s15sf", record_data)  # แยกข้อมูลออกเป็นรูปแบบที่กำหนด
                                records.append(record)  # เก็บข้อมูลในรายการ

                            # สร้างตารางเพื่อแสดงข้อมูล
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
                                    f"{record[6]:.2f}"
                                ])
                            print("ข้อมูลทั้งหมดที่เช่ารถ:")
                            print(table)
                    except Exception as e:
                        print(f"เกิดข้อผิดพลาดในการอ่านข้อมูล: {e}")
                        return None
                
                # ถ้าผู้ใช้เลือกค้นหาเฉพาะ
                elif search_data_menu == 2:
                    try:
                        keep_going2 = True  # ตัวแปรเพื่อควบคุมลูปค้นหา
                        while keep_going2:
                            print("\t\t\tรายการเมนูค้นหาข้อมูลเฉพาะ")
                            print("-"*100)
                            print("1. No.")
                            print("2. customer name")
                            print("3. car Model")
                            print("4. car type")
                            print("7. ออกจากเมนูการค้นหาข้อมูล")
                            print("-"*100)
                            search_data_menu = int(input("กรุณาเลือกรายการ : ")) 
                            
                            # ค้นหาตามลำดับที่
                            if search_data_menu == 1:
                                search_id = int(input("กรุณากรอกลำดับที่ที่ต้องการค้นหา: "))
                                try:
                                    with open("Doc/datas_drive_now.bin", "rb") as file:
                                        record_size = struct.calcsize("i100s50s50s15s15sf")
                                        found = False  # ตัวแปรเพื่อเช็คว่าพบข้อมูลหรือไม่

                                        # สร้างตารางเพื่อแสดงข้อมูล
                                        table = PrettyTable()
                                        table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]

                                        while True:
                                            record_data = file.read(record_size)  # อ่านข้อมูลจากไฟล์
                                            if not record_data:
                                                break 
                                            
                                            record = struct.unpack("i100s50s50s15s15sf", record_data)  # แยกข้อมูลออก
                                            if record[0] == search_id:  # เช็คว่าลำดับที่ตรงกับที่ค้นหาหรือไม่
                                                found = True
                                                table.add_row([
                                                    record[0],
                                                    record[1].decode().strip(),
                                                    record[2].decode().strip(),
                                                    record[3].decode().strip(),
                                                    record[4].decode().strip(),
                                                    record[5].decode().strip(),
                                                    f"{record[6]:.2f}"
                                                ])
                                                break  # ออกจากลูปเมื่อพบข้อมูล
                                        if found:
                                            print("ข้อมูลทั้งหมดที่ของผู้เช่ารถ:")
                                            print(table)
                                        else:
                                            print(f"ไม่พบข้อมูล No : {search_id}")

                                except Exception as e:
                                    print(f"เกิดข้อผิดพลาดในการค้นหาข้อมูล: {e}")
                            # ค้นหาตามชื่อ
                            elif search_data_menu == 2:
                                search_name = input("กรุณากรอกชื่อที่ต้องการค้นหา: ")
                                try:
                                    with open("Doc/datas_drive_now.bin", "rb") as file:
                                        record_size = struct.calcsize("i100s50s50s15s15sf")
                                        found = False

                                        # สร้างตารางเพื่อแสดงข้อมูล
                                        table = PrettyTable()
                                        table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]

                                        while True:
                                            record_data = file.read(record_size)  # อ่านข้อมูลจากไฟล์
                                            if not record_data:
                                                break
                                            
                                            record = struct.unpack("i100s50s50s15s15sf", record_data)  # แยกข้อมูลออก
                                            if search_name.lower() in record[1].decode().lower():  # เช็คชื่อ
                                                found = True
                                                table.add_row([
                                                    record[0],
                                                    record[1].decode().strip(),
                                                    record[2].decode().strip(),
                                                    record[3].decode().strip(),
                                                    record[4].decode().strip(),
                                                    record[5].decode().strip(),
                                                    f"{record[6]:.2f}"
                                                ])
                                        
                                        if found:
                                            print("ข้อมูลทั้งหมดที่ของผู้เช่ารถ:")
                                            print(table)
                                        else:
                                            print(f"ไม่พบข้อมูล Customer Name: {search_name}")

                                except Exception as e:
                                    print(f"เกิดข้อผิดพลาดในการค้นหาข้อมูล: {e}")
                            
                            # ค้นหาตามรุ่นรถ
                            elif search_data_menu == 3:
                                search_model = input("กรุณากรอกรถรุ่นที่ต้องการค้นหา: ")
                                try:
                                    with open("Doc/datas_drive_now.bin", "rb") as file:
                                        record_size = struct.calcsize("i100s50s50s15s15sf")
                                        found = False
                                        
                                        # สร้างตารางเพื่อแสดงข้อมูล
                                        table = PrettyTable()
                                        table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]

                                        while True:
                                            record_data = file.read(record_size)  # อ่านข้อมูลจากไฟล์
                                            if not record_data:
                                                break
                                            
                                            record = struct.unpack("i100s50s50s15s15sf", record_data)  # แยกข้อมูลออก
                                            if search_model.lower() in record[2].decode().lower():  # เช็ครุ่นรถ
                                                found = True
                                                table.add_row([
                                                    record[0],
                                                    record[1].decode().strip(),
                                                    record[2].decode().strip(),
                                                    record[3].decode().strip(),
                                                    record[4].decode().strip(),
                                                    record[5].decode().strip(),
                                                    f"{record[6]:.2f}"
                                                ])
                                        
                                        if found:
                                            print("ข้อมูลทั้งหมดที่ของผู้เช่ารถ:")
                                            print(table)
                                        else:
                                            print(f"ไม่พบข้อมูล Car Model: {search_model}")

                                except Exception as e:
                                    print(f"เกิดข้อผิดพลาดในการค้นหาข้อมูล: {e}")
                            
                            # ค้นหาตามประเภทของรถ
                            elif search_data_menu == 4:
                                search_type = input("กรุณากรอกประเภทของรถที่ต้องการค้นหา: ")
                                try:
                                    with open("Doc/datas_drive_now.bin", "rb") as file:
                                        record_size = struct.calcsize("i100s50s50s15s15sf")
                                        found = False
                                        
                                        # สร้างตารางเพื่อแสดงข้อมูล
                                        table = PrettyTable()
                                        table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]

                                        while True:
                                            record_data = file.read(record_size)  # อ่านข้อมูลจากไฟล์
                                            if not record_data:
                                                break
                                            
                                            record = struct.unpack("i100s50s50s15s15sf", record_data)  # แยกข้อมูลออก
                                            if search_type.lower() in record[3].decode().lower():  # เช็คประเภทของรถ
                                                found = True
                                                table.add_row([
                                                    record[0],
                                                    record[1].decode().strip(),
                                                    record[2].decode().strip(),
                                                    record[3].decode().strip(),
                                                    record[4].decode().strip(),
                                                    record[5].decode().strip(),
                                                    f"{record[6]:.2f}"
                                                ])
                                        
                                        if found:
                                            print("ข้อมูลทั้งหมดที่ของผู้เช่ารถ:")
                                            print(table)
                                        else:
                                            print(f"ไม่พบข้อมูล Car Type: {search_type}")

                                except Exception as e:
                                    print(f"เกิดข้อผิดพลาดในการค้นหาข้อมูล: {e}")

                            # ออกจากเมนูค้นหา
                            elif search_data_menu == 7:
                                keep_going2 = False  # ออกจากลูปค้นหา
                            else:
                                print("กรุณาเลือกรายการที่ถูกต้อง")
                    except Exception as e:
                        print(f"เกิดข้อผิดพลาดในการค้นหาข้อมูล: {e}")    
                # ออกจากเมนูค้นหาข้อมูล
                elif search_data_menu == 3:
                    keep_going = False  # ออกจากลูปหลัก
                else:
                    print("กรุณาเลือกรายการที่ถูกต้อง")
        
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการค้นหาข้อมูล: {e}")



def rent_car(menu_number):  # ฟังก์ชันนี้ใช้สำหรับการทำรายการเช่ารถ โดยจะมีเมนูให้ผู้ใช้เลือกแสดงรายการรถหรือทำการเช่ารถ
    detail_car = {  # ดิกชันนารีเก็บข้อมูลรุ่นรถและประเภทรถ
                "Nissan Altima": "Sedan",
                "Ford Mustang": "Coupe",
                "Honda CR-V": "SUV",
                "Toyota Corolla": "Sedan",
                "Audi A5": "Coupe",
                "Hyundai Sonata": "Sedan",
                "BMW X5": "SUV",
                "Tesla Model 3": "Sedan",
                "Mercedes GLA": "SUV",
                "Chevy Camaro": "Coupe",
                "Mazda CX-5": "SUV",
                "Subaru Impreza": "Sedan",
                "Porsche 911": "Coupe",
                "Lexus RX": "SUV",
                "Volvo XC90": "SUV",
                "Jaguar F-Type": "Coupe",
                "Ford F-150": "Truck",
                "Dodge Challenger": "Coupe",
                "Kia Sorento": "SUV",
                "Volkswagen Passat": "Sedan",
                "Ford Explorer": "SUV"
            }
    if menu_number == 2:  # ถ้าหมายเลขเมนูที่ป้อนคือ 2 (เมนูเช่ารถ)
        try:
            keep_going = True  # สถานะควบคุมลูปเมนู
            while keep_going:  # ลูปนี้จะแสดงเมนูเช่ารถจนกว่าจะเลือกออก
                print("\t\t\tรายการเมนูการเช่ารถ")  # แสดงหัวข้อเมนูการเช่ารถ
                print("-"*100)  # เส้นแบ่งสำหรับความสวยงาม
                print("1. แสดงรายการรถที่มีให้เช่า")  # ตัวเลือกที่ 1: แสดงรายการรถ
                print("2. ทำรายการเช่ารถ")  # ตัวเลือกที่ 2: ทำรายการเช่ารถ
                print("3. ออกจากเมนูการเช่ารถ")  # ตัวเลือกที่ 3: ออกจากเมนูการเช่ารถ
                print("-"*100)  # เส้นแบ่งเพิ่มเติม
                rent_car_menu = int(input("กรุณาเลือกรายการ : "))  # รับหมายเลขเมนูจากผู้ใช้
                
                if rent_car_menu == 1:  # ถ้าผู้ใช้เลือกตัวเลือกที่ 1 (แสดงรายการรถที่มีให้เช่า)
                    print("รายการรถที่มีให้เช่า:")  # แสดงข้อความหัวข้อ
                    for numer_id, (key, value) in enumerate(detail_car.items(), start=1):  # วนลูปแสดงรายการรถและประเภทรถ
                        print(f"{numer_id}. รถรุ่น: {key}, ประเภทรถ: {value}")  # แสดงลำดับ, รุ่นรถ และประเภทรถ
                        
                elif rent_car_menu == 2:  # ถ้าผู้ใช้เลือกตัวเลือกที่ 2 (ทำรายการเช่ารถ)
                    date_rent = datetime.datetime.now()  # เก็บวันที่และเวลาปัจจุบันเป็นวันที่เริ่มเช่า
                    print("...กรอกข้อมูลการเช่า...")  # แสดงข้อความให้กรอกข้อมูล
                    id_cus = ex.get_next_id()  # ดึงหมายเลขลำดับถัดไปของผู้เช่า
                    print(f"ลำดับที่ (ID): {id_cus}")  # แสดงหมายเลขลำดับที่ของผู้เช่า
                    cus_name = input("ชื่อ-นามสกุล : ")  # รับชื่อ-นามสกุลของผู้เช่า
                    car_model = input("รถรุ่น : ")  # รับรุ่นรถที่ผู้เช่าต้องการเช่า
                    
                    if car_model not in detail_car:  # ถ้ารุ่นรถที่ป้อนไม่มีในรายการ
                        print("รถรุ่นที่เลือกไม่มีในรายการ โปรดลองอีกครั้ง")  # แสดงข้อความเตือน
                        continue  # กลับไปแสดงเมนูใหม่อีกครั้ง
                    
                    car_type = detail_car[car_model]  # กำหนดประเภทรถจากรุ่นรถที่เลือก
                    print(f"ประเภทรถ: {car_type}")  # แสดงประเภทรถที่ตรงกับรุ่นรถ
                    return_date_input = int(input("จำนวนวันที่เช่า : "))  # รับจำนวนวันที่เช่ารถ
                    return_date = date_rent + datetime.timedelta(days=return_date_input)  # คำนวณวันที่คืนรถโดยเพิ่มจำนวนวันที่เช่าจากวันเริ่มต้น
                    cost_rent = float(input("ค่าเช่าวันละ : "))  # รับค่าเช่าต่อวันจากผู้ใช้
                    total_cost_rent = cost_rent * return_date_input  # คำนวณค่าเช่ารวมโดยคูณค่าเช่าต่อวันกับจำนวนวันที่เช่า
                    
                    with open("Doc/datas_drive_now.bin", "ab") as file:  # เปิดไฟล์ไบนารีในโหมดเพิ่มข้อมูล
                        data = struct.pack("i100s50s50s15s15sf", id_cus, cus_name.encode(), car_model.encode(), car_type.encode(), date_rent.strftime("%Y/%m/%d").encode(), return_date.strftime("%Y/%m/%d").encode(), total_cost_rent)  # เขียนข้อมูลการเช่ารถในรูปแบบไบนารี
                        file.write(data)  # บันทึกข้อมูลลงไฟล์ไบนารี
                        
                    return {  # ส่งคืนข้อมูลการเช่ารถในรูปแบบดิกชันนารี
                        "ลำดับที่": id_cus,  # หมายเลขลำดับ
                        "ชื่อ-นามสกุล": cus_name,  # ชื่อ-นามสกุลของผู้เช่า
                        "รถรุ่น": car_model,  # รุ่นรถที่เช่า
                        "ประเภทรถ": car_type,  # ประเภทรถ
                        "วันที่เช่า": date_rent.strftime("%Y/%m/%d"),  # วันที่เริ่มเช่า
                        "จำนวนวันที่เช่า": return_date_input,  # จำนวนวันที่เช่า
                        "จำนวนเงิน": f"{total_cost_rent:.2f}",  # จำนวนเงินรวมที่ต้องจ่าย
                        "วันที่คืนรถ": return_date.strftime("%Y/%m/%d")  # วันที่คืนรถ
                    }
                elif rent_car_menu == 3:  # ถ้าผู้ใช้เลือกตัวเลือกที่ 3 (ออกจากเมนูการเช่ารถ)
                    print("ออกจากเมนูการเช่ารถ")  # แสดงข้อความว่าออกจากเมนู
                    keep_going = False  # กำหนดให้ลูปหยุดการทำงานเพื่อออกจากเมนู
                else:  # ถ้าผู้ใช้ป้อนหมายเลขเมนูที่ไม่ถูกต้อง
                    print("เมนูที่เลือกไม่ถูกต้อง")  # แสดงข้อความเตือนว่าหมายเลขเมนูไม่ถูกต้อง
        except Exception as e:  # จัดการข้อผิดพลาดที่อาจเกิดขึ้น
            print(f"เกิดข้อผิดพลาด: {e}")  # แสดงข้อความข้อผิดพลาดพร้อมรายละเอียด

                   
def edit_data_customer(menu_number):  # ฟังก์ชันนี้ใช้สำหรับจัดการข้อมูลลูกค้าผู้เช่ารถ โดยขึ้นอยู่กับตัวเลือกในเมนู
    if menu_number == 3:  # ตรวจสอบว่าหมายเลขเมนูที่ผู้ใช้ป้อนคือ 3 หรือไม่
        try:
            keep_going = True  # กำหนดตัวแปร keep_going เพื่อใช้ควบคุมลูปเมนูแก้ไข
            while keep_going:  # วนลูปแสดงเมนูการแก้ไขข้อมูลลูกค้าผู้เช่ารถจนกว่าผู้ใช้จะเลือกออกจากเมนู
                print("\t\t\tรายการเมนูการเช่ารถ")  # แสดงหัวข้อเมนู
                print("-"*100)  # แสดงเส้นแบ่ง
                print("1. แสดงข้อมูลทั้งหมด")  # ตัวเลือกที่ 1: แสดงข้อมูลลูกค้าผู้เช่ารถทั้งหมด
                print("2. แก้ไขข้อมูลผู้เช่ารถ")  # ตัวเลือกที่ 2: แก้ไขข้อมูลผู้เช่ารถตามหมายเลขลำดับ
                print("3. ออกจากเมนูการเช่ารถ")  # ตัวเลือกที่ 3: ออกจากเมนูการเช่ารถ
                print("-"*100)  # แสดงเส้นแบ่งเพิ่มเติม
                
                edit_car_menu = int(input("กรุณาเลือกรายการ : "))  # รับหมายเลขเมนูที่ผู้ใช้เลือก
                
                if edit_car_menu == 1:  # ถ้าผู้ใช้เลือกตัวเลือกที่ 1 (แสดงข้อมูลทั้งหมด)
                    try:
                        with open("Doc/datas_drive_now.bin", "rb") as file:  # เปิดไฟล์ไบนารีเพื่ออ่านข้อมูล
                            record_size = struct.calcsize("i100s50s50s15s15sf")  # คำนวณขนาดของเรคคอร์ดในไฟล์
                            table = PrettyTable()  # สร้างตารางเพื่อแสดงข้อมูล
                            table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]  # กำหนดหัวข้อตาราง
                            
                            while True:
                                record_data = file.read(record_size)  # อ่านข้อมูลตามขนาดที่คำนวณไว้
                                if not record_data:  # ถ้าไม่มีข้อมูลในไฟล์อีกแล้ว ให้หยุดการอ่านข้อมูล
                                    break
                                
                                record = struct.unpack("i100s50s50s15s15sf", record_data)  # ถอดรหัสข้อมูลจากไบนารีเป็นเรคคอร์ด
                                table.add_row([  # เพิ่มข้อมูลในแต่ละเรคคอร์ดลงในตาราง
                                    record[0],
                                    record[1].decode().strip(),
                                    record[2].decode().strip(),
                                    record[3].decode().strip(),
                                    record[4].decode().strip(),
                                    record[5].decode().strip(),
                                    f"{record[6]:.2f}"
                                ])
                            
                            print("ข้อมูลทั้งหมดของผู้เช่ารถทั้งหมด:")  # แสดงข้อความหัวข้อข้อมูลทั้งหมด
                            print(table)  # แสดงข้อมูลทั้งหมดในรูปแบบตาราง

                    except Exception as e:  # จัดการกรณีเกิดข้อผิดพลาด
                        print(f"เกิดข้อผิดพลาดในการอ่านข้อมูล: {e}")
                
                elif edit_car_menu == 2:  # ถ้าผู้ใช้เลือกตัวเลือกที่ 2 (แก้ไขข้อมูลผู้เช่ารถ)
                    edit_id = int(input("กรุณากรอกลำดับที่ผู้เช่ารถที่ต้องการแก้ไข: "))  # รับหมายเลขลำดับของลูกค้าที่ต้องการแก้ไข
                    records = []  # สร้างลิสต์สำหรับเก็บเรคคอร์ดทั้งหมด

                    try:
                        with open("Doc/datas_drive_now.bin", "rb") as file:  # เปิดไฟล์ไบนารีเพื่ออ่านข้อมูล
                            record_size = struct.calcsize("i100s50s50s15s15sf")  # คำนวณขนาดของเรคคอร์ดในไฟล์
                            
                            while True:
                                record_data = file.read(record_size)  # อ่านข้อมูลจากไฟล์ตามขนาดที่คำนวณไว้
                                if not record_data:  # ถ้าไม่มีข้อมูลเหลืออยู่ ให้หยุดการอ่าน
                                    break
                                
                                record = struct.unpack("i100s50s50s15s15sf", record_data)  # ถอดรหัสข้อมูลจากไบนารี
                                records.append(record)  # เพิ่มข้อมูลเรคคอร์ดลงในลิสต์ records
                                if record[0] == edit_id:  # ตรวจสอบว่าหมายเลขลำดับตรงกับที่ผู้ใช้ระบุหรือไม่
                                    print("ข้อมูลที่พบ:")  # แสดงข้อความว่าพบข้อมูล
                                    print(f"ชื่อ-นามสกุล: {record[1].decode().strip()}")  # แสดงชื่อผู้เช่ารถ
                                    
                                    new_name = input(f"ชื่อใหม่ (กด Enter เพื่อไม่แก้ไข): ").encode('utf-8') or record[1]  # ถ้ากด Enter ให้ใช้ข้อมูลเดิม
                                    print(f"รถรุ่น: {record[2].decode().strip()}")
                                    new_model = input(f"แบบรถใหม่ (กด Enter เพื่อไม่แก้ไข): ") or record[2].decode().strip()  # ถ้ากด Enter ให้ใช้ข้อมูลเดิม
                                    
                                    # ดิกชันนารีสำหรับจับคู่รุ่นรถกับประเภทรถ
                                    detail_car = {  # ดิกชันนารีเก็บข้อมูลรุ่นรถและประเภทรถ
                                                "Nissan Altima": "Sedan",
                                                "Ford Mustang": "Coupe",
                                                "Honda CR-V": "SUV",
                                                "Toyota Corolla": "Sedan",
                                                "Audi A5": "Coupe",
                                                "Hyundai Sonata": "Sedan",
                                                "BMW X5": "SUV",
                                                "Tesla Model 3": "Sedan",
                                                "Mercedes GLA": "SUV",
                                                "Chevy Camaro": "Coupe",
                                                "Mazda CX-5": "SUV",
                                                "Subaru Impreza": "Sedan",
                                                "Porsche 911": "Coupe",
                                                "Lexus RX": "SUV",
                                                "Volvo XC90": "SUV",
                                                "Jaguar F-Type": "Coupe",
                                                "Ford F-150": "Truck",
                                                "Dodge Challenger": "Coupe",
                                                "Kia Sorento": "SUV",
                                                "Volkswagen Passat": "Sedan",
                                                "Ford Explorer": "SUV"
                                            }
                                    
                                    if new_model not in detail_car:  # ตรวจสอบว่ารุ่นรถที่ป้อนมีในรายการหรือไม่
                                        print("รถรุ่นที่เลือกไม่มีในรายการ โปรดลองอีกครั้ง")  # ถ้ารุ่นรถไม่มีในรายการจะแสดงข้อความเตือน
                                        continue
                                    
                                    car_type = detail_car[new_model]  # กำหนดประเภทรถตามรุ่นที่ผู้ใช้เลือก
                                    print(f"ประเภทรถ: {car_type}")  # แสดงประเภทรถที่ตรงกับรุ่น
                                    
                                    new_type = car_type.encode('utf-8')  # แปลงประเภทรถเป็นไบนารี (utf-8)
                                    print(f"วันที่เช่าเดิม: {record[4].decode().strip()}")
                                    new_rent_date = input(f"วันที่เช่าใหม่ (กด Enter เพื่อไม่แก้ไข): ").encode('utf-8') or record[4]  # ถ้ากด Enter ให้ใช้ข้อมูลเดิม
                                    print(f"วันที่คืนรถ: {record[5].decode().strip()}")
                                    new_return_date = input(f"วันที่คืนใหม่ (กด Enter เพื่อไม่แก้ไข): ").encode('utf-8') or record[5]  # ถ้ากด Enter ให้ใช้ข้อมูลเดิม
                                    print(f"ราคาเดิม: {record[6]:.2f}")
                                    new_cost = float(input(f"จำนวนเงินใหม่ (กด Enter เพื่อไม่แก้ไข): ") or record[6])  # ถ้ากด Enter ให้ใช้ข้อมูลเดิม
                                    
                                    updated_record = (  # สร้างเรคคอร์ดใหม่ที่มีข้อมูลที่แก้ไข
                                        record[0],  # หมายเลขลำดับ
                                        new_name.ljust(100),  # ชื่อที่แก้ไขแล้ว (จัดขนาดให้เท่ากัน)
                                        new_model.ljust(50).encode('utf-8'),  # รุ่นรถที่แก้ไขแล้ว
                                        new_type.ljust(50),  # ประเภทรถที่แก้ไขแล้ว
                                        new_rent_date.ljust(15),  # วันที่เช่าที่แก้ไขแล้ว
                                        new_return_date.ljust(15),  # วันที่คืนที่แก้ไขแล้ว
                                        new_cost  # ค่าใช้จ่ายที่แก้ไขแล้ว
                                    )
                                    
                                    records[-1] = updated_record  # อัปเดตเรคคอร์ดในลิสต์ records ด้วยข้อมูลที่แก้ไข
                                    break  # ออกจากลูปเมื่อพบข้อมูลที่ต้องการแก้ไข
                            
                            else:
                                print("ไม่พบข้อมูลสำหรับ ID ที่ระบุ")  # ถ้าไม่พบหมายเลขลำดับที่ระบุจะแสดงข้อความเตือน

                    except FileNotFoundError:  # จัดการกรณีไม่พบไฟล์ข้อมูล
                        print("ไม่พบไฟล์ข้อมูล โปรดตรวจสอบเส้นทางไฟล์")
                    except Exception as e:  # จัดการข้อผิดพลาดทั่วไป
                        print(f"เกิดข้อผิดพลาดในการอ่านข้อมูล: {e}")

                    # ส่วนของการบันทึกข้อมูลหลังจากแก้ไขเสร็จแล้ว
                    try:
                        with open("Doc/datas_drive_now.bin", "wb") as file:  # เปิดไฟล์ในโหมดเขียน (wb)
                            for rec in records:  # วนลูปเพื่อเขียนข้อมูลแต่ละเรคคอร์ดลงในไฟล์
                                file.write(struct.pack("i100s50s50s15s15sf", *rec))  # เขียนข้อมูลที่จัดรูปแบบแล้วกลับไปที่ไฟล์
                        print("บันทึกข้อมูลเรียบร้อยแล้ว")  # แสดงข้อความเมื่อบันทึกข้อมูลเสร็จสิ้น

                    except Exception as e:  # จัดการข้อผิดพลาดในการเขียนไฟล์
                        print(f"เกิดข้อผิดพลาดในการบันทึกข้อมูล: {e}")

                elif edit_car_menu == 3:  # ถ้าผู้ใช้เลือกตัวเลือกที่ 3 (ออกจากเมนู)
                    keep_going = False  # ตั้งค่า keep_going ให้เป็น False เพื่อออกจากลูปเมนู

        except ValueError:  # จัดการกรณีที่ผู้ใช้ป้อนค่าไม่ถูกต้อง
            print("โปรดป้อนตัวเลขที่ถูกต้อง")


def delet_data(menu_number):  # ฟังก์ชันนี้ใช้สำหรับลบข้อมูลการเช่ารถ หากผู้ใช้เลือกเมนูหมายเลข 4
    if menu_number == 4:  # ตรวจสอบว่าหมายเลขเมนูที่ผู้ใช้ป้อนคือ 4 หรือไม่
        try:
            delete_id = int(input("กรุณากรอกลำดับที่ผู้เช่าที่ต้องการลบ: "))  # รับหมายเลขลำดับของผู้เช่าที่ต้องการลบจากผู้ใช้
            found = False  # กำหนดตัวแปร found เพื่อใช้ตรวจสอบว่าพบข้อมูลผู้เช่าที่ต้องการลบหรือไม่
            records = []  # สร้างลิสต์ว่างเพื่อเก็บข้อมูลการเช่าที่ไม่ถูกลบ
            try:
                with open("Doc/datas_drive_now.bin", "rb") as file:  # เปิดไฟล์ไบนารี "datas_drive_now.bin" ในโหมดอ่าน (rb)
                    record_size = struct.calcsize("i100s50s50s15s15sf")  # คำนวณขนาดของแต่ละเรคคอร์ดในไฟล์ตามโครงสร้างที่ใช้ใน struct.unpack
                    while True:
                        record_data = file.read(record_size)  # อ่านข้อมูลจากไฟล์ตามขนาดที่คำนวณไว้
                        if not record_data:  # ถ้าไม่มีข้อมูลให้หยุดการวนลูป (บรรทัดสุดท้ายของไฟล์)
                            break
                        
                        record = struct.unpack("i100s50s50s15s15sf", record_data)  # ถอดรหัสข้อมูลจากไบนารีเป็นข้อมูล Python
                        if record[0] == delete_id:  # ตรวจสอบว่าลำดับที่ผู้เช่าตรงกับลำดับที่ต้องการลบหรือไม่
                            found = True  # ถ้าพบลำดับที่ผู้เช่าที่ต้องการลบ กำหนด found เป็น True
                        else:
                            records.append(record)  # ถ้าไม่ตรงกับที่ต้องการลบ ให้นำข้อมูลนั้นไปเก็บในลิสต์ records
            except Exception as e:
                print(f"เกิดข้อผิดพลาดในการอ่านข้อมูล: {e}")  # แสดงข้อความข้อผิดพลาดหากมีปัญหาในการอ่านไฟล์

            if found:  # ถ้าพบข้อมูลผู้เช่าที่ต้องการลบ
                confirmation = input(f"คุณแน่ใจหรือไม่ว่าต้องการลบข้อมูลของผู้เช่าลำดับที่ {delete_id}? (y/n): ").lower()  # ถามยืนยันจากผู้ใช้ก่อนลบข้อมูล
                if confirmation == 'y':  # ถ้าผู้ใช้ยืนยันว่าต้องการลบ
                    try:
                        with open("Doc/datas_drive_now.bin", "wb") as file:  # เปิดไฟล์ในโหมดเขียน (wb) เพื่อเขียนข้อมูลที่เหลือกลับลงไฟล์
                            for rec in records:  # วนลูปเขียนข้อมูลทุกเรคคอร์ดที่ไม่ถูกลบลงในไฟล์
                                file.write(struct.pack("i100s50s50s15s15sf", *rec))  # เขียนข้อมูลในฟอร์แมตไบนารีลงไฟล์
                            print("ข้อมูลถูกลบเรียบร้อยแล้ว")  # แสดงข้อความยืนยันว่าข้อมูลถูกลบเรียบร้อยแล้ว

                    except Exception as e:
                        print(f"เกิดข้อผิดพลาดในการบันทึกข้อมูล: {e}")  # แสดงข้อความข้อผิดพลาดหากมีปัญหาในการเขียนไฟล์
                else:
                    print("การลบถูกยกเลิก")  # ถ้าผู้ใช้ยกเลิกการลบ จะแสดงข้อความว่าการลบถูกยกเลิก
            else:
                print(f"ไม่พบข้อมูลสำหรับลำดับที่: {delete_id}")  # ถ้าไม่พบลำดับที่ผู้เช่าที่ต้องการลบ จะแสดงข้อความว่าไม่พบข้อมูล

        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {e}")  # แสดงข้อความข้อผิดพลาดหากมีข้อผิดพลาดอื่น ๆ เกิดขึ้นระหว่างกระบวนการ
