English version, Romanian version is below (Versiunea in Română e mai jos)

### Predicting Used Car Prices

George Ungureanu

Hello! Welcome to my Machine Learning project that predicts the price of a car based on its characteristics.

#### 1 Why do we need such a model?

Every person needs guidance when they want to post a for-sale listing, so people look on the platform and take into consideration several prices from other cars similar to the one they want to sell.

Today I built a regression model (it estimates the price) that "looked at" many cars (~56,000) and estimates the price in correlation with all the examples received, thus providing a better approximation for users who want to list their car for sale.

#### 2 Performance and Costs

The model offers very good performance for cheaper cars. It has a deviation of ~830 for cars cheaper than $35,000, ~8,790 for more expensive cars (over $35,000), with a few large exceptions, being worse than a guess for these.

#### 3 Data Presentation

The data received comes from a CSV that contains the following columns:

**make, model, price_usd, car_age, condition, kilometers, fuel_type, volume, transmission, drive_unit, segment, is_luxury_brand, km_per_year, new**

The most significant column is: car_age

#### 4 Limitations

One of the model's limitations is the lack of examples for expensive or luxury cars; the features present in the dataset are fairly general and can be shared by a wide variety of cars. Therefore, the model does not have special features (such as power, chassis material, engine, lights, wheels, transmission details, etc.) to be able to distinguish a very expensive car from one with an average price, which is why it is focused on the most common cars, those with an average price.

#### 5 Conclusion

The model demonstrated good functionality for common cars in the dataset, which gives the impression that it overfitted, but in reality there is a small percentage of luxury/sports cars and details that could indicate their components in the dataset so that it can detect them.

The next steps are:

a much larger and more detailed dataset to increase the quality of the responses.

testing more models to increase performance

* There is a `model_testing.py` file to run the model on a dataset.




### Prezicerea preturilor de masini second-hand.

Ungureanu George

Salutare! Bine ati venit la proiectul meu de Machine Learning care prezice pretul unei masini conform careacteristicilor acesteia.

#### 1 De ce avem nevoie de un astfel de model?

Fiecare om are nevoie de o orientare atunci când vrea să posteze un anunț de vânzare, așadar oamenii se uită pe platformă și iau în considerare mai multe prețuri de la alte mașini similare cu cea pe care ar vrea să o vândă.

Astăzi am făcut un model de regresie (estimează prețul) care "s-a uitat" la mai multe mașini (~56.000) și estimează prețul în corelație cu toate exemplele primite, astfel oferind o aproximare mai bună utilizatorilor care vor să își pună mașina la vânzare.

#### 2 Performante si Costuri

Modelul oferă performanțe foarte bune pentru mașinile mai ieftine. Are o deviație de ~830 pentru mașinile mai ieftine decât 35.000 dolari, ~8790 pentru mașinile mai scumpe (peste 35.000) cu câteva excepții mari, fiind mai slab decât o ghicire pentru acestea.

#### 3 Prezentarea datelor

Datele primite provin dintr-un csv care contine uramtoarele coloane

**make, model, price_usd, car_age, condition, kilometers, fuel_type, volume, transmission, drive_unit, segment, is_luxury_brand, km_per_year, new**

Cele mai semnficiativa coloana fiind : car_age

#### 4 Limitari

Una dintre limitările modelului este lipsa de exemple pentru mașini scumpe sau de lux, caracteristicile prezente în setul de date sunt destul de generale și pot să fie însușite de o varietate mare de mașini. Așadar modelul nu are caracteristici speciale (precum putere, material șasiu, motor, lumini, roți, detalii transmisie etc.) pentru a putea diferenția o mașină foarte scumpă de una cu preț mediu, motiv pentru care acesta este axat pe mașinile cele mai comune, cele cu preț mediu.

#### 5 Concluzie

Modelul a dovedit o funcționalitate bună în cazul mașinilor comune din setul de date, ce oferă percepția că a dat overfit, dar în realitate există un procent mic de mașini de lux/sport și detalii care ar putea indica componentele acestora în setul de date pentru a putea să le detecteze.

Următorii pași sunt:

un set de date mult mai extins și mai detaliat pentru a mări calitatea răspunsurilor.

testarea mai multor modele pentru a mări performanța

* există un fișier model_testing.py pentru a rula modelul pe un set de date.
