all: armenisch kyrillisch

armenisch:
	pdflatex -interaction batchmode HajozAjbuben.tex
	rm *aux *log

kyrillisch:
	pdflatex -interaction batchmode cyrillic.tex
	rm *aux *log

#while true; do make &  myPID=$! ; inotifywait -e modify HajozAjbuben.tex ; kill $myPID; killall pdflatex; done