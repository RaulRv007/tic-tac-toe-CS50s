
# 🧠 Tic-Tac-Toe with Minimax AI

This project is a Python implementation of the classic **Tic-Tac-Toe** game, featuring an unbeatable AI powered by the **Minimax algorithm**. It's designed as part of the [CS50's Introduction to Artificial Intelligence with Python](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/home) course.

## 🎮 Features

- ✅ Play against an AI that never loses
- 🧠 Uses the Minimax algorithm for optimal decision-making
- 🧪 Clean and readable code with comments
- 🐍 Built with pure Python (no external libraries required)

## 📂 Project Structure

```
├── tictactoe.py     # Game logic and Minimax algorithm
├── test.py          # Optional test script (if included)
├── README.md        # You're here!
```

## 🧠 How It Works

The AI uses the **Minimax algorithm**, a recursive backtracking technique for decision-making in game theory. The algorithm simulates all possible moves and selects the one that maximizes the AI’s chances of winning while minimizing the player's chances.

- **Maximizing player:** AI (X)
- **Minimizing player:** Human (O)
- Evaluates terminal states: win, loss, or draw
- Explores all possible moves using recursion

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed

### Run the Game

Clone the repo and run the script:

```bash
git clone https://github.com/yourusername/tic-tac-toe-minimax.git
cd tic-tac-toe-minimax
python tictactoe.py
```

*Note: This version is a logic engine, not a GUI. Input/output is handled via terminal or scripts.*

## 📚 Learning Resources

- [CS50 AI Course](https://cs50.harvard.edu/ai/)
- [Minimax Algorithm – Wikipedia](https://en.wikipedia.org/wiki/Minimax)

## 🛠️ Future Improvements

- Add a graphical interface (e.g., with Tkinter or Pygame)
- Add difficulty levels by limiting Minimax depth
- Multiplayer mode

## 🧑‍💻 Author

**Your Name**  
GitHub: [@yourusername](https://github.com/yourusername)

## 📝 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
