#!/usr/bin/python

_NMR_Website_ = "http://www.nmr.chem.uu.nl/"
__Author__    = "  M. Krzeminski  "
__version__   = 1.0
__Name__      = "SAMPLEX"
__Contact__   = "mkrzemin@nmr.chem.uu.nl"
__Title__     = "SAMPLEX by MK, KL and AB"

Bijvoet_symbol_3_4 = """\
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\
BkgQgeYUUYAb4IAOhUD+yd2m/e57n00BAQA7"""

import threading as _th
import string, sys, os, math
import re, time, commands, random
import tempfile as _tmpf
from Tkinter import *
import tkFileDialog as _tkF, tkMessageBox as _tkM

##########################################################
#                                                        #
#        Definition of functions and classes.            #
#                                                        #
##########################################################

class Preparation(Frame):
	""" This class allows to retrieve all parameters of the system
	    necessary to perform all calculations. """

	def __init__(self, master=None, filename=""):

		self.cd         = commands.getoutput("pwd")
		self.input_data = {}
		self.filename   = filename

		if _graphical:
			self.master = master
			Frame.__init__(self, self.master)
			self.master.title(__Title__)
			self.build()

		self.load()

	def title(self, master=None):
		self.flag = PhotoImage(data=Bijvoet_symbol_3_4)
		Label(master, image=self.flag).grid(column=0, row=0, rowspan=3)

		self.titre = Text(master, relief=GROOVE, padx=50, pady=10, width=50, height=3, takefocus=0, foreground="#660000")
		self.titre.insert(END, "Welcome to " + __Name__ + os.linesep + "Prediction of Perturbed regions from NMR chemical shifts")
		self.titre.tag_add("title",    1.0,  1.18)
		self.titre.tag_add("subtitle", 1.19, END )
		self.titre.tag_config("title",    font="times 14 italic bold", justify=CENTER, wrap=WORD)
		self.titre.tag_config("subtitle", font="times 12 italic bold", justify=CENTER, wrap=WORD)
		self.titre.grid(column=1, row=0, columnspan=4, rowspan=3)
		

	def build(self):
		"""
		Builds up graphical interface
		"""
		
		# Set row and column sizes
		self.master.columnconfigure(tuple(range(6)), weight=1)
		self.master.rowconfigure(20, weight=1)		# The canvas

		# Title
		self.title(self.master)

		# A way to access the websites of each author
		authors = {1: {"name":__Author__           , "site":"mkrzemin"},
		           2: {"name":"  K. Loth  "        , "site":"kloth"   },
			   3: {"name":"  A.M.J.J. Bonvin  ", "site":"abonvin" }}

		for i in authors.keys():
			authors[i]["l_aut"] = Label(self.master, text=authors[i]["name"], anchor="center", relief="flat",\
			                            cursor="right_ptr",padx=0, pady=0, width=20, font="times 10 bold", foreground="#0000FF")
			authors[i]["l_aut"].grid(column=5, row=i-1, columnspan=2)
			authors[i]["l_aut"].bind("<Button-1>", func=lambda event, name=authors[i]["site"]: self._website(who=name))


		# Short help
		Button(self.master, font="Times 10 bold", cursor="spraycan", bg="grey75", fg="orange", bd=3, pady=1, command=self.introduction, text="Short Introduction", anchor=CENTER, takefocus=1).grid(column=0, row=10 , sticky=E+W, columnspan=7)



		# Creation of the middle frame
		self.main_info_can = Canvas(self.master, bd=0, height=250, bg="#eeeee6", highlightcolor="#eeeee6", highlightthickness=0, confine="true", relief=FLAT, takefocus=0)
		self.main_info_can.grid(column=0, row=20, columnspan=6, sticky=N+S+E+W)

		self.VScrMainInfo = Scrollbar(self.master, orient=VERTICAL, command=self.main_info_can.yview, takefocus=1, repeatdelay=300, repeatinterval=100)
		self.VScrMainInfo.grid(column=6, row=20, sticky=N+S)
		self.main_info_can["yscrollcommand"] = self.VScrMainInfo.set
		self.HScrMainInfo = Scrollbar(self.master, orient=HORIZONTAL, command=self.main_info_can.xview)
		self.HScrMainInfo.grid(column=0, row=21, columnspan=6, sticky=E+W)
		self.main_info_can["xscrollcommand"] = self.HScrMainInfo.set

		self.nottodestroy = self.master.winfo_children()

		self.main_info_can.update_idletasks()
		self.main_info_frame = Frame(self.main_info_can, bd=0, relief=FLAT)
		self.main_info_can.create_window(0, 0, anchor=NW, window=self.main_info_frame)

		can_size = int(self.main_info_can.cget("width"))
		for i in range(8): self.main_info_frame.columnconfigure(i, minsize=can_size/6.)

		
		# Filling the middle frame

		############################# 
		#   General Informations    #
		#############################

		Label(self.main_info_frame, text="General Information",   justify="center", relief="ridge", padx=50, font="times 25 italic bold", foreground="#336600", takefocus=0).grid(column=0, row=0,  sticky=S+E+W, columnspan=9)
		self.l_wd = Label(self.main_info_frame, text="Working Directory",    takefocus=0); self.l_wd.grid(column=0, row=5 , columnspan=2, sticky=E)
		self.l_sf = Label(self.main_info_frame, text="Structures File",      takefocus=0); self.l_sf.grid(column=0, row=10, columnspan=2, sticky=E)

		self.e_wd = Entry(self.main_info_frame, cursor="pencil", font="Times 17", takefocus=1); self.e_wd.grid(column=2, row=5, sticky=E+W, columnspan=5)	# Working directory
		self.e_sf = Entry(self.main_info_frame, cursor="pencil", font="Times 17", takefocus=1); self.e_sf.grid(column=2, row=10, sticky=E+W, columnspan=5)	# Structure file

		self.b_wd = Button(self.main_info_frame, font="Times 16", cursor="hand2", command=self.browsewd, text="Browse", anchor=CENTER, takefocus=1).grid(column=7, row=5 , sticky=E+W)
		self.b_sf = Button(self.main_info_frame, font="Times 16", cursor="hand2", command=self.browsesf, text="Browse", anchor=CENTER, takefocus=1).grid(column=7, row=10, sticky=E+W)

		self.separator(12, 50)

		self.l_ef = Label(self.main_info_frame, text="Experimental file",   takefocus=0); self.l_ef.grid(column=0, row=15,  columnspan=2, sticky=E)
		self.e_ef = Entry(self.main_info_frame, cursor="pencil", font="Times 17", takefocus=1);	self.e_ef.grid(column=2, row=15, sticky=E+W, columnspan=5)	# Experimental file
		self.b_ef = Button(self.main_info_frame, font="Times 16", cursor="hand2", command=self.browseef, text="Browse", anchor=CENTER, takefocus=1).grid(column=7, row=15, sticky=E+W)

		self.separator(20, 100, 0)

		############################# 
		#     Advanced options      #
		#############################		

		self.limits = {"lower": {"value":0.45, "variable":DoubleVar()}, "upper":{"value":0.55, "variable":DoubleVar()}}
		
		Label(self.main_info_frame, text="Advanced Options", justify="center", relief="ridge", padx=50, width=61, font="times 25 italic bold", foreground="#336600", takefocus=0).grid(column=0, row=200,  sticky=S+E+W, columnspan=9)

		self.separator(201, 25)

		self.lowth = Label(self.main_info_frame, text="The lower threshold between the core and the intermediate", takefocus=0).grid(column=1, row=205, columnspan=5, sticky=W)
		self.uppth = Label(self.main_info_frame, text="The lower threshold between the intermediate and the non-core", takefocus=0).grid(column=1, row=215, columnspan=5, sticky=W)

		self.limits["lower"]["scale"] = Scale(self.main_info_frame, cursor="sb_up_arrow", font="Times 10 bold", activebackground="black", from_=0., to=1.01, tickinterval=.25,\
		                   showvalue=1, orient="horizontal", relief="flat", resolution=.01, repeatdelay=1, command=self.check_the_upper_scale, variable=self.limits["lower"]["variable"], takefocus=1)
		self.limits["lower"]["scale"].grid(column=1, row=210, sticky=E+W, columnspan=6)
		self.limits["upper"]["scale"] = Scale(self.main_info_frame, cursor="sb_up_arrow", font="Times 10 bold", activebackground="black", from_=0., to=1.01, tickinterval=.25,\
		                   showvalue=1, orient="horizontal", relief="flat", resolution=.01, repeatdelay=1, command=self.check_the_lower_scale, variable=self.limits["upper"]["variable"], takefocus=1)
		self.limits["upper"]["scale"].grid(column=1, row=220, sticky=E+W, columnspan=6)

		
		self.separator(225, 25)

		self.pymol = {"state":IntVar()}
		self.pymol["chkbut"] = Checkbutton(self.main_info_frame, width=5, height=1, borderwidth=2, offvalue=0, onvalue=1,\
		                                   indicatoron=1, variable=self.pymol["state"], command=self.pymol_on,\
		                                   font="times 12 bold", anchor=W, justify="left", text="Use pymol to display the results",\
		                                   bg="#eeeee6", activebackground="#eeeee6", activeforeground="black", foreground="black",\
		                                   selectcolor="grey75")
		self.pymol["pathway"] = Entry(self.main_info_frame, cursor="pencil", font="Times 12", state=DISABLED, takefocus=1)
		
		self.pymol["chkbut"].deselect()
		self.pymol["chkbut"].grid(column=1, row=230, sticky=E+W, columnspan=6)
		self.pymol["pathway"].grid(column=1, row=235, sticky=E+W, columnspan=6)

		self.main_info_frame.update_idletasks()
		self.main_info_can.configure(scrollregion=(0,0,self.main_info_frame.winfo_width(), self.main_info_frame.winfo_height()))


		# Creation of the action buttons
		Button(self.master, font="Times 17", cursor="exchange",       command=self.check,     text="Launch",  anchor=CENTER, width=8, takefocus=1).grid(column=0, row=30, sticky=S)
		Button(self.master, font="Times 17", cursor="sb_right_arrow", command=self.save,      text="Save",    anchor=CENTER, width=8, takefocus=1).grid(column=1, row=30, sticky=S)
		Button(self.master, font="Times 17", cursor="sb_up_arrow",    command=self.default,   text="Default", anchor=CENTER, width=8, takefocus=1).grid(column=2, row=30, sticky=S)
		Button(self.master, font="Times 17", cursor="sb_left_arrow",  command=self.load,      text="Load",    anchor=CENTER, width=8, takefocus=1).grid(column=3, row=30, sticky=S)
		Button(self.master, font="Times 17", cursor="X_cursor",       command=self.erase_all, text="Erase",   anchor=CENTER, width=8, takefocus=1).grid(column=4, row=30, sticky=S)
		Button(self.master, font="Times 17", cursor="gumby",          command=self.bye,       text="Quit",    anchor=CENTER, width=8, takefocus=1).grid(column=5, row=30, sticky=S)
		
		self.toremove = self.master.winfo_children()[-6:-1]

	def separator(self, where, thick=50, line=1):
		separator = Canvas(self.main_info_frame, height=thick, borderwidth=0, bg="#eeeee6", highlightbackground="#eeeee6", highlightcolor="#eeeee6", highlightthickness=0, takefocus=0)
		separator.grid(column=0, row=where, columnspan=9, sticky=E+W)
		if line: separator.create_line(0, 25, 2000, 25, fill="grey50")


	def pymol_on(self):
		if self.pymol["state"].get():
			self.pymol["pathway"]["state"] = NORMAL
			if (self.pymol["pathway"].get() == ''):		# First checking of the box
				self.pymol["pathway"].insert(0, "Specify PyMol pathway here...")
		else:
			self.pymol["pathway"]["state"] = DISABLED


	def check_the_upper_scale(self, event):
		if (self.limits["lower"]["variable"].get() > self.limits["upper"]["variable"].get()):
			self.limits["upper"]["variable"].set(self.limits["lower"]["variable"].get())


	def check_the_lower_scale(self, event):
		if (self.limits["upper"]["variable"].get() < self.limits["lower"]["variable"].get()):
			self.limits["lower"]["variable"].set(self.limits["upper"]["variable"].get())


	def browsewd(self):
		saveprm = _tkF.askdirectory(title = "Working Directory")
		if saveprm:
			# Delete the previous value
			for i in range(len(self.e_wd.get())): self.e_wd.delete(1)
			# Display the new directory
			if (saveprm[-1] != os.sep): saveprm += os.sep
			self.e_wd.insert(0, saveprm)

	def browsesf(self):
		saveprm = _tkF.askopenfilename(title = "Structure file", filetypes = [('List Format', '*.list'), ('all files', '*.*')])
		if saveprm:
			# Delete the previous value
			for i in range(len(self.e_sf.get())): self.e_sf.delete(0)
			# Display the new directory
			self.e_sf.insert(0, saveprm)

	def browseef(self):
		saveprm = _tkF.askopenfilename(title = "Folded state", filetypes = [('csp Format', '*.csp'), ('all files', '*.*')])
		if saveprm:
			# Delete the previous value
			for i in range(len(self.e_ef.get())): self.e_ef.delete(0)
			# Display the new directory
			self.e_ef.insert(0, saveprm)

	def introduction(self):
		intro = """
		    NMR experiments are powerfull tools to monitor pertubations within macromolecules. SAMPLEX aims at determining, from perturbation data (HSQC, S2,...), which residues are significantly pertubed.
		For this purpose, SAMPLEX requires first the structure file in which is specified the absolute (or relative) pathway of the three-dimensional structure(s).
		Then, a perturbation data file must be provided and might look like:
			7	0.2911
			11	0.0712
			20	0.1101
			21	0.0810
			27	0.2310
			...
		The residue numbers in the first column must fit the ones in the model(s) specified in the structure file.
		


* * * * * * * * * * * * * * * * * THAT'S ALL! * * * * * * * * * * * * * * * * *


		
		Some extra options will give you the possibility to modify the acceptance of residues to be considered as perturbed, intermediate oe non-perturbed.
		Moreover, a XMGRace files will be created to display the initial data and the starting confidences (in the file raw_data.agr) and the final confidences (in the file prob_data.agr).
		You can also visualize the result with Pymol, after specifying the pathway. You can also do it afterwards, as the file samplex_pymol.pml is created.
		"""

		self.shorti = Toplevel(bd=3)
		self.shorti.title("Short introduction to SAMPLEX")
		self.shorti.resizable(width=None, height=None)
		self.shorti.lift()
		self.title(self.shorti)

		self.intro = Text(self.shorti, wrap=WORD, bd=0, selectborderwidth=0, padx=20, relief=FLAT, takefocus=0, tabs="1c", width=80, height=30)
		self.intro.grid(column=0, row = 10, sticky=N+S+E+W, columnspan=4)
		self.introasceY = Scrollbar(self.shorti,orient=VERTICAL, takefocus=0, command=self.intro.yview)
		self.introasceY.grid(column=4, row=10, sticky=N+S)
		self.intro["yscrollcommand"] = self.introasceY.set
		self.intro.insert(1.0, intro)
		
		self.outshorti = Button(self.shorti, width=20, text="Close", anchor=CENTER, command=self.shorti.destroy).grid(column=0, row=20, columnspan=5)


	def check(self):
		error   = []
		nberror = 0
		info = self.main_info_frame

		if(not (self.e_wd.get() and self.e_sf.get() and self.e_ef.get())):
			self.bell()
			if not (self.e_wd.get()): error.append("The Working Directory field is empty")
			if not (self.e_sf.get()): error.append("The Structure File field is empty")
			if not (self.e_ef.get()): error.append("The experimental file field is empty")

			if error:
				if(len(error)==1):
					_tkM.showerror(title="Error encoutered", message=error[0])
				elif(len(error)>1):
					for i in range(len(error)): message += "%d. %s%s"(i, error[i], os.linesep)
					_tkM.showerror(title="Errors encoutered", message=error)
				return
		else:
			self.input_data['workdir'], self.input_data['structurefile'], self.input_data['expfile'] = self.e_wd.get(), self.e_sf.get(), self.e_ef.get()


		# Checking the Working directory
		if not os.path.exists(self.input_data['workdir']):
			self.bell()
			new_wd = _tkM.askquestion(title = "Unknown directory", message = "The specified working directory does not exist." + os.linesep + "Would you like to create it ?")
			if (new_wd.upper() == "YES"):
				self.create_workdir()
			else:
				return
		if self.input_data['workdir'][-1] != os.sep: self.input_data['workdir'] += os.sep


		# Checking the structure files
		if (self.input_data['structurefile'][0] != os.sep):		# Relative pathway
			self.input_data['structurefile'] = self.input_data['workdir'] + self.input_data['structurefile']
		while (self.input_data['structurefile'][-1] == os.sep):		# It must be a file and not a directory
			self.input_data['structurefile'] = self.input_data['structurefile'][:-1]

		try:                            # Test the existence of all files in the structure file
			f = open(self.input_data['structurefile'], "r")
		except:
			error.append("The specfied Structure File (" + self.input_data['structurefile'].split(os.sep)[-1] + ") does not exist.")
		else:
			files = f.readlines()
			f.close()
			for i in files:
				filename = i.strip()
				if (filename[0] != os.sep):		# Relative pathway
					filename = self.input_data['workdir'] + filename
			while (filename[-1] == os.sep):			# It must be a file and not a directory
				filename = filename[:-1]
			if not os.path.exists(filename):
				error.append("Missing structure: " + filename.split(os.sep)[-1])


		# Checking the experimental file
		if not os.path.exists(self.input_data['expfile']): error.append("Missing experimental file: " + self.input_data['expfile'])


		# Recording lower and upper limits of the final decision
		self.input_data['lower'] = self.limits["lower"]["variable"].get()
		self.input_data['upper'] = self.limits["upper"]["variable"].get()

		if (self.pymol["state"].get()):
			if not os.path.exists(self.pymol["pathway"].get()):
				error.append("PyMol pathway is not correct.")
			else:
				self.input_data["pymol"] = self.pymol["pathway"].get()

		# Messsage in case of errors
		if error:
			self.bell()		# useless under Linux, but we never know...
			if (len(error) > 1):
				alert = "The following errors have been encountered:" + os.linesep * 2
				for i in range(len(error)):
					alert += "%d. %s%c"%(i, error[i], os.linesep)
			else:
				alert = "The following error has been encountered: " + os.linesep * 2 + error[0] + os.linesep
				_tkM.showerror(title = "Provided information errors", message = alert)
			return


		# Everything is OK there
		self.giv_data = "Working directory                   :" + str(self.e_wd.get()) + os.linesep +\
	                        "Structure file                      :" + str(self.e_sf.get()) + os.linesep +\
		                "Experimental file                   :" + str(self.e_ef.get()) + os.linesep +\
				"Lower limit                         :" + str(self.limits["lower"]["variable"].get()) + os.linesep +\
				"Upper limit                         :" + str(self.limits["upper"]["variable"].get()) + os.linesep
				

		# We can quit and run all calculations
		self.quit()


	def default(self):

		self.input_data['workdir']		= self.cd
		self.input_data['structurefile']	= ""
		self.input_data['expfile']		= ""
		self.input_data['lower']		= 0.45
		self.input_data['upper']		= 0.55
		self.input_data['pym_ok']		= 0
		self.input_data['pym_path']		= ""

		if _graphical:
			self.erase_all()

			self.e_wd.insert(0, self.input_data['workdir'])
			self.limits["lower"]["variable"].set(self.input_data['lower'])
			self.limits["upper"]["variable"].set(self.input_data['upper'])


	def create_workdir(self):
		os.system("mkdir " + self.input_data['workdir'])


	def save(self):
		intro = "! This file is an exemple of input file you can use with Pred(U)Re." + os.linesep + "! You may always have at least one space between the definition and"+os.linesep+"! the '=' and between the '=' and the corresponding data." + os.linesep * 2
		self.input_data = {}
		expl            = {}
		self.input_data['workdir'], self.input_data['structurefile'], self.input_data['expfile'] = self.e_wd.get(), self.e_sf.get(), self.e_ef.get()
		self.input_data['lower'], self.input_data['upper'] = self.limits["lower"]["variable"].get(), self.limits["upper"]["variable"].get()
		self.input_data['pym_ok'], self.input_data['pym_path'] = self.pymol["state"].get(), self.pymol["pathway"].get()
		expl['workdir']           = "! The working directory used by default" + os.linesep + "Working Directory\t\t\t=\t"
		expl['structurefile']     = "! The file that contains all structures to take into account" + os.linesep + "Structure File\t\t\t\t=\t"
		expl['expfile']           = "! The file that contains chemical shifts pertubations between the folded and the unfolded states" + os.linesep + "Chemical Shift Perturbation File\t=\t"
		expl['lower']             = "! The threshold value that will set the limit between the core and the intermediate" + os.linesep + "Lower limit\t\t\t\t\t=\t"
		expl['upper']             = "! The threshold value that will set the limit between the intermediate and the non-core" + os.linesep + "Upper limit\t\t\t\t\t=\t"
		expl['pym_ok']            = "! Do you want to display the result in PyMol ?" + os.linesep + "PyMol display\t\t\t\t\t=\t"
		expl['pym_path']          = "! PyMol pathway" + os.linesep + "PyMol pathway\t\t\t\t\t=\t"
		
		saveprm = _tkF.asksaveasfile(title = "Saving parameters", filetypes = [('SAMPLEX format file', '*.samx'), ('all files', '*.*')])
		if (saveprm):
			saveprm.write(intro)
			for data in ('workdir', 'structurefile', 'expfile', 'lower', 'upper', 'pym_ok', 'pym_path'):
				try:
					saveprm.write(expl[data])
					saveprm.write(str(self.input_data[data]) + os.linesep*2)
				except:
					pass

			saveprm.write(os.linesep+"That's all!"+os.linesep)
			saveprm.close()
			return 1						# If the file has been properly saved
		else:
			return 0						# In case where the user changes his mind


	def load(self):
		self.input_data = {}
		
		if self.filename:		# If non graphical and filename provided: OK
			pass
		elif _graphical:		# If graphical
				try:
					self.filename = _tkF.askopenfilename(title = "Opening parameter file", filetypes = [('pnle Format', '*.samx'), ('all files', '*.*')])
				except:
					return
		else:
				print("You have to provide the name of a pnle file...%cThe program will be aborted%s"%(os.linesep, os.linesep*2))
				sys.exit()

		try:
			if not os.path.exists(self.filename):
				if _graphical:
					_tkM._show(title = "Not existing file", message = "The file has not be found!\nDefault values will be used.", icon = _tkM.ERROR, type=_tkM.OK)
				else:
					print "The file has not be found!\nDefault values will be used."
				self.default()	
			else:
				f = open(self.filename, "r")
		except:
			return
		
		try:
			argum = f.readline()
			while (argum):
				try:
					args = argum.lower().split()
					if (args[0][0] == '!'):		# Comment
						pass
					elif ("working directory" in argum.lower()):
						try:
							self.input_data['workdir'] = string.join(argum.split()[args.index("=") + 1:])
						except:
							self.input_data['workdir'] = commands.getoutput("pwd")
					elif ("structure file" in argum.lower()):
						try:
							self.input_data['structurefile'] = string.join(argum.split()[args.index("=") + 1:])
						except:
							self.input_data['structurefile'] = ""

					elif ("chemical shift perturbation" in argum.lower()):
						try:
							self.input_data['expfile'] = string.join(argum.split()[args.index("=") + 1:])
						except:
							self.input_data['expfile'] = ""

					elif ("lower limit" in argum.lower()):
						try:
							self.input_data['lower'] = float(argum.split()[args.index("=") + 1])
						except:
							self.input_data['lower'] = 0.45
					elif ("upper limit" in argum.lower()):
						try:
							self.input_data['upper'] = float(argum.split()[args.index("=") + 1])
						except:
							self.input_data['upper'] = 0.55
					elif ("pymol display" in argum.lower()):
						try:
							self.input_data['pym_ok'] = string.join(argum.split()[args.index("=") + 1:])
						except:
							self.input_data['pym_ok'] = 0
					elif ("pymol pathway" in argum.lower()):
						try:
							self.input_data['pym_path'] = string.join(argum.split()[args.index("=") + 1:])
							if not os.path.exists(self.input_data['pym_path']): self.input_data['pym_path'] = "Specify PyMol pathway here..."
						except:
							self.input_data['pym_path'] = "Specify PyMol pathway here..."
				except:
					pass
				argum = f.readline()
		except:
			pass


		"""
		# TO REVIEW: NOT SURE THIS WILL WORK, BECAUSE VALUES OF STARTDATA ARE NEVER EMPTY
		test = ""
		for i in startdata.values(): test += str(i)
		if test:
			self.input_data = startdata.copy()
			del startdata
		else:
			if _graphical:
				_tkM._show(title="File Error!", message="The file you specified seems not to be a pnle file" + os.linesep, icon = _tkM.ERROR, type = _tkM.OK)
				return
			else:
				print("File Error!%cThe file you specified seems not to be a pnle file!%cThe program will be stopped.%s"%(os.linesep, os.linesep, os.linesep*2))
				sys.exit()

		"""

		

		if _graphical:
			# Here, we put the values we retrieved
	
			self.erase_all()

			try:
				self.e_wd.insert(0, self.input_data['workdir'])
			except:
				pass
			try:
				self.e_sf.insert(0, self.input_data['structurefile'])
			except:
				pass
			try:
				self.e_ef.insert(0, self.input_data['expfile'])
			except:
				pass
			try:
				self.limits["lower"]["variable"].set(self.input_data['lower'])
			except:
				pass
			try:
				self.limits["upper"]["variable"].set(self.input_data['upper'])
			except:
				pass
			try:
				if (int(self.input_data['pym_ok'])):
					self.pymol["chkbut"].select()
					self.pymol["pathway"]["state"] = NORMAL
			except:
				pass
			try:
				self.pymol["pathway"]["state"] = NORMAL
				self.pymol["pathway"].insert(0, self.input_data['pym_path'])
				if (not int(self.input_data['pym_ok'])): self.pymol["pathway"]["state"] = DISABLED
			except:
				pass
			
				
		else:		# Each value must be transformed into readable values...
			try:
				self.input_data['lower'] = eval("1. * "+self.input_data['lower'])
			except:
				print "Incorrect saved value for the lower limit.\nThe lower value will be set to 0.45"
				self.input_data['lower'] = .45
			try:
				self.input_data['upper'] = eval("1. * "+self.input_data['upper'])
			except:
				print "Incorrect saved value for the upper limit.\nThe upper value will be set to 0.55"
				self.input_data['upper'] = .55

	def erase_all(self):
		for t in ("wd", "sf", "ef"):
			exec("for i in range(len(self.e_"+t+".get())): self.e_"+t+".delete(0)")
		for i in range(len(self.pymol["pathway"].get())): self.pymol["pathway"].delete(0)


	def bye(self):
		ans = _tkM._show(title = "Quit", message = "Do you really want to quit ?", icon = "question", type = _tkM.YESNO)
		if (ans == "yes" or ans == 1):						# Bug : After the second time, ans="True", hence the condition 'ans == 1'
			try:
				model.result_win._Thread__stop()
			except:
				pass
			try:
				model.result_win.win.destroy()
			except:
				pass

			try:
				model._Thread__stop()
			except:
				pass
			try:
				prep.master.destroy()
			except:
				pass
			sys.exit()
		else:
			return


class System(_th.Thread):

	def __init__(self, data):

		if _graphical: _th.Thread.__init__(self)
		self.data        = data
		self.inputfile   = self.data.input_data["structurefile"]

		self.neigh_ctf   = 7.5		#float(self.data.e_th.get())

	def get_prob_csp(self, table):

		"""
		From a given dictionnary 'table', calculate for each value in this table the
		Range-Normalised Absolute Value
		"""

		mincsp = min(table.values())
		maxcsp = max(table.values())
		
		csp = {}
		for i in table.keys():
			csp[i] = (table[i] - mincsp) / (maxcsp - mincsp)
		
		return csp


	def run(self):
		"""
		Here we get all data of the system necessary for the prediction:
			1. Retrieving all provided structures
			2. Retrieving the residue numbers from the first given structure
			3. Retrieving the coordinates of all N and HN atoms from all provided structures (Barycentre)
			5. Retrieving the CS of structures from the values extracted from the two spectra and calculating CSP values
		"""
	
		self.structures  = self.get_structures()		# Tuple of the names of the pdb files: (str_1.pdb, str_2.pdb, ...)

		self.allresnb    = self.get_residues()			# Return a list of residue numbers from a structure file: [2, 3, 4, 10, 11, ...]

		

		self.coord       = self.get_coordinates()		# Dictionnary of the coordinates of the barycentres of NH groups, for each structure
									# {0: {1:{'N':(x, y, z), 'H':(x,y,z)}, 2:{'N':(x, y, z), 'H':(x,y,z)},...}, 1: {{'N':(x, y, z), 'H':(x,y,z)}, 2:{'N':(x, y, z), 'H':(x,y,z)},...}}
									#  ^                      ^            ^                      ^
									# Structure               Atom type    Residue               (x, y, z) coordinates

		self.res         = self.coord[0].keys()			# List of the residue numbers in the structure files: [2, 3, 4, 10, 11, ...]
		self.res.sort()

		self.neighbours  = self.get_neighbours(7.5)		# Finding all neighbours within a certain cut-off: {1: [2, 3, 39, 40], 2: [1, 3, 4. 40], ...}		


		self.cspvalues   = self.get_CSP(self.data.input_data["expfile"])		# Dictionnary of CSP values   {1: 0.00215, 2: 0.012578, ...}


		
		if self.disappear:
			self.disappear.sort()
			printp(progress, "The peaks of the following residues disappeared:"+os.linesep)
			for i in self.disappear: printp(progress, "%d "%i)
			printp(progress)
			printp(progress, "These residues will first be considered in a non-native like environment"+os.linesep)

		

		self.cspres      = self.cspvalues.keys()		# List of residues numbers having a CSP values

		self.black       = []					# List of residues without any csp value, that is futhermore impossible to infer

		self.no_cspres   = [m for m in self.res if m not in self.cspres+self.prolines+self.disappear]	# List of residue numbers having no CSP values (except prolines)


		if _graphical:
			self.data.quit()
		else:
			return


	def get_residues(self):
		"""
		Return a list of residue numbers from a structure file (pdb, ent,...)
		"""
		
		allreslist=[]
		seq=[]

		strucfile = open(self.structures[0],"r")	# Assuming that all structures have the same number of residues
		line      = strucfile.readline()

		while (1):					# Reading the structure file until the first atom
			try:
				if (line[0:4].upper()=="ATOM"):
					break
			except:
				pass
			line = strucfile.readline()

		while (line[0:4].upper()=="ATOM"):
			resnb   = line[22:26].strip()
			resname = line[17:21].upper().strip()
			allreslist.append(int(resnb))
			seq.append(resname)
			try:
				while (line[22:26].strip()==resnb):
					line = strucfile.readline()
			except:
				pass
		
		return allreslist


	def get_structures(self):
		"""
		This function returns a tuple which contains all structure files
		"""

		structures = []
		try:
			file = open(self.inputfile,"r")
		except:
			print self.inputfile, "does not exist!"
			print "Program will be aborted."+os.linesep*2
			sys.exit()

		filenames = file.readlines()
		for i in filenames:
			filename = i.strip()
			if (filename != ""):
				try:
					f = open(filename)
					f.close()
					structures.append(filename)
				except:
					print filename, "does not exist!"
		file.close()
		return tuple(structures)


	def get_coordinates(self):
		"""
		This function retrieves all coordinates of the NH groups
	        and store them in a dictionnary as following:
		
		{0: {1:(x, y, z), 2:(x,y,z),...}, 1: {1:(x, y, z), 2:(x,y,z),...}}
		 ^                ^                      ^
		Structure        Residue                (x, y, z) coordinates
		"""

		printp(progress, "Retrieving all NH-HN coordinates" + os.linesep)
		if _graphical:
			prog   = Canvas(progress, bg="grey75", borderwidth=2, relief=RIDGE, height=20., width=300.)
			prog.create_rectangle(3., 3., 3., 23., fill="blue", width=0)
			prog.create_text(150., 12., anchor=CENTER, font="times 10 italic bold", fill="white", text="%.2f%c finished"%(0., '%'))
			progress.window_create(INSERT, window=prog)
		else:
			print "Progression : %6.2f"%0.,

		printp(progress, os.linesep*2)
		self.prolines = []
		coord = {}
		count = 0.00
		start_time = time.time()
		
		self.atom_types = {'N': ('N', 'NH'), 'H': ('H', 'HN')}
		
		for filenb in range(0, len(self.structures), 1):		
			
			stru = open(self.structures[filenb], "r")
			coord[filenb] = {}

			line = stru.readline()
			while (line):				# Reading the structure file until the first atom
				try:
					if (line[0:4].upper() == "ATOM"):
						break
				except:
					pass
				line = stru.readline()

			while(line):
				resnb   = int(line[22:26].strip())
				resname = line[17:20].strip()

				x={}							# Variables initialization
				y={}
				z={}
				extrem = 0						# For the N- and C-termini
				try:
					while(int(line[22:26].strip()) == resnb):
						if (line[12:16].strip().upper() in self.atom_types['N']+self.atom_types['H']):
							x[line[12:16].strip().upper()] = float(line[30:38].strip())
							y[line[12:16].strip().upper()] = float(line[38:46].strip())
							z[line[12:16].strip().upper()] = float(line[46:54].strip())
						line = stru.readline()
				except:
					pass

				for i in self.atom_types:
					if i not in [a[0] for a in x.keys()]:
						printp(progress, "Residue %d does not have any %s coordinates!\n"%(resnb, i))
				if (x and y and z):
					coord[filenb][resnb] = (stat([x[a] for a in x])[0], stat([y[a] for a in y])[0], stat([z[a] for a in y])[0])
				else:
					remark = "No coordinates in %s file for residue %s.%c"%(self.structures[filenb],resnb,os.linesep) + "The program will be aborted." + os.linesep
					if _graphical:
						_tkM.showerror(title="Missing coordinates", message=remark)
						system__stopped = True
						prep.quit()
					else:
						system.__stopped = True
						print remark
						sys.exit()


				try:
					if (line[0:4] != "ATOM"): break
				except:
					break


			count += 1.00
			finish = count * 100.0 / (len(self.structures) * len(self.allresnb))
			if _graphical:
				prog.coords(1, 3., 3.,  3.+3.0*finish, 23.)
				prog.itemconfigure(2, text="%.2f%c finished"%(finish, '%'))
			else:
				print "\b" * 9 + "%6.2f finished"%finish,
			stru.close()

		if _graphical:
			prog.coords(1, 3., 3., 303., 23.)
			prog.itemconfigure(2, text="All distances have been calculated successfully")
			printp(progress)
		else:
			print "\b" * 21 + "All distances have been calculated successfully"
		return coord



	def get_coord(self):
		coord = {}
		for i in self.coord[0].keys():
			cttiax    = [self.coord[m][i][0] for m in self.coord.keys()]
			cttiay    = [self.coord[m][i][1] for m in self.coord.keys()]
			cttiaz    = [self.coord[m][i][2] for m in self.coord.keys()]
			coord[i] = (sum(cttiax)/len(cttiax), sum(cttiay)/len(cttiay), sum(cttiaz)/len(cttiaz))
		return coord


	def get_neighbours(self, cutoff=7.5):
		"""
		This function builds up a dictionnary of all neighbours of a given residue
		within a certain cut-off distance (7.5 Amgstrom)
		If several structures are provided, the arithmetic average distance is considered.
		"""

		neighbours = {}
		for i in self.res:				# i and j are the residue numbers; residues without any CSP are also considered there
			neighbours[i] = {}			# Hence "i in self.coord[0].keys()"
			for j in self.res:
				if (j != i):
					sumdist = 0.
					for k in self.coord:
						sumdist += self.get_distance(self.coord[k][i][0], self.coord[k][i][1], self.coord[k][i][2],\
						                             self.coord[k][j][0], self.coord[k][j][1], self.coord[k][j][2])
					aver_dist = sumdist/len(self.coord)
					if (aver_dist < cutoff): neighbours[i][j] = aver_dist
		return neighbours


	def get_CSP(self, inputfile):
		tmp_csp={}
		self.disappear = []

		f = open(inputfile,"r")		# The existence of this file has been tested previously

		line = f.readline()

		while (line):
			try:
				resi = int(line.split()[0])
				if tmp_csp.has_key(resi):
					printp(progress, "Warning : Duplication of residue "+resn+"!"+os.linesep)
				else:
					try:
						tmp_csp[resi] = (float(line.split()[1]))
					except:
						if (len(line.split()) > 1 and line.split()[1].upper()=='D'): self.disappear.append(resi)
			except:
				# print line
				pass
			line=f.readline()
		return tmp_csp


	def reject_highest_values(self, table, k=1.5):

		val = list(table.values())
		val.sort()
		eps = 0.00001

		# Determination of the median
		if len(val)%2:		# If there is an odd number of values
			average = val[(len(val)-1)/2]
		else:				# If there is an even number of values
			average = (val[len(val)/2-1]+val[len(val)/2])/2.

		# Determination of the first quartile
		val_1 = [a for a in val if a-average<=eps]
		val_2 = [a for a in val if a-average>=eps]
		if len(val_1)%2:		# If there is an odd number of values
			average_1 = val_1[(len(val_1)-1)/2]
		else:				# If there is an even number of values
			average_1 = (val_1[len(val_1)/2-1]+val_1[len(val_1)/2])/2.

		# Determination of the second quartile
		if len(val_2)%2:		# If there is an odd number of values
			average_2 = val_2[(len(val_2)-1)/2]
		else:				# If there is an even number of values
			average_2 = (val_2[len(val_2)/2-1]+val_2[len(val_2)/2])/2.

		# Returning the list of residues that are out of range
		return [[a for a in table if table[a]>average_2 + k * (average_2 - average_1)], average_2 + k * (average_2 - average_1)]

	
	
	def get_distance(self, xa, ya, za, xb, yb, zb):
		return math.sqrt((xa-xb)*(xa-xb)+(ya-yb)*(ya-yb)+(za-zb)*(za-zb))





class Model(_th.Thread):
	"""
	This class performs all calculations from the parameters
	retrieved for the system.
	"""
	
	def __init__(self, universe):
	
		if _graphical:
			_th.Thread.__init__(self)

			# Creation of the window that will display results
			self.result_win = Display(universe.allresnb)
			self.result_win.start()

		self._end = _th.Event()
		
		self.universe = universe				# All data from the system

		self.raw_cspvalues = self.universe.cspvalues.copy()	# Keep somewhere in memory raw data

		self.upper = 0.05		# Limits for the final verdict
		self.lower = -0.05		# below=NLE, above=non-NLE, between=intermediate

		# Setting up the equation
		# This equation is of the form: F(prob)*G(dist)
		# Where F(prob) is something like F(prob) = prob^2
		#   and G(dist) is a sigmoidal function that has a value very close to 1.0 when x=0 and very close to 0.0 when x=cut-off
		#   It is of the form:
		#                                 S(dist) =   exp(-lamb*dist)
		#                                           -------------------
		#                                           a + exp(-lamb*dist)
		#
		# From such a function, I can determine what is the influence of a neighbour on a given atom
		self.epsilon = 0.0001			# For a sigmoidal functionm y coordinates when x is equal the cut-off, or 1-y when x is equal to 0
		self.a    = self.epsilon / (1. - self.epsilon)
		self.lamb = (math.log(1.-self.epsilon) - math.log(self.a*self.epsilon)) / self.universe.neigh_ctf


	def rangelist(self, liste=[]):
		tmpliste = [m for m in liste]
		tmpliste.sort()

		text = str(tmpliste[0])
		refe = tmpliste[0]
		for i in range(1, len(tmpliste), 1):
			if (tmpliste[i] - refe > 1):
				if text[-1] == '-':
					text += str(refe) + ", "
				else:
					text += ", "
				try:
					text += str(tmpliste[i])
				except:
					pass
			else:
				if text[-1] != '-': text += '-'
			refe = tmpliste[i]

		if text[-1] == '-': text += str(tmpliste[-1])

		del tmpliste
		return text


	def median(self, table):

		"""
		Return the median, the first and second quartiles of a sorted table.
		"""

		# median
		if len(table)%2:		# If there is an odd number of values
			median = table[(len(table)-1)/2]
		else:				# If there is an even number of values
			median = (table[len(table)/2-1]+table[len(table)/2])/2.

		# First quartile
		val_L = [a for a in table if a-median<=self.epsilon]
		if len(val_L)%2:		# If there is an odd number of values
			quartil_25 = val_L[(len(val_L)-1)/2]
		else:				# If there is an even number of values
			quartil_25 = (val_L[len(val_L)/2-1]+val_L[len(val_L)/2])/2.
		
		# Second quartile
		val_R = [a for a in table if a-median>=self.epsilon]
		if len(val_R)%2:		# If there is an odd number of values
			quartil_75 = val_R[(len(val_R)-1)/2]
		else:				# If there is an even number of values
			quartil_75 = (val_R[len(val_R)/2-1]+val_R[len(val_R)/2])/2.

		return median, quartil_25, quartil_75


	def reject_highest_value(self, table, k=1.):

		val = [(table[a], a) for a in table]
		val.sort()

		# Determination of the median
		median, quartil_25, quartil_75 = self.median([a[0] for a in val])

		# Returning the list of residues that are out of range
		threshold = quartil_75 + k * (quartil_75 - quartil_25)

		print "For k =", k, ",the threshold value is:", threshold

		reject = [a for a in table.keys() if table[a]>threshold]
		reject.sort()

		return reject


	def running_average(self):

		"""
		The running average is a bit specific there. 
		"""

		val_tmp = {}
		
		for i in self.prob:
			neighb = []
			for j in self.universe.neighbours[i]:
				dist = sum([self.universe.get_distance(self.universe.coord[k][i][0], self.universe.coord[k][i][1], self.universe.coord[k][i][2],\
				            self.universe.coord[k][j][0], self.universe.coord[k][j][1], self.universe.coord[k][j][2]) \
				            for k in self.universe.coord.keys()])/len(self.universe.coord)		
				if self.prob.has_key(j): neighb.append((dist, self.prob[j], j))
			neighb.sort()
			if (neighb):
				val_tmp[i] = self.evol_prob[0][i]			# Considering the starting value
				distt = 1.
				for j in neighb:
					g = math.exp(-self.lamb*j[0]) / (self.a + math.exp(-self.lamb*j[0]))
					val_tmp[i] += (j[1] * g)
					distt      += g
				val_tmp[i] /= distt
			else:
				printp(progress, "      %d has not been modified!%c"%(i, os.linesep))
				val_tmp[i] = self.prob[i]	# No modification!
				
		return val_tmp






	def bary_inter(self, which):
		"""
		This function infers the CSP value of a given residue, regarding its neighbourhood.
		A barycentric approach is used for this purpose:
		
		                   n                n
			         _____            _____
		                 \                |   |
				  \     csp(j) *  |   |  d(i,j)
				  /               |   |
				 /____            |   | 
				  j=1              m=1
				                   m#j
				 
		       csp(i) = --------------------------------
		                        n      n
			              _____  _____
		                      \      |   |
				       \     |   |  d(i,j)
				       /     |   |
				      /____  |   | 
				       j=1    m=1
				              m#j
		       
		Where n is the number of neighbours, and d(i,j) the distance between atons i and j.
		The number of neighbours must be at least equal to 2, or else the CSP value of the
		residue is not infered and is put in a black list.

		"""
		
		neigh = [a for a in self.universe.neighbours[which] if a in self.prob]
		
		if (len(neigh) < 2): return None

		sumu = 0.
		sumd = 0.
		for i in neigh:
			dist = sum([self.universe.get_distance(self.universe.coord[k][which][0], self.universe.coord[k][which][1], self.universe.coord[k][which][2],\
                                   self.universe.coord[k][i][0], self.universe.coord[k][i][1], self.universe.coord[k][i][2]) \
                                   for k in self.universe.coord.keys()])/len(self.universe.coord)
			fact  = (math.exp(-self.lamb*dist) / (self.a + math.exp(-self.lamb*dist))) 
			sumd += fact
			sumu += (self.prob[i] * fact)
		return sumu / sumd
		


	def run(self):

		# Step 1. Adjusting extreme csp values
		# Here, we detect whether there is a real perturbation of the environment of the protein
		# If no extreme value is found, the protein is fully in a native-like environment


		printp(progress, "%sStep 1. Attributing probabilities%c"%(os.linesep*2, os.linesep))

		self.prob = {}
		pc_sele = 15
		resi_with_csp = self.universe.cspvalues.keys()
		resi_with_csp.sort()
		nb_sele = int(round(pc_sele*len(resi_with_csp)/100.))
		n_trial = len(self.universe.cspvalues) * 25		# This value will be divided by 100 in the second part


		printp(progress, "    %d residues with experimental value.%c"%(len(resi_with_csp), os.linesep))
		printp(progress, "    For each run, %d residues randomly selected.%c"%(nb_sele, os.linesep))


		# First, we need to determine the minimum value requiered to be sure that the highest value will have a probability of 1.
		maxcsp = {"resi": 0, "csp": 0.}
		mincsp = {"resi": 0, "csp": 1.E10}
		for count in self.universe.cspvalues:
			if (self.universe.cspvalues[count]>maxcsp["csp"]):
				maxcsp["resi"] = count
				maxcsp["csp"]  = self.universe.cspvalues[count]
			if (self.universe.cspvalues[count]<mincsp["csp"]):
				mincsp["resi"] = count
				mincsp["csp"]  = self.universe.cspvalues[count]

		ensembles_to_test = []
		mincoeff_high = 100.
		mincoeff_low = -100.
		count = 0
		khigh, klow = 0., 0.
		while (count<n_trial):
			# Selection of random structures
			selected = random.sample(resi_with_csp, nb_sele)
			ensembles_to_test.append([a for a in selected])

			# We want both the highest and the lowest csp residues to be in this randomly selected sub-ensemble
				
			if maxcsp["resi"] not in selected:
				if selected[-1] != mincsp["resi"]:
					selected[-1] = maxcsp["resi"]
				else:
					selected[-2] = maxcsp["resi"]
			if mincsp["resi"] not in selected:
				if selected[-1] != maxcsp["resi"]:
					selected[-1] = mincsp["resi"]
				else:
					selected[-2] = mincsp["resi"]
				
			# Statistics about the selected sample
			aver = sum([self.universe.cspvalues[a] for a in selected]) / nb_sele
			stdv = 0.
			for i in selected: stdv += ((self.universe.cspvalues[i]-aver)*(self.universe.cspvalues[i]-aver))
			stdv = math.sqrt(stdv/nb_sele)
			
			count += 1

			try:
				khigh = (maxcsp["csp"] - aver) / stdv
				klow  = (mincsp["csp"] - aver) / stdv
				if (khigh<mincoeff_high):
					mincoeff_high = khigh
					count = 0
				if (klow>mincoeff_low):
					mincoeff_low = klow
					count = 0
			except:
				pass

		printp(progress, "\tCoefficient of regulation high = %.3f%s"%(mincoeff_high, os.linesep))
		printp(progress, "\tCoefficient of regulation  low = %.3f%s"%(mincoeff_low, os.linesep))

		# Then, we calculate the probability for each residue to be in a non-native like environment
		for resi in resi_with_csp:
			self.prob[resi] = 0.
			for sel in ensembles_to_test:
				# Selection of random structures
				#selected = random.sample(resi_with_csp, nb_sele)
				selected = [a for a in sel]
				if resi not in selected: selected[0] = resi	# We want the residue to be in this randomly selected sub-ensemble

				# Statistics about the selected sample
				aver = sum([self.universe.cspvalues[a] for a in selected]) / nb_sele
				stdv = 0.
				for i in selected: stdv += ((self.universe.cspvalues[i]-aver)*(self.universe.cspvalues[i]-aver))
				stdv = math.sqrt(stdv/nb_sele)

				try:
					k = (self.universe.cspvalues[resi] - aver) / stdv
				
					if (k>=mincoeff_high):
						self.prob[resi] += 1.
					elif (k<=mincoeff_low):
						self.prob[resi] -= 1.
					else:
						self.prob[resi] += ((2 * k - mincoeff_high - mincoeff_low) / (mincoeff_high - mincoeff_low))
					#count += 1
				except:
					pass
			self.prob[resi] /= len(ensembles_to_test)
			if _graphical: self.result_win.modify_size(resi, self.prob[resi])
			printp(progress, "      Residue %d:\t%.5lf\n"%(resi, self.prob[resi]))
				

		printp(progress)


		# Step 2. Inference of missing values using the barycentric method
		# OK, this method is quite tricky, but the goal is not to find the correct value, but only to find a certain confidence!
		# If a residue can not be infered, it is put in the black list
		printp(progress, "%sStep 2. Inferencing missing values%c"%(os.linesep*2, os.linesep))
		self.inferred = []
		for i in self.universe.no_cspres+self.universe.prolines+self.universe.disappear:
			new_conf = self.bary_inter(i)
			if new_conf:
				self.inferred.append((i, new_conf))
				if _graphical: self.result_win.modify_size(i, new_conf)
			else:
				self.universe.black.append(i)

		if self.inferred:
			self.inferred.sort()
			for i in self.inferred:
				printp(progress, "      Residue %d:\t%.10lf%c"%(i[0], i[1], os.linesep))
				self.prob[i[0]] = i[1]
		else:
			printp(progress, "      No residue to infer%c"%os.linesep)

		if self.universe.black:
			self.universe.black.sort()
			printp(progress, "      The following residues can not be infered and will%c"%os.linesep)
			printp(progress, "      not be taken into account in future calculations: %s%s"%(self.rangelist(self.universe.black), os.linesep*2))


		printp(progress, "%s"%(os.linesep*2))



		# Normalization (This step is theoritically not necessary, but we never know...)
		maxcsp = max(self.prob.values())
		mincsp = min(self.prob.values())
		for i in self.prob: self.prob[i] = (2 * self.prob[i] - maxcsp - mincsp) / (maxcsp - mincsp)

		printp(progress, "%s"%(os.linesep*2))




		# Step 3. Homogenisation of values with a pseudo-"running average"
		# At least two neighbours with a csp value
		# If not, we do not know whether missing neighbours had a high or small csp, so it is impossible
		# to modify the csp value of the single residue of interest
		
		printp(progress, "Step 3. Homogenisation of probabilities"+os.linesep)

		self.precision = 1.E-5


		self._end.clear()
		count = 0

		self.evol_prob = {count: self.prob.copy()}
		self.evol_prob_total = self.prob.copy()

		while not self._end.isSet():
			printp(progress, "Run %d..."%count)
			count += 1
			self.evol_prob[count] = self.running_average()	# This function returns a dictionnary

			maxcsp = max(self.evol_prob[count].values())
			mincsp = min(self.evol_prob[count].values())
			midcsp = (maxcsp + mincsp) / 2.

			for i in self.evol_prob[count]:
				self.evol_prob[count][i] = (2 * self.evol_prob[count][i] - maxcsp - mincsp) / (maxcsp - mincsp)
				if _graphical: self.result_win.modify_size(i, self.evol_prob[count][i])

			# Checking whether we reached the convergence
			sumt = 0.
			for i in self.evol_prob[count]: sumt += ((self.evol_prob[count][i]-self.prob[i])\
			                                       * (self.evol_prob[count][i]-self.prob[i]))

			diffrun = math.sqrt(sumt/len(self.evol_prob[count]))
			printp(progress, "\tDifference: %.12f%c"%(diffrun, os.linesep))

			self.prob = self.evol_prob[count].copy()
			
			# We stop the process when the root mean square difference between
			# two consecutive runs is lower than the specified precision
			if (diffrun < self.precision): self._end.set()


		printp(progress, "%s"%os.linesep*2)
		printp(progress, "FINAL CONFIDENCES\n-----------------\n")
		for i in self.prob: printp(progress, "%2d\t%.5lf\n"%(i, self.prob[i]))

		
		self.pumo = [a for a in self.prob if self.prob[a]>=self.upper]
		self.core = [a for a in self.prob if self.prob[a]<self.lower]
		self.inte = [a for a in self.prob if a not in self.pumo+self.core]
		self.pumo.sort()
		self.core.sort()
		self.inte.sort()
		

		# Displaying the final result
		if (self.core and self.pumo and self.inte):
			printp(progress, os.linesep+"In conclusion:\n\t%u residues are in the core of the protein: %s%c"%(len(self.core), self.rangelist(self.core), os.linesep))
			printp(progress, os.linesep+"\t%u residues are intermediate: %s%c"%(len(self.inte), self.rangelist(self.inte), os.linesep))
			printp(progress, os.linesep+"\t%u residues are in the non-core of the protein: %s%c"%(len(self.pumo), self.rangelist(self.pumo), os.linesep))
		elif (self.core and self.pumo):
			printp(progress, os.linesep+"In conclusion:\n\t%u residues are in the core of the protein: %s%c"%(len(self.core), self.rangelist(self.core), os.linesep))
			printp(progress, os.linesep+"\t%u residues are in the non-core of the protein: %s%c"%(len(self.pumo), self.rangelist(self.pumo), os.linesep))
		elif (self.core and self.inte):
			printp(progress, os.linesep+"In conclusion:\n\t%u following residues are in the core of the protein: %s%c"%(len(self.core), self.rangelist(self.core), os.linesep))
			printp(progress, os.linesep+"\t%u residues are intermediate: %s%c"%(len(self.inte), self.rangelist(self.inte), os.linesep))
		elif(self.pumo and self.inte):
			printp(progress, os.linesep+"In conclusion:\n\t%u residues are intermediate: %s%c"%(len(self.inte), self.rangelist(self.inte), os.linesep))
			printp(progress, os.linesep+"\t%u residues are in the non-core of the protein: %s%c"%(len(self.pumo), self.rangelist(self.pumo), os.linesep))
		elif(self.core):
			printp(progress, os.linesep+"In conclusion, all residues (%u ) are in the core.%c"%(len(self.inte), os.linesep))
		else:		# We can not have all residues only in the intermediate state
			printp(progress, os.linesep+"In conclusion, all residues (%u ) are in the non-core of the protein.%c"%(len(self.inte), os.linesep))
		

		if _graphical:
			model.result_win._Thread__stop()
			prep.quit()
			
		else:
			return



class Display(Model):

	def __init__(self, residues):
	
		_th.Thread.__init__(self)
		
		self.residues = residues
		self.residues.sort()
		self.first_residue = min(self.residues)
		
		self.nb_res = len(self.residues)
		self.width  = 5
		self.build()
		

	def modify_size(self, which, proba):
		self.can.delete(self.histo[which])
		self.histo[which] = self.can.create_rectangle(45+(which-self.first_residue)*self.width, 150, 44+(which-self.first_residue+1)*self.width, 150-proba*100., fill="orange", outline="blue")
		#time.sleep(.1)
		
	def build(self):
		self.win = Tk()
		self.can = Canvas(self.win, bd=0, bg="black", height=300, width=self.width*self.nb_res+100)
		self.can.create_line(40, 249, 40, 50, fill="red")
		self.can.create_line(40, 150, self.width*self.nb_res+50, 150, fill="red")

		self.histo = {}
		
		for i in self.residues:
			self.histo[i] = self.can.create_rectangle(45+(i-self.first_residue)*self.width, 150, 44+(i-self.first_residue+1)*self.width, 150, fill="orange", outline="blue")

		self.can.pack()
		
	
	def run(self):
		self.win.mainloop()
		
	def quit(self):
		self.win.quit()


		
class Conclusion(System):

	def __init__(self, forward_model):

		if _graphical: _th.Thread.__init__(self)
		
		# Some pointers to make my life easier...
		self.model     = forward_model
		self.universe  = forward_model.universe
		self.evol_prob = forward_model.evol_prob
		self.init_prob = self.evol_prob[0]
		self.end_prob  = self.evol_prob[max(self.evol_prob.keys())]


	def mean_coord(self):
		coord_mean = {}
		for i in self.coord[0].keys():		# Browsing the residue numbers
			cttiax_CA, cttiay_CA, cttiaz_CA = [], [], []
			cttiax_CB, cttiay_CB, cttiaz_CB = [], [], []
			for j in self.coord.keys():		# Browsing the structure numbers
				try :
					x, y, z = self.coord[j][i]["CA"][0], self.coord[j][i]["CA"][1], self.coord[j][i]["CA"][2]
					cttiax_CA.append(float(x))
					cttiay_CA.append(float(y))
					cttiaz_CA.append(float(z))
				except:
					pass
				try :
					x, y, z= self.coord[j][i]["CB"][0], self.coord[j][i]["CB"][1], self.coord[j][i]["CB"][2]
					cttiax_CB.append(float(x))
					cttiay_CB.append(float(y))
					cttiaz_CB.append(float(z))
				except:
					pass

			if ((cttiax_CA and cttiay_CA and cttiaz_CA) or (cttiax_CB and cttiay_CB and cttiaz_CB)):
				coord_mean[i] = {}
				if (cttiax_CA and cttiay_CA and cttiaz_CA):
					coord_mean[i]["CA"] = (sum(cttiax_CA)/len(cttiax_CA), sum(cttiay_CA)/len(cttiay_CA), sum(cttiaz_CA)/len(cttiaz_CA))
				if (cttiax_CB and cttiay_CB and cttiaz_CB):
					coord_mean[i]["CB"] = (sum(cttiax_CB)/len(cttiax_CB), sum(cttiay_CB)/len(cttiay_CB), sum(cttiaz_CB)/len(cttiaz_CB))
		return coord_mean


	def save_output(self):
		intro = "This output file has been generated by PredNLE" + os.linesep + "Prediction of native-like environment from chemical shifts" + os.linesep + "for partially unfolded states of proteins (by Fuentes G, Krzeminski M and Bonvin A)" + os.linesep*2
		text  = progress.get(6.0, END)
		saveoutput = _tkF.asksaveasfile(title = "Saving output file", filetypes = [('PredNLE output format file', '*.sampout'), ('all files', '*.*')])
		if (saveoutput):
			saveoutput.write(intro+os.linesep*2+self.model.universe.data.giv_data+os.linesep*2+text)
			saveoutput.close()


	def write_eps_file_of_raw_data(self, filename_raw, filename_conf, pumo, inte):

		intro = """# Grace project file
#
@version 50114
@page size 800, 612
@page scroll 5%
@page inout 5%
@link page off
@map font 0 to "Times-Roman", "Times-Roman"
@map font 1 to "Times-Italic", "Times-Italic"
@map font 2 to "Times-Bold", "Times-Bold"
@map font 3 to "Times-BoldItalic", "Times-BoldItalic"
@map font 4 to "Helvetica", "Helvetica"
@map font 5 to "Helvetica-Oblique", "Helvetica-Oblique"
@map font 6 to "Helvetica-Bold", "Helvetica-Bold"
@map font 7 to "Helvetica-BoldOblique", "Helvetica-BoldOblique"
@map font 8 to "Courier", "Courier"
@map font 9 to "Courier-Oblique", "Courier-Oblique"
@map font 10 to "Courier-Bold", "Courier-Bold"
@map font 11 to "Courier-BoldOblique", "Courier-BoldOblique"
@map font 12 to "Symbol", "Symbol"
@map font 13 to "ZapfDingbats", "ZapfDingbats"
@map color 0 to (255, 255, 255), "white"
@map color 1 to (0, 0, 0), "black"
@map color 2 to (255, 0, 0), "red"
@map color 3 to (0, 255, 0), "green"
@map color 4 to (0, 0, 255), "blue"
@map color 5 to (255, 255, 0), "yellow"
@map color 6 to (188, 143, 143), "brown"
@map color 7 to (220, 220, 220), "grey"
@map color 8 to (148, 0, 211), "violet"
@map color 9 to (0, 255, 255), "cyan"
@map color 10 to (255, 0, 255), "magenta"
@map color 11 to (255, 165, 0), "orange"
@map color 12 to (114, 33, 188), "indigo"
@map color 13 to (103, 7, 72), "maroon"
@map color 14 to (64, 224, 208), "turquoise"
@map color 15 to (0, 139, 0), "green4"
@reference date 0
@date wrap off
@date wrap year 1950
@default linewidth 1.0
@default linestyle 1
@default color 1
@default pattern 1
@default font 0
@default char size 1.000000
@default symbol size 1.000000
@default sformat "%.8g"
@background color 0
@page background fill on
@timestamp off
@timestamp 0.03, 0.03
@timestamp color 1
@timestamp rot 0
@timestamp font 0
@timestamp char size 1.000000
@timestamp def "Wed Jul 16 12:15:26 2008"
@g0 on
@g0 hidden false
@g0 type XY
@g0 stacked false
@g0 bar hgap 0.000000
@g0 fixedpoint off
@g0 fixedpoint type 0
@g0 fixedpoint xy 0.000000, 0.000000
@g0 fixedpoint format general general
@g0 fixedpoint prec 6, 6
@with g0
@    world xmin XMIN
@    world xmax XMAX
@    world ymin YMIN
@    world ymax YMAX
@    stack world 0, 0, 0, 0
@    znorm 1
@    view xmin 0.153595
@    view xmax 1.153595
@    view ymin 0.150000
@    view ymax 0.850000
@    title ""
@    title font 0
@    title size 1.500000
@    title color 1
@    subtitle ""
@    subtitle font 0
@    subtitle size 1.000000
@    subtitle color 1
@    xaxes scale Normal
@    yaxes scale Normal
@    xaxes invert off
@    yaxes invert off
@    xaxis  on
@    xaxis  type zero false
@    xaxis  offset 0.000000 , 0.000000
@    xaxis  bar on
@    xaxis  bar color 1
@    xaxis  bar linestyle 1
@    xaxis  bar linewidth 1.0
@    xaxis  label ""
@    xaxis  label layout para
@    xaxis  label place auto
@    xaxis  label char size 1.000000
@    xaxis  label font 0
@    xaxis  label color 1
@    xaxis  label place normal
@    xaxis  tick on
@    xaxis  tick major 10
@    xaxis  tick minor ticks 1
@    xaxis  tick default 6
@    xaxis  tick place rounded true
@    xaxis  tick in
@    xaxis  tick major size 1.000000
@    xaxis  tick major color 1
@    xaxis  tick major linewidth 1.0
@    xaxis  tick major linestyle 1
@    xaxis  tick major grid off
@    xaxis  tick minor color 1
@    xaxis  tick minor linewidth 1.0
@    xaxis  tick minor linestyle 1
@    xaxis  tick minor grid off
@    xaxis  tick minor size 0.500000
@    xaxis  ticklabel on
@    xaxis  ticklabel format general
@    xaxis  ticklabel prec 5
@    xaxis  ticklabel formula ""
@    xaxis  ticklabel append ""
@    xaxis  ticklabel prepend ""
@    xaxis  ticklabel angle 0
@    xaxis  ticklabel skip 0
@    xaxis  ticklabel stagger 0
@    xaxis  ticklabel place normal
@    xaxis  ticklabel offset auto
@    xaxis  ticklabel offset 0.000000 , 0.010000
@    xaxis  ticklabel start type auto
@    xaxis  ticklabel start 0.000000
@    xaxis  ticklabel stop type auto
@    xaxis  ticklabel stop 0.000000
@    xaxis  ticklabel char size 0.900000
@    xaxis  ticklabel font 0
@    xaxis  ticklabel color 1
@    xaxis  tick place both
@    xaxis  tick spec type none
@    yaxis  on
@    yaxis  type zero false
@    yaxis  offset 0.000000 , 0.000000
@    yaxis  bar on
@    yaxis  bar color 1
@    yaxis  bar linestyle 1
@    yaxis  bar linewidth 1.0
@    yaxis  label ""
@    yaxis  label layout para
@    yaxis  label place auto
@    yaxis  label char size 1.000000
@    yaxis  label font 0
@    yaxis  label color 1
@    yaxis  label place normal
@    yaxis  tick on
@    yaxis  tick major TICK_MAJOR
@    yaxis  tick minor ticks 1
@    yaxis  tick default 6
@    yaxis  tick place rounded true
@    yaxis  tick in
@    yaxis  tick major size 1.000000
@    yaxis  tick major color 1
@    yaxis  tick major linewidth 1.0
@    yaxis  tick major linestyle 1
@    yaxis  tick major grid off
@    yaxis  tick minor color 1
@    yaxis  tick minor linewidth 1.0
@    yaxis  tick minor linestyle 1
@    yaxis  tick minor grid off
@    yaxis  tick minor size 0.500000
@    yaxis  ticklabel on
@    yaxis  ticklabel format general
@    yaxis  ticklabel prec 5
@    yaxis  ticklabel formula ""
@    yaxis  ticklabel append ""
@    yaxis  ticklabel prepend ""
@    yaxis  ticklabel angle 0
@    yaxis  ticklabel skip 0
@    yaxis  ticklabel stagger 0
@    yaxis  ticklabel place normal
@    yaxis  ticklabel offset auto
@    yaxis  ticklabel offset 0.000000 , 0.010000
@    yaxis  ticklabel start type auto
@    yaxis  ticklabel start 0.000000
@    yaxis  ticklabel stop type auto
@    yaxis  ticklabel stop 0.000000
@    yaxis  ticklabel char size 0.900000
@    yaxis  ticklabel font 0
@    yaxis  ticklabel color 1
@    yaxis  tick place both
@    yaxis  tick spec type none
@    altxaxis  off
@    altyaxis  off
@    legend on
@    legend loctype view
@    legend 0.85, 0.8
@    legend box color 1
@    legend box pattern 1
@    legend box linewidth 1.0
@    legend box linestyle 1
@    legend box fill color 0
@    legend box fill pattern 1
@    legend font 0
@    legend char size 1.000000
@    legend color 1
@    legend length 4
@    legend vgap 1
@    legend hgap 1
@    legend invert false
@    frame type 0
@    frame linestyle 1
@    frame linewidth 1.0
@    frame color 1
@    frame pattern 1
@    frame background color 0
@    frame background pattern 0
@    s0 hidden false
@    s0 type bar
@    s0 symbol 0
@    s0 symbol size SYMBOL_SIZE
@    s0 symbol color 1
@    s0 symbol pattern 1
@    s0 symbol fill color 1
@    s0 symbol fill pattern 1
@    s0 symbol linewidth 1.0
@    s0 symbol linestyle 1
@    s0 symbol char 65
@    s0 symbol char font 0
@    s0 symbol skip 0
@    s0 line type 0
@    s0 comment "Cols 1:2"
@    s0 legend  ""
@    s1 hidden false
@    s1 type bar
@    s1 symbol 0
@    s1 symbol size SYMBOL_SIZE
@    s1 symbol color 7
@    s1 symbol pattern 1
@    s1 symbol fill color 7
@    s1 symbol fill pattern 5
@    s1 symbol linewidth 1.0
@    s1 symbol linestyle 1
@    s1 symbol char 65
@    s1 symbol char font 0
@    s1 symbol skip 0
@    s1 line type 0
@    s1 comment "Cols 1:2"
@    s1 legend  ""
"""

		type_of_curve = """@    XX hidden false
@    XX type xy
@    XX symbol 2
@    XX symbol size SYMBOL_SIZE
@    XX symbol color COLOR
@    XX symbol pattern 1
@    XX symbol fill color COLOR
@    XX symbol fill pattern 1
@    XX symbol linewidth 1.0
@    XX symbol linestyle 1
@    XX symbol skip 0
@    XX line type 0
@    XX line linestyle 1
@    XX line linewidth 2.0
@    XX line color COLOR
@    XX line pattern 5
@    XX baseline type 0
@    XX baseline off
@    XX dropline off
@    XX fill type 0
@    XX fill rule 0
@    XX fill color 10
@    XX fill pattern 1
@    XX avalue off
@    XX avalue type 2
@    XX avalue char size 1.000000
@    XX avalue font 0
@    XX avalue color 1
@    XX avalue rot 0
@    XX avalue format general
@    XX avalue prec 3
@    XX avalue prepend ""
@    XX avalue append ""
@    XX avalue offset 0.000000 , 0.000000
@    XX errorbar off
@    XX comment "Cols 1:3"
@    XX legend  ""
"""


		# Raw data
		x_range = "%.5f"%(50./(max(self.universe.cspvalues.keys()) - min(self.universe.cspvalues.keys()) + 2))	# Size of each bar
		ymax  = "%.5f"%(max([self.model.raw_cspvalues[a] for a in self.model.raw_cspvalues if a in pumo]) + 0.2 * sum([self.model.raw_cspvalues[a] for a in self.model.raw_cspvalues if a in pumo])/len([self.model.raw_cspvalues[a] for a in self.model.raw_cspvalues if a in pumo]))
		ymin  = "%.5f"%(min([self.model.raw_cspvalues[a] for a in self.model.raw_cspvalues if a in pumo]) - 0.2 * sum([self.model.raw_cspvalues[a] for a in self.model.raw_cspvalues if a in pumo])/len([self.model.raw_cspvalues[a] for a in self.model.raw_cspvalues if a in pumo]))

		for a in (100., 10., 1., 0.1, 0.01):
			if (max(self.universe.cspvalues.values()) > a):
				TICK_MAJOR = str(2. * a)
				break
		
		intro_raw = intro.replace("XMIN", str(min(self.universe.cspvalues.keys())-1)).replace("XMAX", str(max(self.universe.cspvalues.keys())+1)).replace("TICK_MAJOR", TICK_MAJOR)
		intro_raw = intro_raw.replace("YMAX", ymax).replace("YMIN", ymin).replace("SYMBOL_SIZE", x_range)

		if inte: intro_raw += type_of_curve.replace("XX", "s2").replace("COLOR", "8").replace("SYMBOL_SIZE", x_range)	# For inte (purple)
		if pumo: intro_raw += type_of_curve.replace("XX", "s3").replace("COLOR", "2").replace("SYMBOL_SIZE", x_range)	# For pumo (red)

		upper = 0.2 * sum(self.universe.cspvalues.values()) / len(self.universe.cspvalues)

		# Building up data for chart of raw_data
		intro_raw += "@target G0.S0%c@type bar%c"%(os.linesep, os.linesep)
		for i in self.model.raw_cspvalues: intro_raw += "%d %.4f%c"%(i, self.model.raw_cspvalues[i], os.linesep)
		intro_raw += "&"+os.linesep
		intro_raw += "@target G0.S1%c@type bar%c"%(os.linesep, os.linesep)
		for i in self.universe.cspvalues: intro_raw += "%d %.4f%c"%(i, self.universe.cspvalues[i], os.linesep)
		intro_raw += "&"+os.linesep


		# Displaying up stars to show the selection
		try:		# Sometimes, there is no intermediate
			pos_symb = (float(ymax) + max([self.model.raw_cspvalues[a] for a in self.model.raw_cspvalues if a in inte])) / 2.
		except:
			pos_symb = (float(ymax) + max([self.model.raw_cspvalues[a] for a in self.model.raw_cspvalues if a not in inte+pumo])) / 2.
		if inte:
			intro_raw += "@target G0.S2%c@type xy%c"%(os.linesep, os.linesep)
			
			for i in inte: intro_raw += "%d %.4f%c"%(i, pos_symb, os.linesep)
			intro_raw += "&"+os.linesep

		if pumo:
			intro_raw += "@target G0.S3%c@type xy%c"%(os.linesep, os.linesep)

			for i in pumo: intro_raw += "%d %.4f%c"%(i, pos_symb, os.linesep)
			intro_raw += "&"+os.linesep

		f = open(filename_raw, "w")
		f.write(intro_raw)
		f.close()


		# Confidences
		ymax  = "1.2"; ymin = "-1.2"
		TICK_MAJOR = str(.2)
		intro_conf = intro.replace("XMIN", str(min(self.universe.cspvalues.keys())-1)).replace("XMAX", str(max(self.universe.cspvalues.keys())+1)).replace("TICK_MAJOR", TICK_MAJOR)
		intro_conf = intro_conf.replace("YMAX", ymax).replace("YMIN", ymin).replace("SYMBOL_SIZE", x_range)

		if inte: intro_conf += type_of_curve.replace("XX", "s2").replace("COLOR", "8").replace("SYMBOL_SIZE", x_range)	# For inte (purple)
		if pumo: intro_conf += type_of_curve.replace("XX", "s3").replace("COLOR", "2").replace("SYMBOL_SIZE", x_range)	# For pumo (red)

		# Building up data for chart of raw_data
		intro_conf += "@target G0.S0%c@type bar%c"%(os.linesep, os.linesep)
		for i in self.init_prob: intro_conf += "%d %.4f%c"%(i, self.init_prob[i], os.linesep)
		intro_conf += "&"+os.linesep
		intro_conf += "@target G0.S1%c@type bar%c"%(os.linesep, os.linesep)
		for i in self.end_prob : intro_conf += "%d %.4f%c"%(i, self.end_prob[i], os.linesep)
		intro_conf += "&"+os.linesep


		# Building up stars to show the selection
		pos_symb = 1.1
		if inte:
			intro_conf += "@target G0.S2%c@type xy%c"%(os.linesep, os.linesep)
			
			for i in inte: intro_conf += "%d %.4f%c"%(i, pos_symb, os.linesep)
			intro_conf += "&"+os.linesep

		if pumo:
			intro_conf += "@target G0.S3%c@type xy%c"%(os.linesep, os.linesep)

			for i in pumo: intro_conf += "%d %.4f%c"%(i, pos_symb, os.linesep)
			intro_conf += "&"+os.linesep

		f = open(filename_conf, "w")
		f.write(intro_conf)
		f.close()


	def run(self):
	
		printp(progress, "%sGenerating graphical file for xmgrace... "%(os.linesep*2))
		self.write_eps_file_of_raw_data(self.model.universe.data.input_data['workdir']+"/raw_data.agr", self.model.universe.data.input_data['workdir']+"/prob_data.agr", self.model.pumo, self.model.inte)
		printp(progress, "DONE%c"%os.linesep)

		
		if _graphical:
			if (_tkM.askquestion(title="Calculations Finished...", message="Calculations finished successfully!"+os.linesep+"Do you want to save"+os.linesep+"the output display ?"+os.linesep) == "yes"): self.save_output()
			prep.quit()
		else:
			print "\n\nCalculations finished successfully!\n\n"
			return


class Pymol(_th.Thread):

	def __init__(self, result):
	
		_th.Thread.__init__(self)

		self.result = result					# Coming from Model class
		self.resi = self.result.universe.res			# Known residues from the pdb file(s)

		self.infered = self.pymol_rangelist(self.result.universe.no_cspres+self.result.universe.prolines)

		# Classification of residues in the evolution of confidences
		self.resi_classification()


	def pymol_rangelist(self, liste=[]):
		tmplist = [m for m in liste]
		tmplist.sort()
		
		txt = ""
		
		# Determination of blocks of residues
		blocks = [[tmplist[0]]]
		single = []
		for i in range(1, len(tmplist), 1):
			if (tmplist[i] - tmplist[i-1] > 1):
				if (len(blocks[-1])<2):
					single.extend(blocks[-1])
					del blocks[-1]
				blocks.append([tmplist[i]])
			else:
				blocks[-1].append(tmplist[i])
		
		if (len(blocks[-1])<2):
			single.extend(blocks[-1])
			del blocks[-1]
		
		for i in blocks:
			if txt: txt += " or "
			txt += "resi %d-%d"%(i[0], i[-1])
		
		if single:
			if txt: txt += " or "
			txt += "resi " + "+".join([str(a) for a in single])
		
		
		return txt


	def resi_classification(self):
		# Need to know which residues we are going to color
		self.res_col = {}
		shift = 0
		for i in self.result.evol_prob:
			self.res_col[i+1-shift] = {"core":[], "inte":[], "pumo":[]}
			for j in self.result.evol_prob[i]:
				if (self.result.evol_prob[i][j]<self.result.lower):
					self.res_col[i+1-shift]["core"].append(j)
				elif(self.result.evol_prob[i][j]>self.result.upper):
					self.res_col[i+1-shift]["pumo"].append(j)
				else:
					self.res_col[i+1-shift]["inte"].append(j)
			# Checking whether this evolution is not present yet
			for j in range(1, i+1-shift):
				if (self.res_col[i+1-shift]==self.res_col[j]):
					del self.res_col[i+1-shift]
					shift += 1
					break


	def write_PyMol_file(self, filename):
	
		# Creation of the initial PyMol file

		pymol_script = """from pymol import cmd
import os
cmd.set("hide_underscore_names", "1")
cmd.set("bg_rgb", "[.75, .75, .75]")
cmd.set("sphere_scale", "0.4")
cmd.load("%s", "_prot")
cmd.hide("everything")
cmd.show("cartoon")
cmd.show("sphere", "resn pro and name n+nh")
"""%(self.result.universe.structures[0])

		f = open(filename, "w")
		f.write(pymol_script)

		if self.infered:
			f.write('cmd.select("_infered", "%s")%c'%(self.infered, os.linesep))
			f.write('cmd.show("sphere", "_infered  and name ca")%c'%os.linesep)


		f.write('cmd.mset("1 -%d")%c'%(len(self.res_col), os.linesep))
		for i in self.res_col:
			f.write('cmd.mdo(%d, "color black'%i)
			if self.res_col[i]["core"]: f.write('; color blue, %s'%self.pymol_rangelist(self.res_col[i]["core"]))
			if self.res_col[i]["inte"]: f.write('; color purple, %s'%self.pymol_rangelist(self.res_col[i]["inte"]))
			if self.res_col[i]["pumo"]: f.write('; color red, %s'%self.pymol_rangelist(self.res_col[i]["pumo"]))
			f.write('")%c'%os.linesep)
		
		f.write('cmd.mplay()%c'%os.linesep)
		f.close()


	def run(self):

		printp(progress, "Generating evolution file for PyMol... ")
		self.write_PyMol_file(self.result.universe.data.input_data['workdir']+"/samplex_pymol.pml")
		printp(progress, "DONE%c"%os.linesep)


		os.system(self.result.universe.data.input_data["pymol"]+" "+self.result.universe.data.input_data['workdir']+"/samplex_pymol.pml &")



def printp(win, text=os.linesep):
	# This function is writing in the progression windows
	if _graphical:
		win.insert(END, text)
		win.see(END)
	else:
		print text,

def stat(v):
	"""
	This function returns the average and the variance of values of a given vector
	"""
	   
	sum_   = 0.00
	sum_sq = 0.00
	for i in v:
		try:
			sum_   += float(i)
			sum_sq += math.pow(float(i), 2)
		except:
			pass
	aver = sum_ / len(v)
	return [aver, sum_sq / len(v) - math.pow(aver,2)]


def avstdv(v):
	"""
	This function returns the average and the standard deviation of values of a given vector
	"""

	# Calculation of the arithmetic average
	average = 1. * sum(v) / len(v)

	# Calculation of the standard deviation
	stdv = 0.
	for i in v: stdv += ((i - average) * (i - average))
	stdv = math.sqrt(stdv/len(v))

	return average, stdv

	
def msort(liste, indice):
	"""
	This function sorts a vector regarding values of the indice 'indice'
	Indice start from 0
	"""
	
	tmp = [[tbl[indice]]+[tbl] for tbl in liste]
	tmp.sort()
	liste = [cl[1] for cl in tmp]
	del tmp
	return liste

	
def usage():
	print("\tUsage : ./csp.py [-f filename.pnle] [-ng] [-pymol]")
	print("\nThe filename.pnle is required when -ng (non-graphical interface) is specified\n\n")
	sys.exit()



if (__name__ == "__main__"):


	# Retrieving all data via a graphical interface
	for arg in ("-H", "-HELP"):
		if arg in sys.argv: usage()

	filename = ""
	for arg in (sys.argv):
		if arg.upper() in ("-F", "-FILE"): filename = sys.argv[sys.argv.index(arg)+1]

	_PYMOL = 1

	if "-ng" in sys.argv:
		_graphical = 0
		if not filename: usage()

		prep = Preparation(filename=filename)		# Preparation
	else:
		_graphical = 1

		try:
			lib_to_add = "idelib.TreeWidget and ScrolledText libraries"
			from idlelib.TreeWidget import *
			lib_to_add = "ScrolledText library"
			from ScrolledText import *
		except:
			print "Some crucial graphical libraries are missing on this computer!"
			print "You might re-run the program on Non-Graphical interface ('-ng' option),\nor add", lib_to_add, "for your Python version.\n\n"
			sys.exit()

		prep = Preparation(filename=filename)		# Preparation
		prep.mainloop()

		for i in (prep.winfo_children()): i.destroy()
		for i in (prep.main_info_frame.winfo_children()): i.destroy()
		prep.main_info_frame.destroy()		# Removing the main frame
		for i in prep.toremove: i.destroy()
		



	# Retrieving the characteristics of the system
	system = System(prep)

	if _graphical:
		progress = Text(prep.main_info_can, relief=FLAT, takefocus=0, padx=2, pady=12, foreground="#333300", font="courier 12 bold")
		progress.grid(column=0, row=0, rowspan=14, columnspan=6, sticky=S+E+W+N)
		prep.VScrMainInfo.configure(command=progress.yview)
		prep.HScrMainInfo.configure(command=progress.xview)
		progress["yscrollcommand"] = prep.VScrMainInfo.set
		progress["xscrollcommand"] = prep.HScrMainInfo.set
		prep.main_info_frame.update_idletasks()
		prep.main_info_can.configure(scrollregion=(0, 0, progress.winfo_width(), progress.winfo_height()))	
		system.start()
		prep.mainloop()
	else:
		progress = ""		# Fake declaration because 'progress' does not exist in non-graphical mode
		print "SAMPLEX"+os.linesep+"Prediction of perturbed and unperturbed regions of proteins from HSQC NMR data"+os.linesep+"G. Fuentes, M. Krzeminski, A. Bonvin"+os.linesep*3
		system.run()



	# Creation of the thread that will run calculations
	model = Model(system)
	if _graphical:
		model.start()		# New process launched
		prep.mainloop()

		try:
			end = Conclusion(model)
			end.start()
			prep.mainloop()

			if (prep.pymol["state"].get()):
				pymol = Pymol(model)
				pymol.start()

			prep.mainloop()		# To keep the window opened if the user wants to check results
		except:
			pass
	else:
		model.run()		# Mere function launched

		end = Conclusion(model)
		end.run()



