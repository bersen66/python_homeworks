#!/bin/sh

docker build -t build_tex . 
docker run -v "$(pwd)/artifacts:/artifacts" build_tex

docker build -f "$(pwd)/ConverToPdf"  -t gen_pdf .
docker run -v "$(pwd)/artifacts/:/artifacts/" gen_pdf 

