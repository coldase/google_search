from tkinter import *
import requests
import webbrowser

def main():

	def google_search(term):
		url = "https://www.google.com/search"
		res = requests.get(url,
			headers={"Accept":"text/plain"},
			params={"q":term,"oq":term})
		return res.url

	def get_value():
		new_term = search_entry.get()
		url = google_search(new_term)
		webbrowser.open(url)

	def key_pressed(event):
		get_value()


	root = Tk()
	root.title("GoogleSearch")
	root.geometry("200x100")
	root.bind("<Return>",key_pressed)

	search_entry = Entry(root)
	search_btn = Button(root, command=get_value, text="Search")

	search_entry.pack(pady=15)
	search_btn.pack()

	mainloop()


if __name__ == "__main__":
	main()