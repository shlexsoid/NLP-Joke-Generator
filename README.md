# NLP-Joke-Generator

## Directory structure
* Result.pdf
This file describes our models and results
* main.py
We connected to VK API with vk_api library. It helped us to get russian jokes.
* temp_data.csv
Russian jokes dataset that we got as a result of parsing with vk_api.
* shortjokes.csv
English jokes dataset.
* EnJokes.ipynb
Jupyter notebook where we trained our model to generate some english jokes
* Res_jokes.ipynb
Jupyter notebook where we trained our model to generate some russian jokes



Missed credential.py for main.py. This file contains token for vk api. It looks like
```
token = 'yourtoken'
```
