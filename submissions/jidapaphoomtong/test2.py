# โจทย์ 2 : การหาคำที่ใช้ตัวอักษรทุกตัวในภาษาอังกฤษอย่างน้อยหนึ่งครั้ง (Pangram)
# รายละเอียด: เขียนโปรแกรมที่รับสตริงหนึ่งสตริงแล้วตรวจสอบว่าสตริงนั้นเป็น Pangram หรือไม่ ถ้าใช่ ให้หาคำที่ยาวที่สุดในสตริงนั้น

import string

def is_pangram(s):
    #ตรวจสอบว่าสตริงเป็น Pangram หรือไม่
    s = s.lower()  # เปลี่ยนเป็นตัวพิมพ์เล็กเพื่อให้การตรวจสอบไม่แยกความแตกต่างระหว่างตัวพิมพ์ใหญ่และตัวพิมพ์เล็ก
    return set(string.ascii_lowercase).issubset(set(s))

def longest_word(s):
    #หาคำที่ยาวที่สุดในสตริง
    words = s.split()  # แยกสตริงเป็นคำ
    return max(words, key=len)

def main():
    # รับสตริงจากผู้ใช้
    input_string = input("กรุณากรอกสตริง: ").strip()

    # ตรวจสอบว่าสตริงเป็น Pangram หรือไม่
    if is_pangram(input_string):
        # ถ้าเป็น Pangram, หาคำที่ยาวที่สุด
        result = longest_word(input_string)
        print('คำที่ยาวที่สุด: ',result)
    else:
        # ถ้าไม่ใช่ Pangram
        print("Not a Pangram")

if __name__ == "__main__":
    main()

