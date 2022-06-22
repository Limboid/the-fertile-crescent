# The Artificial Ecosystem

[![Discord](https://img.shields.io/discord/950148027715293220?label=discord)](https://discord.gg/tbaPRNknET)
[![GitHub](https://img.shields.io/github/license/Limboid/the-limboid-ecosystem)](https://github.com/Limboid/the-limboid-ecosystem/blob/main/LICENSE)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/Limboid)](https://github.com/sponsors/JacobFV)
[![Lines of code](https://img.shields.io/tokei/lines/github/Limboid/the-limboid-ecosystem)](https://github.com/Limboid/the-limboid-ecosystem)
[![GitHub Repo stars](https://img.shields.io/github/stars/Limboid/the-limboid-ecosystem?style=social)](https://github.com/Limboid/the-limboid-ecosystem)

*:construction: **This repository is under construction.** :construction: Expect a public release coming this Summer 2022.*

*Want to contribute? Check out the GitHub container repository [Limboid/the-artificial-ecosystem](https://github.com/Limboid/the-artificial-ecosystem) for this project.*

The Aritificial Ecosystem is a monorepo:
- that establishes a common ecosystem of tools and libraries for ML R&D
- which are used in the Computatrum, Limboid, I:blue_heart:U and other professional projects by Limboid LLC
- to promote the sustained evolution of artificial intelligence
- all permissively released under the MIT license.

## Roadmap


[ ] format all subrepo's
  [ ] change urls in banners
  [ ] define common README format
  [ ] give each repo a quick bulleted description
  [ ] give each repo an image or logo
  [ ] make a proposal paper and video for each repo
  [ ] add bib citation entry under each repo
  [ ] copy same MIT license to all repos
  [ ] add changelog and contributors to each repo
  [ ] copy .github settings across *most* repos (e.g.: no need for issues or features requests on container repo's)
  [ ] format engineering repos with docs in a single top-level folder instead of scattered everywhere
  [ ] write welcome message in discord
[ ] Publish these md docs in a simple static site. (why?)

## License

```
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## Contributing

We're glad you're here to contribute! We're looking for people who are passionate about AI and want to help us build the ecosystem. Please note:

- If you're just looking to work with a specific repository in the Artificial Ecosystem, go to that repo's README for instructions. 
- If you're looking to make changes to the Artificial Ecosystem itself, but not its submodules, you should be fine cloning like normal: 
  ```
  git clone https://github.com/Limboid/the-artificial-ecosystem
  ```
- If you plan on making changes to the Artificial Ecosystem, and those changes will involve working with its submodules, include the `--recurse-submodules` flag in your clone statement:
  ```
  git clone --recurse-submodules https://github.com/Limboid/the-artificial-ecosystem
  ```
  Remember to commit the individual submodules before commiting the central repo. And ensure they are all compatible before commiting!

  If git submodules are a new concept, don't let them scare you. You might find [chapter 7.11 in the Pro Git book](https://git-scm.com/book/en/v2/Git-Tools-Submodules) helpful.

- Please adhere to the [contributing guide](CONTRIBUTING.md) and [code of conduct](CODE_OF_CONDUCT.md) when contributing.

Thanks for contributing!