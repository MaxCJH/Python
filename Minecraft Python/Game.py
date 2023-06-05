'''
Nombre del archivo: Game.py
Autor: Max Carlos
Fecha de creación: 21/06/2022 
'''

# Aquí comienza el código del script...

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
app = Ursina()
class Voxel(Button):
    def __init__(self, position=Vec3(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            color=color.color(random.uniform(0.6, 0.8), random.uniform(0.4, 0.6), random.uniform(0.2, 0.4)),
            texture='white_cube',
            highlight_color=color.lime,
        )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)
            elif key == 'right mouse down':
                destroy(self)
                # Verificar si hay un árbol en la posición actual y destruirlo si lo hay
                hit_info = mouse.intersected_entity
                if hit_info and isinstance(hit_info.entity, Tree):
                    destroy(hit_info.entity)
class Tree(Entity):
    def __init__(self, position=Vec3(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            color=color.brown,
            texture='white_cube',
            highlight_color=color.lime,
            scale=(1, random.randint(5, 9), 1)
        )
        self.create_leaves()
    def create_leaves(self):
        leaves_position = self.position + (0, self.scale_y / 2 + 0.5, 0)
        leaves_scale = random.randint(3, 5)
        leaves = Entity(
            parent=scene,
            position=leaves_position,
            model='sphere',
            color=color.green,
            texture='white_cube',
            highlight_color=color.lime,
            scale=(leaves_scale, leaves_scale, leaves_scale)
        )
chunk_size = 10
tree_spacing = 5
for z in range(chunk_size):
    for x in range(chunk_size):
        voxel = Voxel(position=Vec3(x, 0, z))
        if random.random() < 0.1:
            tree_x = x * tree_spacing
            tree_z = z * tree_spacing
            tree = Tree(position=Vec3(tree_x, 1, tree_z))
player = FirstPersonController()
Sky()
app.run()
