"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # SOLUTION by David Mutchler: 1. PUT YOUR NAME IN THE ABOVE LINE.

"""
Academic Integrity: I got help on this module from:
         PUT_HERE_THE_NAMES_OF_PEOPLE_WHO_HELPED_YOU_ON_THIS_MODULE_(IF_ANY).
"""  # DONE: If you got help from anyone on this module, list their names here.

import tkinter
from tkinter import ttk


def main():
    """Constructs a GUI with stuff on it."""
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root["background"] = "light gray"

    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #    ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    frame = ttk.Frame(root, padding=20)
    frame.grid()

    # -------------------------------------------------------------------------
    # DONE: 4. Now ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    button = ttk.Button(frame, text="Print hello and goodbye")
    button.grid()

    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing  "Hello"  followed by  "Goodbye"  on the Console. **
    #   Use two  print  statements, which will force a lambda expression.
    # -------------------------------------------------------------------------
    button["command"] = lambda: print_hello_and_goobye()

    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string "ok", but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    entry = ttk.Entry(frame)
    entry.grid()

    button2 = ttk.Button(frame, text="Print conditionally")
    button2["command"] = lambda: print_conditionally(entry)
    button2.grid()

    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #  _
    #      Pressing this new Button causes the STRING that the user typed
    #      in the FIRST Entry box to be printed N times on the Console,
    #        where N is the INTEGER that the user typed
    #        in the SECOND Entry box.
    #   _
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    # -------------------------------------------------------------------------
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    # -------------------------------------------------------------------------
    entry2 = ttk.Entry(frame)
    entry2.grid()

    button3 = ttk.Button(frame, text="Print N times")
    button3["command"] = lambda: print_n_times(entry, entry2)
    button3.grid()

    # -------------------------------------------------------------------------
    # DONE: 8. After reading and understanding the m5e module,
    #   -- Make your GUI widgets appear in a grid (details do not matter).
    # -------------------------------------------------------------------------
    button.grid(row=0, column=0)
    button2.grid(row=1, column=0)
    button3.grid(row=2, column=0)

    entry.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    # -------------------------------------------------------------------------
    # NOT DONE: 9. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------
    root.mainloop()


def print_hello_and_goobye():
    print("Hello")
    print("Goodbye")


def print_conditionally(entry):
    string = entry.get()
    if string == "ok":
        print("Hello")
    else:
        print("Goodbye")


def print_n_times(entry_for_string, entry_for_n):
    string = entry_for_string.get()
    n = int(entry_for_n.get())
    for _ in range(n):
        print(string)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
