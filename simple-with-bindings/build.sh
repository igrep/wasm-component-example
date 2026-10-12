#!/bin/bash

set -eux

cd "$(dirname "$0")"

uv run componentize-py -d example.wit -w example bindings bindings
uv run componentize-py -d example.wit -w example componentize python -o python.wasm
pnpm exec jco transpile python.wasm -o out-python

# node index.js
