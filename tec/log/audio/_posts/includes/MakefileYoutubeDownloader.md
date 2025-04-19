#{{ include.headingmodifier }} Makefile for youtube-dl

Any repetitive manual task should be automated, for example the analysis of a whole YouTube channel.
For speedy access to the videos the files need to be downloaded to the local harddrive, which is the core functionality of the Python-based commandline program `youtube downloader` and its improved fork yt-dl.

And a conveninet way to make this whole process repeateble is to write a shell script in the form of a Makefile. To run such files from the Unix world on Windows the WSL Windows Subsystem for Linux can be used.

The Makefile is published as a GitHub Gist https://gist.github.com/cprima/0d331d5a2c366688998071f6b61774fd

Result is that a few commands may be run daily and produce the raw material for an analysis.

Youtube downloader keeps track of the videos already downloaded in the past.

The metadata from YouTube is returned in JSON Format and again Python is a good technological fit to aggregate each individual file into a tabular format. A quick Jupyter Notebook does the job well.


```bash
#/**
# * Helper commands to analyse YouTube videos
# *
# * @author: Christian Prior-Mamulyan <cprior@gmail.com>
# * @license: MIT
# *
# * @usage: export YTCHANNELVIDEOURL=https://www.youtube.com/watch?v=iavXywwUh1c
# * @usage: make -e download_audio
# *
# * depends on https://github.com/yt-dlp/yt-dlp
# */

YTCHANNELBASEURL=https://www.youtube.com/channel/
YTCHANNELID=UCPdtz4gd_iYebJFYq9N8pWA
YTCHANNELVIDEOURL?=https://www.youtube.com/watch?v=7UN1xRN24xY
BATCH_FILE=urls.txt
ARCHIVE_FILE=archive.txt
SLEEP_REQUESTS=8
MIN_SLEEP_INTERVAL=8
MAX_SLEEP_INTERVAL=128
SUBTILES_LANG=en
LIMIT_RATE=5M
TROTTLED_RATE=50K
_BESTEALTHY=--limit-rate $(LIMIT_RATE) --throttled-rate $(TROTTLED_RATE) --min-sleep-interval $(MIN_SLEEP_INTERVAL) --max-sleep-interval $(MAX_SLEEP_INTERVAL) --sleep-requests $(SLEEP_REQUESTS)
_WRITEMETADATA=--write-url-link --write-info-json --write-description --write-info-json --write-thumbnail --write-auto-subs --sub-lang $(SUBTILES_LANG)


.PHONY: list_channel_videourls
list_channel_videourls:
	@echo "# pipe the output to e.g. >> $(BATCH_FILE)"
	@yt-dlp --get-filename --no-warnings --quiet -o "https://www.youtube.com/watch?v=%(id)s" $(addprefix $(YTCHANNELBASEURL),$(YTCHANNELID))

.PHONY: download_videos
download_videos:
	yt-dlp --limit-rate $(LIMIT_RATE) $(_BESTEALTHY) --continue --ignore-errors --no-overwrites --output "%(upload_date)s_%(acodec)s_%(asr)s_%(title)s.%(ext)s" --batch-file $(BATCH_FILE) $(_WRITEMETADATA)

```
