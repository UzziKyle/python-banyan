from typing import Optional, Tuple, Union
from customtkinter import *


class UsernameInputDialog(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("ENTER YOUR NAME")

        self.name_label = CTkLabel(master=self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=(16, 8), pady=16)
        
        self.name_entry = CTkEntry(master=self, width=160, placeholder_text="Enter your name here...")
        self.name_entry.grid(row=0, column=1, padx=(0, 8), pady=16)
        
        self.accept_button = CTkButton(master=self, width=64, text="Accept")
        self.accept_button.grid(row=0, column=2, padx=(0, 16), pady=16)
        

if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.selling_input_dialog = UsernameInputDialog(master=self)
        
        
    app = Tester()
    app.withdraw()
    app.mainloop()
    