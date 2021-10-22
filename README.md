
# remarkavision

smarter OCR for remarkable templates


### Requirements

- tesseract
- pytesseract
- python3 + libraries


### Installing tesseract

You need to install the tesseract binary to use pytesseract.  Here is how I did it according to the instructions [here](https://tesseract-ocr.github.io/tessdoc/Compiling-%E2%80%93-GitInstallation.html)
`sudo apt-get install automake ca-certificates g++ git libtool libleptonica-dev make pkg-config libpango1.0-dev`

Get last full release available.  May eventually test 5.0 beta.
`git clone --depth 1  --branch 4.1.1 https://github.com/tesseract-ocr/tesseract.git`

and build (I suggest you split this into multiple commands in case it breaks you'll know what broke):
`cd tesseract && ./autogen.sh && ./configure && make && sudo make install && sudo ldconfig`

Download tesseract "traineddata" files:

`cd /usr/local/share/tessdata && sudo wget https://github.com/tesseract-ocr/tessdata/raw/main/eng.traineddata`

### Installing python dependencies

