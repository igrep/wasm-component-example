#!/bin/bash

set -eux

cd "$(dirname "$0")"

uv run componentize-py -d example.wit -w example componentize python -o python.wasm
pnpm exec jco transpile python.wasm -o out-python

pnpm exec jco componentize processor.js --wit example.wit --world-name processor-world --disable all -o processor.wasm
pnpm exec jco transpile processor.wasm -o out-processor --map 'example:example/blobs=../out-python/python.js#blobs'

# Run this to reproduce `TypeError: Resource error: Not a valid "Blob" resource.`
# node processor-host.js
