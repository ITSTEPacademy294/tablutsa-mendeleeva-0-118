
import tkinter as tk
import random

# ---------------- ЕЛЕМЕНТИ ----------------

elements = [
    (1, "H", "Гідроген", "Hydrogen"),
    (2, "He", "Гелій", "Helium"),
    (3, "Li", "Літій", "Lithium"),
    (4, "Be", "Берилій", "Beryllium"),
    (5, "B", "Бор", "Boron"),
    (6, "C", "Карбон", "Carbon"),
    (7, "N", "Нітроген", "Nitrogen"),
    (8, "O", "Оксиген", "Oxygen"),
    (9, "F", "Флуор", "Fluorine"),
    (10, "Ne", "Неон", "Neon"),
    (11, "Na", "Натрій", "Sodium"),
    (12, "Mg", "Магній", "Magnesium"),
    (13, "Al", "Алюміній", "Aluminium"),
    (14, "Si", "Силіцій", "Silicon"),
    (15, "P", "Фосфор", "Phosphorus"),
    (16, "S", "Сульфур", "Sulfur"),
    (17, "Cl", "Хлор", "Chlorine"),
    (18, "Ar", "Аргон", "Argon"),
    (19, "K", "Калій", "Potassium"),
    (20, "Ca", "Кальцій", "Calcium"),
    (21, "Sc", "Скандій", "Scandium"),
    (22, "Ti", "Титан", "Titanium"),
    (23, "V", "Ванадій", "Vanadium"),
    (24, "Cr", "Хром", "Chromium"),
    (25, "Mn", "Манган", "Manganese"),
    (26, "Fe", "Ферум", "Iron"),
    (27, "Co", "Кобальт", "Cobalt"),
    (28, "Ni", "Нікель", "Nickel"),
    (29, "Cu", "Купрум", "Copper"),
    (30, "Zn", "Цинк", "Zinc"),
    (31, "Ga", "Галій", "Gallium"),
    (32, "Ge", "Германій", "Germanium"),
    (33, "As", "Арсен", "Arsenic"),
    (34, "Se", "Селен", "Selenium"),
    (35, "Br", "Бром", "Bromine"),
    (36, "Kr", "Криптон", "Krypton"),
    (37, "Rb", "Рубідій", "Rubidium"),
    (38, "Sr", "Стронцій", "Strontium"),
    (39, "Y", "Ітрій", "Yttrium"),
    (40, "Zr", "Цирконій", "Zirconium"),
    (41, "Nb", "Ніобій", "Niobium"),
    (42, "Mo", "Молібден", "Molybdenum"),
    (43, "Tc", "Технецій", "Technetium"),
    (44, "Ru", "Рутеній", "Ruthenium"),
    (45, "Rh", "Родій", "Rhodium"),
    (46, "Pd", "Паладій", "Palladium"),
    (47, "Ag", "Аргентум", "Silver"),
    (48, "Cd", "Кадмій", "Cadmium"),
    (49, "In", "Індій", "Indium"),
    (50, "Sn", "Станум", "Tin"),
    (51, "Sb", "Стибій", "Antimony"),
    (52, "Te", "Телур", "Tellurium"),
    (53, "I", "Йод", "Iodine"),
    (54, "Xe", "Ксенон", "Xenon"),
    (55, "Cs", "Цезій", "Caesium"),
    (56, "Ba", "Барій", "Barium"),
    (57, "La", "Лантан", "Lanthanum"),
    (58, "Ce", "Церій", "Cerium"),
    (59, "Pr", "Празеодим", "Praseodymium"),
    (60, "Nd", "Неодим", "Neodymium"),
    (61, "Pm", "Прометій", "Promethium"),
    (62, "Sm", "Самарій", "Samarium"),
    (63, "Eu", "Європій", "Europium"),
    (64, "Gd", "Гадоліній", "Gadolinium"),
    (65, "Tb", "Тербій", "Terbium"),
    (66, "Dy", "Диспрозій", "Dysprosium"),
    (67, "Ho", "Гольмій", "Holmium"),
    (68, "Er", "Ербій", "Erbium"),
    (69, "Tm", "Тулій", "Thulium"),
    (70, "Yb", "Ітербій", "Ytterbium"),
    (71, "Lu", "Лютецій", "Lutetium"),
    (72, "Hf", "Гафній", "Hafnium"),
    (73, "Ta", "Тантал", "Tantalum"),
    (74, "W", "Вольфрам", "Tungsten"),
    (75, "Re", "Реній", "Rhenium"),
    (76, "Os", "Осмій", "Osmium"),
    (77, "Ir", "Іридій", "Iridium"),
    (78, "Pt", "Платина", "Platinum"),
    (79, "Au", "Аурум", "Gold"),
    (80, "Hg", "Меркурій", "Mercury"),
    (81, "Tl", "Талій", "Thallium"),
    (82, "Pb", "Плюмбум", "Lead"),
    (83, "Bi", "Бісмут", "Bismuth"),
    (84, "Po", "Полоній", "Polonium"),
    (85, "At", "Астат", "Astatine"),
    (86, "Rn", "Радон", "Radon"),
    (87, "Fr", "Францій", "Francium"),
    (88, "Ra", "Радій", "Radium"),
    (89, "Ac", "Актиній", "Actinium"),
    (90, "Th", "Торій", "Thorium"),
    (91, "Pa", "Протактиній", "Protactinium"),
    (92, "U", "Уран", "Uranium"),
    (93, "Np", "Нептуній", "Neptunium"),
    (94, "Pu", "Плутоній", "Plutonium"),
    (95, "Am", "Америцій", "Americium"),
    (96, "Cm", "Кюрій", "Curium"),
    (97, "Bk", "Берклій", "Berkelium"),
    (98, "Cf", "Каліфорній", "Californium"),
    (99, "Es", "Ейнштейній", "Einsteinium"),
    (100, "Fm", "Фермій", "Fermium"),
    (101, "Md", "Менделевій", "Mendelevium"),
    (102, "No", "Нобелій", "Nobelium"),
    (103, "Lr", "Лоуренсій", "Lawrencium"),
    (104, "Rf", "Резерфордій", "Rutherfordium"),
    (105, "Db", "Дубній", "Dubnium"),
    (106, "Sg", "Сіборгій", "Seaborgium"),
    (107, "Bh", "Борій", "Bohrium"),
    (108, "Hs", "Гасій", "Hassium"),
    (109, "Mt", "Майтнерій", "Meitnerium"),
    (110, "Ds", "Дармштадтій", "Darmstadtium"),
    (111, "Rg", "Рентгеній", "Roentgenium"),
    (112, "Cn", "Коперницій", "Copernicium"),
    (113, "Nh", "Ніхоній", "Nihonium"),
    (114, "Fl", "Флеровій", "Flerovium"),
    (115, "Mc", "Московій", "Moscovium"),
    (116, "Lv", "Ліверморій", "Livermorium"),
    (117, "Ts", "Теннессин", "Tennessine"),
    (118, "Og", "Оганесон", "Oganesson")
]

# Секретний елемент
secret_element = (0, "?", "Невідомий елемент №0", "UNKNOWN")

# ---------------- НАЛАШТУВАННЯ ----------------

root = tk.Tk()
root.title("Елемент №0")
root.geometry("520x600")
root.resizable(False, False)
root.configure(bg="#10131f")

title = tk.Label(
    root,
    text="ТАЄМНИЦЯ ТАБЛИЦІ",
    font=("Arial", 23, "bold"),
    bg="#10131f",
    fg="#65e6ff"
)
title.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Знайди всі 118 елементів... і дещо більше",
    font=("Arial", 10),
    bg="#10131f",
    fg="#b8c2d9"
)
subtitle.pack(pady=5)

# Картка елемента
card = tk.Frame(
    root,
    bg="#20283d",
    width=300,
    height=270,
    highlightbackground="#394765",
    highlightthickness=2
)
card.pack(pady=25)
card.pack_propagate(False)

number_label = tk.Label(
    card,
    text="№ ???",
    font=("Arial", 13),
    bg="#20283d",
    fg="#b8c2d9"
)
number_label.pack(anchor="nw", padx=18, pady=(15, 0))

symbol_label = tk.Label(
    card,
    text="?",
    font=("Arial", 76, "bold"),
    bg="#20283d",
    fg="#65e6ff"
)
symbol_label.pack(pady=8)

name_label = tk.Label(
    card,
    text="Натисни кнопку!",
    font=("Arial", 17, "bold"),
    bg="#20283d",
    fg="white",
    wraplength=270
)
name_label.pack(pady=5)

english_label = tk.Label(
    card,
    text="ELEMENT DISCOVERY",
    font=("Arial", 10),
    bg="#20283d",
    fg="#a8b5d1"
)
english_label.pack(pady=5)

# Статистика
stats_label = tk.Label(
    root,
    text="Відкрито елементів: 0 / 119",
    font=("Arial", 12),
    bg="#10131f",
    fg="#b8c2d9"
)
stats_label.pack(pady=5)

# Повідомлення
message_label = tk.Label(
    root,
    text="Тут може ховатися щось невідоме...",
    font=("Arial", 10),
    bg="#10131f",
    fg="#a8b5d1",
    wraplength=460
)
message_label.pack(pady=8)

# ---------------- ЛОГІКА ГРИ ----------------

discovered = set()

def discover_element():
    # Усі 118 елементів + секретний №0
    all_elements = elements + [secret_element]
    element = random.choice(all_elements)

    number, symbol, name, english = element

    number_label.config(text=f"№ {number:03d}" if number != 0 else "№ 000")
    symbol_label.config(text=symbol)
    name_label.config(text=name)
    english_label.config(text=english)

    if number == 0:
        card.config(bg="#351a48", highlightbackground="#e45cff")
        for label in (number_label, symbol_label, name_label, english_label):
            label.config(bg="#351a48", fg="#ff8cff")

        message_label.config(
            text="НЕМОЖЛИВО! Ти знайшов секретний елемент №0!",
            fg="#ff8cff"
        )
    else:
        card.config(bg="#20283d", highlightbackground="#394765")
        for label in (number_label, symbol_label, name_label, english_label):
            label.config(bg="#20283d")

        number_label.config(fg="#b8c2d9")
        symbol_label.config(fg="#65e6ff")
        name_label.config(fg="white")
        english_label.config(fg="#a8b5d1")

        message_label.config(
            text=f"Відкрито елемент: {name}",
            fg="#65e6ff"
        )

    discovered.add(number)
    stats_label.config(
        text=f"Відкрито елементів: {len(discovered)} / 119"
    )

    if len(discovered) == 119:
        message_label.config(
            text="ВІТАЄМО! Ти відкрив усі 119 елементів!",
            fg="#65ff9b"
        )

def reset_game():
    discovered.clear()

    number_label.config(text="№ ???")
    symbol_label.config(text="?")
    name_label.config(text="Натисни кнопку!")
    english_label.config(text="ELEMENT DISCOVERY")

    card.config(bg="#20283d", highlightbackground="#394765")

    number_label.config(bg="#20283d", fg="#b8c2d9")
    symbol_label.config(bg="#20283d", fg="#65e6ff")
    name_label.config(bg="#20283d", fg="white")
    english_label.config(bg="#20283d", fg="#a8b5d1")

    stats_label.config(text="Відкрито елементів: 0 / 119")
    message_label.config(
        text="Тут може ховатися щось невідоме...",
        fg="#a8b5d1"
    )

# Кнопки
discover_button = tk.Button(
    root,
    text="ВІДКРИТИ ЕЛЕМЕНТ",
    font=("Arial", 14, "bold"),
    bg="#167d9b",
    fg="white",
    activebackground="#24a6c9",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=discover_element
)
discover_button.pack(fill="x", padx=65, pady=(5, 10), ipady=10)

reset_button = tk.Button(
    root,
    text="Почати спочатку",
    font=("Arial", 10),
    bg="#252d42",
    fg="#d6def0",
    activebackground="#394765",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=reset_game
)
reset_button.pack(pady=3)

root.mainloop()
