#!/bin/bash

pushd /home/fcbr/repos/syntaxnet/models/syntaxnet > /dev/null

/home/fcbr/repos/syntaxnet/models/syntaxnet/syntaxnet/models/parsey_universal/parse.sh /home/fcbr/repos/syntaxnet/models/syntaxnet/English

popd > /dev/null
