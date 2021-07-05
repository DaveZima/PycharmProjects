#def example2():

root.title("Dave is Great")

user_name = tk.StringVar()

name_label = ttk.Label(root,text="Name: ")
name_label.pack(side="left",padx=(0,10)) # add 10 pixel spacing
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(root,text="Greet",command=greet)
greet_button.pack(side="left",fill="x",expand=True)

def example3():

    root = tk.Tk()

    # side = anchor point
    # fill x=horizontal y=vertical both=x+y
    # container considers multiple element relationships,priorities
    # expand - request as much space as possible
    tk.Label(root, text="Label 1", bg="green").pack(side="left", fill="both", expand=True)
    tk.Label(root, text="Label 2", bg="red").pack(side="top")

    root.mainloop()

def example4():
    root = tk.Tk()

    # Create a frame to better manage the labels
    # Frame becomes the first element in the root
    # Element interaction for the 3rd label is now with the frame
    main = ttk.Frame(root)

    # pack is an algorithm for component/element interaction
    # it is a TKinter geometry manager
    main.pack(side="left", fill="both", expand=True)

    # place the first two labels in the frame
    tk.Label(main, text="Label top", bg="red").pack(side="top", fill="both", expand=True)
    tk.Label(main, text="Label top", bg="red").pack(side="top", fill="both", expand=True)

    tk.Label(root, text="Label left", bg="green").pack(
        side="left", expand=True, fill="both"
    )

    root.mainloop()

def greet():
    # user_name has global scope
    # or expression within f variable
    print(f"Hello {user_name.get() or 'World'}")  # user_name is global

########
# main #
########

root = tk.Tk()

# Create a frame to better manage the labels
# Frame becomes the first element in the root
# Element interaction for the 3rd label is now with the frame
main = ttk.Frame(root)

# pack is an algorithm for component/element interaction
main.pack(side="left", fill="both", expand=True)

# place the first two labels in the frame
tk.Label(main, text="Label top", bg="red").pack(side="top", fill="both", expand=True)
tk.Label(main, text="Label top", bg="red").pack(side="top", fill="both", expand=True)

tk.Label(root, text="Label left", bg="green").pack(
    side="left", expand=True, fill="both"
)

root.mainloop()


