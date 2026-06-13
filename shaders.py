import pygame
import moderngl
import sys
from array import array

pygame.init()

screen = pygame.display.set_mode((800,600),pygame.OPENGL|pygame.DOUBLEBUF)
display = pygame.Surface((800,600))
ctx = moderngl.create_context()

clock = pygame.time.Clock()

img = pygame.image.load('pynaccle/Sprites/Cards/Hearts/1_23x36.png')

img = pygame.transform.scale_by(img,7)


quad_buffer = ctx.buffer(data=array('f',[

    # pos xy uv cords xy
    -1.0,1.0,0.0,0.0, #tl
    1.0,1.0,1.0,0.0, # tr
    -1.0,-1.0,0.0,1.0, # bl
    1.0,-1.0,1.0,1.0, # br
]))


vert_shader = '''
#version 330 core

in vec2 vert;
in vec2 texcoord;
out vec2 uvs;

void main() {
    uvs = texcoord;
    gl_Position = vec4(vert,0.0,1.0);

}

'''



frag_shader = '''
#version 330 core

uniform sampler2D tex;
uniform float time;

in vec2 uvs;
out vec4 f_color;

void main() {
    float xxx = time;
    vec2 sample_pos = vec2(uvs.x* cos(1*time*0.01) ,uvs.y* cos(1*time*0.01));
    f_color = vec4(texture(tex,sample_pos).r,texture(tex,sample_pos).g ,texture(tex,sample_pos).b,1.0);
}

'''
# + sin(uvs.y / 0.07 + time *0.01)*0.1


program = ctx.program(vertex_shader=vert_shader,fragment_shader=frag_shader)
render_object = ctx.vertex_array(program,[(quad_buffer,'2f 2f','vert','texcoord')])

def surf_to_texture(surf):

    tex = ctx.texture(surf.get_size(),4)

    tex.filter = (moderngl.NEAREST,moderngl.NEAREST)

    tex.swizzle = 'BGRA'

    tex.write(surf.get_view('1'))

    return tex

t = 0

while True:

    t += 1

    display.fill((0,0,0))
    # mysurf.fill((0,0,0))
    # mysurf.blit(img)
    display.blit(img,(100,100))
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

    frame_tex = surf_to_texture(display)

    frame_tex.use(0)

    program['tex'] = 0
    program['time'] = t

    render_object.render(mode=moderngl.TRIANGLE_STRIP)

    pygame.display.flip()

    frame_tex.release()
    
    clock.tick(60)