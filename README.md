# Assignment One

**Name:** Fan Yi  
**Main file:** `assignment 1_FanYi.py`

This program contains two activities: Turtle Drawing and a keyword-based QA Bot.

## Requirements

- Python 3 with Tkinter support.
- A desktop environment to display the Turtle drawing window.
- No third-party Python packages are required.

Run the program locally in a terminal, such as PowerShell, or an IDE that supports keyboard input and desktop windows.

## Start the program

Download the Python file, open a terminal in the folder containing it, and run:

```powershell
python "assignment 1_FanYi.py"
```

On Windows, you can also use:

```powershell
py "assignment 1_FanYi.py"
```

Keep the quotation marks because the filename contains a space. If you rename the file, use its new name in the command.

The main menu appears:

```text
ASSIGNMENT ONE
1 - Turtle Drawing
2 - QA Bot
3 - Exit
Choose 1, 2 or 3:
```

Type a menu number and press **Enter**.

## 1. Turtle Drawing

Enter `1` to open the drawing window. The program draws 96 rotating squares whose colours and side lengths change with each iteration. Their overlapping outlines create a rainbow pattern. A square, triangle and five-pointed star also appear below the pattern.

Here, **Turtle** refers to Python's drawing library; the picture does not need to depict a turtle.

Close the drawing window to return to the main menu.

## 2. QA Bot

Enter `2` to start the bot. Type a keyword or an English question containing one of these keywords, then press **Enter**:

| Keyword | Example question |
| --- | --- |
| HKU | `What is HKU?` |
| robot | `Tell me about a robot.` |
| jetson | `What is Jetson?` |
| ai | `What does AI mean?` |
| human | `What is a human?` |

Example interaction:

```text
You: What is HKU?
Bot: HKU stands for The University of Hong Kong.
You: What does AI mean?
Bot: AI means Artificial Intelligence: computers performing tasks such as recognition.
You: quit
Bot: Goodbye!
```

Matching is case-insensitive and uses whole words. The bot also recognises `robots` and `humans`. If a question contains several supported keywords, it uses this priority:

```text
HKU > robot > Jetson > AI > human
```

An unknown topic receives a fallback response. Empty input prompts you to enter a question. This is a fixed-response bot using `if / elif / else`; it does not generate answers to arbitrary questions.

Type `quit`, `exit` or `bye` on its own to return to the main menu.

## 3. Exit

Enter `3` at the main menu to close the program. You can also press **Ctrl+C** in the terminal to end the session.

## Troubleshooting

- **File not found:** Open the terminal in the folder containing the file and check the filename, including spaces.
- **`python` is not recognised:** Try `py` on Windows, or check that Python 3 is installed and available in your terminal.
- **Tkinter error or no drawing window:** Use a local desktop Python installation with Tkinter support. You can check Tkinter with `python -m tkinter`; a small demonstration window should appear.
- **The terminal seems to be waiting after drawing:** Close the drawing window to continue using the main menu.
