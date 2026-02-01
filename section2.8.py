import tkinter as tk
from tkinter import colorchooser, filedialog

class GraphicsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Програма Графіка")
        
        self.color = "black"
        self.tool = "line" 
        self.start_x = None
        self.start_y = None
        self.temp_item = None

        controls = tk.Frame(self.root)
        controls.pack(side="top", fill="x", padx=5, pady=5)

        tk.Button(controls, text="Колір", command=self.choose_color).pack(side="left", padx=2)
        tk.Button(controls, text="Лінія", command=lambda: self.set_tool("line")).pack(side="left", padx=2)
        tk.Button(controls, text="Коло", command=lambda: self.set_tool("circle")).pack(side="left", padx=2)
        tk.Button(controls, text="Очистити", command=self.clear_canvas).pack(side="left", padx=2)
        tk.Button(controls, text="Зберегти (.ps)", command=self.save_canvas).pack(side="right", padx=2)

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white", cursor="cross")
        self.canvas.pack(padx=10, pady=10)

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def choose_color(self):
        color = colorchooser.askcolor(title="Оберіть колір")[1]
        if color:
            self.color = color

    def set_tool(self, tool):
        self.tool = tool

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        path = filedialog.asksaveasfilename(defaultextension=".ps", filetypes=[("PostScript", "*.ps")])
        if path:
            self.canvas.postscript(file=path)

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        if self.temp_item:
            self.canvas.delete(self.temp_item)
            
        if self.tool == "line":
            self.temp_item = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color)
        elif self.tool == "circle":
            self.temp_item = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=self.color)

    def on_release(self, event):
        self.temp_item = None 

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphicsApp(root)
    root.mainloop()