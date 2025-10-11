# Assignment 1 — Ring Destroyer (Intro to AI)
Author: Mikhail Shumakov  
Course: Introduction to Artificial Intelligence  
University: Innopolis University  

---

## Stage 1 — Project Setup
- [x] Create project structure (`src/`, `tests/`, `reports/`)
- [x] Add `.gitignore`, `README.md`, `requirements.txt`
- [x] Set up Python virtual environment
- [x] Make the first commit and push to GitHub

---

## Stage 2 — Understanding the Assignment and Interface
- [x] Study the input/output protocol of the interactor
- [x] Understand all possible commands (`m x y`, `r`, `rr`, `e k`)
- [x] Learn enemy types and their danger zones
- [x] Define the main objective (Reach Gollum → Reach Mount Doom)

---

## Stage 3 — Agent Architecture
- [ ] Design an `Agent` class with state variables (position, ring, mithril)
- [ ] Implement core functions:
  - `observe()` — read and parse the environment
  - `decide()` — choose the next action
  - `act()` — send the command
- [ ] Maintain a 13×13 map and update danger zones dynamically
- [ ] Implement ring toggling and mithril pickup logic

---

## Stage 4 — Backtracking Agent
- [ ] Implement DFS-based safe path search
- [ ] Add a stack for visited states and backtracking
- [ ] Add ring toggle handling when required
- [ ] Detect reaching Gollum and switch the target to Mount Doom
- [ ] Finish the task using the `e k` command
- [ ] Test the implementation on sample maps

---

## Stage 5 — A* Agent
- [ ] Represent the grid as a graph of safe cells
- [ ] Implement Manhattan distance heuristic
- [ ] Build A* search with `open_set`, `g`, and `f = g + h`
- [ ] Add re-planning after each observation
- [ ] Integrate ring toggle logic (switch between configurations)
- [ ] Test A* on random maps

---

## Stage 6 — Map Generation and Testing
- [ ] Implement `tests/test_maps_generator.py`
- [ ] Generate 1000 random maps for both perception variants
- [ ] Test both agents on generated maps
- [ ] Collect statistics:
  - Execution time (mean, median)
  - Success/failure rate
  - Number of ring toggles

---

## Stage 7 — Report and Analysis
- [ ] Create `reports/draft_report.md`
- [ ] Write up to three paragraphs for Backtracking and A* each
- [ ] Add PEAS description for the agent
- [ ] Insert tables with statistics and plots
- [ ] Include examples of unsolvable maps
- [ ] Export the final PDF report (`Assignment1_Report.pdf`)

---

## Stage 8 — Final Review
- [ ] Verify all commands (`m`, `r`, `rr`, `e`) work correctly
- [ ] Ensure compatibility with the Codeforces environment
- [ ] Check code readability and comments
- [ ] Review repository structure and naming
- [ ] Final commit: `"Complete Assignment 1 solution"`

---

Status: In progress