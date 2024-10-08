# ============================================================ Imports

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import save_ui
import dwelling_basic_ui as ibv

# Ventana 1
# ============================================================ Classes

class Georeferenciation(ttk.Frame):
	
	""" Class dedicated to get geolocation of the dwelling """
	
	def __init__ (self, parent):
		"""
		Initializes the Georeferenciation class.

		Parameters:
			parent (object): The parent object of the Georeferenciation class.

		Returns:
			None

		Initializes the Georeferenciation class by setting up the font, creating a labelframe for georeferenciation,
		adding a button to replace the image, and creating entry fields for latitude and longitude.
		"""
		ttk.Frame.__init__(self,parent)
		self.font = ('Iosevka 11')

		# ~ fotografia
		# --------------------------------------------------- Geo_Frame
		self.geo_frame =  ttk.Labelframe(self, text = 'Georreferenciación de vivienda')
		self.geo_frame.pack(fill = tk.X, padx = 5, pady = 5)
		
		self.photo_button = ttk.Button(self.geo_frame, text = 'Reemplazar', command = self.replace_image).grid(row = 0, column = 0, sticky = 'WE', padx = 5, pady = 10)
		
		# ~ latitud
		# ~ self.latitud = tk.StringVar()
		ttk.Label(self.geo_frame, text = 'Latitud').grid(row = 5, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		self.latitude_entry = ttk.Entry(self.geo_frame)
		self.latitude_entry.grid(row = 5, column = 1, sticky = 'WE', padx = 10)
		self.latitude_entry.insert(0,random.randint(-1000,1000))
		self.latitude_entry.configure(font = self.font, background = '#5FE888', foreground = '#E8A548', state = 'readonly')
		
		# ~ longitud
		# ~ self.longitud = tk.StringVar()
		ttk.Label(self.geo_frame, text = 'Longitud').grid(row = 6, column = 0, sticky = 'WE', padx = 5, pady = 5)
		
		self.longitude_entry = ttk.Entry(self.geo_frame)
		self.longitude_entry.grid(row = 6, column = 1, sticky = 'WE', padx = 10)
		self.longitude_entry.insert(0,random.randint(-1000,1000))
		self.longitude_entry.configure(font = self.font, background = '#5FE888', foreground = '#E8A548', state = 'readonly')
		
		# --------------------------------------------------------- Btn
		# ~ siguiente
		self.next_button = ttk.Button(self, text = 'Siguiente', command = lambda: self.message_data(parent))
		self.next_button.pack(fill = tk.X, padx = 5, pady = 10)
	
	def replace_image (self):
		"""
		Replaces the current image with a new one.
		
		Parameters:
			self: The instance of the class.
		
		Returns:
			None
		"""
		print('Replace Image')
	
	def message_data (self, parent):
		message = f'''
Latitud: {self.latitude_entry.get()}
Longitud: {self.longitude_entry.get()}
		'''
		
		if messagebox.askyesno(message = message, title = 'Salvar georreferenciación'):
			print('Los datos de georreferenciación han sido guardados exitosamente')
			save_ui.save_georreferenciation(self.latitude_entry.get(), self.longitude_entry.get())
			parent.switch_frame(ibv.Dwelling_basic)

class Application(tk.Tk):
	
	def __init__ (self):
		"""
		Class initialiser.
		
		Initialises the Application class by calling the Tk class initialiser and creating a new Georeferenciation frame.
		
		Parameters:
			self: The instance of the class.
		
		Returns:
			None
		"""
		tk.Tk.__init__(self)
		self._frame = Georeferenciation(self)
		self._frame.pack()

# ====================================================== Program Entry

def main():
	"""
	The main function is the entry point of the program. It creates an instance of the Application class and starts the main event loop.

	Parameters:
		None

	Returns:
		int: The program exit status, which is always 0.
	"""

	root = Application()
	root.mainloop()
	return 0

if __name__ == '__main__':
	main()
