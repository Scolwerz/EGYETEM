import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt


# Az osztályok száma (0-9 számjegyek)
num_classes = 10

# Bemeneti kép mérete:
# 28x28 pixel, 1 színcsatorna (szürkeárnyalatos)
input_shape = (28, 28, 1)


# -----------------------------
# ADATOK BETÖLTÉSE
# -----------------------------

# Az MNIST adatbázis betöltése
# x_train -> tanító képek
# y_train -> tanító címkék
# x_test  -> teszt képek
# y_test  -> teszt címkék
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()


# -----------------------------
# ADATOK NORMALIZÁLÁSA
# -----------------------------

# A pixelértékek eredetileg 0-255 között vannak
# Átskálázzuk őket 0-1 közé
# Ez gyorsabb és stabilabb tanítást eredményez
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255


# -----------------------------
# DIMENZIÓ HOZZÁADÁSA
# -----------------------------

# A CNN modellek 4D bemenetet várnak:
# (minta_db, magasság, szélesség, csatornák)

# Az expand_dims hozzáad egy plusz dimenziót
# így:
# (60000, 28, 28)
# ->
# (60000, 28, 28, 1)

x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)


# -----------------------------
# INFORMÁCIÓK KIÍRÁSA
# -----------------------------

# A train adatok shape-jének kiírása
print("x_train shape:", x_train.shape)

# Train minták száma
print(x_train.shape[0], "train samples")

# Test minták száma
print(x_test.shape[0], "test samples")


# -----------------------------
# ELSŐ 9 KÉP MEGJELENÍTÉSE
# -----------------------------

# Az első 9 kép kirajzolása
for i in range(9):

    # 3x3-as rács létrehozása
    plt.subplot(330 + 1 + i)

    # Kép megjelenítése szürkeárnyalatos módban
    plt.imshow(x_train[i], cmap=plt.get_cmap('gray'))

# Az összes kép megjelenítése
plt.show()


# -----------------------------
# ONE-HOT ENCODING
# -----------------------------

# A címkéket bináris vektorokká alakítjuk
#
# Példa:
# 5
# ->
# [0,0,0,0,0,1,0,0,0,0]

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


# -----------------------------
# MODELL LÉTREHOZÁSA
# -----------------------------

# Sequential modell:
# a rétegek egymás után következnek
model = keras.Sequential(

    [

        # Bemeneti réteg
        keras.Input(shape=input_shape),

        # -------------------------------------------------
        # ELSŐ KONVOLÚCIÓS RÉTEG
        # -------------------------------------------------
        #
        # 32 szűrő
        # 3x3-as kernel
        # ReLU aktiváció
        #
        # A modell egyszerű mintázatokat tanul:
        # élek, vonalak, alakzatok
        layers.Conv2D(
            32,
            kernel_size=(3, 3),
            activation="relu"
        ),

        # -------------------------------------------------
        # MAX POOLING
        # -------------------------------------------------
        #
        # Lekicsinyíti a feature mapeket
        # Csökkenti a számítási igényt
        # Segít a zaj csökkentésében
        layers.MaxPooling2D(pool_size=(2, 2)),


        # -------------------------------------------------
        # MÁSODIK KONVOLÚCIÓS RÉTEG
        # -------------------------------------------------
        #
        # 64 szűrő
        # Komplexebb minták felismerése
        layers.Conv2D(
            64,
            kernel_size=(3, 3),
            activation="relu"
        ),

        # Második pooling réteg
        layers.MaxPooling2D(pool_size=(2, 2)),


        # -------------------------------------------------
        # FLATTEN RÉTEG
        # -------------------------------------------------
        #
        # A 2D feature mapeket 1D vektorrá alakítja
        layers.Flatten(),


        # -------------------------------------------------
        # DROPOUT
        # -------------------------------------------------
        #
        # A neuronok 50%-át véletlenszerűen kikapcsolja
        # Segít az overfitting csökkentésében
        layers.Dropout(0.5),


        # -------------------------------------------------
        # KIMENETI RÉTEG
        # -------------------------------------------------
        #
        # 10 neuron:
        # minden számjegyhez egy
        #
        # Softmax:
        # valószínűségeket ad vissza
        layers.Dense(
            num_classes,
            activation="softmax"
        ),
    ]
)


# -----------------------------
# MODELL ÖSSZEFOGLALÓ
# -----------------------------

# Kiírja:
# - rétegek típusa
# - paraméterszámok
# - kimeneti shape-ek
model.summary()


# -----------------------------
# TANÍTÁSI PARAMÉTEREK
# -----------------------------

# Egyszerre feldolgozott minták száma
batch_size = 128

# Epochok száma
# (hányszor megy végig a teljes train adathalmazon)
epochs = 1


# -----------------------------
# MODELL FORDÍTÁSA
# -----------------------------

model.compile(

    # Többosztályos osztályozási veszteségfüggvény
    loss="categorical_crossentropy",

    # Optimalizáló algoritmus
    optimizer="adam",

    # Kiértékelési metrika
    metrics=["accuracy"]
)


# -----------------------------
# MODELL TANÍTÁSA
# -----------------------------

model.fit(

    # Train képek
    x_train,

    # Train címkék
    y_train,

    # Batch méret
    batch_size=batch_size,

    # Epochok száma
    epochs=epochs,

    # A train adatok 10%-a validációra lesz használva
    validation_split=0.1
)


# -----------------------------
# MODELL KIÉRTÉKELÉSE
# -----------------------------

# Kiértékelés a teszt adatokon
score = model.evaluate(x_test, y_test, verbose=0)


# -----------------------------
# EREDMÉNYEK KIÍRÁSA
# -----------------------------

# Loss érték kiírása
print("Test loss:", score[0])

# Accuracy kiírása
print("Test accuracy:", score[1])