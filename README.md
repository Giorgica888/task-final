dolari

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
