# Ice-Hockey


Ice Hockey is a simple yet exciting 2D ice hockey game built with Pygame. Control your paddle, score points, and challenge an AI opponent with fuzzy logic that adapts its movement speed based on the ball's distance!

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Settings](#game-settings)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Acknowledgments](#acknowledgments)

## Features

- Single-player mode with AI-powered opponent paddle
- Adjustable difficulty levels: Easy, Medium, Hard
- Fuzzy logic-based AI for realistic movement
- Customizable settings for game dimensions, paddle speed, and win conditions
- User-friendly interface with simple keyboard controls

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/IceHockey.git
    cd IceHockey
    ```

2. **Install dependencies**:
   - Ensure you have Python and Pygame installed:
    ```bash
    pip install pygame
    ```

3. **Run the game**:
    ```bash
    python ice_hockey.py
    ```

## How to Play

1. Run the game and enter your username.
2. Select a difficulty level (Easy, Medium, Hard).
3. Set the maximum points required to win.
4. Start the game by typing "START" and pressing Enter.

Use the **Up** and **Down** arrow keys to control your paddle. Score points by getting the ball past the opponent's paddle.

## Game Settings

- **Difficulty Levels**: Controls the ball speed and the AI paddle response.
- **Paddle and Ball Settings**: Defined in the code for easy customization.
- **Colors**: The game uses a Maya Blue theme (`RGB: 115, 194, 251`) for the background and a classic white paddle and ball.

## Project Structure

- **`ice_hockey.py`**: Main game code with Paddle, Ball, and fuzzy logic functions.
- **README.md**: Documentation for the game.

## Technologies Used

- **Python**
- **Pygame**: For creating the game window, handling inputs, and rendering graphics.

## Acknowledgments

- Pygame documentation and community examples for providing insights on 2D game development.
  
Enjoy playing Ice Hockey, and feel free to contribute to enhance the game!
