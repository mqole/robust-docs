# Website

Unofficial static documentation site for SS14. See also [official documentation](https://github.com/space-wizards/docs).

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

All content on this site is released under the Mozilla Public License v2.0.

## Proposed site structure (WIP)

If you're a contributor who wants to 'claim' writing one of these pages, just add your name beside it or open an issue.

```
docs
├── about these docs
│   └── contributing to docs
├── getting started
│   ├── setup (use howdoicode index?)
│   │   ├── how do i git?
│   │   └── how do i localhost? (link to server hosting for more info)
│   ├── codebase info
│   │   ├── codebase organization (should give a basic rundown of file extensions)
│   │   │   ├── Robust Station Image
│   │   │   └── file attribution
│   │   └── code conventions
│   ├── troubleshooting & debugging
│   │   └── debugging tools (include how to search for in game text)
│   └── contributing
│       ├── pull request guidelines for WizDen (include info on engine pr)
│       ├── big feature proposals
│       │   └── how to write a design doc
│       ├── release process
│       └── contributing translations
├── robust toolbox (WIP- need to go through entire robust folder)
│   ├── testing against launcher
│   └── updating CEF
├── ss14
│   ├── how do i...?
│   │   ├── how to yaml
│   │   ├── how to fluent
│   │   ├── how to map
│   │   │   ├── stations and non-stations
│   │   │   └── common mapping mistakes
│   │   └── bikehorn guide
│   ├── common systems
│   │   ├── networking
│   │   │   └── prediction
│   │   ├── sprites
│   │   │   ├── displacement maps
│   │   │   └── making walls with the aseprite template
│   │   ├── ui
│   │   │   └── ui toolbox & common controls
│   │   ├── entitytables
│   │   └── triggersystem
│   └── specifics
│       ├── the guidebook
│       ├── solutions & solution containers
│       │   ├── reagents & reactions
│       │   └── metabolism
│       ├── the body (literally just a placeholder page.)
│       ├── construction
│       │   └── how to write a construction graph
│       ├── destructible
│       ├── device networking
│       ├── nodes (is this power?)
│       └── NPCs (LOL)
└── server hosting & forking
    ├── hosting tutorial (probably split the og file)
    │   ├── port forwarding
    │   ├── config file
    │   └── integrations
    │       ├── replays
    │       ├── discord
    │       ├── robust cdn
    │       ├── high bandwidth
    │       ├── admin
    │       ├── changelog
    │       └── watchdog
    ├── server debugging
    ├── oauth
    └── so you think you can fork
```

## Roadmap

- [X] Finish porting over all of the files on Robust Book (minus the meetings)
- [ ] Reorganize files (BIG STEP!!! WILL TAKE A WHILE!!) & Rewrite whatever needs rewriting
- [ ] Add community documentation where needed
- [ ] ???
- [ ] Profit

## To Fix

- MERMAID NOT WORKING!!!
- Searchbar not loading
- glossary underlining is messy (awaiting [issue](https://github.com/mcclowes/docusaurus-plugin-glossary/issues/129))
