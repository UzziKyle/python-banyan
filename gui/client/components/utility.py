from typing import Optional, Tuple, Union
from customtkinter import *
from threading import Thread, Event
from time import sleep


class Utility(CTkFrame):
    def __init__(self, master: any, 
                 width: int = 200, height: int = 200, 
                 corner_radius: int | str | None = 0, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = "transparent", 
                 border_color: str | Tuple[str, str] | None = None, 
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
        
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
                
        self.grid_columnconfigure(list(range(2)), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.button_holder = CTkFrame(master=self, fg_color="transparent")
        self.button_holder.grid(row=0, column=0, padx=(8, 0), sticky="ew")
        
        self.bid_button = CTkButton(master=self.button_holder, width=64, text="Bid", command=lambda: self.bid_input(), state="disabled")
        self.bid_button.grid(row=0, column=0, padx=0, pady=8)
        
        self.sell_button = CTkButton(master=self.button_holder, width=64, text="Sell", state="disabled")
        self.sell_button.grid(row=0, column=1, padx=(8, 0), pady=8)
        
        self.timer = CTkLabel(master=self, text=f"Time Left: 00:00:00")
        self.timer.grid(row=0, column=1, padx=8, sticky="e")
        
        self.timer_is_on = Event()
        
    def set_bid_button_command(self, function):
        function()   
        
    def set_sell_button_command(self, function):
        self.sell_button.configure(command=lambda: function())
        
    def activate(self) -> None:
        self.bid_button.configure(state="normal")
        self.sell_button.configure(state="normal")
        
    def deactivate(self) -> None:
        self.bid_button.configure(state="disabled")
        self.sell_button.configure(state="disabled") 
                 
    def start_countdown(self, temp: int) -> None:
        self.timer_is_on.set()
        self.activate() 

        while temp >-1:
            if not self.timer_is_on.is_set():
                break
                        
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins, secs = divmod(temp,60) 
            hours = 0
            
            if mins > 60:
                # divmod(firstvalue = temp//60, secondvalue 
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            self.timer.configure(text=f'Time Left: {hours:02d}:{mins:02d}:{secs:02d}')
                            
            # after every one sec the value of temp will be decremented
            # by one
            sleep(1)
            temp -= 1     
            
        self.timer_is_on.clear()
        self.deactivate()
                        
    def stop_countdown(self):
        self.timer_is_on.clear()
        self.deactivate()
        self.timer.configure(text=f"Time Left: 00:00:00")
                       


if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.utility = Utility(master=self)
            self.utility.grid(row=0, column=0, padx=10, pady=10)
        
        
    app = Tester()
    
    app.mainloop()
    