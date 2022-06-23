#! /bin/bash
# Copyright (C) 2021 SanCloud Ltd
# SPDX-License-Identifier: Apache-2.0

set -eo pipefail

if [[ -z "$NOPULL" ]]; then
    if command -v podman &> /dev/null; then
        podman pull docker.io/crops/yocto:ubuntu-20.04-base
    else
        docker pull docker.io/crops/yocto:ubuntu-20.04-base
    fi
fi
