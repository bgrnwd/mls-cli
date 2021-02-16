# mls-cli

[![license](https://img.shields.io/github/license/bgrnwd/mls-cli.svg)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Check [Major League Soccer](https://www.mlssoccer.com/) standings, scores, and stats from your terminal. Inspired by [nba-go](https://github.com/homerchen19/nba-go)

## Table of Contents

- [mls-cli](#mls-cli)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Usage](#usage)
    - [Game](#game)
    - [Player](#player)
      - [Get regular season stats](#get-regular-season-stats)
      - [Get playoff stats](#get-playoff-stats)
    - [Standings](#standings)
  - [Contributing](#contributing)
  - [License](#license)

## Install

```sh
pip install mls-cli
```

## Usage

### Game

TODO

### Player

#### Get regular season stats

```bash
mls p "Andre Blake" -r
```

#### Get playoff stats

```bash
mls p "Ilsinho" -p
```

### Standings

```bash
mls s
```

Will return the supporters shield standings. If you want to see each conference individually, run

```bash
mls s east

mls s west
```

## Contributing

Feel free to [open an issue](https://github.com/bgrnwd/mls-cli/issues/new) or submit a pull request.

## License

[MIT](./LICENSE) © Brian Greenwood
