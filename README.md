# Bird_Calls
### 📌 Objective: The purpose of this experiment is to train a machine learning algorithm, in this case a 2D convolutional network (CNN), to produce predictions of call types of bird call recordings. The resulting prediction probabiltiies will be compositional data, or in other words, sum to 1. The species used for this iteration was the Downy Woodpecker (*Dyrobates pubescens*), whose characteristic calls can broadly be separated into three classes: pik, drum, and laugh. 

## 1. Data
### The data used for training this 2D-CNN model used in this experiment was gathered from the [Macauly Library repository](https://www.macaulaylibrary.org/?doing_wp_cron=1723063926.9250679016113281250000). After visually inspecting the calls on the Macauly website, samples with the distinct calls within the 1-2s mark of the recording were set aside to be used as training data. The `.wav` files were then cropped, converted into spectrograms, and converted into images to be used to train the CNN. 

## 2. Train
### The cropped sample spectrograms then served as the training data for the model.

## 3. Predict 
### After achieving a respectable accuracy rate (>90%) on the validation data, the model was used to predict on unobserved recordings to produce compositional representations of the call information. The resulting data were saved and used for visualization. 

## 4. Visualize 
### The compositional prediction data were then joined with the associated recording meta-data to create a Shiny application to visualize the call distribution across North America, along with climatic, geographic, and demographic information to observe any potentially obvious relationships.  
