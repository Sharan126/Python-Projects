# =============================
# Video to Audio Converter (MP3)
# =============================

import subprocess
import imageio_ffmpeg as ffmpeg
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Hide tkinter window
Tk().withdraw()

print("Select a video file...")

video_path = askopenfilename(
    title="Choose Video File",
    filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov *.flv")]
)

if not video_path:
    print("❌ No file selected.")
    exit()

# Get FFmpeg executable path automatically
ffmpeg_path = ffmpeg.get_ffmpeg_exe()

# Output file
output_audio = os.path.splitext(video_path)[0] + ".mp3"

try:
    print("⏳ Extracting audio...")

    subprocess.run([
        ffmpeg_path,
        "-i", video_path,
        "-vn",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_audio
    ], check=True)

    print("✅ Audio saved as:", output_audio)

except Exception as e:
    print("❌ Error:", e)

print("--- Program Finished ---")
