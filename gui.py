import tkinter as tk
from tkinter import messagebox

def show_recommendations():
    title = entry.get().strip()
    if title:
        recommendations = netflix_recommendation(title)
        messagebox.showinfo("Recommendations", "\n".join(recommendations))
    else:
        messagebox.showwarning("Input Error", "Please enter a valid title.")

# Create the GUI window
window = tk.Tk()
window.title("Netflix Recommendation System")

# Create GUI components
label = tk.Label(window, text="Enter a movie/TV show title:")
label.pack()

entry = tk.Entry(window, width=30)
entry.pack()

button = tk.Button(window, text="Show Recommendations", command=show_recommendations)
button.pack()

# Start the GUI event loop
window.mainloop()
