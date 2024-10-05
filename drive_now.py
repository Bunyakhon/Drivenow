import time
import func_drive_now as fdn
import gen_report as re
def main():
    try:
        keep_going = True
        rental_info = {}  # ประกาศตัวแปร rental_info เพื่อใช้ในเมนูที่ 2
        while keep_going:
            print("==========================================================")
            print("\t\t\tรายการเมนู")
            print("==========================================================")
            print("1. ค้นหาข้อมูล")
            print("2. จองรถ")
            print("3. แก้ไขข้อมูลการเช่ารถ")
            print("4. ลบข้อมูลการเช่ารถ")
            print("5. รายงานข้อมูลการเช่า")
            print("6. ปิดโปรแกรม")
            print("==========================================================")

            try:
                number_menu = int(input("กรุณาใส่หมายเลข : "))
                if number_menu == 1:
                    output = fdn.search_data(number_menu)
                    time.sleep(1)
                elif number_menu == 2:
                    rental_info = fdn.rent_car(number_menu)
                    if rental_info:
                        print("\nข้อมูลการเช่าที่ได้รับ:")
                        for key, value in rental_info.items():
                            print(f"{key}: {value}")
                    time.sleep(1)
                elif number_menu == 3:
                    output = fdn.edit_data_customer(number_menu)
                    time.sleep(1)
                elif number_menu == 4:
                    output = fdn.delet_data(number_menu)
                    time.sleep(1)
                elif number_menu == 5:
                    output = re.report_data(number_menu)
                    time.sleep(1)
                elif number_menu == 6:
                    print("จบการทำงาน")
                    keep_going = False
                else:
                    print("ใส่หมายเลขเมนูให้ถูกต้อง")
                    time.sleep(1)
            except ValueError:
                print("กรุณาใส่หมายเลขให้ถูกต้อง")
                time.sleep(1)
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    main()
