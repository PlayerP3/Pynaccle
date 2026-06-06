import pygame,os,json,ast,sys
from .screen import gameScreen
# from .objectsystem import objectManager

class Tilemap():
    def __init__(self):


        self.accessible_tiles = []
        self.inacessible_tiles = []
        self.tilemap = {}
        self.astar_graph = {}

        # chunk vars
        self.currentChunk = "0"
        self.openChunks = ["0"]

        # objects and the chunks they are on
        self.chunkObj = {}

    def load_tilemap(self,tileampJSONDir:str,classMappings:dict):

        # list jsons in tilemap json dir
        chunks = os.listdir(tileampJSONDir)

        for c in chunks:

            # load chunk json
            with open(f"{tileampJSONDir}/{c}", 'r') as f:
                
                params = json.load(f)

            # get chunk
            chunk = c.rstrip('.json')

            # get chunk number
            chunkNo = chunk.lstrip('chunk')

            # add chunk to tilemap
            if chunkNo not in self.tilemap:
                self.tilemap[chunkNo] = {}
                self.chunkObj[chunkNo] = []
        

            # add window for chunk
            # set chunk in bg surf
            gameScreen.add_window(chunk,width=12000,height=12000,pos=(gameScreen.fullscreen_width//2,gameScreen.fullscreen_height//2),zoom=gameScreen.windows['win'].zoom)
            gameScreen.windows[chunk].bg_offset_x = (gameScreen.windows[chunk].win_width)//2
            gameScreen.windows[chunk].bg_offset_y = (gameScreen.windows[chunk].win_height)//2


            # store all pos and layers
            layerPos = []

            # store layer and pos as kv pair
            for layer,layerData in params[chunkNo].items():

                for pos,metadata in layerData.items():

                    layerPos.append((layer,pos))

            # go through kv pair and remove animated sprite class and ad vars you want
            for lp in layerPos:

                buildJSON = {}

                layer = lp[0]
                pos = lp[1]

                # get wallss
                if params[chunkNo][layer][pos]['AnimatedSprite']['img_path'].split('/')[-1] == 'Wall.png':
                    params[chunkNo][layer][pos]['class'] = 'Wall'


                # get class to convert to
                className = params[chunkNo][layer][pos]['class']
                classConversion = params[chunkNo][layer][pos]['class']
                del params[chunkNo][layer][pos]['class']

                # get sprite obj
                objinit = params[chunkNo][layer][pos]

                buildJSON.update(objinit['AnimatedSprite'])
                del objinit['AnimatedSprite']
                buildJSON.update(objinit)

                # add variables of interest from the animated sprite class, can actuall use getattr to be more efficient and have a list of vars you want
                
                # init obj absed on its class and set attrs
                newObj = classMappings[classConversion]()
                for att,val in buildJSON.items():
                    setattr(newObj,att,val)

                # sprite.surface_to_draw_on = 'tilemap'
                # sprite.vertice = 'topleft'
                newObj.hurtbox.topleft= ast.literal_eval(pos)
                newObj.zlayer_drawing = int(layer)
                newObj.spawnLocation = ast.literal_eval(pos)

                # start building copy
                if layer not in self.tilemap[chunkNo]:
                    self.tilemap[chunkNo][layer] = {} 
                
                if pos not in self.tilemap[chunkNo][layer]:
                    self.tilemap[chunkNo][layer][pos] = {}

                # add animated sprite info to myCopy
                self.tilemap[chunkNo][layer][pos] = newObj

                
                # determine what happens to different objs
                if className == 'BgTile':

                    newObj.surface_to_draw_on = chunk
                    newObj.init_sprite()

                    posss = ast.literal_eval(pos)

                    # if posss == (0,0):
                    #     continue
                    newObj.draw_surface(position=ast.literal_eval(pos),schedule_deletion=False)

                    # objectManager.active_pool.append(newObj)
                    # gameScreen.bgSurface['Chunk1'].blit(newObj.sprite,pos)
                

                else:

                    # if className in ['Door','Wallbuy']:
                    #     print(pos)
                    #     sys.exit()


                    newObj.is_active = True
                    newObj.connectedChunk = chunkNo

                    # store objs
                    self.chunkObj[chunkNo].append(newObj)

                    # objectManager.active_pool.append(newObj)

                    # if door attach connected chunk
                    if className == 'Door':

                        newObj.connectedChunk = "1"

            gameScreen.windows[chunk].render_objects()



            


        
tilemapProcessor = Tilemap()