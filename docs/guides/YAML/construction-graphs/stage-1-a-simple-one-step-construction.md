---
sidebar_position: 2
---
# Stage 1: A simple one step construction

Construction Graphs are the key to how all construction works within SS14. Anything that is within your construction menu will utilise a graph of some kind in order to be built. These graphs can be incredibly confusing at first glance however, so we're going to keep to a simple, one step graph first that makes an item.

For this first part we are going to be borrowing our item from [Adding your own Item](../tutorials/your-first-item.md).

```yaml
- type: entity
  name: my item
  description: "My tutorial item."
  parent: BaseItem
  id: TutorialItem
  components:
  - type: Sprite
    sprite: _OurFork/Objects/Tutorial/myitem.rsi
    state: icon
```

First off what you will need to do is make 2 new `.yml` files

`Resources/Prototypes/_OurFork/Recipes/Crafting/myitem.yml`

`Resources/Prototypes/_OurFork/Recipes/Crafting/Graphs/myitemgraph.yml`

- `Crafting` is the directory specifically for graphs related to item crafting.
- `myitem.yml` is the file that will allow us to have our graph appear in the construction menu. This will also let us define more information in future tutorials.
- `myitemgraph.yml` is the file that will contain our actual construction graph.

:::info[Quick Tip!]
`myitem.yml` isn't technically a **required** file as you don't actually need to have your constructs appear within the construction menu. For the purpose of this tutorial though, it is needed!
:::

---
So how does a construction graph actually look. Let's start by defining the base of the graph in the `myitemgraph.yml`

```yaml
- type: constructionGraph
  id: MyItemGraph
  start: start
  graph:
    - node: start 
```

- `start` is the node we start at during construction

Now the immediate question is, what is a node? A node is what defines each step of our construction process. When you for instance, build a wall, each of those steps is a node.

The actual setup of a node will look something like this at its most simplified form

```yaml
 - node: start
   edges:
   - to: end
     steps:
     - material: thing
   
 - node: end
```

So already this will either make sense or look confusing depending on how experienced you are, so let me break it down a little.

- `edges` are the inner part of a node. Within them will be a series of `to`'s controlling what direction the current construction goes. How it decides what `to` to listen to is based on the action within each `to`.
- `to`'s are the inner steps of an edge. What a `to` does is it directs what node the graph should move to next depending on what is done within. In our example, supplying the required `thing` would make the graph progress to the `end` node.
- `steps` are what actually need to be done during crafting. In this case the step is simply having the required `thing` in your inventory when pressing the in game craft button, but for other constructions it might be more detailed. This will be expanded on later.
- `material` is the material to craft the item. It's worth noting that a step will sometimes require something else like a `tag` if you aren't using a standard material like steel or wood. This will be expanded on later.

So applying this information to our construction graph, let's say we want our item to be made out of 5 planks of wood. How would we go about doing this?

```yaml
- type: constructionGraph
  id: MyItemGraph
  start: start
  graph:
    - node: start 
      edges:
        - to: end
          steps:
            - material: WoodPlank
              amount: 5
              doAfter: 4
        
    - node: end
      entity: TutorialItem
```
- `doAfter` is how long in seconds it will take to craft this step.
- `entity` is what will spawn upon reaching the final step.

:::info[Quick Tip!]
Nodes can generally be named whatever you want them to be. But the standard is for the `start` node to be named `start` and for the `end` node to have a name relating to the thing being constructed.

If you looked in `bat.yml` you would see that the final node is called `bat`. We only name it `end` in this tutorial for readability purposes.
:::
---
You now have your construction graph defined, but we aren't done yet. Go back to `myitem.yml` that you made earlier. This is the file that will communicate several things to the game:
- Our construction graph exists
- What nodes it starts and ends on
- The category it will go in in the construction menu
- What kind of object it makes (Item, Structure, etc.)

How this will look in YAML is something like this;

```yaml
- type: construction
  id: MyItemConstruct
  graph: MyItemGraph
  startNode: start
  targetNode: end
  category: construction-category-misc
  objectType: Item
```
- `graph` is the construction graph itself.
- `startNode` is the node the graph starts on.
- `targetNode` is the node the graph ends on.
- `category` is the category of the construction menu it is in. The name is a localised name, hence why it looks strange. There is a [Page dedicated to Localisation](/docs/upstream/ss14-by-example/fluent-and-localization.md) in the Upstream section. 
- `objectType` is the type of thing we are constructing.

That is all this file will require.

---

Now there is one more step before we can be done. Head back to your items main YML as there is one more component we need to add before it is truly constructible which will help define our items place within the construction graph.

```yaml
- type: entity
  name: my item
  description: "My tutorial item."
  parent: BaseItem
  id: TutorialItem
  components:
  - type: Sprite
    sprite: _OurFork/Objects/Tutorial/myitem.rsi
    state: icon
  - type: Construction
    graph: MyItemGraph
    node: end
```

- `Construction` is the component that allows this entity to be constructed in the first place.
- `graph` is the graph associated with this entity's construction.
- `node` is the node that this entity will be spawned on. Note that this is different from the end node! As some nodes will change the entity being constructed before the end. This will be expanded on later.

If you now go into the game and peek into the Misc tab of the Construction menu, you will find our item!

![image](https://hackmd.io/_uploads/By-aK1yffl.png)

All done! Partially. This is how construction graphs look at their absolute simplest form but the more you want to do with them, the more complex they will become. Multi step construction, deconstruction, custom materials, all these things will make construction graphs go from a simple few lines to hulking behemoths.

I would heavily advise feeling comfortable with construction graphs at this stage **before** moving forward to more complex graphs.

---