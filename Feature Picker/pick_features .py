#!/usr/bin/env python3
"""
pick_combos.py

Interactive tool to select Monster Hunter Frontier Z weapon combinations
and compute their bitmask IDs based on the game's in‑game mask mapping.
"""

# Per‑weapon mask mapping
mask_for = {
    1:   16,    # SnS
    2:   64,    # DB
    3:    1,    # GS
    4:  128,    # LS
    5:    4,    # Hammer
    6:  256,    # HH
    7:    8,    # Lance
    8:  512,    # GL
    9: 4096,    # Saf
    10:2048,    # Tonfa
    11:8192,    # MS
    12:  32,    # LBG
    13:   2,    # HBG
    14:1024     # Bow
}

# Human‑readable names
weapon_names = {
    1:  "SnS (Sword & Shield)",
    2:  "DB (Dual Blades)",
    3:  "GS (Great Sword)",
    4:  "LS (Long Sword)",
    5:  "Hammer",
    6:  "HH (Hunting Horn)",
    7:  "Lance",
    8:  "GL (Gunlance)",
    9:  "Saf (Switch Axe F)",
    10: "Tonfa",
    11: "MS (Magnet Spike)",
    12: "LBG (Light Bowgun)",
    13: "HBG (Heavy Bowgun)",
    14: "Bow"
}

def compute_mask(weapons):
    """Compute the bitmask for a list of weapon IDs."""
    m = 0
    for w in weapons:
        m |= mask_for.get(w, 0)
    return m

def parse_input(s):
    """Parse comma- or space-separated string of weapon IDs into a list of ints."""
    parts = s.replace(',', ' ').split()
    return [int(p) for p in parts]

def main():
    # --- Print weapon mapping upfront ---
    print("Monster Hunter Frontier Z Weapon Mask Picker\n")
    print("Weapon ID → Weapon Name")
    print("------------------------")
    for wid in range(1, 15):
        print(f" {wid:2} → {weapon_names[wid]}")
    print("\nNow enter any combination of those IDs to compute its mask.\n")
    
    print("Type 'done' or press Enter on an empty line to exit.\n")

    while True:
        s = input("Combo (e.g. 6,8,9,11): ").strip()
        if not s or s.lower() == 'done':
            print("Exiting.")
            break
        try:
            weapons = parse_input(s)
            # Validate
            for w in weapons:
                if w < 1 or w > 14:
                    raise ValueError(f"Weapon ID {w} is out of range (1–14).")
            mask = compute_mask(weapons)
            names = [weapon_names[w] for w in weapons]
            print(f"\nWeapons {weapons} → {', '.join(names)}")
            print(f"Mask: {mask}\n")
        except Exception as e:
            print("Error:", e, "\n")

if __name__ == "__main__":
    main()
