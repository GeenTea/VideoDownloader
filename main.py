from pytubefix import YouTube   # Import the 'YouTube' class from the 'pytube' library for downloading YouTube videos.
from pytubefix.cli import on_progress

def Download(link, value): # Define a function named 'Download' that takes two arguments: 'link' (the video URL) and 'value' (either 'mp3', 'mp4', or 'both').
    try:
        youtube_object = YouTube(link) # Create a YouTube object from the video URL provided.
        youtube_object = youtube_object.streams.get_highest_resolution()# Fetch the highest resolution video stream available.


        video = YouTube(link) # Create another YouTube object for extracting audio.
        mp3 = video.streams.filter(only_audio=True).first() # Filter and select the first available audio stream (MP3).

        if mp3_mp4 == "mp4":
            youtube_object.download() # If the user chose 'mp4', download the highest resolution video.
        elif mp3_mp4 == "mp3":
            mp3.download(filename=f"{video.title}.mp3") # If 'mp3' is selected, download the audio and save it as an .mp3 file with the video's title.
        elif mp3_mp4 == "both":
            youtube_object.download() # If 'both' is selected, download the highest resolution video...
            mp3.download(filename=f"{video.title}.mp3") # ... and download the audio as an .mp3 file.

        print("Download has completed successfully") # Print a success message when the download finishes.
    except Exception as e:
        print(f"An error has occurred: {e}") # If an exception occurs, print the error message.


link = input("Enter the YouTube video URL:") # Ask the user to input the YouTube video URL.
mp3_mp4 = input("Do you want download mp3,mp4 or both :") # Ask the user if they want mp3, mp4, or both.

while mp3_mp4 != "mp3" and mp3_mp4 != "mp4" and mp3_mp4 != "both":
    mp3_mp4 = input("Try again, give value, mp3 or mp4:") # Keep asking the user for a valid input until they enter 'mp3', 'mp4', or 'both'.

Download(link, mp3_mp4) # Call the 'Download' function with the user's input values (the URL and the format).
