<!--
Copyright (C) 2021-2022 SanCloud Ltd
SPDX-License-Identifier: CC-BY-4.0
-->

# SanCloud Container Images

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/SanCloudLtd/containers/dev.svg)](https://results.pre-commit.ci/latest/github/SanCloudLtd/containers/dev)

This repository contains source files
for building container images used by SanCloud.

These images are made available
in the hope that they are useful to others.

## Available images

The container images defined in this repository
are pushed to the [Quay.io](https://quay.io/) Container Registry
and can be
[browsed online](https://quay.io/organization/sancloudltd).
They can be used with either [Docker/Moby](https://mobyproject.org/)
or [Podman](https://podman.io/).
The example commands below use `docker`
but substituting for `podman` should give equivalent results.

### iot-build

This image is intended to be used
for native development of IoT solutions.
It is based on Ubuntu 20.04
with common build tools
and libraries for MQTT communication.

```
docker pull quay.io/sancloudltd/iot-build
```

### iot-arm-build

This image is intended to be used
for cross-compilation of IoT solutions
intended to run on the SanCloud BBE.
It is based on the `iot-build` image described above
with the addition of the armv7-eabihf glibc toolchain
from <https://toolchains.bootlin.com/>.

```
docker pull quay.io/sancloudltd/iot-arm-build
```

### poky-build

This image is intended to be used
to build Poky distro images using Yocto Project
for the Sancloud BBE.
It is based on the [CROPS](https://github.com/crops/)
Ubuntu 20.04 images with the addition of pip
and with SSH configured to trust new keys on first use (TOFU).

```
docker pull quay.io/sancloudltd/poky-build
```

### arago-build

This image is intended to be used
to build Arago distro images using Yocto Project
for the SanCloud BBE.
It is based on the `poky-build` image described above
with the addition of the ARM toolchain
required by the Arago distro.

```
docker pull quay.io/sancloudltd/arago-build
```

## Contributing

[Pull requests](https://github.com/SanCloudLtd/containers/pulls)
and [issue reports](https://github.com/SanCloudLtd/containers/issues)
are welcome for this repository.

For further support enquiries
please contact us via email to <opensource@sancloud.com>.

## License

Copyright (c) 2021-2022 SanCloud Ltd.

* Code files are distributed under the
  [Apache 2.0 License](https://tldrlegal.com/license/apache-license-2.0-(apache-2.0)).

* Documentation files are distributed under the
  [CC BY 4.0 License](https://tldrlegal.com/license/creative-commons-attribution-4.0-international-(cc-by-4)).

* Trivial data files are distributed under the
  [CC0 1.0 License](https://tldrlegal.com/license/creative-commons-cc0-1.0-universal).
