

mkdir -p ./tmp
rm tmp/KeePass-screenshots_*png
for f in ./KeePass-screenshots_*png; do
  convert $f -gravity center -background black -extent 852x480 ./tmp/$f
done

convert -delay 100 tmp/KeePass-screenshots_0*png -loop 0 KeePassCreateDatabaseWindows.gif
rm tmp/KeePass-screenshots_*png

#rmdir tmp

#set delay BEFORE
convert -delay 256 KeePass-downloadsources_00*png  -loop 0 -verbose KeePass-downloadsources.gif