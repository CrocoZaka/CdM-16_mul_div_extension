# CdM-16 Multiplication Extension

## Project Overview

This project extends the **CdM-16 processor architecture** by adding **hardware-supported multiplication instructions**. To achieve this, we implemented a new processor variant **cdm16m**, which supports multiplication instructions. The multiplication instructions are provided as a separate extension (`m`), which can be enabled by the user.

## Supported Instructions

The multiplication extension introduces the following instructions:

* `mulu` — unsigned multiplication
* `muls` — signed multiplication

## How to Use

### 1. Write Assembly Code

Create an assembly source file (e.g. `program.asm`) using the multiplication instructions:

```asm
    mulu r1, r2
    muls r3, r4
```

### 2. Assemble the Program

Use the assembler with the **CdM-16 target and the `m` extension enabled**:

```bash
cocas program.asm -t cdm16m
```

As a result, the assembler produces an image file:

```text
out.img
```

### 3. Load the Program into Logisim

1. Open **Logisim**.
2. Load the memory image using
   **logisim-banked-memory-0.2.2.jar**:

   * Insert the memory module
   * Load `out.img` into the memory contents
3. Connect the memory module to the **`cdm16m` processor module**.
4. Start the simulation.

The program will execute using the hardware multiplication instructions.
