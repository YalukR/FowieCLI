# ─── FOWIE ── Unicode puro, sin ASCII ──────────────────────────────────────

PIXEL_FONT = {
    'F': [
        "█████",
        "█    ",
        "████ ",
        "█    ",
        "█    ",
    ],
    'O': [
        "█████",
        "█   █",
        "█   █",
        "█   █",
        "█████",
    ],
    'W': [
        "█   █",
        "█   █",
        "█ █ █",
        "██ ██",
        "█   █",
    ],
    'I': [
        "█████",
        "  █  ",
        "  █  ",
        "  █  ",
        "█████",
    ],
    'E': [
        "█████",
        "█    ",
        "████ ",
        "█    ",
        "█████",
    ],
}

def pixel_word(word: str, gap: int = 2) -> str:
    """Renderiza una palabra con letras pixel 5×5 en Unicode."""
    rows = [""] * 5
    sep = " " * gap
    for i, ch in enumerate(word.upper()):
        glyph = PIXEL_FONT.get(ch, ["     "] * 5)
        for r in range(5):
            rows[r] += glyph[r] + (sep if i < len(word) - 1 else "")
    return "\n".join(rows)


FOWIE_FACE = """
    ╱▔╲╱▔╲
   ╲ ◉ ◉ ╱
    ╲▂▽▂╱
━━━◉━━━━━◉━━━
"""

def show_face():
    print(FOWIE_FACE)

def show_banner():
    print(FOWIE_FACE)
    print(pixel_word("FOWIE"))
    print()

if __name__ == "__main__":
    show_banner()