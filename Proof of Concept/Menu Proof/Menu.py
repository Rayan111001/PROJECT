#Proof for a menu system that takes you to different windows for later use in the game
#Code for menu system from tutorial online at https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
import tkinter as tk


class Windows(tk.Tk):
    def __init__(self, *args, **kwargs): #Allows for extra arguments
        tk.Tk.__init__(self, *args, **kwargs)
        #Title
        self.wm_title("Test")
        self.geometry("600x600")

        #Create a frame and assign it to a container
        container = tk.Frame(self, height=400, width=600)
        #The region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        #Configuring the location of the container in the grid
        container.grid_rowconfigure(0, weight=1) #non zero weight allows for container to be scaled when window is larger than widgets
        container.grid_columnconfigure(0, weight=1)

        #Dictionary of frames
        self.frames = {}
        #Components of dictionary is the different frames that exist
        for F in (MainPage, PlayPage, AiPlayPage):  #List of different pages
            frame = F(container, self)

            #This window class acts as root window for all the frames
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #Method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        #Raises current frame to the top
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Menu")
        label.pack(padx=10, pady=10)

        #Switch window button calls show_frame method as lambda function
        switch_window_playPage_btn = tk.Button(self, text="Play Game", command=lambda: controller.show_frame(PlayPage), activebackground="red", bg= "#e88504", width=40)
        switch_window_playPage_btn.pack(pady=100)
        switch_window_aiplayPage_btn = tk.Button(self, text="AI Play", command=lambda: controller.show_frame(AiPlayPage), activebackground="red", bg= "#e88504", width=40)
        switch_window_aiplayPage_btn.pack()
        quit_btn = tk.Button(self, text="Quit", command=lambda: exit(), activebackground="red", bg= "#e88504", width=40)
        quit_btn.pack(pady=100)

class PlayPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Play Page")
        label.pack(padx=10, pady=10)

        #Switch window button calls show_frame method as lambda function
        switch_window_playPage_btn = tk.Button(self, text="Back to menu", command=lambda: controller.show_frame(MainPage),activebackground="red", bg= "#e88504")
        switch_window_playPage_btn.pack(side="bottom", fill=tk.X)

class AiPlayPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="AI Play")
        label.pack(padx=10, pady=10)

        #Switch window button calls show_frame method as lambda function
        switch_window_playPage_btn = tk.Button(self, text="Back to menu", command=lambda: controller.show_frame(MainPage),activebackground="red", bg= "#e88504")
        switch_window_playPage_btn.pack(side="bottom", fill=tk.X)

if __name__ == "__main__":
    testObj = Windows()
    testObj.mainloop()
