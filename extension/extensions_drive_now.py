import struct  # นำเข้าโมดูล struct ซึ่งใช้สำหรับจัดการข้อมูลในรูปแบบไบนารี

# ฟังก์ชัน get_next_id ใช้เพื่อดึงหมายเลข ID ล่าสุดในไฟล์และคืนค่า ID ถัดไป
def get_next_id():
    try:
        # เปิดไฟล์ไบนารี "datas_drive_now.bin" ในโหมดอ่าน ("rb" = read binary)
        with open("Doc/datas_drive_now.bin", "rb") as file:
            records = []  # สร้างลิสต์ว่างเพื่อเก็บข้อมูลบันทึก (records)
            
            # กำหนดขนาดของบันทึกข้อมูลแต่ละรายการตามโครงสร้างข้อมูลที่บันทึกอยู่ในไฟล์
            record_size = struct.calcsize("i100s50s50s15s15sf")
            
            # วนลูปอ่านข้อมูลจากไฟล์ทีละบันทึกจนกว่าจะไม่มีข้อมูล
            while True:
                record_data = file.read(record_size)  # อ่านข้อมูลตามขนาดบันทึกที่กำหนด
                if not record_data:
                    break  # ถ้าไม่มีข้อมูลให้ออกจากลูป
                
                # ใช้ struct.unpack เพื่อแปลงข้อมูลที่อ่านมาให้อยู่ในรูปแบบที่เข้าใจได้
                record = struct.unpack("i100s50s50s15s15sf", record_data)
                
                # เก็บข้อมูลบันทึกลงในลิสต์ records
                records.append(record)
        
        # ถ้ามีบันทึกข้อมูลในไฟล์ ให้ดึง ID สูงสุดแล้วเพิ่มค่าอีก 1 เพื่อนำไปใช้เป็น ID ถัดไป
        if records:
            max_id = max(record[0] for record in records)  # ค้นหา ID สูงสุดจากบันทึกข้อมูล
            return max_id + 1  # คืนค่า ID ถัดไป (ID สูงสุด + 1)
        else:
            return 1  # ถ้าไฟล์ว่างหรือไม่มีบันทึก คืนค่า ID เริ่มต้นเป็น 1

    # ถ้ามีข้อผิดพลาดเกิดขึ้นขณะอ่านไฟล์ (เช่น ไฟล์ไม่พบหรือรูปแบบข้อมูลผิดพลาด)
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการอ่านข้อมูล: {e}")  # แสดงข้อความข้อผิดพลาด
        return 1  # ในกรณีที่มีข้อผิดพลาด ให้คืนค่า ID เริ่มต้นเป็น 1

# ฟังก์ชัน serach_data_file เป็นฟังก์ชันตัวอย่างที่สร้างขึ้นเพื่อใช้ในการค้นหาไฟล์
def serach_data_file():
    return "file"  # คืนค่าคำว่า "file" (โค้ดยังไม่สมบูรณ์ในส่วนนี้)
