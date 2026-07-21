#version 330 core

uniform sampler2D dissolveTexture;
uniform sampler2D memSlot;
uniform float dissolveValue;
uniform float alpha=1;

in vec2 uvs;
out vec4 f_color;

void main() {

    
    float x = alpha;
    vec4 mainTexture = texture(memSlot, uvs);

    if (mainTexture.a > 0 ){
    
        vec4 noiseTexture = texture(dissolveTexture, uvs);
        mainTexture.a *= floor(dissolveValue + min(1, noiseTexture.r));
        //float cc = dissolveValue;
        f_color = mainTexture;
    }
    else {
        discard;
    }

}