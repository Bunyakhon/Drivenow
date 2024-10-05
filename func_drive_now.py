import datetime
import struct
import extension.extensions_drive_now as ex


def search_data(menu_number):
    if menu_number == 1:
        try:
            keep_going = True
            while keep_going:
                print("\t\t\tรายการเมนูค้นหาข้อมูล")
                print("---------------------------------------------------------")
                print("1. แสดงข้อมูลทั้งหมด")
                print("2. ค้นหาเฉพาะ")
                print("3. ออกจากเมนูการเช่ารถ")
                print("---------------------------------------------------------")
                search_data_menu = int(input("กรุณาเลือกรายการ : ")) 
                
                if search_data_menu == 1:
                    pass
                elif search_data_menu == 2:
                    pass
                elif search_data_menu == 3:
                    print("ออกจากเมนูการค้นหาข้อมูล")
                    keep_going = False
                else:
                    print("เมนูที่เลือกไม่ถูกต้อง")
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
                   
def edit_data_customer(menu_number):
    if menu_number == 3:
        print("แก้ไขข้อมูลการจอง...")
        
def delet_data(menu_number):
    if menu_number == 4:
        print("ลบข้อมูล...")
        
def report_data(menu_number):
    if menu_number == 5:
        print("รายงานข้อมูล...")
