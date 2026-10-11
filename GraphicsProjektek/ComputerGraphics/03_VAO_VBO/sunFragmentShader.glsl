#version 330

out vec4 fragColor;

in vec2 varyingTexCoord;

uniform sampler2D sunTexture;

void main(void) {
	fragColor = texture(sunTexture, varyingTexCoord);
}
