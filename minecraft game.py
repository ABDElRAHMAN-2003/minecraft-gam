
"""you can build a box with left_click"""
"""you can destroy a box with right_click"""
"""use the hook by (L) then left mouse click"""
"""you can change the boxes textures by clicking 1 or 2 or 3 or 4"""

from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import curve    
app = Ursina()
sky_texture=load_texture("skybox.png")
grass_texture=load_texture("grass_block.png")     
stone_texture=load_texture("stone_block.png")
dirt_texture=load_texture("dirt_block.png")
brick_texture=load_texture("brick_block.png")
punch_sound=Audio('mixkit-blow-breaking-the-air-2057.wav' , loop = False, autoplay = False)                #textures of models
punch_sound2=Audio('cloth-inventory.wav', loop=False, autoplay=False) 
arm_texture=load_texture("arm_texture.png")
sound5=Audio('Birds and Wind - Ambient.ogg', loop = True , autoplay = True)
block_pick = 1
window.fps_counter.enabled = False 
window.exit_button.visible = False                                                                      #some options for the interface
window.fullscreen=True 



def update():                             
    global block_pick                                     
    if held_keys["left mouse"] or held_keys["right mouse"]:                 
        hand.active()                                                       
    else:                                                                   
        hand.passive()                                                                                                   
    if held_keys['1'] :                                                      
        block_pick = 1
    if held_keys['2'] :                                                                     #block texture changer(S)
        block_pick = 2
    if held_keys['3'] :
        block_pick = 3
    if held_keys['4'] :
        block_pick = 4

class Vox(Button):
    def __init__(self,position=(0,0,0),texture=grass_texture):                                                               
        super().__init__(
            parent=scene,
            position=position,
            model="block",                                                  #the cubes (M)
            texture=texture,
            color=color.color(0,0,random.uniform(0.9,1)),                 
            origin_y=0.5,
            #highlight_color=color.lime,
            scale=0.5
        )
    def input(self,key):
        if self.hovered:
            if key=="left mouse down":                                           
                #voxel=Vox(position=self.position + mouse.normal) 
                punch_sound.play()   
                if block_pick==1:
                    voxel=Vox(position=self.position + mouse.normal , texture = grass_texture)
                if block_pick==2:
                    voxel=Vox(position=self.position + mouse.normal , texture = dirt_texture)   # block texture changer(S)
                if block_pick == 3:
                    voxel=Vox(position=self.position + mouse.normal , texture = stone_texture)
                if block_pick==4:
                    voxel=Vox(position=self.position + mouse.normal , texture = brick_texture)
            if key=="right mouse down":                                                                                 #destroy sound(S)
                punch_sound2.play()
                destroy(self)

                 #########################################

            if key=="l":
                self.on_click=Func(player.animate_position,                     
                self.position,
                duration=0.5,
                curve=curve.linear         # the hook function(A)
                )
class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,              #the sky function(N)
			scale = 150,
			double_sided = True)
class sun(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model = 'sphere',
            texture="sun_softer.png",  #the sun function(S)
            scale=500,
            double_sided=True,
            rotation=(260,-220,20),
            position=(0,-300,-300)
        )
class magic_planet(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model = 'sphere',
            texture="Main_Base_Color.png",  #the  function of magic planet(M)
            scale=600,
            double_sided=True,
            rotation=(260,-220,20),
            position=(0,-400,-900)
        )
class Mercury(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model = 'sphere',
            texture="rock_type_planet.png",  #the mercury function(A)
            scale=500,
            double_sided=True,
            rotation=(130,-10,0),
            position=(0,-300,1000)
        )
class earth(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model = 'sphere',
            texture="Terrestrial-Clouds-EQUIRECTANGULAR-8-1024x512.png",  #the earth function(N)
            scale=152,
            double_sided=True,
            rotation=(130,-10,0)
        )
class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model ='arm.blend',                         #hand function (M)
			texture = arm_texture,
			scale = 0.21,
			rotation = Vec3(320,-10,0),
            position = Vec2(0.4,-0.6)
            )

	def active(self):
		self.position = Vec2(0.3,-0.5)                 #hand when active(A)


	def passive(self):
		self.position = Vec2(0.4,-0.6)                  #hand when passive(N)



#________________________________________________________________________________

player=FirstPersonController(y=20)#,duration_y=5)         #the carachter controller

####################
Entity(model="maaa.obj",position=(5,0,27),scale=0.5,texture="toadstool_diffuse.tif")
Entity(model="small_mushroom_1_mdl.obj",position=(6,0,26),scale=0.5,texture="toadstool_diffuse.tif")
Entity(model="small_mushroom_2_mdl.obj",position=(7,0,27),scale=0.5,texture="toadstool_diffuse.tif")
Entity(model="treetoonstylized01.obj",position=(2,0,25),scale=1,texture="TextureUVTreeToonStylizedStyle01.png")
Entity(model="car.obj",position=(24,0,17),scale=0.020,rotation=(0,0,0),texture="Kopie von Kopie von corradon.png")
Entity(model="lowpolygarage.fbx",position=(24,0,18),scale=0.015,rotation=(0,0,0),texture="lowpolygarage_Material_AlbedoTransparency.png") # entities or models
Entity(model="maqdy.obj",position=(24,0,8),texture="lllllllll",scale=17,rotation=(0,-90,0))
Entity(model="dog2.obj",rotation=(0,-90,0),position=(14,0.2,6),texture="dooog.png")
Entity(model="DogHouse.obj",rotation=(0,0,0),scale=0.1,position=(12,-1.3,1.7),texture="DogHouseTexture4.jpg")

for z in range(30):
    for x in range(30):
        voxel=Vox(position=(x,0,z))  #plane size(M)

sky=earth()
sky=Sky()
sky=sun()
sky=magic_planet()
sky=Mercury()
hand=Hand()
app.run()