import struct
from prettytable import PrettyTable
from collections import defaultdict
from datetime import datetime
import os

def report_data(number_menu):
    if number_menu == 5:
        try:
            with open("Doc/datas_drive_now.bin", "rb") as file:
                record_size = struct.calcsize("i100s50s50s15s15sf")
                table = PrettyTable()
                table.field_names = ["No.", "Customer Name", "Car Model", "Car Type", "Rent Date", "Return Date", "Total Cost"]

                total_income = 0
                total_rentals = 0
                car_type_stats = defaultdict(lambda: {'count': 0, 'income': 0})
                records = []

                while True:
                    record_data = file.read(record_size)
                    if not record_data:
                        break

                    record = struct.unpack("i100s50s50s15s15sf", record_data)
                    records.append(record) 

                    table.add_row([
                        record[0],
                        record[1].decode().strip(),
                        record[2].decode().strip(),
                        record[3].decode().strip(),
                        record[4].decode().strip(),
                        record[5].decode().strip(),
                        record[6]
                    ])
                    
                    total_income += record[6]
                    total_rentals += 1
                    car_type = record[3].decode().strip()
                    car_type_stats[car_type]['count'] += 1
                    car_type_stats[car_type]['income'] += record[6]

                current_date = datetime.now().strftime('%Y-%m-%d')
                report_file_name = f"Report_{current_date}.txt"

                with open("report/" + report_file_name, "w", encoding="utf-8") as report_file:
                    header = f"Report date : {current_date}\n{'=' * 80}\n{table}\n{'=' * 80}\n"
                    report_file.write(header)
                    print(header)
                    rental_stats = (
                        f"Rental statistics\n{'=' * 80}\n"
                        f"Rental amount : {total_rentals}\n"
                        f"Maximum rent  : {max(record[6] for record in records)}\n"
                        f"Lowest rent   : {min(record[6] for record in records)}\n"
                        f"Total income  : {total_income}\n{'=' * 80}\n"
                    )
                    report_file.write(rental_stats)
                    print(rental_stats)

                    # Print & Write Statistics by Car Type
                    car_type_table = PrettyTable()
                    car_type_table.field_names = ["Car Type", "Total Rentals", "Total Income"]
                    for car_type, stats in car_type_stats.items():
                        car_type_table.add_row([car_type, stats['count'], stats['income']])

                    car_type_stats_output = (
                        f"Statistics by car type\n{'=' * 80}\n"
                        f"{car_type_table}\n"
                        f"Total income : {total_income}\n{'=' * 80}\n"
                    )
                    report_file.write(car_type_stats_output)
                    print(car_type_stats_output)

                    # Print & Write Summary of Car Type Stats
                    max_income_type = max(car_type_stats.items(), key=lambda x: x[1]['income'])
                    min_income_type = min(car_type_stats.items(), key=lambda x: x[1]['income'])
                    most_rented_type = max(car_type_stats.items(), key=lambda x: x[1]['count'])
                    least_rented_type = min(car_type_stats.items(), key=lambda x: x[1]['count'])

                    car_type_summary = (
                        f"Highest income from car type: {max_income_type[0]} {max_income_type[1]['income']}\n"
                        f"Lowest income from car type : {min_income_type[0]} {min_income_type[1]['income']}\n"
                        f"Most rented type : {most_rented_type[0]}\n"
                        f"Least rented type: {least_rented_type[0]}\n"
                    )
                    report_file.write(car_type_summary)
                    print(car_type_summary)

                # เปิดไฟล์หลังจากสร้างเสร็จ
                os.startfile(report_file_name)
                print(f"รายงานถูกบันทึกเป็นไฟล์ {report_file_name} และเปิดเรียบร้อยแล้ว")

        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการอ่านข้อมูล: {e}")
