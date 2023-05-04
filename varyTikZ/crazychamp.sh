#!/bin/bash

# Set the number of iterations
N=20

# Create the directory to store the PDFs and PNGs
rm -rf crazychamps
mkdir crazychamps

# Loop over the number of iterations
for (( i=1; i<=$N; i++ ))
do
    # Generate the filename for this iteration
    filename="crazychamp_${i}"

    # Generate the full paths for the tex, pdf, and png files
    tex_file="${filename}.tex"
    pdf_file="crazychamps/${filename}.pdf"
    png_file="crazychamps/${filename}.png"

    # Call the Python script to generate the tex file
    python crazychamp.py > $tex_file

    # Generate the PDF from the tex file
    pdflatex $tex_file

    # Move the PDF to the crazychamps directory
    mv "${filename}.pdf" $pdf_file

    # Convert the PDF to a PNG image
    pdftoppm -png $pdf_file $png_file

    # Open the PNG file with the default viewer
    # xdg-open $png_file
done

# Assemble the PNG images into a grid
montage -mode concatenate -tile 5x4 crazychamps/*.png crazychamps/grid.png

# Convert the grid of PNG images back into a PDF file
convert crazychamps/grid.png crazychamps/gallery_crazychamps.pdf

# Open the final PDF file with the default viewer
xdg-open crazychamps/gallery_crazychamps.pdf
