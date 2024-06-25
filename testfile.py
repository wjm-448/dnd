#It's the 5 jive!

import tkinter as tk
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

#============ Lists ========================================================================  
         
initial_stats = ["Initiative", "Combatant","AC","HP", "Status"]    

combatant_status = ["Player", "Ally", "Mob", "Neutral"]

player_disp_stats = ["Init", "Name", "DispAC", "DispHP", "Damage", "DispLRs", "UsedLRs", "Condition1", "Condition2", "Condition3"]

dm_stats = ["Key", "Init", "Name", "PCstat", "AC", "CurrHP", "MaxHP", "Damage", "LRs", "UsedLRs", "Condition1", "Condition2", "Condition3"]

all_stats = ["Key", "Current", "Breath", "Init", "Name", "PCstat", "AC", "DispAC", "CurrHP", "MaxHP", "DispHP", "Damage", "LRs", "DispLRs", "UsedLRs", "Condition1", "Condition2", "Condition3"]

conditions = ["Bane", "Bleeding", "Blinded", "Burning", "Charmed", "Deafened", "Difficult Terrain", "Exhausted", "Frightened", "Grappled", "Hidden", "Hunter's Marked", "Incapacitated", "Invisible", "Paralyzed", "Petrified", "Poisoned", "Polymorphed", "Prone", "Restrained", "Silenced", "Sleeping", "Slowed", "Stealthed", "Stunned", "Unconscious", "Wildshaped"]


#============ Combatant Functions ========================================================================

class Combatant:
    def __init__(self, key):
        self.Key = key
        self.Current = False
        self.Breath = "Alive"
        self.Init = 0
        self.Name = "(empty)"
        self.PCstat = "Mob"
        self.AC = 0
        self.DispAC = 15
        self.CurrHP = 0
        self.MaxHP = 0
        self.DispHP = 100
        self.Damage = 0
        self.LRs = 0
        self.DispLRs = 0
        self.UsedLRs = 0
        self.Condition1 = "[None]"
        self.Condition2 = "[None]"
        self.Condition3 = "[None]"

        self.action = "none"
       
    inflicted_damage = []
    assistance = []

    def target_creatures(self):
        if self.action == "attacking":
            set_damage()
        elif self.action == "healing":
            set_healing()
        else:
        
            pass

    def set_damage(self):
        
        damage_creatures()

    def set_healing(self):
        heal_creatures()

    def damage_creatures(self):
        for i, value in enumerate(targeted_creatures):
            pain = inflicted_damage[i]
            self[i].CurrHP -= pain
            self[i].DispHP -= pain
            self[i].Damage += pain
        pass

    def heal_creatures(self):
        for i, value in enumerate(targeted_creatures):
            aid = assistance[i]
            self[i].CurrHP += aid
            self[i].DispHP += aid
            self[i].Damage -= aid
        pass

#============ Encounter Functions ========================================================================

class Encounter:
    def __init__(self):
        self.round = 1
        self.curr_init = 30

    #upper bound for initiative 30, lower is -10
        self.upper = 30
        self.lower = -10



    def init_cycle(self):
        #make this a while loop?

        self.curr_init -= 1
        for i in enumerate(listcomb):
            comb_init = listcomb.init
            if self.curr_init == comb_init:
                take_turn()
        else: 
            pass

    def take_turn():
        
        pass

#============ Start Up Window ========================================================================
class WelcomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome")
        self.root.config(background="grey")
        self.root.geometry("600x200")
        
        self.label = tk.Label(self.root, 
                                text="Welcome to the D&D Combat Tracker!",
                                font=("Arial Black",20,"bold"),
                                background="grey",
                                fg="black")
                                
        self.label.pack(pady=20)
        
        
        self.button = tk.Button(self.root, 
                                    text="Start",
                                    font=("Arial Black",24,"bold"),
                                    command=self.open_new_window,
                                    background="blue",
                                    relief=RAISED,
                                    fg="white")
                                    
        self.button.pack(pady=10)
        
        
    def open_new_window(self):
        new_window = tk.Tk()
        Double_Screens(new_window)
        self.root.destroy()


#============ Start up of the DM Screen and the Player screens ========================================================================   
class Double_Screens:

    #============= DM Screen ========================================================================
    def __init__(self, root):
        self.root = root
        self.root.title("DM Screen")
        self.root.config(background="grey")
        self.root.geometry("1600x1000")
        
        
        self.combnum = 0
        self.slots = []
        self.combatant_names = []
        self.combatants = {}
        self.entries = []
        self.design_display()
        
        
        
    def design_display(self):
        
        DEFAULT_FG = "black"
        DEFAULT_FONT_STYLE = "Arial Black"
        DEFAULT_BD = 3
        DEFAULT_PAD_X = 3
        DEFAULT_PAD_Y= 3
        round = 0
        
        
    #============= Row 0 ========================================================================
        self.label = tk.Label(self.root, 
                                text="DM Screen",
                                font=(DEFAULT_FONT_STYLE, 14, "bold"),
                                fg="red",
                                background="black",
                                relief=RAISED,
                                bd=DEFAULT_BD,
                                padx=DEFAULT_PAD_X,
                                pady=DEFAULT_PAD_Y)

        self.label.grid(row=0,column=0,columnspan = 2, pady=10)
               
               
        
        
        
                                        
        
        
    #============= Row 1 ========================================================================
        
        self.combobox = ttk.Combobox(self.root, values=self.combatant_names)
        self.combobox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.combobox.set("Select Combatant")
        
        self.round_counter = tk.Label(self.root,
                                        text=f"Round: {round}",
                                        font=(DEFAULT_FONT_STYLE, 14, "bold"),
                                        fg="white",
                                        background="blue",
                                        relief=RAISED,
                                        bd=DEFAULT_BD,
                                        padx=DEFAULT_PAD_X,
                                        pady=DEFAULT_PAD_Y)
        self.round_counter.grid(row=1,column=2)
        
        self.heal_button = tk.Button(self.root,
                                        text="Heal",
                                        font=(DEFAULT_FONT_STYLE, 14),
                                        fg="black",
                                        background="green",
                                        command=self.healdemup,
                                        relief=RAISED,
                                        bd=DEFAULT_BD,
                                        padx=DEFAULT_PAD_X,
                                        pady=DEFAULT_PAD_Y)
        
        
        self.attack_button = tk.Button(self.root,
                                        text="Attack",
                                        font=(DEFAULT_FONT_STYLE, 14),
                                        fg="white",
                                        background="red",
                                        command=self.causedempain,
                                        relief=RAISED,
                                        bd=DEFAULT_BD,
                                        padx=DEFAULT_PAD_X,
                                        pady=DEFAULT_PAD_Y)
        
        
        self.other_action_button = tk.Button(self.root,
                                        text="Other",
                                        font=(DEFAULT_FONT_STYLE, 14),
                                        fg="white",
                                        background="blue",
                                        command=self.idkmybffjill,
                                        relief=RAISED,
                                        bd=DEFAULT_BD,
                                        padx=DEFAULT_PAD_X,
                                        pady=DEFAULT_PAD_Y)
                                        
        self.heal_button.grid(row=1, column=3)
        self.attack_button.grid(row=1, column=4)
        self.other_action_button.grid(row=1, column=5)
        
        

        
    #============= Row 2 ========================================================================
        
        self.info_labels = []
            
        for i, value in enumerate(dm_stats):
            self.stats = tk.Label(self.root,
                                    text=f"{value}",
                                    font=(DEFAULT_FONT_STYLE, 12),
                                    background="grey",
                                    bd=DEFAULT_BD,
                                    padx=DEFAULT_PAD_X,
                                    pady=DEFAULT_PAD_Y)
            self.stats.grid(row=2, column = i, padx=15)
            
            
    #============= Row 3 ========================================================================
            
            self.info_label = tk.Label(self.root, 
                                    text="", 
                                    font=(DEFAULT_FONT_STYLE, 10),
                                    background="grey",
                                    bd=DEFAULT_BD,
                                    padx=DEFAULT_PAD_X,
                                    pady=DEFAULT_PAD_Y)
                                    
            self.info_label.grid(row=3, column=i, padx=10, pady=5)
            self.info_labels.append(self.info_label)
            
            
        self.combobox.bind("<<ComboboxSelected>>", self.update_info_label)
            
            
    #============= Row 4 ========================================================================
            
        for i, value in enumerate(dm_stats[1:]):
            self.entry = tk.Entry(self.root, width=len(value)*2)
            self.entry.grid(row=4,column=i+1,padx=10)
            self.entries.append(self.entry)
        
        
    #============= Row 6 ========================================================================
        
        self.add_comb = tk.Button(self.root,
                                    text="Add Combatant",
                                    font=(DEFAULT_FONT_STYLE, 14, "bold"),
                                    fg=DEFAULT_FG,
                                    background="green",
                                    command=self.add_slot,
                                    relief=RAISED,
                                    bd=DEFAULT_BD,
                                    padx=DEFAULT_PAD_X,
                                    pady=DEFAULT_PAD_Y)
        
        self.del_comb = tk.Button(self.root,
                                    text="Delete Combatant",
                                    font=(DEFAULT_FONT_STYLE, 14, "bold"),
                                    fg="white",
                                    background="red",
                                    command=self.del_slot,
                                    relief=RAISED,
                                    bd=DEFAULT_BD,
                                    padx=DEFAULT_PAD_X,
                                    pady=DEFAULT_PAD_Y)
        
        self.add_comb.grid(row=6, column=0, columnspan=3, pady=15)
        self.del_comb.grid(row=6, column=3, columnspan=3, pady=15)
        
        self.update_combatant = tk.Button(self.root,
                                            text="Update Selected Combatant",
                                            font=(DEFAULT_FONT_STYLE, 14, "bold"),
                                            fg="white",
                                            command=self.update_comb_stat,
                                            background="blue",
                                            relief=RAISED,
                                            bd=DEFAULT_BD,
                                            padx=DEFAULT_PAD_X,
                                            pady=DEFAULT_PAD_Y)
        self.update_combatant.grid(row=6, column=6, columnspan = 3)
        
        self.con_button = tk.Button(self.root,
                                    text="Push to Player Screen",
                                    font=(DEFAULT_FONT_STYLE, 14, "bold"),
                                    fg="white",
                                    command=self.push_to_players,
                                    background="blue",
                                    relief=RAISED,
                                    bd=DEFAULT_BD,
                                    padx=DEFAULT_PAD_X,
                                    pady=DEFAULT_PAD_Y)

        self.con_button.grid(row=6, column=9, columnspan = 2)
        
        self.start_button = tk.Button(self.root,
                                    text="Start Combat",
                                    font=(DEFAULT_FONT_STYLE, 14, "bold"),
                                    fg="white",
                                    background="blue",
                                    command=self.initiate_combat,
                                    relief=RAISED,
                                    bd=DEFAULT_BD,
                                    padx=DEFAULT_PAD_X,
                                    pady=DEFAULT_PAD_Y)

        self.start_button.grid(row=6, column=11, columnspan = 2)


    #============= Row 8 ========================================================================

        for i, value in enumerate(dm_stats):
            self.stats = tk.Label(self.root,
                                    text=f"{value}",
                                    font=(DEFAULT_FONT_STYLE, 14, "bold"),
                                    fg="white",
                                    background="black",
                                    relief=RAISED,
                                    bd=DEFAULT_BD,
                                    padx=DEFAULT_PAD_X,
                                    pady=DEFAULT_PAD_Y)
            self.stats.grid(row=8, column = i, padx=15, pady=5)
        
        self.comb_dict = []    
    
    def healdemup(self):
        pass
        
    def causedempain(self):
        pass
        
    def idkmybffjill(self):
        pass
    
    
    def initiate_combat(self):
        print("Ding! Fight!")

    #============= Row 9 ========================================================================
    
    def update_info_label(self, event):
        selected_combatant = self.combobox.get()
        if selected_combatant in self.combatants:
            combatant = self.combatants[selected_combatant]
            for i, value in enumerate(dm_stats):
                stat_value = getattr(combatant, value, "N/a")
                self.info_labels[i].config(text=f"{stat_value}")
    
    def update_combobox(self):
        self.combobox['values'] = self.combatant_names


    def add_slot(self):
        i = self.combnum
        self.combnum += 1

        slot_widgets = []
        name = f"Combatant {i + 1}"
        self.combatant_names.append(name)

        new_combatant = Combatant(key=i)
        self.combatants[name] = new_combatant

        for j, value in enumerate(dm_stats):
            stat_value = getattr(new_combatant, value, "N/A")
            new_combatant_label = Label(self.root, text=stat_value)
            new_combatant_label.grid(row=9 + i, column=j, padx=15, pady=10)
            slot_widgets.append(new_combatant_label)

        self.slots.append(slot_widgets)
        self.update_combobox()
        
    def del_slot(self):           
        if self.slots:
            slot_widgets = self.slots.pop()
            for widget in slot_widgets:
                widget.destroy()
            self.combnum -= 1
            removed_name = self.combatant_names.pop()
            del self.combatants[removed_name] 
            self.update_combobox()
    
    def update_comb_stat(self):
        selected_comb_str = self.combobox.get()  # Get the selected combatant name from the combobox
    
        if selected_comb_str in self.combatants:  # Check if the selected combatant exists
            combatant = self.combatants[selected_comb_str]  # Get the corresponding combatant object
            
            
            for i, entry in enumerate(self.entries):  # Iterate over the entries
                update_stat = entry.get()  # Get the value from the entry widget
                
                if update_stat:  # If the entry is not empty
                  
                    setattr(combatant, dm_stats[i + 1], update_stat) # Update the combatant's attribute with the new value

                    self.slots[self.combnum - 1][i].config(text=update_stat) # Update the corresponding label in the slots

            self.update_displayed_combatants()  # Update the display to reflect changes
            
            for entry in self.entries:
                entry.delete(0, 'end')


    def update_displayed_combatants(self):
        # Iterate over the slots and update the labels to reflect the current combatant stats
        for i, (combatant_name, combatant) in enumerate(self.combatants.items()):
            slot_widgets = self.slots[i]
            for j, value in enumerate(dm_stats):
                stat_value = getattr(combatant, value, "N/A")
                slot_widgets[j].config(text=stat_value)
    

        
    def push_to_players(self):
        self.popup = Toplevel(self.root)
        self.popup.title("Confirm Setup")
        
        confirm_set = Button(self.popup,
                            text="Confirm",
                            fg="white",
                            background="green",
                            relief=RAISED,
                            command=self.enter_combatants)
                            
        
        reject_set = Button(self.popup,
                            text="Reject",
                            fg="white",
                            background="red",
                            relief=RAISED,
                            command=self.popup.destroy)
                            
        confirm_set.grid(row=0, column=0, pady=5, padx=5)
        reject_set.grid(row=0, column=1, padx=5)
        
        
    #============= Player Screen ========================================================================
    def update_player_screen(self):
        pass
                            
        

if __name__ == "__main__":
    root = tk.Tk()
    main_window = WelcomeGUI(root)
    root.mainloop()











