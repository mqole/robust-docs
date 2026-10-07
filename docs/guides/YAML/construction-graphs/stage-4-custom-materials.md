---
sidebar_position: 5
---
# Stage 4: Custom Materials

So let's say you want a construction project that uses non-standard materials. This can be absolutely any item in the game. In this example we're going to be using an **Inert Gravity Anomaly Core.** and adding it to the graph that we made in [Stage 3](stage-3-deconstruction.md)

One again we're going to need 2 new files before we can jump in;

`Resources\Locale\en-US\_OurFork\recipes\tags.ftl`
`Resources\Prototypes\_OurFork\tags.yml`

:::info[Quick Note!]
These files are present in almost every fork of the game, so be sure to check to make sure they already exist before making them!
:::

So first let's explain `tags.yml`, what does it do? Well you may have seen this component in certain YML's if you have poked around in the game files

```yaml
- type: Tag
  tags:
  - SomeTag
```

Tags are a useful way for the game to lump things together, they effectively work as an organisational tool. Let's say we wanted to use a gun in our recipe. Without tags, we would have to define dozens upon dozens of nodes each one allowing the use of a different gun within the recipe. With Tags we only have to make sure that all of those guns share a single tag.

Within `tags.yml` just drop this in. What it will do is it will register `GravityCore` as a recognised Tag for the rest of the game to use.

```yaml
- type: Tag
  id: GravityCore
```
---
What about `tags.ftl`?

This is our [localisation](/docs/upstream/ss14-by-example/fluent-and-localization.md) file for where our material name will be placed. First let's drop this line in the file;

`construction-graph-tag-anomaly-core-gravity = Inert Gravity Anomaly Core`

So what's `construction-graph-tag-anomaly-core-gravity`? This is what we're going to be using within our construction graph to define the name of our material. Any references to the `Inert Gravity Anomaly Core` will have `construction-graph-tag-anomaly-core-gravity` assigned instead of the plain name, this is for translation purposes! 

:::info[Quick Tip!]
A more in-depth look at localisation and how it works can be found on the [Upstream localisation documentation!](/docs/upstream/ss14-by-example/fluent-and-localization.md)
:::

---

So what do we do with our new tag? Well first we need to let the game know what the tag is applied to as right now, it's just an isolated tag with no purpose. For this what we will need to do is go to 

`Resources\Prototypes\Entities\Structures\Specific\Anomaly\cores.yml`

And work our way down to `AnomalyCoreGravityInert`, once we are there we now need to add the `Tag` component onto it as laid out above. This way now the Gravity Core will actually have our tag applied, meaning we can now use it in graphs!

```yaml
# OurFork Edit Start
  - type: Tag
    tags:
    - GravityCore
# OurFork Edit End
```

:::info[Quick Tip!]
You might be confused about those 2 comments there. Well that's a common practice on forks when editing files that are **outside** of your specific forks folder. It lets people know what edits are from what fork or are from upstream!

**Another tip!**
Entities can have **multiple** tags, that's part of why the system is so useful.
:::
---
So now that we have our tag applied, what else is there to do? Yeah it's the graph again.

Head back to our construction graph from [Stage 3](./stage-3-deconstruction.md) and place in a new node called `addAnom` amd set it up like all the other nodes, including a deconstruction step, except in this case within `steps` for the construction phase we aren't going to be defining a `tool` or `material`, instead we will be defining this;

```yaml
            - tag: GravityCore
              name: construction-graph-tag-anomaly-core-gravity
              icon: 
                sprite: Structures/Specific/Anomalies/Cores/gravity_core.rsi
                state: core
              doAfter: 3
```

Okay so what's happening. Let me break it into steps

- `tag` is our tag that we defined earlier, this allows all entities with this tag to be used within the recipe.
- `name` is the name assigned in `tags.ftl` earlier. What this will do is it will let the name display based on the players language settings. The `name` we put in our `step` here is the behind the scenes name that the game will use to get this translated name.
- `icon` is what the icon associated with this material will be in our Construction menu. It's set up very similarly to a typical `Sprite` component, using the same `sprite` and `state` variables.

:::warning[Warning!]
`name` **must** use a localised name, you cannot put a standard name like "Anomaly Core" in there as it will try to search the `.ftl` files for this name!
:::

You should now have a node that looks very similar to this

```yaml
    # ----------------------------------    

    
    - node: addAnom
      edges:
        - to: struct
          steps:
            - tag: GravityCore
              name: construction-graph-tag-anomaly-core-gravity
              icon: 
                sprite: Structures/Specific/Anomalies/Cores/gravity_core.rsi
                state: core
              doAfter: 3

        - to: screwed
          steps:
            - tool: Welding
              doAfter: 3    

    # ----------------------------------
```

:::info[Quick Tip!]
Once again those line comments aren't necessary! I just use them to split the nodes apart for easier readability!
:::

It's now once again time to test this in game. Open up your Construction menu and look for our structure and you should be met with a graph looking like this;

![image](https://hackmd.io/_uploads/r1DmEHNffx.png)

If you were to now follow the steps through, you'd find that our custom material works in the recipe! That's all there really is to custom materials. They can sound a lot more complex than they truly are.