import yt_dlp
import os
import sys
import time
from pathlib import Path

OUTPUT_DIR = "./downloads"       # Folder saved
MP3_QUALITY = "192"              # Bitrate: 128 / 192 / 256 / 320
SLEEP_BETWEEN = 2                # Seconds to wait between downloads
SKIP_ON_ERROR = True             # True = skip failed links, False = stop on first error

def build_ydl_opts(output_dir: str, quality: str) -> dict:
    """Build yt-dlp options for MP3 extraction."""
    return {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "cookiesfile": "cookies.txt", #Your cookies when login into YouTube
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": quality,
            }
        ],
        "quiet": False,
        "no_warnings": False,
        "noplaylist": True,   
        "ignoreerrors": False,
        "retries": 3,
        "fragment_retries": 3,
    }

# Strip whitespace/blank lines from URL list
def sanitize_urls(raw_urls: list[str]) -> list[str]:
    return [u.strip() for u in raw_urls if u.strip()]

# Download a single URL
# Returns True = success, False = Failure.
def download_single(url: str, ydl_opts: dict) -> bool:
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get("title", url)
            print(f"\n  ▶  {title}")
            print(f"     Duration : {info.get('duration', 0) // 60}m {info.get('duration', 0) % 60}s")
            print(f"     Channel  : {info.get('uploader', 'Unknown')}")
            ydl.download([url])
        return True
    except yt_dlp.utils.DownloadError as e:
        print(f"\n  Download failed: {e}")
        return False
    except Exception as e:
        print(f"\n  Unexpected error: {e}")
        return False

# Download MP3 for every URL in the list
# Prints a summary report at the end
def download_all(urls: list[str], output_dir: str = OUTPUT_DIR, quality: str = MP3_QUALITY):
    urls = sanitize_urls(urls)
    if not urls:
        print("No URLs provided.")
        return
 
    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)
 
    ydl_opts = build_ydl_opts(output_dir, quality)
 
    total   = len(urls)
    passed  = []
    failed  = []
    
    # Summary zone
    print(f"\n{'─' * 50}")
    print(f"  YouTube MP3 Downloader")
    print(f"  {total} link(s)  •  {quality} kbps  •  → {output_dir}")
    print(f"{'─' * 50}")
 
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{total}] {url}")
        success = download_single(url, ydl_opts)
 
        if success:
            passed.append(url)
        else:
            failed.append(url)
            if not SKIP_ON_ERROR:
                print("\nStopping due to error (SKIP_ON_ERROR=False).")
                break
 
        # Polite delay between requests (skip after last)
        if i < total:
            time.sleep(SLEEP_BETWEEN)
 
    # Summary
    print(f"\n{'─' * 50}")
    print(f"  Done!  S: {len(passed)} succeeded  F: {len(failed)} failed")
    if failed:
        print("\n  Failed URLs:")
        for url in failed:
            print(f"    • {url}")
    print(f"{'─' * 50}\n")

if __name__ == "__main__":

    # YouTube links in links.txt
    with open("links.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    download_all(urls)