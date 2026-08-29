# mouse-automation-77

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

mouse-automation-77 is a Python autoclicker built for precise, repetitive mouse input. It handles high-frequency clicking with configurable timing and controls for testing, automation, and productivity tasks.

## Features
- Click intervals configurable down to 0.01 seconds
- Support for left, right, and middle mouse buttons
- Toggle automation using the F8 hotkey
- Optional click limit with automatic termination

## Installation

```bash
git clone https://github.com/Developer/mouse-automation-77.git
cd mouse-automation-77
pip install pyautogui
```

## Usage

Run from the command line with your preferred settings:

```bash
python main.py --interval 0.05 --button left --limit 500
```

This performs 500 left clicks at 50ms intervals. Press F8 during execution to stop the process early.