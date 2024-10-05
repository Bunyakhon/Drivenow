import struct
def get_next_id():
    try:
        with open("Doc/datas_drive_now.bin", "rb") as file:
            records = []
            record_size = struct.calcsize("i100s50s50s15s15sf")
            
            while True:
                record_data = file.read(record_size)
                if not record_data:
                    break
                record = struct.unpack("i100s50s50s15s15sf", record_data)
                records.append(record)
        if records:
            max_id = max(record[0] for record in records)
            return max_id + 1
        else:
            return 1
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการอ่านข้อมูล: {e}")
        return 1
def serach_data_file():
    
    return "file"