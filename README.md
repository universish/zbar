QR CODE SCREENSHOT IMG FILE (.png) TO TOTP SECRET CODE CONVERTER - QR CODE DECODER WITH zbarimg.exe
====================

The Python script is an easy way to learn the TOTP secret code using zbarimg.exe.

It is used to decoder the 2fa QR Code generated when generating the 2factor code for 2-step verification. QRCode is scanned and TOTP secret code is extracted from it.

The 2fa QR Code is is decoded and converting into TOTP Secret code.

Some websites do not show the code when generating the 2fa code. For example on patika.dev website. QR code is given only for scanning with authenticator applications. In Windows, for example, applications like ente-auth cannot scan QR code. TOTP secret code is needed.

There are QR code decoder tools on the internet, but you cannot trust them. You might lose your important code to hackers.

I have tried open source QR code scanner apps to prevent this, they don't work. They scan QR codes that lead to websites. They cannot decode such special QR codes.

So I used zbar.

But it is troublesome to use. Because there is no GUI for zbarimg.

So I wrote a python script to make it easier to use.

	totp_secret_extractor.py

I also created a bat file to easily run the python script.

	run.bat

-------------------------------------------------

Steps:

Meet all requirements. Install Python 3.6+ and Zbar bar code reader. Install the required Python libraries (instructions below)

Take a screenshot of the 2fa two-step verification QR code. If possible in .png format.

run.bat file is double clicked and allowed to run.

run.bat file runs totp_secret_extractor.py in powershell.

python.exe runs. 

File Explorer opens. You are prompted to select the img file.

If you select the QR Code screenshot file, runs zbarimg.exe to scan the 2fa QR code!

zbarimg.exe converts the img file to totp save code.

separates the TOTP secret code after "secret=". Shows it on the Powershell screen.

If you add this code to your authenticator application and save it, it will show you your 6 digit TOTP code at certain time intervals.

Then you are asked if you want to save the TOTP secret code as txt.

Then you are asked if you want to close the window.

------------------------------------------------------

First of all, download the Zbar bar code reader app:

https://sourceforge.net/projects/zbar/

Install. The installation location should be the "C:\Program Files (x86)" directory.

zbarimg.exe location:

	"C:\Program Files (x86)\ZBar\bin\zbarimg.exe"

 must be.

---------------------------------------------------------

Requirements:

 Python 3.6+
 
	pip install -r requirements.txt

 totp_secret_extractor.py additionally needs Thinker to run. If you don't have Thinker installed (it is usually installed with python):

 	winget install Python.Python.3 --override "/InstallAllUsers=1 /AddToPath=1 /Include_tkinter=1"


-------------------------------------------  
  OR



The use of zbarimg.exe:

To convert a QR code screen image to TOTP, use the following code (for powershell):

	"C:\Program Files (x86)\ZBar\bin\zbarimg.exe" -q --raw "<path_to_file>\qr_code.png"



-------------------------------------------------
-------------------------------------------------

ZBAR BAR CODE READER
====================

ZBar Bar Code Reader is an open source software suite for reading bar
codes from various sources, such as video streams, image files and raw
intensity sensors. It supports EAN-13/UPC-A, UPC-E, EAN-8, Code 128,
Code 93, Code 39, Codabar, Interleaved 2 of 5, QR Code and SQ Code.

Included with the library are basic applications for decoding captured bar
code images and using a video device (e.g. webcam) as a bar code scanner.
For application developers, language bindings are included for C, C++,
Python 2 and Perl as well as GUI widgets for Qt, GTK and PyGTK 2.0.

Zbar also supports sending the scanned codes via dbus, allowing its
integration with other applications.

Check the ZBar home page for the latest release, mailing lists, etc.:

- <https://github.com/mchehab/zbar>

Tarballs with ZBar can be obtained from:

- <https://linuxtv.org/downloads/zbar/>

Since ZBar version 0.23.90, binaries auto-generated from Github's
Actions workflows are auto-generated for each release:

- <https://linuxtv.org/downloads/zbar/binaries/>

They contain binaries for:

- Ubuntu SID, generated via pbuilder;
- Mac OS;
- Windows, for 4 different configurations:
  - 32 bits/64 bits;
  - Video for Windows (VfW) or DirectShow (DShow).

License information can be found in `COPYING`.

You may find some outdated documentation at the original ZBar's
site at Sourceforge, but please notice that the content there is not
updated for ages:
	http://zbar.sourceforge.net/



BUILDING
========

See `INSTALL.md` for generic configuration and build instructions.

Please notice that at least autotools related packages and a
C compiler are needed, in order to generate the configure script.

So, on Debian, at least those packages are needed:
	autoconf autopoint pkg-config libtool gcc make

If you have installed all needed dependencies, all you need to do is to run:

```
autoreconf -vfi
./configure
make
```


* NOTES


  1) Currently, we maintain a Continuous Integration build test at
     TravisCI:

        <https://travis-ci.org/github/mchehab/zbar/>

     Due to that, there are scripts meant to test ZBar build on
     Linux, Windows and MacOS, that could be helpful. Please see
     the `.travis.yml` file, and the corresponding scripts under `travis/`.

  2) On version 0.23, since the support for gtk3 and python3 are new,
     the default is to use gtk2 and python2.

     If you want to use gtk3 and python3, you should have the development
     packages for them, and run:
```
autoreconf -vfi
./configure --with-gtk=auto --with-python=auto
make
```

  This will make the building system to seek for the latest versions
  for gtk and python.

The scanner/decoder library itself only requires a few standard
library functions which should be available almost anywhere.

The zbarcam program uses the video4linux API (v4l1 or v4l2) to access
the video device.  This interface is part of the linux kernel, a 3.16
kernel or upper is recommended for full support.  More information is
available at:

- <http://www.linuxtv.org/wiki/>

`pkg-config` is used to locate installed libraries.  You should have
installed `pkg-config` if you need any of the remaining components.
pkg-config may be obtained from:

- <http://pkg-config.freedesktop.org/>

The `zbarimg` program uses `ImageMagick` to read image files in many
different formats.  You will need at least `ImageMagick` version 6.2.6
if you want to scan image files. You may also use `GraphicsMagick`
package instead.

`ImageMagick` may be obtained from:

- <http://www.imagemagick.org/>

Qt Widget
---------

The Qt widget requires Qt4 or Qt5. You will need Qt if you would like to
use or develop a Qt GUI application with an integrated bar code
scanning widget. Qt4 may be obtained from:

- <https://www.qt.io/>

Gtk Widget
----------

The GTK+ widget requires GTK+-2.x or GTK+3.x.  You will need GTK+ if you
would like to use or develop a GTK+ GUI application with an integrated bar
code scanning widget.  GTK+ may be obtained from:

- <http://www.gtk.org/>

Python widgets
--------------

**Python 2 legacy Gtk widget**

The PyGTK 2.0/pygobject 2.0 wrapper for the GTK+ 2.x widget requires Python 2,
PyGTK. You will need to enable both pygtk2 and gtk2 if you would like to use
or develop a Python 2  GUI application with an integrated bar code scanning
widget.  PyGTK may be obtained from:

- <http://www.pygtk.org/>

**Python 2 or 3 GIR Gtk widget**

The GObject Introspection (GIR) wrapper for GTK+ widget is compatible with
PyGObject, with works with either Python version 2 or 3. You will need to
enable both Gtk and Python in order to use or develop a Python application
with an integrated bar code scanning and webcam support. In order to build
it, you need the required dependencies for GIR development. The actual
package depends on the distribution. On Fedora, it is `pygobject3-devel`.
On Debian/Ubuntu, it is `libgirepository1.0-dev` and `gir1.2-gtk-3.0`.
While GIR builds with Gtk2, It is strongly recommended to use GTK+
version 3.x, as there are known issues with version 2.x and GIR, with
will likely make it to fail. A test script can be built and run with:
`make check-gi`. Instructions about how to use are GIR on Python are
available at:

- <https://pygobject.readthedocs.io/en/latest/>

**Python bindings**

The Python bindings require Python 2 or 3 and provide only non-GUI functions.
You will need Python and PIL or Pillow if you would like to scan images or
video directly using Python. Python is available from:

- <http://python.org/>

Perl Widget
-----------

The Perl bindings require Perl (version 5).  You will need Perl if you
would like to scan images or video directly using Perl.  Perl is
available from:

- <http://www.perl.org/>

If required libraries are not available you may disable building for
the corresponding component using configure (see configure --help).

The Perl bindings must be built separately after installing the
library.  see:

- `perl/README`

Java Widget
-----------

The Java ZBar widget uses Java Native Interface (JNI), meaning that the
widget will contain machine-dependent code. It works with Java version
7 and above.  Java open JDK is available from:

- <https://openjdk.java.net/>

RUNNING
=======

`make install` will install the library and application programs.  Run
`zbarcam-qt` or `zbarcam` to start the video scanner. Use `zbarimg <file>`
to decode a saved image file.

Check the manual to find specific options for each program.

DBUS TESTING
============

In order to test if dbus is working, you could use:

	$ dbus-monitor --system interface=org.linuxtv.Zbar1.Code

or build the test programs with:

	$ make test_progs

And run:
	$ ./test/test_dbus

With that, running this command on a separate shell:

	$ ./zbarimg/zbarimg examples/code-128.png
	CODE-128:https://github.com/mchehab/zbar
	scanned 1 barcode symbols from 1 images in 0.01 seconds

Will produce this output at test_dbus shell window:

	Waiting for Zbar events
	Type = CODE-128
	Value = https://github.com/mchehab/zbar

REPORTING BUGS
==============

Bugs can be reported on the project page:

- <https://github.com/mchehab/zbar>

Please include the ZBar version number and a detailed description of
the problem.  You'll probably have better luck if you're also familiar
with the concepts from:

- <http://www.catb.org/~esr/faqs/smart-questions.html>
