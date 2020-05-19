#!/bin/bash
find ./ -name "*rwf" -delete
find ./ -name "Gau*" -delete
find ./ -name "*.chk" -exec /work/lopez/g16/formchk {} \;
find ./ -name "*.chk" -delete
