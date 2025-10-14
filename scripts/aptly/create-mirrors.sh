#!/bin/bash

ARCHIVE=http://gb.archive.ubuntu.com

for mirror in noble noble-updates noble-security noble-backports jammy jammy-updates jammy-security jammy-backports; do
    aptly mirror create -architectures=amd64 $mirror $ARCHIVE $mirror main multiverse restricted universe
done
