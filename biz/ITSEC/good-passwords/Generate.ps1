

cd $PSScriptRoot

#D:\opt\ffmpeg.exe -i images/%03d.png .\images\animated.gif

#sample text to docx
#--lua-filter ..\..\..\..\tec\Pandoc\include-files.lua
pandoc --lua-filter ..\..\..\..\tec\Pandoc\include-files.lua -s  `
    -o .\article.docx `
    .\metadata.txt `
    .\article.md `
    --reference-doc=..\..\..\marketing\templates\pandoc-WBI-datafile.docx


# sample slides to pptx, reveal.js.
pandoc --lua-filter ..\..\..\..\tec\Pandoc\include-files.lua --slide-level 2 `
    -o .\slides.pptx `
    .\metadata.txt `
    .\slides.md `
    --reference-doc=..\..\..\marketing\templates\pandoc-WBI-datafile.pptx

pandoc --lua-filter ..\..\..\..\tec\Pandoc\include-files.lua -s -t revealjs -V theme=solarized --slide-level 2 `
    -o .\slides.html `
    .\metadata.txt `
    .\slides.md `

