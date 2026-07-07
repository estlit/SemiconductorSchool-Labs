# Semiconductor School — FPGA Labs

Hands-on FPGA lab source code for the **Semiconductor School** curriculum, built with **Verilog HDL** and **Xilinx Vivado** on the **Digilent Arty S7-25 (Spartan-7)** board.

This repository is the **central archive for every lab across all curriculum levels**. Each lab is uploaded as a self-contained `.zip` archive, and the file name tells you which level it belongs to.

> **YouTube:** Semiconductor School (@EdgeChipLab) · **Web:** www.SemiconductorSchool.co.kr

---

## File Naming

Every lab archive follows this pattern:

```
Level<N>_Lab<M>_<short_name>.zip
```

- **`Level<N>`** — curriculum level (difficulty tier)
- **`Lab<M>`** — lab number within that level
- **`<short_name>`** — short description of the project

**Examples**

```
Level2_Lab1_7segment_clock.zip
Level2_Lab2_ultrasonic_sonar.zip
Level3_Lab1_....zip
```

> The YouTube video playlist and the curriculum levels are numbered on independent axes. File names here follow the **curriculum** level.

---

## Inside Each Archive

Extract any `.zip` to find a self-contained lab folder. Source files are sorted by type:

```
Level2_Lab1_7segment_clock.zip
└─ Lab1_7segment_clock/
    ├─ Verilog_RTL/     # Verilog design sources (.v / .sv / .vhd)
    ├─ Verilog_TB/      # testbenches (tb_*, *_tb, sim sources)
    ├─ Vivado_xdc/      # constraints (.xdc — pin mapping, clock, I/O standards)
    ├─ Golden_Data/     # reference / memory-init data (.hex / .mem / .coe / .txt)
    └─ Python_Source/   # helper / modeling scripts (.py)
```

| Folder | Contents |
|--------|----------|
| `Verilog_RTL`  | Synthesizable Verilog design sources |
| `Verilog_TB`   | Testbenches for simulation |
| `Vivado_xdc`   | Vivado constraint files (pins, clock, I/O standards) |
| `Golden_Data`  | Reference vectors / memory-initialization data |
| `Python_Source`| Python helper and modeling scripts |

> **Note:** Folders are created only when a lab actually contains those files. Depending on the lab, some folders (e.g. `Golden_Data` or `Python_Source`) may be omitted.

---

## How to Download

No Git command line required.

1. On this repository page, click the green **`< > Code`** button and choose **Download ZIP** to get everything, **or**
2. Click a single `Level<N>_Lab<M>_*.zip` file and choose **Download** to grab just that lab.
3. Extract the archive and open the lab folder.

---

## Working with a Lab (Vivado)

1. Launch **Vivado** → **Create Project** → select the **Arty S7-25** board (`XC7S25`).
2. **Add Sources** → add the Verilog files from `Verilog_RTL/` (and `Verilog_TB/` for simulation), then set the top module.
3. **Add Sources → Constraints** → add the `.xdc` from `Vivado_xdc/` (port names must match the RTL exactly).
4. Run **Synthesis → Implementation** and confirm timing is met (**WNS ≥ 0**).
5. **Generate Bitstream**, open the **Hardware Manager**, connect the board, and **Program Device**.

The free edition of Vivado (2024.x or later recommended) supports the Spartan-7 device used here.

---

## License & Use

Educational material for the Semiconductor School FPGA curriculum. Free to use for learning and teaching. Please credit **Semiconductor School (EdgeChipLab)** when redistributing.

---

**Maintainer:** Roger Kim · EdgeChipLab · Soongsil University
