# Generating the book

The bookmanager can be installed natively, but it is easier 
to just use docker. So please make sure docker is installed on your system.
Docker must be running, as well. If you have
docker desktop, simply start the program and
have it running in the background.


A number of different repositories must
be cloned to your ~/cm folder before
generating the book. These are the required
repositories:

```bash
mkdir ~/cm
cd ~/cm
git clone https://github.com/cloudmesh-community/pub
git clone https://github.com/cloudmesh-community/book
git clone https://github.com/cloudmesh/cloudmesh-nlp
git clone https://github.com/cybertraining-dsc/su22-reu-385
git clone https://github.com/cyberaide/bookmanager
```



Navigate to the bookmanager directory and run
`make image`.

```bash
git clone ... TBD
cd ~/cm/bookmanager
make image
```

To generate the book, stand in reu2022/book
and compile it

```bash
cd ~/cm/reu2022
make book
```
