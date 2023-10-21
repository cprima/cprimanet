---
checklists: []
---

https://clarkgrubb.com/makefile-style-guide

https://stackoverflow.com/a/34508832



```Makefile
YTCHANNELBASEURL=https://www.youtube.com/channel/
YTCHANNELID=UCPdtz4gd_iYebJFYq9N8pWA
BATCH_FILE=urls.txt
ARCHIVE_FILE=archive.txt
SLEEP_REQUESTS=8
MIN_SLEEP_INTERVAL=8
MAX_SLEEP_INTERVAL=128
SUBTILES_LANG=en
LIMIT_RATE=5M
TROTTLED_RATE=50K

.PHONY: list_channel_videos
list_channel_videos:
        @echo "# pipe the output to e.g. >> $(BATCH_FILE)"
        @yt-dlp --get-filename --no-warnings --quiet -o "https://www.youtube.com/watch?v=%(id)s" $(addprefix $(YTCHANNELBASEURL),$(YTCHANNELID))

.PHONY: download_videos
download_videos:
        yt-dlp --limit-rate $(LIMIT_RATE) --throttled-rate $(TROTTLED_RATE) --min-sleep-interval $(MIN_SLEEP_INTERVAL) --max-sleep-interval $(MAX_SLEEP_INTERVAL) --sleep-requests $(SLEEP_REQUESTS) --continue --ignore-errors --no-overwrites --output "%(upload_date)s_%(acodec)s_%(asr)s_%(title)s.%(ext)s" --batch-file $(BATCH_FILE) --download-archive $(ARCHIVE_FILE) --write-url-link --write-info-json --write-description --write-info-json --write-thumbnail --write-auto-subs --sub-lang $(SUBTILES_LANG)
```