import tkinter as tk 
from tkinter import ttk 
import random 
from verses import ORTHODOX_BIBLE_VERSES 
 
class OrthodoxBibleQuoteGenerator: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("Orthodox Bible Quote Generator") 
        self.root.geometry("600x400") 
        self.root.resizable(True, True) 
 
        # Initialize style 
        self.setup_style() 
 
        # Create GUI elements 
        self.create_widgets() 
 
        # Generate first quote 
        self.generate_quote() 
 
    def setup_style(self): 
        self.style = ttk.Style() 
        self.style.configure("TFrame", background="#f0f0f0") 
        self.style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10)) 
        self.style.configure("Title.TLabel", font=("Helvetica", 16, "bold"), foreground="#8B4513") 
        self.style.configure("Reference.TLabel", font=("Helvetica", 12, "bold"), foreground="#8B0000") 
        self.style.configure("Accent.TButton", foreground="white", background="#8B4513", font=("Helvetica", 12, "bold")) 
 
    def create_widgets(self): 
        # Main frame 
        self.main_frame = ttk.Frame(self.root, padding="20", style="TFrame") 
        self.main_frame.pack(fill=tk.BOTH, expand=True) 
 
        # Title label 
        self.title_label = ttk.Label( 
            self.main_frame,  
            text="Daily Orthodox Bible Verse", 
            style="Title.TLabel" 
        ) 
        self.title_label.pack(pady=10) 
 
        # Quote frame 
        self.quote_frame = ttk.LabelFrame( 
            self.main_frame,  
            text="Today's Verse", 
            padding="20" 
        ) 
        self.quote_frame.pack(fill=tk.BOTH, expand=True, pady=10) 
 
        # Reference label 
        self.reference_label = ttk.Label( 
            self.quote_frame, 
            text="", 
            style="Reference.TLabel" 
        ) 
        self.reference_label.pack(pady=(0, 10)) 
 
        # Quote text 
        self.quote_text = tk.Text( 
            self.quote_frame, 
            wrap=tk.WORD, 
            height=6, 
            font=("Helvetica", 12), 
            padx=10, 
            pady=10, 
            bg="#FFF8DC", 
            relief=tk.FLAT 
        ) 
        self.quote_text.pack(fill=tk.BOTH, expand=True) 
 
        # Button frame 
        self.button_frame = ttk.Frame(self.main_frame) 
        self.button_frame.pack(pady=10) 
 
        # Generate button 
        self.generate_button = ttk.Button( 
            self.button_frame, 
            text="Get Orthodox Bible Verse", 
            command=self.generate_quote, 
            style="Accent.TButton" 
        ) 
        self.generate_button.pack(pady=5, ipadx=10, ipady=5) 
 
    def generate_quote(self): 
        """Generate and display a random Bible verse""" 
        reference, verse = random.choice(ORTHODOX_BIBLE_VERSES) 
 
        self.reference_label.config(text=reference) 
 
        self.quote_text.config(state=tk.NORMAL) 
        self.quote_text.delete(1.0, tk.END) 
        self.quote_text.insert(tk.END, verse) 
        self.quote_text.config(state=tk.DISABLED) 
 
if __name__ == "__main__": 
    root = tk.Tk() 
    app = OrthodoxBibleQuoteGenerator(root) 
    root.mainloop() 
