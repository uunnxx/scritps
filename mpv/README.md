# MPV Related Scripts



## Requirements

```
python-mpv-jsonipc
```

## Usage

`mpv_nowplaying.py:`
Broadcast currently playing to `dunstify` if any changes.

```
./mpv_nowplaying.py

# or just run as daemon:
(./mpv_nowplaying.py&)&
```

----------------------------------------------------------

`mpv_control.py:`
Controls `mpv` with:

```
./mpv_control.py pause
./mpv_control.py play
./mpv_control.py next
./mpv_control.py prev
```

OR:

```
# Rename without .py
mv ./mpv_nowplaying ~/.local/bin/
mv ./mpv_control.py ~/.local/bin/

# daemonize broadcaster
(mpv_nowplaying&)&

mpv_control pause
mpv_control play
mpv_control next
mpv_control prev
```

