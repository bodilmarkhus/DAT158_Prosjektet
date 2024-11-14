import gradio as gr
import tensorflow as tf
import numpy as np

# Importing the trained model
model = tf.keras.models.load_model('C:/Users/arege/Dokumenter/Dataingenior Bachelor/DAT158/Machine Learning/Big Project/fruitoo_v2.keras')

# Names of all the fruit classifications
class_names = ['Apple', 'Banana', 'Starfruit', 'Guava', 'Kiwi', 'Mango', 'Orange', 'Peach', 'Pear', 'Persimon', 'Dragonfruit', 'Plum', 'Pomegranate', 'Tomato', 'Canteloupe']

def run_fruitoo(fruit):
    
    # Preprocessing the image
    fruit_array = tf.keras.preprocessing.image.smart_resize(
        fruit,
        (180, 180),
    )

    # The input image as an array for processing through the model
    fruit_array = tf.expand_dims(fruit_array, 0)
    
    # The actual predicting on the input image
    predictions = model.predict(fruit_array)
    score = tf.nn.softmax(predictions[0])

    # Return the predition results
    return (
        "I, the great Fruitoo, predict with a {:.2f} percent confidence that this is an image of a {}!"
        .format(100 * np.max(score), class_names[np.argmax(score)])
    )

# Website interface
website = gr.Interface (
    fn = run_fruitoo, 
    inputs = gr.Image(),
    outputs = gr.Label(),
)

# Start the website for the image prediction
website.launch()