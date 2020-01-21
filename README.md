# Flask-Application-for-Goa-Monuments-Prediction

## Application deployed on Google Cloud Platform for classifying different monuments of Goa

### Problem Statement:

Goa is a major tourist destination which pulls thousands of tourists every year. Goa is known for its beautiful beaches and hospitality. There are a number of monuments and landmarks depicting the cultural, history and development of Goa. Due to high inflow of domestic as well as international tourists, the manpower required to guide the tourist on these landmark is not sufficient and sometimes lack in the information that need to be given and highlighted to the tourist. 

Hence there must be a mobile application which renders information about the monument or landmark just by taking their live pictures as inputs. In other word, the application should allow the user to click a photograph and based on the picture it should display information about the monument/landmark. 

#### Website: https://goaml-265511.appspot.com/ (Deployed on Google Cloud Platform)

![Basilica_of_Bom_Jesus_-_Old_Goa](https://user-images.githubusercontent.com/34116562/72215966-9445c180-3540-11ea-9d09-97b193d42eb5.jpg)

### Source Code:
#### GitHub: https://github.com/prateeksawhney97/Goa-Monument-Prediction

### Solution: 

A web application is developed using Flask and deployed on Google Cloud Platform. The user can upload the image of the monument and click the predict button. The background machine learning model will predict its name and various other details. The user can navigate to the Source Code and also the GitHub profile.

### Monuments Included:

1. Ajoba Temple Goa
2. Shanta Durga Temple
3. Fort Aguada
4. Our Lady of the Immaculate Conception Church, Goa
5. Viceroys Arch, Goa


### Screenshots:

![Screenshot from 2020-01-21 19-43-05](https://user-images.githubusercontent.com/34116562/72812295-43904000-3c87-11ea-975e-73451f8c882f.png)
![Screenshot from 2020-01-21 19-43-25](https://user-images.githubusercontent.com/34116562/72812300-44c16d00-3c87-11ea-8e6b-c5b14d744929.png)
![Screenshot from 2020-01-21 19-43-39](https://user-images.githubusercontent.com/34116562/72812304-468b3080-3c87-11ea-997c-3a8062b863f8.png)
![Screenshot from 2020-01-21 19-43-42](https://user-images.githubusercontent.com/34116562/72812313-47bc5d80-3c87-11ea-81a3-95153a819f99.png)
![Screenshot from 2020-01-21 19-43-51](https://user-images.githubusercontent.com/34116562/72812324-4c811180-3c87-11ea-816a-78a3b23f0eae.png)


### Model Architecture Used:



| Layer         		|     Output Shape	        					| Param |
|:---------------------:|:---------------------------------------------:|:---------------------------------------------:| 
| Convolution Layer 1   	| (None, 118, 126, 24 	|  1824 |
| Convolution Layer 2	    | (None, 57, 61, 36)    									|  21636 |
| Convolution Layer 3		| (None, 27, 29, 48) |      43248 									|
| Convolution Layer 4				| (None, 25, 27, 64)      |  		27712							|
|	Convolution Layer 5					|		(None, 23, 25, 64)			|					36928		|
| Dropout Layer 1              |     (None, 23, 25, 64)   |   0    |
| Flatten Layer 1              |        (None, 36800)  |  0    |
|	Dense Layer 1				|		(None, 100)		|		3680100	|
| Dense Layer 2		| (None, 50)     |   	5050								|
|	Dense Layer 3				|		(None, 10)						|   510  |
| Dense Layer 4		| (None, 5)   |     				55			|

- Total params: 3,817,063
- Trainable params: 3,817,063
- Non-trainable params: 0


##### Accuracy:  0.9940
##### Validation Accuracy: 0.7381
