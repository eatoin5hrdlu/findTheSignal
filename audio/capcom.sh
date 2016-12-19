#!/bin/bash

while ((1)); do aplay -D$1 $2; sleep 1; done

