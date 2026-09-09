---
sidebar_position: 3
---

# YML Parenting

Parenting is a very key utility for anyone to understand when it comes to developing for SS14. All Entities have a large amount of information that make up what they are, mostly within the components. Sometimes we want to make a group of entities that all do similar things, but all slightly differently.

Without parenting, this could involve having 5 seperate entities all of which have to define the same exact components in the same exact way for each entity. This makes development far more annoying because not only does it result in large, unreadable `.yml` files but it also means if we wanted to change a single variable that all those entities use, we would have to change it in each entity individually.

Let's throw out an example entity for this

```yaml  showLineNumbers=1
- type: entity
  name: entity one
  description: "One!"
  id: EntityOne
  components:
  - type: tag
    tags:
    - example
  - type: MeleeWeapon
    wideAnimationRotation: -135
    damage:
      types:
        Blunt: 8
    soundHit:
      collection: MetalThud
  - type: PhysicalComposition
    materialComposition:
      Steel: 100
  - type: StaticPrice
    price: 22
```

In this entity we have 4 seperate components attached to it, each with their own specifically defined variables. Now let's say we wanted 3 variants of this entity where the only differences are the damage defined in `Blunt`.

```yaml  showLineNumbers=1
- type: entity
  name: entity one
  description: "One!"
  id: EntityOne
  components:
  - type: tag
    tags:
    - example
  - type: MeleeWeapon
    wideAnimationRotation: -135
    damage:
      types:
        Blunt: 8
    soundHit:
      collection: MetalThud
  - type: PhysicalComposition
    materialComposition:
      Steel: 100
  - type: StaticPrice
    price: 22

- type: entity
  name: entity two
  description: "Two!"
  id: EntityTwo
  components:
  - type: tag
    tags:
    - example
  - type: MeleeWeapon
    wideAnimationRotation: -135
    damage:
      types:
        Blunt: 16
    soundHit:
      collection: MetalThud
  - type: PhysicalComposition
    materialComposition:
      Steel: 100
  - type: StaticPrice
    price: 22

- type: entity
  name: entity three
  description: "three!"
  id: EntityThree
  components:
  - type: tag
    tags:
    - example
  - type: MeleeWeapon
    wideAnimationRotation: -135
    damage:
      types:
        Blunt: 32
    soundHit:
      collection: MetalThud
  - type: PhysicalComposition
    materialComposition:
      Steel: 100
  - type: StaticPrice
    price: 22
```

It's a huge wall of text! This is what happens when we don't use parenting. This now also means that if we perhaps wanted to set the `StaticPrice` of all entities to be perhaps 30, we would have to change that variable in each entity seperately.

So let's try this with parenting

```yaml  showLineNumbers=1
- type: entity
  name: entity one
  description: "One!"
  id: EntityOne
  components:
  - type: tag
    tags:
    - example
  - type: MeleeWeapon
    wideAnimationRotation: -135
    damage:
      types:
        Blunt: 8
    soundHit:
      collection: MetalThud
  - type: PhysicalComposition
    materialComposition:
      Steel: 100
  - type: StaticPrice
    price: 22

- type: entity
  name: entity two
  description: "Two!"
  parent: EntityOne
  id: EntityTwo
  components:
  - type: MeleeWeapon
    wideAnimationRotation: -135
    damage:
      types:
        Blunt: 16
    soundHit:
      collection: MetalThud

- type: entity
  name: entity three
  description: "Three!"
  parent: EntityOne
  id: EntityThree
  components:
  - type: MeleeWeapon
    wideAnimationRotation: -135
    damage:
      types:
        Blunt: 32
    soundHit:
      collection: MetalThud
```

Immediately the huge wall has been cut down significantly as now entity 2 and 3 only have to redefine `MeleeWeapon` without having to define the other components alongside it. When parenting is used all components that are on the parent entity will be transferred to the child entity.

This is incredibly useful when changing variables that should be the same across all entities of that type. In this case we could now change `price` on one entity without having to change it on all 3.

:::warning[Warning!]
Parenting entities will copy **ALL** information to the child entity from the parent. You can redefine information such as the name, description and such. **But you cannot remove information.** This means all components from the parent will be added to the child!

A hacky workaround to this is to redefine a component you don't want on the child like so

```yaml  showLineNumbers=1
  components:
  - type: MeleeWeapon
```

This will set all the variables in that component to their default values. While it is not the same as removing the component, this is the closest there is for now.
:::

:::info[Quick note!]
You might see some entities use `abstract: true` in their YML. All this does is it hides the entity in the admin spawn menu and stops other features of the game spawning that specific entity in.

Abstract is used for entities whose existence is **only** to be used as a base for other entities to parent off of!
:::

## YML Multiparenting

You might see certain YML's use more than one parent on a single entity. An example using the Interdyne Gas Mask from DeltaV:

```yaml  showLineNumbers=1
- type: entity
  parent: [ClothingMaskGas, Tier1Contraband]
  id: ClothingMaskInterdyneChemistry
  name: Interdyne gas mask # imp preference for capsing company names
  description: A face-covering mask that can be connected to an air supply.
  components:
  - type: Sprite
    sprite: _DV/Clothing/Mask/interdynechemmask.rsi
  - type: Clothing
    sprite: _DV/Clothing/Mask/interdynechemmask.rsi
  - type: HideLayerClothing # imp
    slots:
    - SnoutCover
```

Multiparenting allows for inheriting the components from 2 seperate entities. This is primarily useful if you have 2 different entities that you want to inherit from without needing to manually copy components over from one entity to your entity.

```yaml  showLineNumbers=1
- type: entity
  id: ParentOne
  components:
  - type: Sprite
  
- type: entity
  id: ParentTwo
  components:
  - type: Anchorable
  
- type: entity
  parent: [ParentOne, ParentTwo]
  id: OurEntity
```

In this example, `OurEntity` would inherit both the `Sprite` and `Anchorable` components from the other 2 entities.

But what happens if 2 of the parents share the same component type though? Let's say for example we have an entity whose parents both have `Sprite` in their components;

```yaml  showLineNumbers=1
- type: entity
  id: ParentOne
  components:
  - type: Sprite
    sprite: MySprite
  
- type: entity
  id: ParentTwo
  components:
  - type: Sprite
    sprite: MyOtherSprite
  
- type: entity
  parent: [ParentOne, ParentTwo]
  id: OurEntity
```

The way the game resolves parents is by going **left to right** in the parent order, but it will also skip **variables** that have been already defined. This means in this case, `OurEntity` will use the `sprite` from `ParentOne` as the game will skip the `sprite` variable when adding the remaining parents.

If you wanted `OurEntity` to use `ParentTwo`'s `sprite` then you would need to redefine it within the entity itself like so

```yaml  showLineNumbers=1
- type: entity
  parent: [ParentOne, ParentTwo]
  id: OurEntity
  - type: Sprite
    sprite: MyOtherSprite
```