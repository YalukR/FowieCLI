import time
import sys

from fowie.face import pixel_word, FOWIE_FACE
from fowie.metrics import cpu_usage, ram_usage
from fowie.rules import cpu_alert, ram_alert
from fowie.notify import notify


# ─── ANSI helpers ────────────────────────────────────────────────────────────

def _write(s: str):
    sys.stdout.write(s)
    sys.stdout.flush()

def cursor_up(n: int):
    """Sube el cursor n líneas."""
    if n > 0:
        _write(f"\033[{n}A")

def clear_line():
    """Borra la línea actual desde el cursor."""
    _write("\033[2K\r")

def hide_cursor():
    _write("\033[?25l")

def show_cursor():
    _write("\033[?25h")


# ─── Sección de métricas ─────────────────────────────────────────────────────

def _bar(pct: float, width: int = 20) -> str:
    """Barra de progreso Unicode."""
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)

def _color(pct: float) -> str:
    """Color ANSI según nivel."""
    if pct >= 80:
        return "\033[91m"   # rojo
    if pct >= 50:
        return "\033[93m"   # amarillo
    return "\033[92m"       # verde

RESET = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"

def _metric_lines(cpu: float, ram: float) -> list[str]:
    """Devuelve exactamente las líneas que se refrescan."""
    lines = []
    for label, pct in (("CPU", cpu), ("RAM", ram)):
        c   = _color(pct)
        bar = _bar(pct)
        lines.append(
            f"  {BOLD}{label}{RESET}  {c}{bar}{RESET}  {c}{BOLD}{pct:5.1f}%{RESET}"
        )
    lines.append(f"  {DIM}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    lines.append(f"  {DIM}actualizando cada 2 s  ·  Ctrl+C para salir{RESET}")
    return lines

# Número fijo de líneas que ocupa la sección dinámica
_METRIC_LINES = 4


# ─── Banner estático (se imprime una sola vez) ────────────────────────────────

def _print_static_banner():
    print(FOWIE_FACE)
    print(pixel_word("FOWIE"))
    print()
    print(f"  {DIM}─────────────────────────────────{RESET}")
    print()


# ─── Loop principal ───────────────────────────────────────────────────────────

def watch(interval: float = 2):
    hide_cursor()
    try:
        _print_static_banner()

        # Primera pasada: imprime las líneas métricas normalmente
        cpu = cpu_usage()
        ram = ram_usage()
        lines = _metric_lines(cpu, ram)
        for line in lines:
            print(line)

        # Alertas iniciales
        if cpu_alert(cpu):
            notify("CPU alta")
        if ram_alert(ram):
            notify("RAM alta")

        while True:
            time.sleep(interval)

            cpu = cpu_usage()
            ram = ram_usage()
            new_lines = _metric_lines(cpu, ram)

            # Sube exactamente _METRIC_LINES líneas y las sobreescribe
            cursor_up(_METRIC_LINES)
            for line in new_lines:
                clear_line()
                print(line)

            if cpu_alert(cpu):
                notify("CPU alta")
            if ram_alert(ram):
                notify("RAM alta")

    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        print()  # deja el cursor en línea limpia


def main():
    watch()


if __name__ == "__main__":
    main()