#!/bin/bash

set -eux

cd "$(dirname "$0")"

rm -rf out-python out-processor __pycache__ python.wasm processor.wasm
