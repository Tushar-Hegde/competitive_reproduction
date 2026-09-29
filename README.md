# Plant Evolution & Competition Simulation

A Python CLI visual simulation that models plant reproduction, competition for limited grid space, mutation, and host-parasite dynamics across generations.

---

## Overview

This project simulates evolutionary dynamics on a 2D grid matrix. Plant species compete for empty spatial blocks by spreading seeds into neighboring coordinates. Over successive generations, you can observe natural selection, population equilibrium, and parasitic interaction.

---

## Plant Types & Entities

| Entity / Symbol | Name | Description | Seed Spread / Behavior |
| :--- | :--- | :--- | :--- |
| **`0`** (White) | Empty Block | Unoccupied spatial cell on the grid. | Available for seeds to land on. |
| **`2`** (Blue) | Two-Seed Plant | Spreads seeds to 2 neighboring spaces plus its own cell. Has a 2% chance per seed to mutate into a Four-Seed plant. | Moderate reproductive rate. |
| **`4`** (Red) | Four-Seed Plant | Spreads seeds to all 4 neighboring spaces plus its own cell. Has a 5% chance per seed to mutate into a Two-Seed plant. | Aggressive reproductive rate. |
| **`X`** (Green) | Parasite Plant | Infections spread to adjacent plant cells with a 20% takeover rate. Parasites persist for a fixed lifespan of 3 steps before dying. | Host-pathogen control mechanism. |

---

## Observations & Simulation Examples

### 1. Run Without Mutations (Competitive Exclusion)

In a scenario without mutations, species with higher dispersal rates (**Red / 4-Seed Plants**) rapidly outcompete lower-dispersal species (**Blue / 2-Seed Plants**) for available space on the board.

![No Mutation Run](https://github.com/user-attachments/files/16735244/ev.pdf)

*Red plants quickly take over the majority of the matrix due to their superior spread rate.*

---

### 2. Run With Mutations (Population Equilibrium)

When mutations are enabled, plant species mutate into one another over time. Regardless of starting conditions, the population ratio eventually stabilizes into a dynamic equilibrium (roughly 85–87% Red plants to 13–15% Blue plants).

![Mutation Run](https://github.com/user-attachments/files/16735245/ev.1.pdf)

*The terminal output tracks plant percentages and total cumulative mutations generation by generation.*

---

## Prerequisites & Installation

### Requirements

* **Python 3.x**
* **`colored` library** (for ANSI terminal color outputs)

### Installing Dependencies

Install the required ANSI color dependency via `pip`:

```bash
pip install colored
```

---

## How to Run

> **Important:** Run this program inside a standard command terminal (Terminal / Command Prompt / PowerShell) rather than IDE execution windows like IDLE, as ANSI escape characters for color codes require standard console terminal rendering.

1. Clone or download the repository.
2. Open your terminal and navigate to the project directory.
3. Execute the simulation:

```bash
python competitive_reproduction.py
```

4. Press <kbd>Enter</kbd> in the console to step forward to the next generation.
