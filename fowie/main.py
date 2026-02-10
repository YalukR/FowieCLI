import time
import os
import platform

from fowie.face import show_face
from fowie.metrics import cpu_usage, ram_usage
from fowie.rules import cpu_alert, ram_alert
from fowie.notify import notify


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


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


def watch(interval=2):
    while True:
        clear()
        status()
        time.sleep(interval)


def main():
    watch()   # por ahora arranca directo en vigilancia


if __name__ == "__main__":
    main()
