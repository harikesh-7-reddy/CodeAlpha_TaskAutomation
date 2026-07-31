# Task Automation with Python

## Description
This project automates a simple task by moving all `.jpg` files from a source folder to a destination folder. It uses Python's built-in `os` and `shutil` modules.

## Features
- Moves all `.jpg` files automatically.
- Creates the destination folder if it does not exist.
- Leaves other file types unchanged.
- Displays the names of the moved files.

## Requirements
- Python 3.x

## Project Structure

```
TaskAutomation/
│── task_automation.py
│── README.md
│── source/
└── destination/
```

## How to Run

1. Place your `.jpg` files inside the `source` folder.
2. Open a terminal in the project folder.
3. Run the program:

```bash
python task_automation.py
```

## Sample Output

```
image1.jpg moved successfully.
image2.jpg moved successfully.
photo.jpg moved successfully.

All JPG files have been moved.
```

## Concepts Used
- os
- shutil
- loops
- if statements
- file handling

## Author
Beginner Python Project
