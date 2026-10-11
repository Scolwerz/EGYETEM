#version 330

layout (location = 0) in vec3 aPosition;	// Csúcspont pozíció
//layout (location = 1) in vec3 aNormal;		// Csúcspont normálvektora
layout (location = 2) in vec2 aTexCoord;	// Textúra

out vec2 varyingTexCoord;

uniform mat4 matModel;
uniform mat4 matView;
uniform mat4 matProjection;

void main(void) {
	varyingTexCoord = aTexCoord;
	gl_Position = matProjection * matView * matModel * vec4(aPosition, 1.0);
}
