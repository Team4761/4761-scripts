#!/usr/bin/python2

from Tkinter import *
import re
import subprocess
import tkFileDialog
import tkMessageBox

class App:
	def __init__(self, master):
		self.master = master
		self.master.title("RasPi Movie GUI")
		self.file_to_play = None
		self.movie_player_command = "omxplayer"
		
		self.loop_l = Label(master, text="Loop:")
		self.loop_v = StringVar()
		self.loop_cb = Checkbutton(master, onvalue="--loop", offvalue="", variable=self.loop_v)
		self.loop_cb.select()
		
		self.play_b = Button(master, text="Play", command=self.play)
		
		self.menubar = Menu(master)
		master.config(menu=self.menubar)

		filemenu = Menu(self.menubar)
		filemenu.add_command(label="Open Movie...", command=self.choose_file)
		filemenu.add_command(label="Quit", command=master.quit)
		self.menubar.add_cascade(label="File", menu=filemenu)
		
		self.loop_l.grid(row=0, column=0)
		self.loop_cb.grid(row=0, column=1)
		self.play_b.grid(row=1, column=0, columnspan=2)
	
	def choose_file(self):
		self.file_to_play = tkFileDialog.askopenfilename()
		if self.file_to_play not in [None, (), '']:
			split_path = re.split('/', self.file_to_play)
			self.master.title("RasPi Movie GUI - " + split_path[len(split_path) - 1])
			#self.movie_text.set(split_path[len(split_path) - 1])
		else:
			self.master.title("RasPi Movie GUI")
	
	def play(self):
		if self.file_to_play in [None, (), '']:
			tkMessageBox.showwarning("Play Movie", "No movie has been selected!")
		else:
			args = " ".join([self.loop_v.get()])
			subprocess.Popen("{cmd} {args} -b \"{movie}\"".format(cmd=self.movie_player_command, args=args, movie=self.file_to_play), shell=True)

root = Tk()

app = App(root)

root.mainloop()
root.destroy()
