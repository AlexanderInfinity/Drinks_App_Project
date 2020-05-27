#!/bin/zsh
set -eu
coverage run -m unittest
coverage report
open htmlcov/index.html