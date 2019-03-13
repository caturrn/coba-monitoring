# coba-monitoring

sudo apt-get update

sudo apt-get install build-essential fakeroot dpkg-dev

sudo apt-get build-dep git

mkdir ~/git-openssl

cd ~/git-openssl

apt-get source git

dpkg-source -x git_1.7.9.5-1.dsc

cd git-1.7.9.5

(Remember to replace 1.7.9.5 with the actual version of git in your system.)

Then, edit debian/control file (run the command: gksu gedit debian/control) and replace all instances of libcurl4-gnutls-dev with libcurl4-openssl-dev.

Then build the package (if it's failing on test, you can remove the line TEST=test from the file debian/rules):

sudo apt-get install libcurl4-openssl-dev

sudo dpkg-buildpackage -rfakeroot -b

Install new package:

i386: sudo dpkg -i ../git_1.7.9.5-1_i386.deb

x86_64: sudo dpkg -i ../git_1.7.9.5-1_amd64.deb
