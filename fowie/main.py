from fowie.face import show_face
from fowie.metrics import cpu_usage, ram_usage
from fowie.rules import cpu_alert, ram_alert
from fowie.notify import notify

def status():
    show_face()
    cpu = cpu_usage()
    ram = ram_usage()

    print(f"CPU: {cpu}%")
    print(f"RAM: {ram}%")

    if cpu_alert(cpu):
        notify("CPU alta")

    if ram_alert(ram):
        notify("RAM alta")

def main():
    status()

if __name__ == "__main__":
    main()
