# โจทย์ 1 : การหาค่าผสมที่เป็นไปได้ของเลขชุดที่ให้ผลรวมเป็นจำนวนเฉพาะ 
# รายละเอียด: เขียนโปรแกรมที่รับอาร์เรย์ของจำนวนเต็มและจำนวนเต็มหนึ่งจำนวน (ผลรวมที่ต้องการ) 
# แล้วทำการหาค่าผสมของตัวเลขในอาร์เรย์ที่มีผลรวมเป็นจำนวนเฉพาะ

from itertools import combinations

def is_prime(n):
    # เช็คว่านี่เป็นจำนวนเฉพาะหรือไม่
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_primes(arr):
    # เช็คว่าอาร์เรย์ประกอบด้วยจำนวนเฉพาะทั้งหมด
    return all(is_prime(x) for x in arr)

def find_combinations(arr, target_sum):
    # หาค่าผสมที่ผลรวมเป็นจำนวนเต็มที่กำหนด
    result = []
    # for r in range(1, len(arr) + 1):
    for comb in combinations(arr, 2):
        if sum(comb) == target_sum:
            result.append(list(comb))
    return result

# รับค่าอินพุตจากผู้ใช้
def get_input():
    # รับอาร์เรย์จากผู้ใช้
    array_input = input("กรุณากรอกอาร์เรย์ของจำนวนเฉพาะ (ใช้ ',' คั่นระหว่างจำนวน): ")
    array = list(map(int, array_input.split(',')))
    
    # รับผลรวมที่ต้องการ
    target_sum = int(input("กรุณากรอกผลรวมที่ต้องการ: "))
    
    # ตรวจสอบว่าอาร์เรย์ประกอบด้วยจำนวนเฉพาะทั้งหมด
    if not all_primes(array):
        print("อาร์เรย์ที่กรอกไม่ประกอบด้วยจำนวนเฉพาะทั้งหมด")
        return None, None
    
    return array, target_sum

# เรียกใช้ฟังก์ชันเพื่อรับค่าและหาผลลัพธ์
array, target_sum = get_input()

if array is not None and target_sum is not None:
    output = find_combinations(array, target_sum)
    print("ค่าผสมที่มีผลรวมตรงตามที่ต้องการ:", output)