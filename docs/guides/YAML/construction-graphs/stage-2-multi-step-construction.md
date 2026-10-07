---
sidebar_position: 3
---
# Stage 2: Multi Step Construction

So now that we've gotten basic crafting out of the way, let's move to the next subject. Construction.

For this we will be using our structure from [Your First Structure](../tutorials/your-first-structure.md) so if you haven't done that tutorial, you should!

First step, similarly to the last, is to make 2 new files.

`Resources/Prototypes/_OurFork/Recipes/Construction/mystructure.yml`

`Resources/Prototypes/_OurFork/Recipes/Construction/Graphs/mystructuregraph.yml`

:::info[Quick Tip!]
You'll notice we're using the **Construction** directory instead of **Crafting** this time. This is just for organisation purposes! Most forks will split their graphs in this way.
:::

For these files, repeat the steps from [Stage 1](stage-1-a-simple-one-step-construction.md) except for our [Structure](../tutorials/your-first-structure.md) until you have 3 YML's that look like these

`Structures/Tutorial/mystructure.yml`
```yaml
- type: entity
  name: my structure
  parent: BaseStructure
  id: TutorialStructure
  description: "My Tutorial Structure."
  components:
  - type: Sprite
    sprite: _OurFork/Structures/Tutorial/mystructure.rsi
    state: icon
    noRot: true
  - type: Anchorable
  - type: Transform
    anchored: true
    noRot: true
  - type: Pullable
  - type: Construction
    graph: MyStructGraph
    node: struct
```
`Graphs/mystructuregraph.yml`
```yaml
- type: constructionGraph
  id: MyStructGraph
  start: start
  graph:
    - node: start 
      edges:
        - to: struct
          steps:
            - material: Steel
              amount: 5
              doAfter: 4
        
    - node: struct
      entity: TutorialStructure
```
`Construction/mystructure.yml`
```yaml
- type: construction
  id: MyStructConstruct
  graph: MyStructGraph
  startNode: start
  targetNode: struct
  category: construction-category-misc
  objectType: Structure
```

You will likely notice that I swapped a couple of things around. Mainly naming the `end` node `struct` and swapping `WoodPlank` for `Steel`. These are just personal choices, whether you do them or not is up to you!

Now back in our `MyStructConstruct` YML we're going to be adding a few new things that can be utilised within structure constructions.

```yaml
- type: construction
  id: MyStructConstruct
  graph: MyStructGraph
  startNode: start
  targetNode: struct
  category: construction-category-misc
  objectType: Structure
  placementMode: SnapgridCenter
  canRotate: false
  canBuildInImpassable: false
  conditions:
  - !type:TileNotBlocked
```
* `placementMode` is the variable that handles how the construction ghost gets placed. Whether it's free placing or snaps to a tile.
* `canRotate` is the variable that controls whether you can rotate the contruction ghost.
* `canBuildInImpassable` is the variable that controls if you can build on tiles that block movement such as walls.
* `conditions` are the rules that need to be followed to construct the ghost. In this case, the tile must not have anything on it.

Now that we have these components in place, it's time for the real test of Construction Graphs. Keeping them readable.

Let's take another look at our construction graph.

```yaml
- type: constructionGraph
  id: MyStructGraph
  start: start
  graph:
    - node: start 
      edges:
        - to: struct
          steps:
            - material: Steel
              amount: 5
              doAfter: 4
        
    - node: struct
      entity: TutorialStructure
```

A big issue with construction graphs, and to some extent YML in general, is that it's hard to keep it all very readable. Some IDE's will have tools for this such as drawing lines so you can see what word is at what indentation, but it's not the best solution.

For this tutorial, **do not be surprised if you get tripped up by how big the graph gets!** One of the easiest ways to slip up making a construction graph is from missing an indent or something similar.

---

So what is our goal for Stage 2? Well what we aim to do is have a structure that takes 3 steps to complete:
1. Initial placing of a base
2. Screwing the structure
3. Adding the final materials

So how do we do this? If you've understood the tutorials so far then you've probably twigged it. `Node`. Each `Node` defines a step in the construction process to move between. Think of them a bit like stepping stones, you can move to or from a node by jumping between them.

So let's go ahead and define 2 more nodes in our graph. `screwed` and `addMat`. `screwed` will be the node for the screwing step and `addMat` will be the node for adding the final material before we finish. The order the nodes will go in will be

`start` > `screwed` > `addMat` > `struct`

So let's see how this looks in YML form;

```yaml
- type: constructionGraph
  id: MyStructGraph
  start: start
  graph:
    - node: start 
      edges:
        - to: screwed
          steps:
            - material: Steel
              amount: 5
              doAfter: 4
    
    - node: screwed
      edges:
        - to: addMat
          steps:
            - tool: Screwing
              doAfter: 2

    - node: addMat
      edges:
        - to: struct
          steps:
            - material: Steel
              amount: 2
              doafter: 2

    - node: struct
      entity: TutorialStructure
```

- `tool` defines what tool type will be used ont he construction.

:::info[Quick Tip!]
The available tool types you can use in a graph are:
* Screwing
* Prying
* Cutting
* Welding
* Anchoring
* Slicing
* Honking
:::

When laid out like this it actually looks pretty simple. If you were to open the game up now and test the graph, you would see it looks like this.

![image](https://hackmd.io/_uploads/BJnyVPWGMg.png)

You'll notice though if you go through the graph, the structure remains as a ghost until you finish construction, but why? Well it's because if you look at the `struct` node

```yaml
    - node: struct
      entity: TutorialStructure
```

We aren't actually defining an entity until we hit this node since of course, this is our finished entity. So what we are going to need is an entity to work as an "unfinished" version of the structure.

---

Head back to `mystructure.rsi` and add in a new sprite for your unfinished structure. Then within the `meta.json` add a new `state` that uses the same name as your unfinished sprite, in this case mine is called `unfinished`.

```jsonld
{
    "version": 1,
    "license": "CC-BY-SA-3.0",
    "copyright": "FancyPlanks from hackmd.io/@FancyPlanks",
    "size": {
        "x": 32,
        "y": 32
    },
    "states": [
        {
            "name": "icon"
        },
        {
            "name": "unfinished"
        }        
    ]
}

```

Then head back to `mystructure.yml` and make a new YML for your unfinished entity. We can make this new entity use our `TutorialStructure` as a [Parent](../introduction/yml-parenting.md) to save us a bit of work. You only need to define 2 components in the new entity, those being `Sprite` and `Construction`. You can copy them over from our `TutorialStructure` as there are only 2 things you need to change:

1. Change `state` in `Sprite` to be what you named the unfinished sprite in `meta.json`.
2. Change `node` in `Construction` to be `screwed`.

You should now have a YML that looks like this;

```yaml
- type: entity
  name: my structure
  parent: TutorialStructure
  id: UnfinishedTutorialStructure
  description: "My Tutorial Structure. But unfinished."
  components:
  - type: Sprite
    sprite: _OurFork/Structures/Tutorial/mystructure.rsi
    state: unfinished
    noRot: true
  - type: Construction
    graph: MyStructGraph
    node: screwed
```

Now all that needs to be done is for you to head back to `mystructuregraph.yml` and place one new line under `node: screwed`

* `entity: UnfinishedTutorialStructure`

When with this in your node it will now replace your ghost with the new entity when you begin construction! With all this done you should now have a construction graph that looks something like this;

```yaml
- type: constructionGraph
  id: MyStructGraph
  start: start
  graph:
    - node: start 
      edges:
        - to: screwed
          steps:
            - material: Steel
              amount: 5
              doAfter: 4
    
    - node: screwed
      entity: UnfinishedTutorialStructure
      edges:
        - to: addMat
          steps:
            - tool: Screwing
              doAfter: 2

    - node: addMat
      edges:
        - to: struct
          steps:
            - material: Steel
              amount: 2
              doafter: 2

    - node: struct
      entity: TutorialStructure
```

:::warning[Warning!]
The node you spawn your entity on must **always** match the node defined in that entities YML!

You should also avoid spawning an entity in the `start` node when it comes to construction graphs utilising a ghost in game! The ghost will always be the `start` node, meaning you cannot spawn your unfinished entity on it!
:::

Congratulations! You now have a multi step construction graph using a structure. This isn't the end of Construction Graphs though as there are still two more things to teach.