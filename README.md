# MP3 Downloader

A lightweight Python-based YouTube MP3 downloader with synced lyrics generation support.

Built with:
- `yt-dlp`
- `ffmpeg`
- `syncedlyrics`

---

# Features

- Download YouTube audio as MP3
- Batch download using `links.txt`
- Automatic MP3 conversion
- Synced `.lrc` lyrics generation
- Retry + error handling system
- Clean terminal output
- Custom bitrate configuration

---

# Preview

<img width="1446" height="520" alt="python mp3" src="https://github.com/user-attachments/assets/90756391-90bb-4acc-b789-257cb4fa64c2" />

---

# Requirements

## Python Packages

Install required libraries:

```bash
pip install yt-dlp syncedlyrics
```

---

## FFmpeg

FFmpeg is required for MP3 conversion.

### Windows
Download FFmpeg and add it to PATH.

### Linux

```bash
sudo apt install ffmpeg
```

### macOS

```bash
brew install ffmpeg
```

---

# Project Structure

```txt
.
├── download_mp3.py
├── generate_lyrics.py
├── links.txt
├── cookies.txt
├── downloads/
└── README.md
```

---

# Setup

## 1. Add YouTube Links

Create a `links.txt` file:

```txt
https://youtu.be/example1
https://youtu.be/example2
```

---

## 2. Add Cookies (Optional)

Some videos may require login cookies.

Export browser cookies into:

```txt
cookies.txt
```

Example:

```txt
.youtube.com TRUE / TRUE 2147483647 SID EXAMPLE_TOKEN
```

Never upload real cookies publicly.

---

# Download MP3 Files

Run:

```bash
python download_mp3.py
```

Downloaded files will be saved into:

```txt
./downloads
```

---

# Generate Synced Lyrics

Edit the song list inside `generate_lyrics.py`:

```python
SONGS = [
    "Song name",
]
```

Run:

```bash
python generate_lyrics.py --music-dir ./downloads
```

This creates synced `.lrc` lyric files.

---

# Configuration

Inside `download_mp3.py`:

```python
OUTPUT_DIR = "./downloads"
MP3_QUALITY = "192" // you can send the quality yourself
SLEEP_BETWEEN = 2
SKIP_ON_ERROR = True
```

---

# MP3 Quality Options

```txt
128
192
256
320
```

---

# Notes

- `syncedlyrics` may not always return accurate timestamps.
- Some YouTube videos may block downloads without cookies.
- Playlist downloading is disabled by default.

---

# Language and libraries Used

- Python
- yt-dlp
- FFmpeg
- SyncedLyrics

---

# Disclaimer

This project is for educational and personal use only.
Please respect copyright laws and YouTube's Terms of Service.

---

# Author

Evelyn
