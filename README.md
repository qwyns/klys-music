# Klys Music Tools

Various Tools used for processing music files

Available tools:
1. File Stats `[ungeneric]`
2. ID3 Retagging (based on my algorithm for storing files) `[ungeneric]`
3. Playlist Generator `[ungeneric]`

---

## File Stats

Pretty self-explanatory, choose a folder and it will tell yoiu how many songs are present across all subfolders. For now, neds to have a layout like hte one described below.

---

## ID3 Retagging

Performs ID3 retagging of all .mp3 files in the given folder following the layout given below. Specifically, the algorithm used is:

Example file: `Chemical Brothers - Believe.mp3` inside  `EDM` folder

| Tag | Value |
| - | - |
| Artist  | Chemical Brothers |
| Album | EDM |
| Title | Believe |
| Genre | `<blank>` |
| Comments | Tagged by Klys' Music Tools |

---

## Playlist Generator

Generates playlists for a given folder's contents. Must be in given layout. Generates `overall.m3u` for all songs and `./Individual/<folder_name>/m3u for subfolders`.


---
### Required Layout

```txt
Parent Directory
+-- Music Type 1
|   +-- Song 1 of Music Type 1
|       .
|       .
|       .
|   +-- Song n of Music Type 1
+-- Music Type 2
|   +-- Song 1 of Music Type 2
|       .
|       .
|       .
|   +-- Song n of Music Type 2
```