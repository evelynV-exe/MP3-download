import os
import argparse
import syncedlyrics # not very accurate so make sure to check the content inside

# ── Song list (edit or extend as needed)
SONGS = [
    "Song-title",
]

# strip off the symbols
def sanitize_filename(name: str) -> str:
    return "".join(c for c in name if c not in r'\/:*?"<>|')

# get lyrics
def fetch_lyrics(songs: list[str], music_dir: str, save_lrc: bool = True) -> None:
    music_dir = os.path.expanduser(music_dir)
    os.makedirs(music_dir, exist_ok=True)

    success, failed = [], []

    for song in songs:
        print(f"\n  Searching: {song}")
        try:
            lrc = syncedlyrics.search(song)
            if lrc:
                if save_lrc:
                    filename = sanitize_filename(song) + ".lrc"
                    out_path = os.path.join(music_dir, filename)
                    with open(out_path, "w", encoding="utf-8") as f:
                        f.write(lrc)
                    print(f"    Saved → {out_path}")
                else:
                    print(lrc[:200], "…")   # preview only
                success.append(song)
            else:
                print(f"     No synced lyrics found.")
                failed.append(song)
        except Exception as e:
            print(f"    Error: {e}")
            failed.append(song)

    # Summary

    print("\n" + "═" * 50)
    print(f"Done!  {len(success)}/{len(songs)} lyrics fetched.")

    # in case it failed
    if failed:
        print("\nMissing lyrics for:")
        for s in failed:
            print(f"  • {s}")
    print("═" * 50)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch synced lyrics for MP3 list.")
    parser.add_argument(
        "--music-dir",
        default=".",
        help="Folder where .lrc files will be saved (default: current directory)",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Print lyrics to console instead of saving files",
    )
    args = parser.parse_args()

    fetch_lyrics(SONGS, music_dir=args.music_dir, save_lrc=not args.preview)