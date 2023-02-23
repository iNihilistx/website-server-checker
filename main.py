import customtkinter
import tkinter as tk
import urllib.request
from urllib.error  import HTTPError, URLError

def test_connection():
	customtkinter.set_appearance_mode("system")
	customtkinter.set_default_color_theme("blue")

	app = customtkinter.CTk()
	app.geometry("400x240")
	app.resizable(False, False)
	app.title("Website Server Tester")
	head = customtkinter.CTkLabel(app, text="Website Server Tester")
	head.pack(pady=20)

	def check_url_connection():
		web = (f"https://{url.get()}")
		try:
			status_code = urllib.request.urlopen(web).getcode()
			server_is_up = status_code == 200
			server_refused = 403
			if server_is_up:
				customtkinter.CTkLabel(app, text="Connection Established!").place(x=130, y=190)
		except URLError as error:
			customtkinter.CTkLabel(app, text="Connection Refused!").place(x=130, y=190)

	url = customtkinter.StringVar()
	entry_text = customtkinter.CTkLabel(app, text="example: www.google.com")
	entry_text.pack(pady=2)
	entry = customtkinter.CTkEntry(app, width=210, textvariable=url)
	entry.pack(pady=10)
	button = customtkinter.CTkButton(app, text="Test", command=check_url_connection)
	button.pack(pady=5)
	app.mainloop()
if __name__ == "__main__":
	test_connection()