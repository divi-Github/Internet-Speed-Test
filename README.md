# Internet-Speed-Test
Building an Internet Speed Test GUI with Python (Tkinter). 
The primary goal of creating an internet speed test application is to provide users with a convenient way to measure their internet connection speed.
Internet speed refers to the rate at which data is transferred between your device and the internet. It’s typically measured in megabits per second (Mbps) and consists of two main components:
            Download Speed: How fast data is downloaded from the internet to your device.
            Upload Speed: How fast data is uploaded from your device to the internet.

Internet Speed Test (IST) Project Explanation

**********Overview**********
The Internet Speed Test (IST) project aims to create a simple application that measures your internet connection speed. It provides information about download speed, upload speed, and ping latency. The project is implemented using Python and the Tkinter library for the graphical user interface (GUI).

**********Code Explanation**********

1. Importing Modules:

The project starts by importing necessary modules:
    tkinter: Provides tools for creating GUI applications.
    ttk (from tkinter): Enhances the standard Tkinter widgets.
    speedtest: A library that allows you to measure internet speed programmatically.

2. Creating the ST() Function:
    The ST() function is the core of the project. It performs the following tasks:
          Initializes a Speedtest object.
          Measures download and upload speeds.
          Calculates and rounds the speeds to megabits per second (Mbps).
          Updates the labels in the GUI with the speed values.

3. Main Window (Tkinter):
    The main window is created using Tkinter:
          Title: “Internet Speed Test”
          Dimensions: 500x400 pixels
          Non-resizable (fixed size)

4. Widgets in the GUI:
   An input label displays the title: “Internet Speed Test.”
   A button labeled “Start Speed Test” triggers the ST() function when clicked.
   Three labels are initially empty:
          download_label: Displays the download speed.
          upload_label: Displays the upload speed.
          ping_label: Displays the ping latency.

5. Running the Tkinter Event Loop:
    The root.mainloop() call starts the event loop, allowing the GUI to respond to user interactions.

End of the Code:
The comment “END OF THE CODE” indicates the completion of the provided code snippet.
