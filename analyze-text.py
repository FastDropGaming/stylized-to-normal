import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from collections import Counter
import os  # Import os for file path handling

def analyze_file(file_path):
    # Create counters for all characters
    character_frequency = Counter()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()  # Read the entire content at once

            # Count all characters
            for char in content:
                character_frequency[char] += 1

        # Generate output
        output_file_path = generate_output(character_frequency)

        # Show success message with output file path and Open button
        show_success_dialog(output_file_path)

    except FileNotFoundError:
        messagebox.showerror("Error", f"The file '{file_path}' was not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def generate_output(character_frequency):
    # Prepare output string
    output_lines = []

    # Sort characters by frequency (highest to lowest)
    sorted_characters = character_frequency.most_common()

    # All characters and their counts
    all_chars_line = " ".join(sorted(character_frequency.keys()))  # No replacement for spaces
    output_lines.append(all_chars_line)

    counts_line = " ".join(str(character_frequency[char]) for char in sorted(character_frequency.keys()))
    output_lines.append(counts_line)

    # Prepare output with sorted characters by frequency
    sorted_output_lines = [f"{char}: {count}" for char, count in sorted_characters]
    output_lines.append("\n".join(sorted_output_lines))

    output_file_content = "\n".join(output_lines)

    # Specify the output file path
    output_file_path = "output.txt"
    
    # Write output to a file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(output_file_content)

    return os.path.abspath(output_file_path)  # Return the full path of the output file

def close_all(success_dialog):
    success_dialog.destroy()  # Close the success dialog
    root.destroy()  # Close the main window

def show_success_dialog(output_file_path):
    # Create a new top-level window for success dialog
    success_dialog = Toplevel()
    success_dialog.title("Success")
    success_dialog.geometry("300x110")
    success_dialog.configure(bg="#212121")  # Set background color
    success_dialog.resizable(False, False)

    # Label to show output file path
    success_label = tk.Label(success_dialog, text=f"Output has been written to:\n{output_file_path}",
                             bg="#212121", fg="white")
    success_label.pack(pady=10)

    # Create buttons with pack layout
    open_button = tk.Button(success_dialog, text="Open", command=lambda: open_output_file(output_file_path),
                            bg="green", fg="white", width=10)
    close_button = tk.Button(success_dialog, text="Close", command=lambda: close_all(success_dialog),
                             bg="red", fg="white", width=10)

    # Pack buttons side by side in a frame
    button_frame = tk.Frame(success_dialog, bg="#212121")  # Frame to hold buttons
    button_frame.pack(pady=10)

    # Center the button frame
    open_button.pack(side=tk.LEFT, padx=25)
    close_button.pack(side=tk.RIGHT, padx=25)

    # Center the button frame
    button_frame.place(relx=0.5, rely=0.7, anchor='center')  # Adjusted to center under the text

def open_output_file(output_file_path):
    """Open the output file in the default text editor."""
    try:
        os.startfile(output_file_path)  # For Windows
    except Exception as e:
        messagebox.showerror("Error", f"Could not open the file: {e}")

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[ 
            ("Text Files", "*.txt"),
            ("CSV Files", "*.csv"),
            ("TSV Files", "*.tsv"),
            ("JSON Files", "*.json"),
            ("XML Files", "*.xml"),
            ("YAML Files", "*.yaml;*.yml"),
            ("INI Files", "*.ini"),
            ("LOG Files", "*.log"),
            ("Markdown Files", "*.md"),
            ("Bash Scripts", "*.sh"),
            ("Python Scripts", "*.py"),
            ("Properties Files", "*.properties"),
            ("All Files", "*.*")
        ]
    )
    if file_path:
        analyze_file(file_path)

# Create GUI
root = tk.Tk()
root.title("Character Analysis")
root.geometry("200x135")  # Set window size
root.configure(bg="#212121")  # Set background color
root.resizable(False, False)

# Button to open the file
open_button = tk.Button(root, text="Select File", command=open_file, bg="#424242", fg="white", width=20)
open_button.pack(pady=50)  # Center the button in the window

# Main loop of the GUI
root.mainloop()