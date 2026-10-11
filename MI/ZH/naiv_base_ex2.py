from numpy import loadtxt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

dataset = loadtxt('emailtexts.csv', delimiter=',') #sor: "Free money now!!!,1"
X = dataset[:,0]
y = dataset[:,1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Szöveg vektorizálás és modell tanítása
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

# predictoin
y_pred = model.predict(X_test_vec)
print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))


user_input = input('Írj be egy üzenetet: ')

if user_input:
    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)[0]

    if prediction == '1': print('Ez valószínűleg SPAM üzenet!')
    else:               print('Ez egy normális (HAM) üzenet.')
