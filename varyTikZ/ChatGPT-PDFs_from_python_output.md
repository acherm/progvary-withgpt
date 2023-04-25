# PDFs from python output.

#### You:
I'd like to call N times (eg N=10) python crazycat.py > out.tex; pdflatex out.tex; xdg-open out.pdf but instead of calling it out.tex (and thus out.pdf) I'd like to name it crazycat_i.tex (crazycat_i.pdf), i being the number of iteration... and I'd like to store all PDFs in a folder called crazycats. Can you write a Bash script?

#### ChatGPT:
Sure, here's a bash script that should do what you're asking for:

```
#!/bin/bash

# Set the number of iterations
N=10

# Create the directory to store the PDFs
mkdir crazycats

# Loop over the number of iterations
for (( i=1; i<=$N; i++ ))
do
    # Generate the filename for this iteration
    filename="crazycat_${i}"

    # Generate the full paths for the tex and pdf files
    tex_file="${filename}.tex"
    pdf_file="crazycats/${filename}.pdf"

    # Call the Python script to generate the tex file
    python crazycat.py > $tex_file

    # Generate the PDF from the tex file
    pdflatex $tex_file

    # Move the PDF to the crazycats directory
    mv "${filename}.pdf" $pdf_file

    # Open the PDF file with the default viewer
    xdg-open $pdf_file
done
```

Here's how the script works:

- Set the number of iterations to 10 (or whatever value you choose)
- Create a directory called `crazycats` to store the PDFs
- Loop over the number of iterations, from 1 to N
- Generate a filename for this iteration, using the format `crazycat_i`
- Generate the full paths for the tex and pdf files, using the filenames
- Call the Python script to generate the tex file, and save it with the appropriate filename
- Generate the PDF from the tex file, using pdflatex
- Move the PDF to the `crazycats` directory, using the appropriate filename
- Open the PDF file with the default viewer, using xdg-open

Make sure to save this script in a file with a `.sh` extension (e.g. `crazycat_script.sh`), and then make it executable with the command `chmod +x crazycat_script.sh`. Finally, you can run the script with the command `./crazycat_script.sh`.


#### You:
now I have 10 PDFs in my folder... I'd like to assemble the 10 PDFs into one... how can I?

#### ChatGPT:
You can use the `pdfunite` command to merge multiple PDF files into a single PDF file. Here's an updated version of the script that adds a line to merge the 10 PDFs into a single PDF file:

```
#!/bin/bash

# Set the number of iterations
N=10

# Create the directory to store the PDFs
mkdir crazycats

# Loop over the number of iterations
for (( i=1; i<=$N; i++ ))
do
    # Generate the filename for this iteration
    filename="crazycat_${i}"

    # Generate the full paths for the tex and pdf files
    tex_file="${filename}.tex"
    pdf_file="crazycats/${filename}.pdf"

    # Call the Python script to generate the tex file
    python crazycat.py > $tex_file

    # Generate the PDF from the tex file
    pdflatex $tex_file

    # Move the PDF to the crazycats directory
    mv "${filename}.pdf" $pdf_file

    # Open the PDF file with the default viewer
    xdg-open $pdf_file
done

# Merge the PDF files into a single PDF file
pdfunite crazycats/*.pdf crazycats/all_crazycats.pdf
```

After the loop that generates the 10 PDF files, this version of the script adds a line that uses the `pdfunite` command to merge all the PDF files in the `crazycats` directory into a single PDF file called `all_crazycats.pdf`. The merged PDF file will also be saved in the `crazycats` directory.


#### You:
can you adapt the script and convert PDF into PNG... and then assemble all PNG in a grid of images, resulting in a final PDF called gallery_crazycats.pdf ?

#### ChatGPT:
Sure! Here's an updated version of the script that adds the conversion of PDF files to PNG images using `pdftoppm` and the assembly of the PNG images into a grid using `montage`, both from the ImageMagick package. The resulting grid of images is then converted back into a PDF file using `convert`:

```
#!/bin/bash

# Set the number of iterations
N=10

# Create the directory to store the PDFs and PNGs
mkdir crazycats

# Loop over the number of iterations
for (( i=1; i<=$N; i++ ))
do
    # Generate the filename for this iteration
    filename="crazycat_${i}"

    # Generate the full paths for the tex, pdf, and png files
    tex_file="${filename}.tex"
    pdf_file="crazycats/${filename}.pdf"
    png_file="crazycats/${filename}.png"

    # Call the Python script to generate the tex file
    python crazycat.py > $tex_file

    # Generate the PDF from the tex file
    pdflatex $tex_file

    # Convert the PDF to a PNG image
    pdftoppm -png $pdf_file $png_file

    # Open the PNG file with the default viewer
    xdg-open $png_file
done

# Assemble the PNG images into a grid
montage -mode concatenate -tile 5x2 crazycats/*.png crazycats/grid.png

# Convert the grid of PNG images back into a PDF file
convert crazycats/grid.png crazycats/gallery_crazycats.pdf

# Open the final PDF file with the default viewer
xdg-open crazycats/gallery_crazycats.pdf
```

After the loop that generates the 10 PNG files, this version of the script adds two lines. The first line uses the `montage` command to assemble the PNG files into a grid with 5 columns and 2 rows. The resulting grid of images is saved as `grid.png` in the `crazycats` directory. The second line uses the `convert` command to convert the grid of PNG images back into a PDF file called `gallery_crazycats.pdf`, which is also saved in the `crazycats` directory. Finally, the script opens the final PDF file with the default viewer.
