#! /usr/bin/env python3
# Copyright (C) 2023 SanCloud Ltd
# SPDX-License-Identifier: Apache-2.0

import argparse
import shutil
import subprocess
import sys

# We don't want to implement a dependency resolver for something as simple as
# this, so the list of images here has just been manually sorted into an order
# which ensures base images come before dependent images. If we're given
# multiple images to build, we build them in the order in which they appear in
# this list.
IMAGES = [
    "dev23-base",
    "dev23-c",
    "dev23-yocto",
    "iot-build",
    "iot-arm-build",
    "poky-build",
    "arago-build",
]


def msg(m):
    print(m, flush=True)


def select_container_engine():
    podman_cmd = shutil.which("podman")
    if podman_cmd:
        return podman_cmd

    docker_cmd = shutil.which("docker")
    if docker_cmd:
        return docker_cmd

    msg("Failed to find podman or docker! Cannot continue.", file=sys.stderr)


ENGINE_CMD = select_container_engine()


def run(cmd, **kwargs):
    return subprocess.run(cmd, shell=True, check=True, **kwargs)


def build_image(img):
    msg(f">>> Building {img}")
    run(f"{ENGINE_CMD} build -t {img} -f Containerfile .", cwd=img)


def pull_deps(img_list):
    # This is a bit manual for now
    msg(">>> Pulling dependencies")
    if "dev23-base" in img_list:
        run(f"{ENGINE_CMD} pull docker.io/library/ubuntu:22.04")
    if "dev23-yocto" in img_list:
        run(f"{ENGINE_CMD} pull docker.io/crops/poky:ubuntu-22.04")


def build_list(img_list):
    # Build in dependency order, not in the order in which the images are given
    for img in IMAGES:
        if img in img_list:
            build_image(img)


def tag_img(img, repo, tag):
    msg(f">>> Tagging {img} as {repo}/{img}:{tag}")
    run(f"{ENGINE_CMD} tag {img} {repo}/{img}:{tag}")


def push_img(img, repo, tag):
    msg(f">>> Pushing {repo}/{img}:{tag}")
    run(f"{ENGINE_CMD} push {repo}/{img}:{tag}")


def deploy_list(img_list, repo_list, tag):
    for img in img_list:
        for repo in repo_list:
            tag_img(img, repo, tag)
            push_img(img, repo, tag)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        "--repository",
        dest="repositories",
        action="append",
        help="Repository to push images to",
    )
    parser.add_argument(
        "-t", "--tag", default="latest", help="Image tag, defaults to 'latest'"
    )
    parser.add_argument(
        "-d",
        "--deploy",
        action="store_true",
        help="Deploy images to the selected repositories",
    )
    parser.add_argument("-a", "--all", action="store_true", help="Build all images")
    parser.add_argument("images", nargs="*", help="List of images to build")

    args = parser.parse_args()
    if not args.repositories:
        args.repositories = ["quay.io/sancloudltd"]

    if args.all:
        args.images = IMAGES

    if not args.images:
        msg("Nothing to do.")
        sys.exit(0)

    return args


def main():
    args = parse_args()
    build_list(args.images)
    if args.deploy:
        deploy_list(args.images, args.repositories, args.tag)


if __name__ == "__main__":
    main()
