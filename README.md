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
WORK_DIR=$(pwd)
IMAGE=openslide-bug-report

TAG=ubuntu-18.04-openslide-master
docker build -f Dockerfile.${TAG} -t ${IMAGE}:${TAG} .
docker run --rm -v ${WORK_DIR}/data:/files/data:ro -v ${WORK_DIR}/output:/files/output ${IMAGE}:${TAG} test.py --output-file-path=/files/output/${TAG}.jpeg

TAGS=(\
"ubuntu-18.04-openslide-master" \
"ubuntu-20.04-openslide-master" \
"alpine-openslide-master" \
"ubuntu-18.04-openslide-3.4.1" \
"ubuntu-20.04-openslide-3.4.1" \
"alpine-openslide-3.4.1" \
"ubuntu-18.04-openslide-repo" \
"ubuntu-20.04-openslide-repo" \
)
for TAG in ${TAGS[*]}; do
    docker build -f Dockerfile.${TAG} -t ${IMAGE}:${TAG} .
    docker run --rm -v ${WORK_DIR}/data:/files/data:ro -v ${WORK_DIR}/output:/files/output ${IMAGE}:${TAG} test.py --output-file-path=/files/output/${TAG}.jpeg
done
```