# Icy Tower (PyOpenGL Remake)

## Overview

**Icy Tower** is a vertical platformer game built using Python. While it utilizes **Pygame** for window management, input handling, and audio, the core rendering engine is built entirely from scratch using direct **OpenGL (PyOpenGL)** commands.

The objective is simple: jump up floating platforms, climb as high as possible, and avoid falling off the bottom of the screen.

## Features

* **Hybrid Rendering:** Uses Pygame for the game loop and context, but all graphics (character, walls, platforms) are drawn using OpenGL vertices, quads, and triangles.
* **Infinite Scrolling:** The game world scrolls vertically endlessly as the player climbs higher.
* **Procedural Platforms:** Platforms are regenerated randomly above the screen as older ones fall below.
* **Score Tracking:** Your score increases as you ascend the tower.
* **Dynamic Elements:** Includes rotating 3D torches rendered in the 2D space.
* **Audio Integration:** Features background music and sound effects for jumping and game over states.

## Screenshots

| Gameplay | Game Over |
| :---: | :---: |
<img src="https://github.com/user-attachments/assets/a064756d-9653-49f2-93f2-160f5e569b00" width="400" alt="Gameplay Screen"> | <img src="https://github.com/user-attachments/assets/3027075f-3eec-46b6-873f-2d72207fc87e" width="400" alt="Game Over Screen"> |

## Prerequisites

To run this game, you need Python installed along with specific libraries.

* **Python 3.x**
* **Pygame** (For windowing and audio)
* **PyOpenGL** (For rendering)

## Installation

1.  **Clone or Download** the repository to your local machine.
2.  **Install Dependencies** using pip:

    ```bash
    pip install pygame PyOpenGL PyOpenGL_accelerate
    ```
    *(Note: `PyOpenGL_accelerate` is optional but recommended for better performance.)*

3.  **Verify Directory Structure:** Ensure your project folder looks like the structure below so the game can find its assets.

## Project Structure

Based on the source code, the critical file structure needed to run the game is:

```text
Project Root/
│
├── Icy Tower.py         # Main game executable script
├── Start Screen.png     # (Optional) For README display
├── Game Over.png        # (Optional) For README display
│
└── assets/              # Directory containing required audio files
    ├── Background.mp3
    ├── Jump.mp3
    └── Gameover 2.wav
```

## How to Play

Run the main script to start the game:
```bash
python "Icy Tower.py"
```
### Controls

| Key | Action |
| :--- | :--- |
| **A** | Move Left |
| **D** | Move Right |
| **SPACEBAR** | Jump |
| **R** | Restart Game (Only active on Game Over screen) |
