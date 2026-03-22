import os
import platform
import shutil
import psutil
# --- [P] PROCESS & [O] OUTPUT ---

def show_os_info():
    """fuction pull CPU info"""
    my_os = platform.system()
    print(f"🖥️  OS: {my_os} {platform.release()}")
    print(f"⚙️  CPU Cores: {os.cpu_count()} Cores")

def show_disk_info():
    # check root path based on OS
    root_path = "C:\\" if platform.system() == "Windows" else "/"
    
    #get disk usage
    total, used, free = shutil.disk_usage(root_path)
    
    #convert to GB
    gb = 1024 ** 3  
    print(f"💾 Disk [{root_path}]: ว่าง {free // gb} GB (จากทั้งหมด {total // gb} GB)")

def clear_screen():
    """fuction clear console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()

def show_ram_info():
    #get info ram
    ram = psutil.virtual_memory()
    gb = 1024 ** 3
    print(f"🧠 RAM: มีทั้งหมด {ram.total // gb} GB | ว่างอยู่ {ram.available // gb} GB | ใช้ไป {ram.percent}%")
    
def menu():
    print("\n"+"="*30)
    print("🚀 CLI Health Monitor")
    print("commands: os, disk, exit, clear, ram, all")
    print("="*30)    

def show_all_functions():
    show_os_info()
    show_disk_info()
    show_ram_info()    
    
commands = {
    # all commands in a dictionary for easy routing
        "os":show_os_info,
        "disk":show_disk_info,
        "ram":show_ram_info,
        "clear":clear_screen,
        "all":show_all_functions,
}
          
def main():
    clear_screen()
    while True:
        #input command
        cmd = input("\nmonitor> ").strip().lower()
        
        # Guard Clause: empty input
        if not cmd:
            continue 
                  
        # (Routing)
        if cmd in commands:
            commands[cmd]()
        elif cmd == "exit":
            print("👋 ออกโปรแกรมแล้วนะครับ! สวัสดีครับ!")
            break
        else:
            print("คำสั่งไม่ถูกต้อง! ลองใหม่อีกครั้งนะครับ!")

#  Start program 
if __name__ == "__main__":
    main()