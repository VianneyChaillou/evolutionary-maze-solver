# 🧬 Evolutionary AI Maze Solver

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame-CE](https://img.shields.io/badge/Pygame--CE-F1C40F?style=for-the-badge&logo=python)
![AI/ML](https://img.shields.io/badge/Machine_Learning-Genetic_Algorithm-FF6F00?style=for-the-badge)

A 2D maze solver powered by a custom-built **Genetic Algorithm (Evolutionary AI)** created entirely from scratch. This project was developed as the October entry for my *1 Project / Month* challenge, showcasing low-level AI logic without relying on traditional pathfinding algorithms like A* or Dijkstra.

## The Genetic Engine

The simulation runs purely on CPU in Python and relies on biological evolution concepts to teach a swarm of agents how to navigate a complex environment.

*   **DNA (The Brain):** Each agent possesses an "DNA" sequence of 1,500 random 2D force vectors (Lifespan = 1500). Every frame, the agent reads a vector that alters its acceleration, velocity, and ultimately its position.
*   **Physics & Environment:** Agents are strictly bound by collision rules via `pygame-ce`. If an agent touches a wall, it dies instantly and stops moving.
*   **Population & Natural Selection:** Each generation consists of a swarm of 250 entities. Once all agents die, a Fitness score is calculated. The best-performing agents have a statistically higher chance of reproducing (weighted selection).
*   **Reproduction & Mutation:** Children inherit a crossover of two parents' DNA. A 1% mutation rate introduces entirely new random vectors to encourage further exploration.
*   **Elitism:** The single best agent of any generation is cloned perfectly into the next to ensure the AI never "unlearns" its most successful path.

## Technical Challenges & Optimizations

Building a Machine Learning model from scratch in pure Python presented significant architectural and performance hurdles:

*   **Escaping "Local Optima":** 
    * *Problem:* The AI initially got stuck behind walls that were physically closest to the final target (bird's-eye view).
    * *Solution:* Implemented a dynamic system of invisible **Checkpoints**. Fitness is now calculated based on the distance to the *next* checkpoint, forcing the AI to learn the maze step-by-step rather than blindly rushing the target.
*   **Curing the "Cowardly AI":** 
    * *Problem:* Initially, wall collisions penalized an agent's score by 50%. This made the AI too cowardly to explore narrow corridors, preferring to spin in safe, open spaces.
    * *Solution:* Removed the collision penalty entirely. Natural death against a wall is a sufficient physical boundary, encouraging aggressive exploration.
*   **CPU Bottleneck (The State Machine Solution):** 
    * *Problem:* Calculating physics for 250 entities over 1,500 steps at 60 FPS took roughly 1.5 hours, bottlenecked by Python's CPU execution.
    * *Solution:* Engineered a Dual-Mode State Machine:
        1.  **TRAINING Mode:** Visual rendering is disabled (flashed only once every 10 generations) and the framerate is unlocked for maximum "Fast-Forward" computation. `pygame.event.pump()` is injected to prevent OS crashes during heavy CPU loads.
        2.  **REPLAY Mode:** Triggered the moment an agent touches the final target. The simulation shifts to 60 FPS, hiding the swarm and exclusively looping the victorious agent's flawless trajectory.

## Evolution Stages

### 1. Generation 1: The Chaos
*(Insert GIF here: showing the initial swarm randomly crashing into the starting walls)*
![Gen 1 Chaos](gif/gif1_first_population)

### 2. Mid-Training: Learning the Checkpoints
*(Insert GIF here: showing the swarm struggling but successfully rounding the first corners)*
![Mid Training](gif/gif2_mid_training

### 3. Final Victory: REPLAY Mode
*(Insert GIF here: showing a single dot smoothly navigating the entire maze)*
![Victory](gif/gif3_victory_replay)

## 🚀 Execution

Ensure you have Python 3 installed.

```bash
# Install the required graphics engine
pip install pygame-ce

# Run the simulation
python main.py