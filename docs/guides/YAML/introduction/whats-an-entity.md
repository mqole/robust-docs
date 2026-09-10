---
sidebar_position: 1
---

# What's an Entity?

Entities are the very core of SS14's interactions. All items, mobs, structures, etc. are entities.

All entities you add will generally has this very base structure
```yaml  showLineNumbers=1
- type: entity
  name: my entity
  description: "My tutorial entity."
  id: TutorialEntity
```

- `type` here denotes what kind of prototype we use. For most things within the game, that will be an entity.
- `name` is what your entity will be called in game.
- `description` is what people will see in the popup box upon examining this entity 
- `id` is what the name used by other prototypes, command, etc will be

:::info[Quick Note!]
All entities in the game will have an all lower case `name`. So it's important to stick to that for consistency! Though how strict this is depends on the particular fork.

All `id`'s in the game generally use proper capitalisation.
:::