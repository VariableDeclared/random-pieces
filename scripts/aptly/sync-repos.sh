#!/bin/bash

for mirror in noble noble-updates noble-security noble-backports jammy jammy-updates jammy-security jammy-backports; do
    aptly mirror update $mirror
    aptly snapshot create "$mirror-$(date -I)" from mirror $mirror
done
