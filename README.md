# Openslide Ubuntu Focal Bug Report

Create data directory and download CMU-1.svs to this directory.

```
cd openslide-ubuntu-focal-bug-report
mkdir data
cd data
curl -fLO http://openslide.cs.cmu.edu/download/openslide-testdata/Aperio/CMU-1.svs
cd ..
```

Run experiments.

```bash
./run-experiments.sh
```
