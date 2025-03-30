import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

data = np.array([[80, 50], [30, 10], [70, 40], [10, 5]])
labels = np.array([1, 0, 1, 0])

scaled_data = scaler.fit_transform(data)
model.fit(scaled_data, labels, epochs=50, verbose=0)

def predict_energy_load(solar, wind):
    scaled_input = scaler.transform([[solar, wind]])
    return model.predict(scaled_input)[0][0]

print(predict_energy_load(60, 30))
