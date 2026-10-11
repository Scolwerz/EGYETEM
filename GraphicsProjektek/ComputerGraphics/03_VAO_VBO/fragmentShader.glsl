#version 330

out vec4 fragColor;

in vec3 varyingFragmentPosition;
in vec3 varyingNormal;

uniform vec3 cubeColor;

uniform vec3 lightPos;
uniform vec3 lightDiffColor;
uniform int lightSwitch;	// 0:kii   1:be

uniform vec3 cameraPos;

void main(void) {
	if (lightSwitch == 0) {		// kikapcsolva
		fragColor = vec4(cubeColor, 1.0);
		return;
	}

	vec3 norm = normalize(varyingNormal);

	vec3 lightDirection = normalize(lightPos - varyingFragmentPosition);

	// nem negatív - hátulról ne mvilágít
	float diffStrength = max(dot(norm, lightDirection), 0.0);
	vec3 diff = diffStrength * lightDiffColor * cubeColor;

	float ambientStrength = 0.15;
	vec3 ambient = ambientStrength * lightDiffColor * cubeColor;

	fragColor = vec4(ambient + diff, 1.0);
}
