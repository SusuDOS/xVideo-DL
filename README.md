# xvideos-dl

<div align="center">

[![Build status](https://github.com/SusuDOS/xvideos-dl/workflows/build/badge.svg?branch=master&event=push)](https://github.com/SusuDOS/xvideos-dl/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/xvideos-dl.svg)](https://pypi.org/project/xvideos-dl/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/SusuDOS/xvideos-dl/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/SusuDOS/xvideos-dl/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/SusuDOS/xvideos-dl/releases)
[![License](https://img.shields.io/github/license/SusuDOS/xvideos-dl)](https://github.com/SusuDOS/xvideos-dl/blob/master/LICENSE)

CLI to download videos from https://xvideos.com

</div>

<div align="center"><a href="https://github.com/SusuDOS/xvideos-dl/blob/master/README_CN.md">中文文档</a></div>

## Features

- [X] Download a single video (requires the URL of the video playback page)
- [X] Download all videos in the favorites (requires the URL of the favorite page)
- [X] Download all videos uploaded by the user (requires the URL of the user's homepage)
- [X] Download all videos published by the channel (requires the URL of the channel homepage)
- [X] Segmented high-speed download, breakpoint download, progress and status display
- [x] Download high quality videos, 1080p or higher
- [X] Support multi-threaded downloading

## Usage

⚠️**Requires:**

- `Python`: >= 3.6.1
- [`ffmpeg`](https://ffmpeg.org/download.html)
  - Ubuntu/Debian: `sudo apt install ffmpeg`
  - MacOS: `brew install ffmpeg`
  - Windows: refer this [issue](https://github.com/SusuDOS/xvideos-dl/issues/86)
- `Cookie`: When you run it for the first time, you will be prompted to enter the cookie, log in https://xvideos.com with your account, copy and paste a long string of cookie (there are many key-value pairs in the cookie, and `session_token=xxx` this pair must exist), then enjoy it.

Cookie is stored in *~/.xvideos/cookie* (or *C:\Users\USER\\.xvideos\cookie*).

- Install `xvideos-dl` and `yt-dlp`

```bash
# install ananconda
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
conda create -n downvideo python=3.8
conda activate downvideo
git clone https://github.com/yt-dlp/yt-dlp.git
cd yt-dlp && pip install .

# or
cd yt-dlp && python setup.py install --force

# install and update xVideo-DL
git clone https://github.com/SusuDOS/xVideo-DL.git
cd xVideo-DL && pip install .
```

- Get CLI help

```bash
xvideos-dl --help
```

- Download single / favorites / uploaded / published videos in one command:

```bash
xvideos-dl https://www.xvideos.com/video37177493/asian_webcam_2_camsex4u.life https://www.xvideos.com/favorite/71879935/_ https://www.xvideos.com/profiles/mypornstation https://www.xvideos.com/channels/av69tv  
```

![DEMO](DEMO1.JPG)
![DEMO](DEMO2.png)

<hr>

## For Contributors

### Initial

1. Fork and clone this repo:

```bash
git clone https://github.com/lonsty/xvideos-dl
```

2. If you don't have `Poetry` installed run:

```bash
make download-poetry
```

3. Initialize poetry and install `pre-commit` hooks:

```bash
make install
```

### Makefile usage

[`Makefile`](https://github.com/lonsty/xvideos-dl/blob/master/Makefile) contains many functions for fast assembling and convenient work.

<details>
<summary>1. Download Poetry</summary>
<p>

```bash
make download-poetry
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

```bash
make install
```

If you do not want to install pre-commit hooks, run the command with the NO_PRE_COMMIT flag:

```bash
make install NO_PRE_COMMIT=1
```

</p>
</details>

<details>
<summary>3. Check the security of your code</summary>
<p>

```bash
make check-safety
```

This command launches a `Poetry` and `Pip` integrity check as well as identifies security issues with `Safety` and `Bandit`. By default, the build will not crash if any of the items fail. But you can set `STRICT=1` for the entire build, or you can configure strictness for each item separately.

```bash
make check-safety STRICT=1
```

or only for `safety`:

```bash
make check-safety SAFETY_STRICT=1
```

multiple

```bash
make check-safety PIP_STRICT=1 SAFETY_STRICT=1
```

> List of flags for `check-safety` (can be set to `1` or `0`): `STRICT`, `POETRY_STRICT`, `PIP_STRICT`, `SAFETY_STRICT`, `BANDIT_STRICT`.

</p>
</details>

<details>
<summary>4. Check the codestyle</summary>
<p>

The command is similar to `check-safety` but to check the code style, obviously. It uses `Black`, `Darglint`, `Isort`, and `Mypy` inside.

```bash
make check-style
```

It may also contain the `STRICT` flag.

```bash
make check-style STRICT=1
```

> List of flags for `check-style` (can be set to `1` or `0`): `STRICT`, `BLACK_STRICT`, `DARGLINT_STRICT`, `ISORT_STRICT`, `MYPY_STRICT`.

</p>
</details>

<details>
<summary>5. Run all the codestyle formaters</summary>
<p>

Codestyle uses `pre-commit` hooks, so ensure you've run `make install` before.

```bash
make codestyle
```

</p>
</details>

<details>
<summary>6. Run tests</summary>
<p>

```bash
make test
```

</p>
</details>

<details>
<summary>7. Run all the linters</summary>
<p>

```bash
make lint
```

the same as:

```bash
make test && make check-safety && make check-style
```

> List of flags for `lint` (can be set to `1` or `0`): `STRICT`, `POETRY_STRICT`, `PIP_STRICT`, `SAFETY_STRICT`, `BANDIT_STRICT`, `BLACK_STRICT`, `DARGLINT_STRICT`, `ISORT_STRICT`, `MYPY_STRICT`.

</p>
</details>

<details>
<summary>8. Build docker</summary>
<p>

```bash
make docker
```

which is equivalent to:

```bash
make docker VERSION=latest
```

More information [here](https://github.com/SusuDOS/xvideos-dl/tree/master/docker).

</p>
</details>

<details>
<summary>9. Cleanup docker</summary>
<p>

```bash
make clean_docker
```

or to remove all build

```bash
make clean
```

