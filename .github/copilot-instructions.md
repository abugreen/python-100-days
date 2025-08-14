# AI Assistant Instructions for python-100-days

## Project Overview
This repository contains Python learning exercises and PyQt GUI applications organized in a progressive learning structure:

1. Daily Python exercises (Day8-Day17) focused on fundamental concepts
2. PyQt GUI applications with various widget examples and a drawing board application
3. Mixed difficulty levels from basic scripts to complex applications

## Key Components

### PyQt Applications (`/pyqt/`)
- **Drawing Board Application**: A complex PyQt application that integrates with Arduino via UART
  - Key files: `drawing_board.py`, `uart_handler.py`
  - Architecture follows MVC pattern with UI components separated from communication logic
  - See `drawing_board_design.md` for detailed architecture overview

- **Widget Examples**: Various PyQt widget demonstrations
  - Layout examples: `Qboxlayout.py`, `qformlayout.py`
  - Input widgets: `qradiobutton.py`, `qcheckbox.py`, `qcombobox.py`
  - Complex widgets: `qtablewidget.py`, `qlistwidget.py`

### Python Learning Exercises
- **Day 8-17**: Progressive difficulty exercises
- Notable implementations:
  - Caesar Cipher (`Day8/main.py`): Text encryption example
  - Blackjack Game (`Day11/main.py`): Card game implementation
  - Quiz Game (`Day17/quiz-game-start/`): OOP-based quiz application

## Development Patterns

### PyQt Development
1. UI Layout Pattern:
```python
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # UI initialization code
```

2. Event Handling Pattern:
```python
def handle_event(self):
    sender = self.sender()
    # Event handling logic
```

### Project-Specific Conventions
1. File Structure:
   - UI files (.ui) are kept separate from Python code
   - Each day's exercises are in separate directories
   - PyQt applications have their own directory

2. Error Handling:
   - UART communication uses dedicated error channels
   - Games implement proper state management

## Common Operations

### Running PyQt Applications
1. Basic application template:
```python
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
```

### Debug Configuration
- VS Code launch configuration is available in `.vscode/launch.json`
- Use integrated terminal for debugging Python files

## Integration Points
1. UART Communication:
   - `uart_handler.py` manages serial communication
   - Baudrate options: 9600, 19200, 38400, 115200
   - Data format: ASCII strings in "x,y" format

## AI Development Guidelines
1. When modifying PyQt applications:
   - Preserve the UI initialization pattern
   - Keep UI and logic separate
   - Maintain error handling patterns for hardware communication

2. When adding new features:
   - Follow existing directory structure
   - Implement proper class inheritance for UI components
   - Document complex algorithms or hardware interactions

3. Code Style:
   - Follow PEP 8 guidelines
   - Use class-based structure for UI components
   - Implement proper event handling patterns for GUI elements
