# Name: Fan Yi
# Assignment One

"""Turtle Drawing and QA Bot. Run this file with Python 3 on a desktop."""

import colorsys
import re
import turtle


def draw_polygon(pen, sides, length):
    """Draw a closed regular polygon using a structured for loop."""
    for side in range(sides):
        pen.forward(length)
        pen.left(360 / sides)


def draw_star(pen, length):
    """Draw a five-pointed star."""
    for point in range(5):
        pen.forward(length)
        pen.right(144)


def write_label(pen, x, y, text, size=12):
    pen.penup()
    pen.goto(x, y)
    pen.color("#e6edf9")
    pen.write(text, align="center", font=("Arial", size, "normal"))


def turtle_drawing():
    """Create a rainbow square mandala with triangle and star details."""
    screen = turtle.Screen()
    screen.setup(860, 740)
    screen.title("Assignment One | Rainbow Orbit")
    screen.bgcolor("#0b1024")
    screen.colormode(1.0)
    screen.tracer(0)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(1.4)

    write_label(pen, 0, 300, "RAINBOW ORBIT", 24)
    write_label(pen, 0, 273, "A mandala made from rotating, growing squares")

    # Both hue and side length change on every iteration.
    # The inner loop in draw_polygon draws each square's four sides.
    for step in range(96):
        length = 32 + step * 3.2
        pen.penup()
        pen.home()
        pen.setheading(step * 7.5)
        pen.backward(length / 2)
        pen.right(90)
        pen.forward(length / 2)
        pen.left(90)
        pen.pencolor(colorsys.hsv_to_rgb(step / 96, 0.78, 1.0))
        pen.pendown()
        draw_polygon(pen, 4, length)
        # Update in batches so the viewer can see the pattern grow.
        if step % 8 == 0:
            screen.update()

    # Three small geometric signatures beneath the mandala.
    for index, shape in enumerate(("SQUARE", "TRIANGLE", "STAR")):
        x = -240 + index * 240
        pen.penup()
        pen.goto(x - 28, -235 if shape == "STAR" else -255)
        pen.setheading(0)
        pen.pencolor(("#53e4ec", "#ffcd70", "#f688db")[index])
        pen.pensize(2.5)
        pen.pendown()
        if shape == "SQUARE":
            draw_polygon(pen, 4, 48)
        elif shape == "TRIANGLE":
            draw_polygon(pen, 3, 58)
        else:
            draw_star(pen, 62)
        write_label(pen, x, -294, shape, 10)

    write_label(pen, 0, -333, "96 squares  |  changing colour + length  |  nested for loops", 11)
    screen.update()
    print("Drawing complete. Close the drawing window to return to the menu.")
    screen.mainloop()


def answer_question(question):
    """Match whole keywords; use a fixed priority if several are present."""
    words = re.findall(r"[a-z0-9]+", question.lower())
    if not words:
        return "Please type a question about HKU, robot, Jetson, AI or human."
    elif "hku" in words:
        return "HKU stands for The University of Hong Kong."
    elif "robot" in words or "robots" in words:
        return "A robot is a programmable machine that can sense and act."
    elif "jetson" in words:
        return "NVIDIA Jetson is a computing platform for AI and robotics at the edge."
    elif "ai" in words:
        return "AI means Artificial Intelligence: computers performing tasks such as recognition."
    elif "human" in words or "humans" in words:
        return "A human is a person; humans design, train and use robots and AI systems."
    else:
        return "Sorry, I do not know that topic. Try HKU, robot, Jetson, AI or human."


def qa_bot():
    print("\nQUESTION ANSWERING BOT")
    print("Topics: HKU, robot, Jetson, AI, human. Type 'quit' to return.")
    print("For multiple keywords, priority is HKU > robot > Jetson > AI > human.")
    while True:
        question = input("You: ").strip()
        if question.lower() in ("quit", "exit", "bye"):
            print("Bot: Goodbye!")
            break
        else:
            print("Bot:", answer_question(question))


def main():
    while True:
        print("\nASSIGNMENT ONE")
        print("1 - Turtle Drawing\n2 - QA Bot\n3 - Exit")
        choice = input("Choose 1, 2 or 3: ").strip()
        if choice == "1":
            try:
                turtle_drawing()
            except turtle.Terminator:
                print("Drawing window closed.")
        elif choice == "2":
            qa_bot()
        elif choice == "3":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nSession ended.")
