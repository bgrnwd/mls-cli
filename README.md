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
      - [Regular season stats](#regular-season-stats)
      - [Playoff stats](#playoff-stats)
    - [Standings](#standings)
      - [Supporter's Shields](#supporters-shields)
      - [Conference](#conference)
    - [Transactions](#transactions)
    - [Team](#team)
    - [League](#league)
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

#### Regular season stats

```sh
mls p --regular "Andre Blake"
```

#### Playoff stats

```sh
mls p --playoffs "Ilsinho"
```

### Standings

#### Supporter's Shields

```sh
mls s
```

#### Conference

```sh
mls s east

mls s west
```

### Transactions

### Team

```sh
mls t --team "Philadelphia Union"
```

### League

```sh
mls t --year 2019
```

## Contributing

Feel free to [open an issue](https://github.com/bgrnwd/mls-cli/issues/new) or submit a pull request.

## License

[MIT](./LICENSE) © Brian Greenwood
