import tkinter, tkinter.filedialog as tf
import moviepy.editor as mp

tk = tkinter.Tk()

def main():
    tkinter.Tk().withdraw() # Close the root window
    in_path = tf.askopenfilename()
    print(in_path)
    convert(in_path)

def convert(filePath):
    video = mp.VideoFileClip(filePath)
    video.audio.write_audiofile("Converted.mp3")

tk.title('Video to Audio')
address_button = tkinter.Button(tk, text="Submit_Address", command = main)
address_button.pack()

tk.mainloop()