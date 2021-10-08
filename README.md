# Webcam Motion Detection
I know there's already better motion detection CCTV in the market. This is just a simple(low-budget DIY) version to make your webcam (external too) a motion detection camera. It plays two different kind of alarm. I'm using this to detect if there are people at my convenience store.

### Setup
Note: Only if you want to use venv
```
> python -m venv venv (if that does not work then try: python3 -m venv venv)
> source venv/bin/activate
```

install all the dependency using this
```
pip install -r requirements.txt
```

Change `alert_diff_limit` value in `main.py` to increase/decrease the time limit for alert.

### How to run
If you're using venv then activate it
```
source venv/bin/activate
```
and run main command
```
python main.py
```


### Alias
You can also create alias in your `.bashrc` or `.zshrc` for shortcut like this.
```
alias wmd="source ~/webcam_motion_detection/venv/bin/activate && python ~/webcam_motion_detection/main.py && deactivate"
```

*The above example assumes that the project is in home folder, change it if you place it elsewhere. Sorry if this does not work on windows* 😂


# TODO:
- Noise filter for detection, sometimes it detects even when nothing is being changed
- Improve or increase the `alert_diff_limit` logic
- Send push notification to the phone
- Track the change detected and record the video

# Future plan:
- Face recognition with multiple camers
