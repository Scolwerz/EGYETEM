enum eVertexArrayObject {
	VAOCubeData,
	VAOSunData,
	VAOCount
};

enum eBufferObject {
	VBOCubeData,
	VBOSunData,
	BOCount
};

enum eProgram {
	CubeProgram,
	SunProgram,
	ProgramCount
};

enum eTexture {
	SunTexture,
	TextureCount
};
GLuint texture[TextureCount];

#include "common.cpp"

GLchar windowTitle[] = "Cubes";
GLfloat aspectRatio;


// Camera
const GLfloat CAMERA_R = 9.0f;					// Kamera henger sugár
const GLfloat HORIZONTAL_SPEED = 0.01f;
const GLfloat VERTICAL_SPEED = 0.1f;
GLfloat cameraAngle = 0.0f;						// Kamera mozgási szög
GLfloat cameraZ = 0.0f;							// Kamera kezdeti magasság
vec3 cameraPos = vec3(CAMERA_R, 0.0f, 0.0f);	// Kamera pozíció
vec3 cameraORIGO = vec3(0.0f, 0.0f, 0.0f);		// Kamera origoba néz
vec3 cameraUpVector = vec3(0.0f, 0.0f, 1.0f);


// Light
const GLfloat LIGHT_R = 2.0f * CAMERA_R;		// Fény kör sugara
const GLfloat LIGHT_SPEED = 1.0f;				// Fény sebessége
vec3 lightPos = vec3(LIGHT_R, 0.0f, 0.0f);		// Fény pozíciója
vec3 lightDiffColor = vec3(1.0f, 0.8f, 0.1f);	// Fény "sárga" diff szín
GLint lightSwitch = 1;							// 1: be, 0: ki


// Cubes
// Sor: x, y, z ,nx, ny, nz (normálvektor)
GLfloat cubeData[] = {
	// Hátsó (z = -0.5), (0, 0, -1)
	-0.5f, -0.5f, -0.5f,  0.0f,  0.0f, -1.0f,
	 0.5f, -0.5f, -0.5f,  0.0f,  0.0f, -1.0f,
	 0.5f,  0.5f, -0.5f,  0.0f,  0.0f, -1.0f,
	 0.5f,  0.5f, -0.5f,  0.0f,  0.0f, -1.0f,
	-0.5f,  0.5f, -0.5f,  0.0f,  0.0f, -1.0f,
	-0.5f, -0.5f, -0.5f,  0.0f,  0.0f, -1.0f,

	// Első (z = 0.5), (0, 0, 1)
	-0.5f, -0.5f,  0.5f,  0.0f,  0.0f,  1.0f,
	 0.5f, -0.5f,  0.5f,  0.0f,  0.0f,  1.0f,
	 0.5f,  0.5f,  0.5f,  0.0f,  0.0f,  1.0f,
	 0.5f,  0.5f,  0.5f,  0.0f,  0.0f,  1.0f,
	-0.5f,  0.5f,  0.5f,  0.0f,  0.0f,  1.0f,
	-0.5f, -0.5f,  0.5f,  0.0f,  0.0f,  1.0f,

	// Bal (x = -0.5), (-1, 0, 0)
	-0.5f,  0.5f,  0.5f, -1.0f,  0.0f,  0.0f,
	-0.5f,  0.5f, -0.5f, -1.0f,  0.0f,  0.0f,
	-0.5f, -0.5f, -0.5f, -1.0f,  0.0f,  0.0f,
	-0.5f, -0.5f, -0.5f, -1.0f,  0.0f,  0.0f,
	-0.5f, -0.5f,  0.5f, -1.0f,  0.0f,  0.0f,
	-0.5f,  0.5f,  0.5f, -1.0f,  0.0f,  0.0f,

	// Jobb (x = 0.5), (1, 0, 0)
	 0.5f,  0.5f,  0.5f,  1.0f,  0.0f,  0.0f,
	 0.5f,  0.5f, -0.5f,  1.0f,  0.0f,  0.0f,
	 0.5f, -0.5f, -0.5f,  1.0f,  0.0f,  0.0f,
	 0.5f, -0.5f, -0.5f,  1.0f,  0.0f,  0.0f,
	 0.5f, -0.5f,  0.5f,  1.0f,  0.0f,  0.0f,
	 0.5f,  0.5f,  0.5f,  1.0f,  0.0f,  0.0f,

	 // Alsó (y = -0.5), (0, -1, 0)
	 -0.5f, -0.5f, -0.5f,  0.0f, -1.0f,  0.0f,
	  0.5f, -0.5f, -0.5f,  0.0f, -1.0f,  0.0f,
	  0.5f, -0.5f,  0.5f,  0.0f, -1.0f,  0.0f,
	  0.5f, -0.5f,  0.5f,  0.0f, -1.0f,  0.0f,
	 -0.5f, -0.5f,  0.5f,  0.0f, -1.0f,  0.0f,
	 -0.5f, -0.5f, -0.5f,  0.0f, -1.0f,  0.0f,

	 // Felső (y = 0.5), (0, 1, 0) 
	 -0.5f,  0.5f, -0.5f,  0.0f,  1.0f,  0.0f,
	  0.5f,  0.5f, -0.5f,  0.0f,  1.0f,  0.0f,
	  0.5f,  0.5f,  0.5f,  0.0f,  1.0f,  0.0f,
	  0.5f,  0.5f,  0.5f,  0.0f,  1.0f,  0.0f,
	 -0.5f,  0.5f,  0.5f,  0.0f,  1.0f,  0.0f,
	 -0.5f,  0.5f, -0.5f,  0.0f,  1.0f,  0.0f
};

vec3 cubePoints[3] = {
	vec3(0.0f,  0.0f,  0.0f),
	vec3(0.0f,  0.0f,  2.0f),
	vec3(0.0f,  0.0f, -2.0f)
};


const int SUN_SECTORS = 32;			// Horizontal segment count
const int SUN_RINGS = 16;			// vertical segment count
const GLfloat SUN_R = 0.25f;		// Nap gömb sugara
vector<GLfloat> sunData;			// Nap gömb háromszög pontjai
GLint sunDataCount = 0;


GLuint cubeColorLoc;			// Kockák színének uniform locationje
GLuint inverseTransposeLoc;     // Inverz transzp mátrix a normálvektorokhoz
GLuint lightPosLoc;             // Fény pozíciója
GLuint lightDiffColorLoc;       // Fény diffúz színe
GLuint lightSwitchLoc;          // világítás be/ki 1:be, 0:ki
GLuint cameraPosLoc;            // Kamera pozíciója
GLuint sunColorLoc;             // Nap anyagszíne
GLuint sunMatModelLoc;          // Nap mátrixa
GLuint sunMatViewLoc;           // Nézeti mátrix a sun shaderben
GLuint sunMatProjectionLoc;     // Projekciós mátrix a sun shaderben
GLuint sunTexLoc;				// Nap textúra


/*void generateSun(float radius, int sectors, int rings) {
	sunData.clear();
	float sectorAngle = 2.0f * (float)M_PI / sectors;
	float ringAngle = (float)M_PI / rings;
	for (int ring = 0; ring < rings; ring++) {
		float fi1 = (float)M_PI / 2.0f - ring * ringAngle;
		float fi2 = (float)M_PI / 2.0f - (ring + 1) * ringAngle;

		float y1 = radius * sin(fi1);
		float y2 = radius * sin(fi2);
		float r1 = radius * cos(fi1);
		float r2 = radius * cos(fi2);

		for (int sector = 0; sector < sectors; sector++) {
			float t1 = sector * sectorAngle;
			float t2 = (sector + 1) * sectorAngle;

			float x1t1 = r1 * cos(t1), z1t1 = r1 * sin(t1);
			float x1t2 = r1 * cos(t2), z1t2 = r1 * sin(t2);
			float x2t1 = r2 * cos(t1), z2t1 = r2 * sin(t1);
			float x2t2 = r2 * cos(t2), z2t2 = r2 * sin(t2);

			float nx1t1 = x1t1 / radius, ny1 = y1 / radius, nz1t1 = z1t1 / radius;
			float nx1t2 = x1t2 / radius, nz1t2 = z1t2 / radius;
			float nx2t1 = x2t1 / radius, ny2 = y2 / radius, nz2t1 = z2t1 / radius;
			float nx2t2 = x2t2 / radius, nz2t2 = z2t2 / radius;
			// Első háromszög: felső-bal, alsó-bal, alsó-jobb
			sunData.insert(sunData.end(), { x1t1,y1,z1t1, nx1t1,ny1,nz1t1 });
			sunData.insert(sunData.end(), { x2t1,y2,z2t1, nx2t1,ny2,nz2t1 });
			sunData.insert(sunData.end(), { x2t2,y2,z2t2, nx2t2,ny2,nz2t2 });
			// Második háromszög: felső-bal, alsó-jobb, felső-jobb
			sunData.insert(sunData.end(), { x1t1,y1,z1t1, nx1t1,ny1,nz1t1 });
			sunData.insert(sunData.end(), { x2t2,y2,z2t2, nx2t2,ny2,nz2t2 });
			sunData.insert(sunData.end(), { x1t2,y1,z1t2, nx1t2,ny1,nz1t2 });
		}
	}
	sunDataCount = (GLint)(sunData.size() / 6);
}*/
void generateSun(float radius, int slices, int stacks) {
	for (int i = 0; i < stacks; ++i) {
		float phi1 = M_PI * (float)i / stacks;
		float phi2 = M_PI * (float)(i + 1) / stacks;

		for (int j = 0; j < slices; ++j) {
			float theta1 = 2.0f * M_PI * (float)j / slices;
			float theta2 = 2.0f * M_PI * (float)(j + 1) / slices;

			// Vertexek és textúra koordináták (s, t)
			auto addVertex = [&](float phi, float theta) {
				float x = radius * sin(phi) * cos(theta);
				float y = radius * sin(phi) * sin(theta);
				float z = radius * cos(phi);
				sunData.push_back(x); sunData.push_back(y); sunData.push_back(z);
				// Textúra koordináták: s = theta / 2pi, t = phi / pi
				sunData.push_back(theta / (2.0f * (float)M_PI));
				sunData.push_back(phi / (float)M_PI);
				};

			addVertex(phi1, theta1); addVertex(phi2, theta1); addVertex(phi2, theta2);
			addVertex(phi1, theta1); addVertex(phi2, theta2); addVertex(phi1, theta2);
		}
	}
}

GLuint loadTexture(const GLchar* texturePath) {
	GLuint textureID = SOIL_load_OGL_texture(texturePath, SOIL_LOAD_AUTO, SOIL_CREATE_NEW_ID, SOIL_FLAG_INVERT_Y);
	if (textureID == 0) {
		std::cerr << "Error: could not find texture image: " << texturePath << std::endl;
		return 0;
	}
	glBindTexture(GL_TEXTURE_2D, textureID);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
	glGenerateMipmap(GL_TEXTURE_2D);
	return textureID;
}


void initCubeShader() {
	ShaderInfo shaderInfo[] = {
		{ GL_VERTEX_SHADER,   "./vertexShader.glsl"   },
		{ GL_FRAGMENT_SHADER, "./fragmentShader.glsl"  },
		{ GL_NONE, nullptr }
	};

	program[CubeProgram] = LoadShaders(shaderInfo);

	locationMatModel = glGetUniformLocation(program[CubeProgram], "matModel");
	locationMatView = glGetUniformLocation(program[CubeProgram], "matView");
	locationMatProjection = glGetUniformLocation(program[CubeProgram], "matProjection");
	cubeColorLoc = glGetUniformLocation(program[CubeProgram], "cubeColor");
	inverseTransposeLoc = glGetUniformLocation(program[CubeProgram], "inverseTransposeMatrix");
	lightPosLoc = glGetUniformLocation(program[CubeProgram], "lightPos");
	lightDiffColorLoc = glGetUniformLocation(program[CubeProgram], "lightDiffColor");
	cameraPosLoc = glGetUniformLocation(program[CubeProgram], "cameraPos");
	lightSwitchLoc = glGetUniformLocation(program[CubeProgram], "lightSwitch");

	glBindVertexArray(VAO[VAOCubeData]);
	glBindBuffer(GL_ARRAY_BUFFER, BO[VBOCubeData]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(cubeData), cubeData, GL_STATIC_DRAW);

	// location = 0: pozíció  
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), (GLvoid*)0);
	glEnableVertexAttribArray(0);

	// location = 1: normálvektor
	glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), (GLvoid*)(3 * sizeof(GLfloat)));
	glEnableVertexAttribArray(1);

	glUseProgram(program[CubeProgram]);

	projectionType = Perspective;
	matModel = mat4(1.0f);
	matView = lookAt(cameraPos, cameraORIGO, cameraUpVector);

	glUniformMatrix4fv(locationMatModel, 1, GL_FALSE, value_ptr(matModel));
	glUniformMatrix4fv(locationMatView, 1, GL_FALSE, value_ptr(matView));
	glUniformMatrix4fv(locationMatProjection, 1, GL_FALSE, value_ptr(matProjection));
	glUniform3f(cubeColorLoc, 1.0f, 1.0f, 1.0f);	// Kockák színe
	glUniform3fv(lightDiffColorLoc, 1, value_ptr(lightDiffColor));
	glUniform3fv(cameraPosLoc, 1, value_ptr(cameraPos));
	glUniform1i(lightSwitchLoc, 1);

	glEnable(GL_DEPTH_TEST);	// Z-buffer
}


void initSunShader() {
	generateSun(SUN_R, SUN_SECTORS, SUN_RINGS);

	ShaderInfo shaderInfo[] = {
		{ GL_VERTEX_SHADER,   "./sunVertexShader.glsl"   },
		{ GL_FRAGMENT_SHADER, "./sunFragmentShader.glsl"  },
		{ GL_NONE, nullptr }
	};

	program[SunProgram] = LoadShaders(shaderInfo);

	sunMatModelLoc = glGetUniformLocation(program[SunProgram], "matModel");
	sunMatViewLoc = glGetUniformLocation(program[SunProgram], "matView");
	sunMatProjectionLoc = glGetUniformLocation(program[SunProgram], "matProjection");
	//sunColorLoc = glGetUniformLocation(program[SunProgram], "sunColor");
	sunTexLoc = glGetUniformLocation(program[SunProgram], "sunTexture");

	glBindVertexArray(VAO[VAOSunData]);
	glBindBuffer(GL_ARRAY_BUFFER, BO[VBOSunData]);
	glBufferData(GL_ARRAY_BUFFER, (GLsizeiptr)(sunData.size() * sizeof(GLfloat)), sunData.data(), GL_STATIC_DRAW);

	// location = 0: pozíció  
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), (GLvoid*)0);
	glEnableVertexAttribArray(0);

	// location = 1: normálvektor
	//glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), (GLvoid*)(3 * sizeof(GLfloat)));
	//glEnableVertexAttribArray(1);

	// location = 2: textúra (s, t)
	glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), (GLvoid*)(3 * sizeof(GLfloat)));
	glEnableVertexAttribArray(2);

	glUseProgram(program[SunProgram]);
	glUniform3fv(sunColorLoc, 1, value_ptr(lightDiffColor));
	texture[SunTexture] = loadTexture("./sunMaterial.jpg");
}

void initShaderProgram() {
	initCubeShader();
	initSunShader();
}


void updateCameraMat() {
	cameraPos.x = CAMERA_R * cos(cameraAngle);
	cameraPos.y = CAMERA_R * sin(cameraAngle);
	cameraPos.z = cameraZ;
	matView = lookAt(cameraPos, cameraORIGO, cameraUpVector);

	glUseProgram(program[CubeProgram]);
	glUniformMatrix4fv(locationMatView, 1, GL_FALSE, value_ptr(matView));
	glUniform3fv(cameraPosLoc, 1, value_ptr(cameraPos));

	glUseProgram(program[SunProgram]);
	glUniformMatrix4fv(sunMatViewLoc, 1, GL_FALSE, value_ptr(matView));
}


void display(GLFWwindow* window, double currentTime) {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	if (keyboard[GLFW_KEY_LEFT])	// z tengely+ (óramutató ellentét)
		cameraAngle += HORIZONTAL_SPEED;
	if (keyboard[GLFW_KEY_RIGHT])	// z tengely- (óramutató megyegyező)
		cameraAngle -= HORIZONTAL_SPEED;
	if (keyboard[GLFW_KEY_UP])		// z tengelyen fel
		cameraZ += VERTICAL_SPEED;
	if (keyboard[GLFW_KEY_DOWN])	// z tengelyen le
		cameraZ -= VERTICAL_SPEED;

	updateCameraMat();

	float lightCircleAngle = (float)(currentTime * LIGHT_SPEED);
	lightPos.x = LIGHT_R * cos(lightCircleAngle);
	lightPos.y = LIGHT_R * sin(lightCircleAngle);
	lightPos.z = 0.0f;

	// KOCKÁK
	glUseProgram(program[CubeProgram]);
	glBindVertexArray(VAO[VAOCubeData]);

	glUniform3fv(lightPosLoc, 1, value_ptr(lightPos));
	glUniform3f(cubeColorLoc, 1.0f, 1.0f, 1.0f);

	for (int i = 0; i < 3; i++) {
		matModel = translate(mat4(1.0f), cubePoints[i]);
		mat3 inverseTransposeMatrix = mat3(inverseTranspose(matModel));

		glUniformMatrix4fv(locationMatModel, 1, GL_FALSE, value_ptr(matModel));
		glUniformMatrix3fv(inverseTransposeLoc, 1, GL_FALSE, value_ptr(inverseTransposeMatrix));

		glDrawArrays(GL_TRIANGLES, 0, sizeof(cubeData) / (6 * sizeof(GLfloat)));
	}

	// NAP
	glUseProgram(program[SunProgram]);
	glBindVertexArray(VAO[VAOSunData]);

	//mat4 sunModel = translate(mat4(1.0f), lightPos);
	//glUniformMatrix4fv(sunMatModelLoc, 1, GL_FALSE, value_ptr(sunModel));
	glUniform3fv(sunColorLoc, 1, value_ptr(lightDiffColor));

	//glDrawArrays(GL_TRIANGLES, 0, sunDataCount);

	matModel = translate(mat4(1.0f), lightPos);

	// Forgatás a saját tengelye körül, hogy látszódjon a textúra mozgása
	matModel = rotate(matModel, (float)currentTime, vec3(0, 0, 1));
	glUniformMatrix4fv(sunMatModelLoc, 1, GL_FALSE, value_ptr(matModel));

	glActiveTexture(GL_TEXTURE0);
	glBindTexture(GL_TEXTURE_2D, texture[SunTexture]);
	glUniform1i(sunTexLoc, 0);

	glBindVertexArray(VAO[VAOSunData]);
	glDrawArrays(GL_TRIANGLES, 0, (GLsizei)sunData.size() / 5);

}

void framebufferSizeCallback(GLFWwindow* window, int width, int height) {
	windowWidth = glm::max(width, 1);
	windowHeight = glm::max(height, 1);
	aspectRatio = (float)windowWidth / (float)windowHeight;
	float nearClipPlane = 0.1f;
	float farClipPlane = 200.0f;

	glViewport(0, 0, windowWidth, windowHeight);
	matProjection = perspective(
		radians(55.0f),		// Látószög 
		aspectRatio,
		nearClipPlane,
		farClipPlane
	);

	glUseProgram(program[CubeProgram]);
	glUniformMatrix4fv(locationMatProjection, 1, GL_FALSE, value_ptr(matProjection));

	glUseProgram(program[SunProgram]);
	glUniformMatrix4fv(sunMatProjectionLoc, 1, GL_FALSE, value_ptr(matProjection));
}

void keyCallback(GLFWwindow* window, int key, int scancode, int action, int mods) {
	// ESC
	if ((action == GLFW_PRESS) && (key == GLFW_KEY_ESCAPE))
		glfwSetWindowShouldClose(window, GLFW_TRUE);

	if (action == GLFW_PRESS)
		keyboard[key] = GL_TRUE;
	else if (action == GLFW_RELEASE)
		keyboard[key] = GL_FALSE;

	// L : megvilágítás ki és be kapcsolása
	if ((action == GLFW_PRESS) && (key == GLFW_KEY_L)) {
		lightSwitch = !lightSwitch;

		glUseProgram(program[CubeProgram]);
		glUniform1i(lightSwitchLoc, lightSwitch ? 1 : 0);

		cout << "Vilagitas: " << (lightSwitch ? "BE" : "KI") << endl;
	}

}

void cursorPosCallback(GLFWwindow* window, double xPos, double yPos) {
}

void mouseButtonCallback(GLFWwindow* window, int button, int action, int mods) {
}


int main(void) {

	init(3, 3, GLFW_OPENGL_COMPAT_PROFILE);

	glClearColor(0.2f, 0.2f, 0.2f, 0.0f);

	initShaderProgram();

	framebufferSizeCallback(window, windowWidth, windowHeight);

	setlocale(LC_ALL, "");
	cout << "ESC\t\tKilépéds" << endl;
	cout << "Bal nyíl:\tKamera forgatás z tengely körül balra" << endl;
	cout << "Jobb nyíl:\tKamera forgatás z tengely körül jobbra" << endl;
	cout << "Fel nyíl:\tKamera mozgatás z tengelyen fel" << endl;
	cout << "Le nyíl:\tKamera mozgatás z tengelyen le" << endl;
	cout << "L:\t\tVilágítás ki/be kapcsolása" << endl << endl;

	while (!glfwWindowShouldClose(window)) {
		display(window, glfwGetTime());
		glfwSwapBuffers(window);
		glfwPollEvents();
	}

	cleanUpScene(EXIT_SUCCESS);

	return EXIT_SUCCESS;
}
