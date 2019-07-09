# Reddit

## libs

This is the main libs used in this project:

* praw
* vcrpy
* unittest

## problem
I never used Reddit and I don't know well the behavior still confuse me with the terms 

## solution
El proyecto tiene un POPO donde vamos dejando la informaciòn que vamos procesando (**RedditModel**). Por falta de tiempo
he escrito una sola clase,(como comentare mas adelante creo que tendria que haber dos partes una de servidor o tra cliente)
cargo la configuración de un fichero init , genero una conexion a  la api usando **praw** y voy procesando el contenido.

Para hacer la ordenacion y he usado una lamda por comodida , con el volumen no he notado nada de mejora que con el modo iterativo

Escribo todo los popo que he generado en una lista y voy recorriendo la lista y generando los kpi y escribiendo en un fichero de txt
### considrations
Al no tener un sistema asincrono no he generado la parte cliente y la parte server

## bonus track
1. How can you integrate your solution with a central scheduler?

No i can't use luigi in my mac.. I'm trying to use docker and pip install ..... but don't work

2. How would you handle restarts and retries of failed tasks?

The principal idea is to generate a server part, this part read the information in an API create a model and send the queque part. 
The other part is a consumer this part reading a topic check the id (in my case an auto-increment number but you can use the id from the post, subreddit) consume the information and generates the kpi and save in persistence layer.  basically the Kappa architecture 
3. How can you containerize the pipeline?

attached my docker file
4. How can you automate deployment and testing of your solution?

the docker exit a script when building the container run the test if the test fail don't build the container  
