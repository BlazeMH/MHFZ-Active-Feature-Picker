# Monster Hunter Frontier Z Weapon Mask Tool

This is a simple tool helps you calculate and interpret the in-game **bitmask IDs** used to represent weapon selections on your private MHF-Z server.
---
## 📖 Background: Why a Bitmask?

- The game uses a **14-bit mask** to track which weapons are selected.  
- Each weapon corresponds to one bit in that mask.  
- When multiple weapons are selected, their bits are **OR'ed** together.  
- With 14 weapons, selecting all gives:  
---
## 🔢 Single-Weapon Mask Mapping

Based on in-game testing, each weapon has this mask value:

| ID | Weapon              | Mask  |
|---:|---------------------|------:|
|  1 | SnS (Sword & Shield)|    16 |
|  2 | DB (Dual Blades)    |    64 |
|  3 | GS (Great Sword)    |     1 |
|  4 | LS (Long Sword)     |   128 |
|  5 | Hammer              |     4 |
|  6 | HH (Hunting Horn)   |   256 |
|  7 | Lance               |     8 |
|  8 | GL (Gunlance)       |   512 |
|  9 | Saf (Switch Axe F)  |  4096 |
| 10 | Tonfa               |  2048 |
| 11 | MS (Magnet Spike)   |  8192 |
| 12 | LBG (Light Bowgun)  |    32 |
| 13 | HBG (Heavy Bowgun)  |     2 |
| 14 | Bow                 |  1024 |

**All selected (14 weapons):** `16383`
---
## 🚀 Using the Picker Script (`pick_features.py`)

1. Ensure you have Python 3 installed.  
2. Place `pick_features.py` in your working directory.  
3. Run with:  

```bash
python pick_features.py
```
## Enter any combination (comma or space separated):
Example Combo: 6,8,9,11
## → HH (Hunting Horn), GL (Gunlance), Saf (Switch Axe F), MS (Magnet Spike)
Mask: 13056

Press Enter on an empty line or type done to quit.
