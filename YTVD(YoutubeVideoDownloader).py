#--------------LIBARY------------
# Importing necessary packages
from tkinter import*
import pytube
from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk

#--------------FUNCTIONS------------
directory = ""
# Defining openPath() to store the path
def openPath():
	global directory
	if(directory == ""):
		directory = filedialog.askdirectory()	
		pathHolder.config(text = directory)

	else:
		removeText(pathHolder)

# Defining removeText() to remove the 
# invalid path
def removeText(pathHolder):
	global directory
	pathHolder.config(text = "")
	directory = ""
	openPath()

# Defining download() to download the video
def download():
	url = urlEntry.get()
	select = downloadTypes.get()

	if(len(url) < 1):
		urlError.config(text = "Please insert URL.")

	if(len(directory) < 1):
		pathError.config(text = "Please insert Path.")

	else:
		urlError.config(text = "")
		pathError.config(text = "")


		yt = YouTube(url)
			
		if(select == downloadOptions[0]):
			ys = yt.streams.get_highest_resolution()
			

		elif(select == downloadOptions[1]):
			ys = yt.streams.filter(only_audio = True).first()

		
		ys.download(directory)
		urlEntry.delete(0, END)

		pathHolder.config(text = "\t")
		downloadOut.config(text = "Downloaded!!")

		name = ys.title
		downloadName.config(text = "Name : " + name)
		downlaodLocation.config(text = "Path : "+ directory)

#--------------TKINTER------------
# Creating object of tk class
root = Tk()

# Setting the title, 
# size of the tkinter window 
root.title("YoutubeVideoDownloader")
root.geometry("600x400")

# Calling the necessary tkinter widgets
name = Label(root, text = "Made by - Shivam Taneja")
name.grid(row = 10, column = 1, padx = 10,pady = 9, sticky = "e")

heading = Label(root, text = "Download Video and Audio from YouTube")
heading.grid(row = 0, column = 0, columnspan = 4, pady = 10)

urlLabel = Label(root, text = "Enter the URL :")
urlLabel.grid(row = 1, column = 0, pady = 5,sticky ="w", padx = 7)

urlEntry = Entry(root, width = 75, borderwidth = 1)
urlEntry.grid(row = 1, column = 1,  pady = 5,sticky ="w", padx = 7)

urlError = Label(root)
urlError.grid(row = 1, column = 1,  pady = 5,sticky ="w", padx = 2)

pathLabel = Label(root, text = "Path :")
pathLabel.grid(row = 2, column = 0, sticky ="w", padx = 7)

pathButton = Button(root, text = "Select Path", command = openPath)
pathButton.grid(row = 3, column = 1,columnspan = 4,pady = 5,sticky ="w",padx = 7)

pathError = Label(root)
pathError.grid(row = 2, column = 1,columnspan = 4,pady = 5,sticky ="w",padx = 9)

pathHolder = Label(root)
pathHolder.grid(row = 2, column = 1,columnspan = 4,pady = 5,sticky ="w",padx = 7)

downloadLabel = Label(root, text = "Downlaod Type :")
downloadLabel.grid(row = 4, column = 0,pady = 5,sticky ="w", padx = 7)

downloadOptions = ["High Quality", "Audio Only"]
downloadTypes = ttk.Combobox(root, values = downloadOptions)
downloadTypes.grid(row = 4, column = 1,columnspan = 4,sticky ="w", padx = 7)

downloadOut = Label(root, font = (10))
downloadOut.grid(row = 9, column = 1,columnspan = 4,sticky ="w", padx = 7)

downloadName = Label(root)
downloadName.grid(row = 6, column = 1,columnspan = 4,sticky ="w", padx = 7)

downlaodLocation = Label(root)
downlaodLocation.grid(row = 7, column = 1,columnspan = 4,sticky ="w", padx = 7)

downloadError = Label(root)
downloadError.grid(row = 9, column = 0, columnspan = 4, pady = 15)

downloadButton = Button(root, text = "DOWNLOAD!",command = download, width = 30, height = 3)
downloadButton.grid(row = 8, column = 0, columnspan = 4, pady = 15)

# Defining infinite loop to run
# application
root.mainloop()