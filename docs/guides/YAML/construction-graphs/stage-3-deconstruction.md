---
sidebar_position: 4
---
# Stage 3: Deconstruction

Deconstruction is where Construction Graphs start to get a little bit messy. The way that construction graphs work is that all construction actions related to an entity remain within **one single graph.** What this means is that all construction, destruction and alternate construction paths are kept within a single graph. 

For this tutorial we're going to carry over our work from [Stage 2](stage-2-multi-step-construction.md).

So, what do we need to do to let the game know we can deconstruct an entity? Well funnily we actually only need to touch the graph this time. To jumping to our entity's YML this time.

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

Chances are you may be thinking of what you need to do already. If you can do steps forward, then it stands to reasont hat they can go backwards too, and you'd be correct. Though there's still some new things to achieve this.

First we are going to need a `to` within our `struct` node. In this case we're going to have the person use a crowbar to begin deconstruction.

```yaml
    - node: struct
      entity: TutorialStructure
      edges:
        - to: addMat
          steps:
            - tool: Prying
              doAfter: 2
```

And this is how it's going to look for the `addMat` node as well, but `screwed` is going to be a tad different. See, screwed will be the **final** step in the deconstruction. This means at this step we will need to have the materials we want the deconstruction to give spawn as well as deleting the entity. But how do we do that? Well we use `completed`.

```yaml
        - to: start
          completed:
            - !type:SpawnPrototype
              prototype: SheetSteel1
              amount: 8
            - !type:DeleteEntity {}
          steps:
            - tool: Welding
              doAfter: 4
```

* `completed` is the action that will be done when a nodes steps are finished. Any node can have a `completed` and they don't all have to delete the entity.
* `!type:SpawnPrototype` is what we use to spawn in new entities from construction.
* `!type:DeleteEntity` does what it says on the tin. It will delete the entity we are deconstructing.

:::info[Quick Tip!]
You've probably noticed that the steel we're dropping is different than what we put in. What we fed into the graph is a `material` but this time it's a `prototype`? Well that's because of how the game handles actual registered materials for things like construction or lathes. We'll be getting into this in Stage 4!

If you need a refresher on what a Prototype is, check back to [What's an Entity?](../introduction/whats-an-entity.md)
:::

So, now your construction graph should look similar to this;

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
    
    # ----------------------------------
    - node: screwed
      entity: UnfinishedTutorialStructure
      edges:
        - to: addMat
          steps:
            - tool: Screwing
              doAfter: 2

        - to: start
          completed:
            - !type:SpawnPrototype
              prototype: SheetSteel1
              amount: 8
            - !type:DeleteEntity {}
          steps:
            - tool: Welding
              doAfter: 4

    # ----------------------------------
    - node: addMat
      edges:
        - to: struct
          steps:
            - material: Steel
              amount: 2
              doafter: 2

        - to: screwed
          steps:
            - tool: Screwing
              doAfter: 2

    # ----------------------------------
    - node: struct
      entity: TutorialStructure
      edges:
        - to: addMat
          steps:
            - tool: Prying
              doAfter: 2
```

:::info[Author's Note]
You might notice those line comments in the YML, those aren't necessary! I put those in to make the seperation of nodes clearer. Whether you do it like that or not, is up to not only you, but the maintainers of the fork you develop for.
:::

And that's it. If you now go in game, spawn your structure and open its right click menu, you'll find an option to deconstruct it. Press that and examine the entity again to see that your deconstruction steps are in!

:::info[Quick Tip!]
The right click menu is generally referred to as the **Context Menu**
:::

At this stage you now have all the info you need to do basic construction and deconstruction. Tables, weapons, furniture, you have what you need. But somehow we are still not fully done.

What about machines? Or double eyepatches? Those can take things that aren't actual materials like steel and wood, but you'll notice that if you try using those in constructions they don't quite work. When you are more comfortable with the general core of construction & deconstruction, return again for Stage 4, Custom Materials.