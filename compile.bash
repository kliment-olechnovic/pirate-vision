#!/bin/bash

pandoc ./README.md \
  -f markdown -t html -s \
  --metadata title='Pirate Vision' \
  -M document-css=false \
  --wrap=none --toc --toc-depth=3 --section-divs \
  --css=styles.css \
  -o ./index.html
