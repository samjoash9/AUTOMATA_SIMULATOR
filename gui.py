import tkinter as tk
from tkinter import ttk, messagebox
from utils import *
from simulator import states, simulate_states, q0

class ModernDFA_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HTML Tag DFA Simulator")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f2f5")
        
        # Set custom theme colors
        self.bg_color = "#f0f2f5"
        self.primary_color = "#4a6fa5"
        self.secondary_color = "#166088"
        self.accent_color = "#4fc3f7"
        self.error_color = "#ff5252"
        self.success_color = "#4caf50"
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background=self.bg_color)
        self.style.configure('TLabel', background=self.bg_color, font=('Segoe UI', 10))
        self.style.configure('TButton', font=('Segoe UI', 10, 'bold'), padding=6)
        self.style.map('TButton',
                      foreground=[('pressed', 'black'), ('active', 'black')],
                      background=[('pressed', self.secondary_color), ('active', self.primary_color)])
        self.style.configure('Primary.TButton', background=self.primary_color, foreground='black')
        
        # Main container
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.title_label = ttk.Label(
            self.header_frame,
            text="HTML Tag Validator",
            font=('Segoe UI', 18, 'bold'),
            foreground=self.secondary_color
        )
        self.title_label.pack(side=tk.LEFT)
        
        # Input section
        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.pack(fill=tk.X, pady=10)
        
        self.input_label = ttk.Label(
            self.input_frame,
            text="Enter HTML Tag:",
            font=('Segoe UI', 10),
            foreground="#555555"
        )
        self.input_label.pack(anchor=tk.W)
        
        self.input_entry = ttk.Entry(
            self.input_frame,
            width=50,
            font=('Segoe UI', 10)
        )
        self.input_entry.pack(fill=tk.X, pady=5, ipady=8)
        self.input_entry.bind('<Return>', lambda e: self.simulate())
        
        # Example text
        self.example_label = ttk.Label(
            self.input_frame,
            text="Examples: <p>Hello</p>, <div class='header'>",
            font=('Segoe UI', 8),
            foreground="#888888"
        )
        self.example_label.pack(anchor=tk.W)
        
        # Button
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=10)
        
        self.simulate_button = ttk.Button(
            self.button_frame,
            text="Validate Tag",
            style='Primary.TButton',
            command=self.simulate
        )
        self.simulate_button.pack(ipadx=20, ipady=5)
        
        # Result section
        self.result_frame = ttk.Frame(self.main_frame)
        self.result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=('Consolas', 11),
            wraplength=550,
            justify="left",
            bg="white",
            bd=2,
            relief=tk.GROOVE,
            padx=10,
            pady=10
        )
        self.result_label.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_bar = ttk.Frame(self.main_frame, height=20)
        self.status_bar.pack(fill=tk.X, pady=(10, 0))
        self.status_label = ttk.Label(
            self.status_bar,
            text="Ready",
            foreground="#666666",
            font=('Segoe UI', 8)
        )
        self.status_label.pack(side=tk.LEFT)
        
        # Focus on entry
        self.input_entry.focus_set()
        
    def simulate(self):
        input_string = self.input_entry.get().strip()
        if not input_string:
            messagebox.showwarning("Empty Input", "Please enter an HTML tag to validate.")
            return
            
        self.status_label.config(text="Processing...")
        self.root.update()
        
        processed = process_input_string(input_string)
        
        if not processed:
            self.status_label.config(text="Invalid input format")
            messagebox.showerror("Error", "Invalid HTML tag format.")
            self.result_label.config(text="", bg="white")
            return
        
        self.result_label.config(text="→ ", fg="black", bg="white")
        
        try:
            # Capture transitions as string
            output = []
            
            def wrapped_simulate(state, input_string, i):
                output.append(f"({state.name}) → ")
                if state.type == 'final':
                    return True
                if len(state.outgoing) == 0 or i >= len(input_string):
                    return False
                if input_string[i] in state.outgoing:
                    return wrapped_simulate(states[state.outgoing[input_string[i]]], input_string, i + 1)
                return False
            
            result = wrapped_simulate(q0, processed, 0)
            
            trace = "".join(output)
            trace = trace[:-3]  # Remove the last arrow
            
            if result:
                trace += "\n\n✅ Valid HTML Tag"
                self.result_label.config(text=trace, fg=self.success_color, bg="#f0fff0")
            else:
                trace += "\n\n❌ Invalid HTML Tag"
                self.result_label.config(text=trace, fg=self.error_color, bg="#fff0f0")
            
            self.status_label.config(text="Ready")
            
        except Exception as e:
            self.status_label.config(text="Error occurred")
            messagebox.showerror("Simulation Error", str(e))
            self.result_label.config(text="", bg="white")


if __name__ == "__main__":
    root = tk.Tk()
    
    # Set window icon (replace with your own icon if available)
    try:
        root.iconbitmap("icon.ico")  # Place an icon file in the same directory
    except:
        pass
    
    # Set minimum window size
    root.minsize(500, 400)
    
    # Add some visual effects
    root.option_add('*tearOff', False)  # Remove ugly tear-off menus
    
    gui = ModernDFA_GUI(root)
    root.mainloop()