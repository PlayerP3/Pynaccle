#version 330 core

uniform vec2 screenSize;
uniform vec2 spriteSize;
uniform vec2 spriteOffset;
uniform vec2 bgOffset;
uniform vec2 position;
uniform float rotation;
uniform int zoom;

in vec2 vertexPosition;
in vec2 textureCoordinate;
out vec2 uvs;

void main() {
    
    uvs = textureCoordinate;

   // uvs = textureCoordinate;
    float bb = zoom;

    

    // find rotation
    float s = sin(rotation);
    float c = cos(rotation);
    //vec2 rotatedVertexPosition = vec2(vertexPosition.x*c - vertexPosition.y*s,vertexPosition.x*s + vertexPosition.y*c);

    // calculate scale/new size of the sprite, multuply by 2 because ndc ranges from -1 to 1 which is 2 whilst pixels are 0 to 1
    vec2 scaledVertexPosition2 = vertexPosition * (vec2(spriteSize.x/screenSize.x,spriteSize.y/screenSize.y)*zoom*2);

    // calculate offset, position center of sprite at this pos
    vec2 offset = vec2(position.x/screenSize.x,-position.y/screenSize.y)*2 + vec2(spriteOffset.x/screenSize.x,-spriteOffset.y/screenSize.y)*2 + vec2(bgOffset.x/screenSize.x,-bgOffset.y/screenSize.y)*2;
    
    // get scaled vertex position
    vec2 scaledVertexPosition = vertexPosition * zoom;
    
    //gl_Position = vec4(scaledVertexPosition,0.0,1.0);

    gl_Position = vec4(vertexPosition,0.0,1.0);

}

