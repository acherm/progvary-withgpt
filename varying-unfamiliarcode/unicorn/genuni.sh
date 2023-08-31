#!/bin/bash

# Part 1: Compile LaTeX files to PDFs
for i in {1..20}
do
    pdflatex "unicorn$i.tex"
done

# Convert PDFs to images using ImageMagick
for i in {1..20}
do
    convert -density 150 "unicorn$i.pdf" -quality 90 "unicorn$i.png"
done

# Part 2: Create a gallery
# This will create a gallery in a 5x4 format
montage unicorn{1..20}.png -geometry +0+0 -tile 5x4 gallery.pdf

# merge pdf
pdftk unicorn{1..20}.pdf cat output merged.pdf