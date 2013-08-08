#!/bin/bash

for t in $(ls -1 tests/*.py | grep -v '^tests/_'); do
    ./$t
done
