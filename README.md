# Algoritmer og datastrukturer
Repository for teori og øvinger til Algoritmer og datastrukturer - TDT 4120.

* Trykk [her](http://www.markdowntopdf.com/) om du ønsker å laste ned markdown-dokumentet som PDF

# Table of Contents
1. [Forelesning 1 - *Problem og algoritmer*](#of1)
2. [Forelesning 2 - *Datastrukturer*](#of2)
3. [Forelesning 3 - *Splitt og hersk*](#of3)
4. [Forelesning 4 - *Rangering i lineær tid*](#of4)
5. [Forelesning 5 - *Rotfaste trestrukturer*](#of5)
6. [Forelesning 6 - *Dynamisk programmering*](#of6)
7. [Forelesning 7 - *Grådige algoritmer*](#of7)
8. [Forelesning 8 - *Traversering av grafer*](#of8)
9. [Forelesning 9 - *Minimale spenntrær*](#of9)
10. [Forelesning 10 - *Korteste vei fra én til alle*](#of10)
11. [Forelesning 11 - *Korteste vei fra alle til alle*](#of11)
12. [Forelesning 12 - *Maksimal flyt*](#of12)
13. [Forelesning 13 - *NP-kompletthet*](#of13)
14. [Forelesning 13 - *NP-komplette problemer*](#of14)



##Forelesning 1 - Problem og algoritmer <a name="of1"></a>



**Induksjon**: Anta at en gitt *løkke-invariant* er sann før en iterasjon, og vis deretter at den er sann etterpå.

**O**: øvre grense.

**Ω**: nedre grense.

**Θ**: øvre og nedre grense.

###Insertion sort
**Input**: En liste *n*-elementers liste.

**Output**: En sortert permutasjon av *Input*


```python
def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        
        # Plasserer A[j] inn i den sorterte sublisten [0..j-1]
        i = j-1
        while i>=0 and A[i] > key:
        
            # Flytter hvert element en til høyre, så lenge key<A[i]
            A[i+1] = A[i]
            i -= 1
            
        # Plasserer key på riktig plass
        A[i+1] = key
```
 **Løkke-invariant**: I starten av hver iterasjon av *for*-løkken består `A[:j - 1]` av de originale elementene i `A[:j - 1]`, i sortert rekkefølge
 
>  Kommentar til selv: Les i boken

**Kjøretid**: 

* Best-case:
* Worst-case:
* Average-case:

 
 

 
 
 
 
## Forelesning 2 - Datastrukturer <a name="of2"></a>


**LIFO**: **L***ast-***I***n-***F***irst-***O***ut*

**FIFO**: **F***irst-***I***n-***F***irst-***O***ut*


### Amortisert analyse:
I en amortisert analyse, regner vi ut den gjennomsnittlige tiden for å utføre en sekvens av datastrukturoperasjoner over alle operasjonene som ble utført. Med amortisert analyse kan vi vise at gjennomsnittskostnaden for en operasjon er liten, hvis vi regner ut gjennomsnitt over en sekvens av operasjoner, selv om en enkelt operasjon i sekvensen kan være dyr. Amortisert analyse skiller seg fra gjennomsnittsanalyse ved at sannsynligheten ikke er involvert – En amortisert analyse garanterer gjennomsnittlig ytelse for hver operasjon i verste tilfelle.

Vi vil definere en *load-factor* α til en ikke-tom tabell *T* til å være `α = elements/T.length`

* **Tabell-ekspansjon**:
	* En tabell er full når enten alle plassene i tabellen er i bruk eller når *load-factoren* α = 1
	* Dersom vi skal innsette et element i en full liste, må vi ekspandere listen, ved å lage en ny liste med fler plasser enn den gamle og kopiere over alle de gamle elementene.
	* Så en gang i blant dersom α = 1 vil innsetting av et element bruke mye lenger tid enn *O(1)*, og dette tar vi med i beregningen med **amortisert analyse**

	```sudocode
	TABLE-INSERT(T,x):
		if T.size == 0:
			allocate T.table with 1 slot
			T.size = 1
			
		if T.num == T.size:
			allocate new-table with 2 * T.size slots
			insert all items in T.table into new-table
			free T.table
			T.table = new-table
			T.size = 2 * T.size
			
		insert x into T.table
		T.num = T.num + 1
	
	```
	


**Dynamisk tabell**: Tabell som blir utvidet dersom alle plassene er tatt eller *load-factor* α = 1


### Lenket liste
* Finnes
	* *Enkle* lenkede lister
	* *Doble* lenkede lister
	* *Sykliske* lenkede lister


```python
class LinkedList:
	def __init__(self):
   		self.head = None
       def isEmpty(self):
    	return self.head == None
   def add(self,item):
    	temp = Node(item)
    	temp.setNext(self.head)
   	 	self.head = temp
   	 
 	def search(self,item):
   		current = self.head
    	found = False
    	while current != None and not found:
        	if current.getData() == item:
            	found = True
        	else:
            	current = current.getNext()

    	return found
    	
    def remove(self,item):
    	current = self.head
    	previous = None
    	found = False
    	while not found:
        	if current.getData() == item:
            	found = True
        	else:
            	previous = current
            	current = current.getNext()

    	if previous == None:
        	self.head = current.getNext()
    	else:
        	previous.setNext(current.getNext())

```
* **Kjøretider** *(antar enkel lenket liste)*:
	*  Innsetting i starten: *O(1)*
	*  Innsetting i slutten: *O(n)*
	*  Oppslag: *O(n)*
	*  Slette element: *Oppslagstid* + *O(1)* = *O(n)*

	

### Queue
* *FIFO-struktur*

```python
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

```

+ Operasjonene bruker *O(1)* tid 


### Stack
* *LIFO-struktur*

```python
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

```
 * Operasjonene bruker *O(1)* tid 



## Forelesning 3 - Splitt og hersk <a name="of3"></a>


**Designmetoden i splitt og hersk**:

* **Splitt** problemet inn i subproblemer som er mindre instanser av det samme problemet.
* **Hersk** subproblemene ved å løse dem rekursivt. Hvis et subproblems størrelse er lite nok, løs subproblemene på en rett frem måte.
* **Kombiner** løsningene på subproblemene inn i løsningen på problemet i utgangspunktet

Vi deler opp problemet helt til vi kommer til minste mulige instans av problemet, så sier vi at rekursjonen har ”bottoms out” og vi har kommet til base case og får resultatet når vi kombinerer løsningene.* *Mangler `MAXIMUM-SUBARRAY (kap. 4.1)`*
###Binærsøk:
**Input**: En liste A, pivot-element *p*, slutt-element *r* og elementet *v* som vi søker etter

**Output**: Indeks *i* slik at `A[i] = v`

*Rekursiv løsning:*

```python
def Recursive_binary_search(A, p, r, v):
    i = p
    if p < r:
        mid = (p+r)//2
        if v <= A[mid]:
            i = Recursive_binary_search(A,p,mid,v)

        else:
            i = Recursive_binary_search(A,mid+1,r,v)
    return i


```

*Iterativ løsning:*

```python
def Iterative_binary_search(A, p, r, v):
    while p < r:
        mid = (p+r)//2

        if v <= A[mid]:
            r = mid

        else:
            p = mid + 1

    return p

```

> Dersom det finnes flere forekomster av *v* i A vil Bisect returnere indeksen til forekomsten lengst til venstre, altså den **laveste** indeksen

**Kjøretid**:

* Θ(*lg n*)


### Merge sort

**Input**: Liste A usortert

**Output**: Liste bestående av elementer fra `A[p..r]` i sortert rekkefølge
> Sammenligningsbasert sorteringsalgoritme

Algortimen foregår slik:

1. **Splitt:** Del opp-steget regner kun ut midten av listen, som tar konstant tid. Da blir `D(n) = Θ(1)`.
2. **Hersk:** Vi løser rekursivt to delproblemer, hver på størrelse n/2, som bidrar med `2*T(n/2)` kjøretid på algoritmen.
3. **Kombiner:** Merge-prosedyren bruker Θ(n) tid på en n-element liste, så derfor blir `C(n) = Θ(n)`Når vi adderer funksjonene D(n) og C(n) for merge-sort analysen, vil summen av (n) og  (1), bli (n). Når vi summerer det igjen sammen med 2T(n/2)-delen fra ”hersk”-seget gir rekurrensen for verste kjøretiden T(n) for merge-sort:

`T(n) = 2T(n/2) + Θ(n)     if  n > 1, else O(1)`

> Dersom vi bruker master-teoremet (**Kap. 4**) så kan vi vise at `T(n) = (n lg n)`.


```python
def merge_sort(A):
    if len(A)>1:
        q = len(A)//2
        lh = merge_sort(A[:q])
        rh = merge_sort(A[q:])
        return merge(lh,rh)

    return A


def merge(lh,rh):
    res = []
    i = 0
    j = 0

    while i<len(lh) and j<len(rh):
        if lh[i] < rh[j]:
            res.append(lh[i])
            i+=1

        else:
            res.append(rh[j])
            j+=1

    if i<len(lh): res.extend(lh[i:])
    if j<len(rh): res.extend(rh[j:])
    
    return res

```


### Quicksort

Quicksort, som *Merge-sort*, benytter seg av _splitt-og-herk paradigmet. Her er de tre splitt og hersk-stegene for å sortere en subliste `A[p..r]`:





## Forelesning 4 - Rangering i lineær tid <a name="of4"></a>


## Forelesning 5 - Rotfaste trestrukturer <a name="of5"></a>


## Forelesning 6 - Dynamisk programmering <a name="of6"></a>


## Forelesning 7 - Grådige algoritmer <a name="of7"></a>


## Forelesning 8 - Traversering av grafer <a name="of8"></a>


## Forelesning 9 - Minimale spenntrær <a name="of9"></a>


## Forelesning 10 - Korteste vei fra én til alle <a name="of10"></a>


## Forelesning 11 - Korteste vei fra alle til alle <a name="of11"></a>


## Forelesning 12 - Maksimal flyt <a name="of12"></a>


## Forelesning 13 - NP-kompletthet <a name="of13"></a>


## Forelesning 14 - NP-komplette problemer <a name="of14"></a>
