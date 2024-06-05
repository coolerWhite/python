#!/bin/bash

mpass() {
    if [$1]; then
        length=$1
    else:
        length=12
    fi
    _hash=`python3 -c "
    import os,base64
    exec('print(base64.b64encode(os.urandom(64))[:${length}].decode(\'utf-8\'))')
    "`
    echo $_hash | xclip -secelction clipboard
    echo "new pass copy to the system"
}