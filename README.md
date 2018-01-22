# Sentiment_Prediction_from_Movie_Reviews
Sentiment is predicted as either positive or negative on the IMDB dataset.

Dataset-IMDB dataset of 50,000 movie reviews.
Words are converted into real-valued vector space using Embedding layer of Keras.

2 models are build-
### Simple Multilayer Perceptron Model

* Embedding layer as the input layer,word vector size of 32.
* Flatten the Embedding Layer.
* Dense hidden layer of 250 units with a rectifier activation function.
* Output layer with one neuron and will use a sigmoid activation function.

### 1D Convolutional Neural Network

* Embedding layer as the input layer,word vector size of 32.
* 1D conv layer ,relu activation,filters 32\*3\*3.
* Maxpooling layer .
* Flatten the layer 
* Dense hidden layer of 250 units with a rectifier activation function.
* Output layer with one neuron and will use a sigmoid activation function.

Network was trained on Amazon EC2 instances using gpu of g2.2x large. 
