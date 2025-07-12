from collections import defaultdict

# === Step 1: Read original POSCAR ===
with open("POSCAR.vasp", "r") as f:
    lines = f.readlines()

# === Step 2: Extract header and lattice ===
header = lines[:5]
coord_start = 8 if lines[7].strip().lower().startswith("direct") else 7
coord_lines = lines[coord_start:]

# === Step 3: Map detailed labels to elements ===
element_mapping = {
    "N001": "N", "N002": "N", "N003": "N",
    "C001": "C", "C002": "C",
    "B001": "B", "B002": "B", "B003": "B"
}

positions_by_element = defaultdict(list)

# === Step 4: Parse coordinates and classify ===
for line in coord_lines:
    parts = line.strip().split()
    if len(parts) < 4:
        continue
    x, y, z = parts[:3]
    label = parts[-1]  # take the last part as the atom label
    base_element = element_mapping.get(label, label[:1])  # fallback to first letter
    positions_by_element[base_element].append(f"{x} {y} {z}\n")

# === Step 5: Define the element order
element_order = ["N", "C", "B"]  # You can also use: sorted(positions_by_element)

# === Step 6: Write corrected POSCAR ===
with open("POSCAR_fixed", "w") as f:
    for line in header:
        f.write(line)

    f.write(" ".join(element_order) + "\n")
    f.write(" ".join(str(len(positions_by_element[el])) for el in element_order) + "\n")
    f.write("Direct\n")
    for el in element_order:
        for pos in positions_by_element[el]:
            f.write(pos)
