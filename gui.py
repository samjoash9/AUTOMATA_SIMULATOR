import tkinter as tk
from tkinter import messagebox
from utils import *
from simulator import states, simulate_states, q0

class DFA_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HTML Tag DFA Simulator")

        self.input_label = tk.Label(root, text="Enter an HTML tag (e.g., <p>Hello</p>):")
        self.input_label.pack(pady=5)

        self.input_entry = tk.Entry(root, width=40)
        self.input_entry.pack(pady=5)

        self.simulate_button = tk.Button(root, text="Simulate", command=self.simulate)
        self.simulate_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=('Courier', 12), wraplength=400, justify="left")
        self.result_label.pack(pady=10)

    def simulate(self):
        input_string = self.input_entry.get().strip()
        processed = process_input_string(input_string)

        if not processed:
            messagebox.showerror("Error", "Invalid HTML tag format.")
            self.result_label.config(text="")
            return

        self.result_label.config(text="→ ", fg="black")

        try:
            # Capture transitions as string
            output = []

            def wrapped_simulate(state, input_string, i):
                output.append(f"({state.name})->")
                if state.type == 'final':
                    return True
                if len(state.outgoing) == 0 or i >= len(input_string):
                    return False
                if input_string[i] in state.outgoing:
                    return wrapped_simulate(states[state.outgoing[input_string[i]]], input_string, i + 1)
                return False

            result = wrapped_simulate(q0, processed, 0)

            trace = "".join(output)
            trace += "Accepted ✅" if result else "Rejected ❌"

            self.result_label.config(text=trace, fg="green" if result else "red")

        except Exception as e:
            messagebox.showerror("Simulation Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    gui = DFA_GUI(root)
    root.mainloop()
