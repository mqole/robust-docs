---
sidebar_position: 1
---
# Introduction

:::warning[Warning!]
Construction graphs can be a very complex topic! It can be a little easy to lose track of what you are doing when working on one so be sure to take it slowly!

If you find yourself frustrated then step away, and try again later.
:::

## What's a Construction Graph?

Construction Graphs are the primary way Space Station 14 handles all item & structure crafting. 

The general structure of a graph can look something like

```
> Graph
    > Node
        > Steps
            > To: Node 2
    
    > Node 2
        > Result
```

This makes them look pretty simple, and in theory they are. But they have a lot of moving parts which are overwhelming at first.

To help make this more digestible, we'll be breaking this tutorial into parts:

* [Stage 1: A Simple One Step Construction](stage-1-a-simple-one-step-construction.md)
* [Stage 2: Multi Step Construction](stage-2-multi-step-construction.md)
* [Stage 3: Deconstruction](stage-3-deconstruction.md)
* [Stage 4: Custom Materials](stage-4-custom-materials.md)
* [Bonus Stage: YAML Anchors & Graphs](bonus-stage-anchors.md)