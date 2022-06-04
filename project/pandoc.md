# Install pandoc from source

releases are at https://github.com/jgm/pandoc/releases

```
sudo apt purge pandoc
export PANDOC_VERSION=2.18
wget https://github.com/jgm/pandoc/releases/download/$PANDOC_VERSION/pandoc-PANDOC_VERSION-1-amd64.deb
sudo dpkg -i pandoc-$PANDOC_VERSION-1-amd64.deb
```
