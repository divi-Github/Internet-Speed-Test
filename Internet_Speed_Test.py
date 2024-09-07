'''
                            [INTERNET SPEED TEST {IST}]
                        Programming language used --> Python  
'''

# Importing Modules
import tkinter as tk
from tkinter import ttk
import speedtest as st

# Creating a function --> ST()
def ST():
    test = st.Speedtest()

    # Calculating Downloading Speed 
    d_speed = test.download()
    d_speed = round(d_speed/10**6,4)

    download_label.config(text=f"Download Speed [in Mbps] --> {d_speed}")
    # print("Download Speed [in Mbps] --> ", d_speed)


    # Calculating Uploading Speed
    u_speed = test.upload()
    u_speed = round(u_speed/10**6,4)

    upload_label.config(text=f"Upload Speed [in Mbps] --> {u_speed}")
    # print("Upload Speed [in Mbps] --> ", u_speed)

    # Ping
    ping = test.results.ping
    ping_label.config(text=f"Ping [in Mbps] --> {ping}")
    # print("Ping --> ", ping)

# ST()
# Main Window (using tkinter)

root = tk.Tk()
root.title("Internet Speed Test")

root.geometry("500x400")
root.resizable(False, False)

# creates label widgets with a text
input_label = tk.Label(root, text="!! Internet Speed Test !!")
input_label.pack(padx=10, pady=20)

# Creating a Button --> "Start Speed Test"
start_button = ttk.Button(root, text = "Start Speed Test", command=ST)
start_button.pack(pady=10)

# Display results
download_label = ttk.Label(root, text="Download Speed [in Mbps] --> ")
download_label.pack(pady=5)

upload_label = ttk.Label(root, text="Upload Speed [in Mbps] --> ")
upload_label.pack(pady=5)

ping_label = ttk.Label(root, text="Ping [in Mbps] --> ")
ping_label.pack(pady=5)

# Running the Tkinter Event Loop
root.mainloop()

'''********************END OF THE CODE********************'''