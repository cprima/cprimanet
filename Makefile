SHELL := /bin/bash

serve:
	export JEKYLL_LOG_LEVEL=debug && bundle exec jekyll serve --livereload
