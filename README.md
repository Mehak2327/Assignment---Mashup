# 🎵 Mashup Generator Assignment

Student Name: Mehak  
Roll Number: 102303792  

This project implements a Mashup Generator using Python. The system downloads multiple YouTube videos of a given singer, converts them into audio files, trims a fixed duration from each audio clip, and merges them into a single mashup file. A simple web application is also provided to perform the same task through a browser.

Project Files:  
102303792.py – Command Line Mashup Program  
app.py – Flask Web Application  
templates/index.html – Web Form  
README.md  
.gitignore  

Technologies Used:  
Python 3.11, yt-dlp, pydub, ffmpeg, Flask  

Installation:  
py -3.11 -m pip install yt-dlp pydub flask  
ffmpeg -version  

Program 1 (Command Line Usage):  
py -3.11 102303792.py "Singer Name" NumberOfVideos Duration OutputFile  

Example:  
py -3.11 102303792.py "Arijit Singh" 15 30 output.mp3  

Program 2 (Web Application):  
py -3.11 app.py  
Open browser and visit: http://127.0.0.1:5000  
Enter required details and click Generate Mashup.

Input Conditions:  
Number of videos must be greater than 10  
Duration must be greater than 20 seconds  

Output:  
A single merged mashup audio file in MP3 format is generated in the project directory.

Note:  
Audio (.mp3) files are ignored using .gitignore and are not uploaded to GitHub.

Conclusion:  
This project demonstrates Python-based automation, multimedia processing, and web integration for mashup generation.

End of File
