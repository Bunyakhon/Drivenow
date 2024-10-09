import struct # นำเข้าโมดูล struct ซึ่งใช้สำหรับจัดการข้อมูลในรูปแบบไบนารี
from prettytable import PrettyTable  # นำเข้าโมดูล PrettyTable ซึ่งเป็นเครื่องมือที่ช่วยในการสร้างตารางข้อมูลในรูปแบบที่อ่านง่าย เช่น ในรูปแบบของ ASCII table (ใช้สำหรับแสดงข้อมูลในรูปแบบตาราง)
from collections import defaultdict  # นำเข้า defaultdict จากโมดูล collections ซึ่งเป็นโครงสร้างข้อมูลคล้าย dict (พจนานุกรม) แต่มีความพิเศษตรงที่สามารถกำหนดค่าเริ่มต้นให้กับคีย์ที่ยังไม่มีใน dict ได้โดยอัตโนมัติ
from datetime import datetime  # นำเข้า datetime จากโมดูล datetime ซึ่งใช้สำหรับการจัดการและรูปแบบของวันเวลา เช่น การดึงวันเวลาปัจจุบัน การคำนวณเวลา และการฟอร์แมตเวลาให้อยู่ในรูปแบบที่กำหนด
import os  # นำเข้าโมดูล os ซึ่งเป็นเครื่องมือสำหรับการจัดการและทำงานกับระบบไฟล์และโฟลเดอร์ต่าง ๆ เช่น การสร้างโฟลเดอร์, ตรวจสอบเส้นทางไฟล์ หรือการลบไฟล์


def report_data(number_menu):
    if number_menu == 5:  # ตรวจสอบว่าผู้ใช้เลือกเมนูที่ 5 สำหรับการสร้างรายงาน
        try:
            # ตรวจสอบว่ามีโฟลเดอร์ "Doc" หรือไม่
            if not os.path.exists("Doc"):
                print("โฟลเดอร์ 'Doc' ไม่พบ กรุณาตรวจสอบการตั้งค่า.")
                return  # ถ้าไม่พบโฟลเดอร์ "Doc" ให้จบการทำงานทันที

            # เปิดไฟล์ไบนารี "datas_drive_now.bin" ในโหมดอ่านแบบไบนารี
            with open("Doc/datas_drive_now.bin", "rb") as file:
                # กำหนดขนาดของบันทึกข้อมูลแต่ละรายการในไฟล์ด้วย struct (กำหนดให้ตรงกับข้อมูลในไฟล์)
                record_size = struct.calcsize("i100s50s50s15s15sf")
                table = PrettyTable()  # สร้างตารางเพื่อแสดงข้อมูล
                table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]

                total_income = 0  # เก็บผลรวมรายได้จากการเช่ารถทั้งหมด
                total_rentals = 0  # เก็บจำนวนครั้งการเช่ารถทั้งหมด
                car_type_stats = defaultdict(lambda: {'count': 0, 'income': 0})  # เก็บสถิติจำนวนครั้งและรายได้สำหรับประเภทของรถแต่ละชนิด
                records = []  # สร้างลิสต์เพื่อเก็บข้อมูลบันทึกแต่ละรายการจากไฟล์

                # วนลูปเพื่ออ่านข้อมูลจากไฟล์ทีละบันทึก
                while True:
                    record_data = file.read(record_size)  # อ่านข้อมูลตามขนาดบันทึกที่กำหนด
                    if not record_data:
                        break  # ถ้าไม่มีข้อมูลให้ออกจากลูป

                    # แปลงข้อมูลไบนารีที่อ่านมาให้เป็นข้อมูลที่มีความหมายตาม format ที่กำหนดใน struct
                    record = struct.unpack("i100s50s50s15s15sf", record_data)
                    records.append(record)  # เก็บบันทึกนี้ไว้ในลิสต์ records

                    # เพิ่มแถวในตารางด้วยข้อมูลที่ถอดรหัสแล้ว
                    table.add_row([
                        record[0],  # ลำดับการเช่า
                        record[1].decode().strip('\x00'),  # ชื่อผู้เช่า (ถอดรหัสจาก bytes และลบช่องว่าง)
                        record[2].decode().strip('\x00'),  # รุ่นรถ (ถอดรหัสจาก bytes และลบช่องว่าง)
                        record[3].decode().strip('\x00'),  # ประเภทรถ (ถอดรหัสจาก bytes และลบช่องว่าง)
                        record[4].decode().strip('\x00'),  # วันที่เช่า (ถอดรหัสจาก bytes และลบช่องว่าง)
                        record[5].decode().strip('\x00'),  # วันที่คืน (ถอดรหัสจาก bytes และลบช่องว่าง)
                        f"{record[6]:.2f}"  # ราคารวม
                    ])

                    # คำนวณรายได้รวมและจำนวนการเช่ารวม
                    total_income += record[6]
                    total_rentals += 1

                    # เก็บสถิติสำหรับประเภทของรถ
                    car_type = record[3].decode().strip('\x00')
                    car_type_stats[car_type]['count'] += 1  # เพิ่มจำนวนครั้งการเช่าสำหรับประเภทนี้
                    car_type_stats[car_type]['income'] += record[6]  # เพิ่มรายได้สำหรับประเภทนี้

                # กำหนดชื่อไฟล์รายงานตามวันที่ปัจจุบัน
                current_date = datetime.now().strftime('%Y-%m-%d')
                report_file_name = f"Report_{current_date}.txt"

                # ตรวจสอบว่าโฟลเดอร์ "report" มีหรือไม่ ถ้าไม่มีให้สร้างขึ้น
                if not os.path.exists("report"):
                    os.makedirs("report")

                # เปิดไฟล์รายงานสำหรับเขียนข้อมูล
                with open("report/" + report_file_name, "w", encoding="utf-8") as report_file:
                    # เขียนส่วนหัวของรายงานลงในไฟล์
                    header = f"{'='*100}\nReport date : {current_date}\n{'=' * 100}\n{table}\n{'=' * 100}\n"
                    report_file.write(header)
                    print(header)  # แสดงส่วนหัวของรายงานบนหน้าจอ

                    # เขียนข้อมูลสถิติการเช่ารถ
                    rental_stats = (
                        f"Rental statistics\n{'=' * 100}\n"
                        f"Rental amount : {total_rentals}\n"  # จำนวนการเช่าทั้งหมด
                        f"Maximum rent  : {max(record[6] for record in records):.2f}\n"  # ค่าเช่าสูงสุด
                        f"Lowest rent   : {min(record[6] for record in records):.2f}\n"  # ค่าเช่าต่ำสุด
                        f"Total income  : {total_income:.2f}\n{'=' * 100}\n"  # รายได้รวมทั้งหมด
                    )
                    report_file.write(rental_stats)
                    print(rental_stats)  # แสดงสถิติการเช่าบนหน้าจอ

                    # สร้างตารางแสดงสถิติสำหรับแต่ละประเภทรถ
                    car_type_table = PrettyTable()
                    car_type_table.field_names = ["Car Type", "Total Rentals", "Total Income"]
                    for car_type, stats in car_type_stats.items():
                        car_type_table.add_row([car_type, stats['count'], f"{stats['income']:.2f}"])

                    # เขียนสถิติตามประเภทของรถลงในไฟล์รายงาน
                    car_type_stats_output = (
                        f"Statistics by car type\n{'=' * 100}\n"
                        f"{car_type_table}\n"
                        f"Total income : {total_income:.2f}\n{'=' * 100}\n"
                    )
                    report_file.write(car_type_stats_output)
                    print(car_type_stats_output)  # แสดงสถิติตามประเภทรถบนหน้าจอ

                    # คำนวณและแสดงข้อมูลเพิ่มเติม เช่น ประเภทรถที่มีรายได้สูงสุด ต่ำสุด จำนวนการเช่ามากที่สุด และน้อยที่สุด
                    max_income_type = max(car_type_stats.items(), key=lambda x: x[1]['income'])
                    min_income_type = min(car_type_stats.items(), key=lambda x: x[1]['income'])
                    most_rented_type = max(car_type_stats.items(), key=lambda x: x[1]['count'])
                    least_rented_type = min(car_type_stats.items(), key=lambda x: x[1]['count'])

                    car_type_summary = (
                        f"Highest income from car type: {max_income_type[0]} = {max_income_type[1]['income']:.2f}\n"  # รายได้สูงสุดจากประเภทรถ
                        f"Lowest income from car type : {min_income_type[0]} = {min_income_type[1]['income']:.2f}\n"  # รายได้ต่ำสุดจากประเภทรถ
                        f"Most rented type : {most_rented_type[0]}\n"  # ประเภทรถที่ถูกเช่ามากที่สุด
                        f"Least rented type: {least_rented_type[0]}\n"  # ประเภทรถที่ถูกเช่าน้อยที่สุด
                    )
                    report_file.write(car_type_summary)
                    print(car_type_summary)  # แสดงสรุปข้อมูลบนหน้าจอ

                # แสดงที่อยู่ของไฟล์รายงานที่บันทึก
                report_full_path = os.path.abspath("report/" + report_file_name)
                print(f"รายงานถูกบันทึกที่: {report_full_path}")

        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการอ่านข้อมูล: {e}")  # ถ้าเกิดข้อผิดพลาดจะแสดงข้อความแจ้งเตือน
