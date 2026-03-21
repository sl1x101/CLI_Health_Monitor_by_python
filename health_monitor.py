import os
import platform
import shutil

# --- [P] PROCESS & [O] OUTPUT ---

def show_os_info():
    """ฟังก์ชันดึงข้อมูล OS และ CPU"""
    my_os = platform.system()
    print(f"🖥️  OS: {my_os} {platform.release()}")
    print(f"⚙️  CPU Cores: {os.cpu_count()} Cores")

def show_disk_info():
    """ฟังก์ชันดึงข้อมูลพื้นที่ความจุในเครื่อง"""
    # เช็คว่าเป็น Windows หรือ Linux จะได้เลือกโฟลเดอร์หลักถูก
    root_path = "C:\\" if platform.system() == "Windows" else "/"
    
    # ดึงข้อมูลจาก OS (หน่วยเป็น Bytes)
    total, used, free = shutil.disk_usage(root_path)
    
    # แปลง Bytes เป็น Gigabytes (GB)
    gb = 1024 ** 3  
    print(f"💾 Disk [{root_path}]: ว่าง {free // gb} GB (จากทั้งหมด {total // gb} GB)")

def clear_screen():
    """ฟังก์ชันล้างหน้าจอ (สำหรับ Windows และ Linux)"""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- [I] INPUT ---

def main():
    print("=== 🚀 CLI Health Monitor (Monk Mode) ===")
    print("คำสั่งที่ใช้ได้: os, disk, all, exit , clear")
    
    while True:
        # รับค่าจากคีย์บอร์ด, ตัดช่องว่างหัวท้าย, และแปลงเป็นตัวพิมพ์เล็ก
        cmd = input("\nmonitor> ").strip().lower()
        
        # Guard Clause: ถ้ากด Enter เปล่าๆ ให้ข้ามไปเริ่มลูปใหม่ทันที
        if not cmd:
            continue
            
        # เช็คคำสั่ง (Routing)
        if cmd == "exit":
            print("👋 ปิดระบบ...")
            break
        elif cmd == "os":
            show_os_info()
        elif cmd == "disk":
            show_disk_info()
        elif cmd == "all":
            show_os_info()
            show_disk_info()
        elif cmd == "clear":
            clear_screen()
            print("=== 🚀 CLI Health Monitor (Monk Mode) ===")
            print("คำสั่งที่ใช้ได้: os, disk, all, exit , clear")
        else:
            print("❌ คำสั่งไม่ถูกต้อง! กรุณาพิมพ์ os, disk, all หรือ exit")

# จุด Start ของโปรแกรม
if __name__ == "__main__":
    main()