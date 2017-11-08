# Algoritmer og datastrukturer
Repository for teori og øvinger til Algoritmer og datastrukturer - TDT 4120.

## Liste over forelesninger
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


* Trykk [her](http://www.markdowntopdf.com/) om du ønsker å laste ned markdown-dokumentet som PDF


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


**LIFO**: *Last-In-First-Out*

**FIFO**: *First-In-First-Out*


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

**Quicksort**, som *Merge-sort*, benytter seg av _splitt-og-herk paradigmet. Her er de tre splitt og hersk-stegene for å sortere en subliste `A[p..r]`:

* **Splitt:** Del opp (omarranger) listen `A[p..r]` til to (mulig tomme) sublister `A[p..q-1]` og `A[q+1..r]`, slik at hvert element i `A[p..q-1]` er mindre eller lik A[q], som igjen er mindre eller lik hvert element i `A[q+1..r]`. Regn ut indeksen q som en del av oppdelings-prosedyren.
* **Hersk:** Sorter de to listene `A[p..q-1]` og `A[q+1..r]` med rekursive kall til quicksort.
* **Kombiner:** Fordi sublistene allerede er sortert, trengs det ikke å gjøres noe for å kombinere dem: hele listen `A[p..r] er nå sortert.


```python
def Quicksort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        Quicksort(A, p, q-1)
        Quicksort(A, q+1, r)


def Partition(A, p, r):
	# Partition jobber slik
	# ≤x | ≥x | x
	
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    # Listen blir slik slik:
    # ≤x | x | ≥x
    return i+1
    
```

*Partition* velger alltid et element `x = A[r]` som pivot-element som deler opp listen `A[p..r]`. Når prosedyren kjører, deler den opp listen i fire (mulig tomme) regioner. På starten av hver iterasjon av for-løkken linje 6-9, tilfredsstiller regionene visse egenskaper. Vi kaller disse egenskapene for en *løkke-invariant*:

1.	`If p ≤ k ≤ i, then A[k] ≤ x`
2. `If	i + 1 ≤ k ≤ j – 1, then A[k] > x`
3. `If  k ==  r, then A[k] = x`> På begynnelsen av hver iterasjon av **for**-løkken på linje 6-9, for enhver liste indeks *k*

* *Quicksort* er **ikke stabil**, da den ikke beholder den relative rekkefølgen til like elementer under sorteringen av listen.

**Under Partition:**

Listeelementet `A[r]` blir pivot-elementet *x*. Lysegrå elementer er alle i den første partisjonen med verdiermindre enn *x*. De mørkegrå elementene er i den andrepartisjonen og er alle større enn *x*. De ufargede elementene er enda ikke plassert i en partisjon.

**Bevis av løkke-invariant:**

1. **Initialisering:** Før den første iterasjonen av løkken, `i = p – 1` og           `j = p`. Fordi det ikke ligger noen verdier mellom *p* og *i*           og ingen verdier mellom `i + 1` og `j – 1`, de to første           betingelsene på løkke-invarianten er tilfredsstilt.2. **Vedlikehold:** Vi ser på to tilfeller, avhengig på resultatet av testen           på linje *7*. Enten så er `A[ j ] > x` eller `A[ j ] ≤ x`, løkkeinvarianten            er fortsatt tilfredsstilt.3. **Terminering:** Ved terminering, `j == r`. Da er hvert eneste element i            listen i en av de tre betingelsene i løkke-invarianten Og vi har            partisjonert elementene til 3 sett; `A[..] ≤ x`, ` A[..] > x ` og ` A[r] = x`> De to siste linjene i Partition avslutter prosedyren ved å bytte pivot elementet A[r] med A[i+1]


**Kjøretid:**

* *Worst-case:* Θ(*n^2*)
* *Forventet kjøretid:*
	* Rekursjonstre med dybde Θ(*lg n*) med O(*n*) arbeid på hvert nivå
	* `T(n) = 2T(n/2) + Θ(n) = Θ(n lg n)` 

	
> 	Fra *master-teoremet (Th. 4.1) 	


### Randomized-Quicksort
Samme algoritme som *quicksort*, bortsett fra at pivot-elementet byttes ut med et tilfeldig element fra listen. Vil gi færre tilfeller av worst-case-kjøretid. 

```python
def Randomized_Quicksort(A,p,r):
    if p < r:
        q = Randomized_Partition(A,p,r)
        Randomized_Quicksort(A,p,q-1)
        Randomized_Partition(A,q+1,r)


def Randomized_Partition(A,p,r):
    i = random.randint(p,r)
    A[i], A[r] = A[r], A[i]

    return Partition(A,p,r)


def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1
```




## Forelesning 4 - Rangering i lineær tid <a name="of4"></a>

### Sammenligningsbasert sortering:
*Disse algoritmene benytter seg kun av sammenlikning av input-elementene. Slike sorteringsalgoritmer har en øvre grense på Ω(n lg n).*
 
 **Teorem**: Enhver sammenligningsbasert sorteringsalgoritme krever (n lg n) sammenlikninger i worst case.
 
 **Bevis**: En valgtre med høyde h og l blader, som gir `n! ≤ l ≤ 2h`. Som gir at `h ≥ lg(n!)` (siden *lg*-funksjonen er monotont stigende). `h = Ω(n lg n)`
 
 
###Counting Sort
Counting sort antar at hvert av de n elementene er et tall mellom 0 og *k*. Når *k* er *O(n)*, sorterer algoritmen på Θ(*n*). 

Algoritmen er **stabil**, som betyr at den beholder elementenes relative ordning, hvilket betyr at like elementer kommer i den samme rekkefølgen i output som i input.

**Input:** En n-element usortert liste *A*

**Output:** En sortert liste bestående av n-elementer fra *A*
 ```python
 def counting_sort(A,k):
    res = [0]*len(A)
    count = [0 for _ in range(k+1)]

    for j in range(0,len(A)):
        count[A[j]] += 1

    # C[i] inneholder nå antall forekomster av element i

    for i in range(1,k+1):
        count[i] += count[i-1]
    # Count er nå kumulativ sum
    # C[i] inneholder nå antall elementer mindre eller lik i

    # Itererer baklengs gjennom A, for at Counting blir stabil. Trekker fra en på count når vi plasserer et element
    for j in range(len(A)-1,-1,-1):
        element = A[j]

        res[count[element]-1] = element
        count[element] -= 1

    return res
 
 ```
 
 
###Radix sort
*Radix sort *er algoritmen som brukes i kort-sortering maskiner. Radix sort løser problemet ikke-intuitivt ved å sortere på det *least significant digit* først. 

```sudocode
RADIX-SORT(A, d)
 	for i = 1 to d
 		use a stable sort to sort array A on digit i

```

**Input:** En liste *A* med *n* elementer bestående av *d* siffer
**Output:** Sortert liste bestående av elementene i *A*

```python
def radix_sort(A, d):
    for i in range(d-1,-1,-1):
        # Bruker vlagfri stabil sorterings algoritme
        A = counting_sort(A,9,i)

    return A


# Sorterer større tall ved å kun se på et siffer.
# k = støste tall (9), i = sifferindeks

def counting_sort(A,k,d):
    res = [0]*len(A)
    count = [0 for _ in range(k+1)]

    for j in range(0,len(A)):
        element = int(str(A[j])[d])
        count[element] += 1

    # C[i] inneholder nå antall forekomster av element i

    for i in range(1,k+1):
        count[i] += count[i-1]
    # Count er nå kumulativ sum
    # C[i] inneholder nå antall elementer mindre eller lik i

    # Itererer baklengs gjennom A, for at Counting blir stabil. Trekker fra en på count når vi plasserer et element
    for j in range(len(A)-1,-1,-1):
        element = A[j]
		  
		 #Plasserer hele elementet i listen selvom jeg sorterer på hensyn på ett siffer
        res[count[int(str(element)[d])]-1] = element
        count[int(str(element)[d])] -= 1

    return res
```

Gitt *n* *d*-siffrede tall kan hvert siffer være en av *k* mulige verdier, vil Radix sort sortere disse tallene i `Θ(d (n + k))` tid, hvis den stabile sorteringsalgoritmen bruker `Θ(n + k)` tid. *Viktig* at sorteringsalgoritmen vi velger er **stabil** fordi at elementene med likt tall på siffer *d* ikke mister sin relative rekkefølge og ødelegger for sorteringen på de tidligere sorteringskallene.

###Bucket sort
Bucket sort antar at instansen er tatt fra en uniform fordeling og har en average-case kjøretid på `O(n)`, og worst-case `O(n^2)`. 

Som *Counting sort* er Bucket sort rask fordi den gjør antagelser på instansen. Bucket sort deler opp intervallet `[0, 1)` inn i n like store intervaller, eller **buckets**.

```python
def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]

    for i in range(n):
        B[int(n*A[i])].insert(-1, A[i])

    for j in range(n):
        insertion_sort(B[j])

    res = []
    for i in range(len(B)):
        res += (B[i])

    return res

```

> Tallet `int(n*A[ i ])` gir hvilken bucket som elementet skal legges i, `n*A[ i ]` rundes ned og blir en verdi i intervallet `[0, 1)` som har *n* buckets



### Minimum og maksimum

```sudocode
MINIMUM(A):
	min = A[1]
	for i = 2 to A.length:
		if min > A[i]:
			min = A[i]
	return min		
```

> Finner maksimum ved å ende `min > A[i]` til `min ≤ A[i]`


### Randomized-Select
*Randomized-Select* jobber kun på **én** side av partisjoneringen, og har derfor forventet kjøretid på `O(n)`, og worst-case `O(n^2)`. Algoritmen skal returnere det *i*’te minste elementet i listen `A[p .. r]`.

**Input:** En liste *A* med pivot-element *p*, sluttelement *r* og ønske om å finne *i* ´te minste element i *A*

**Output:** Indeks i A til *i* ´te minste element

```sudocode
RANDOMIZED-SELECT(A,p,r,i):
	if p == r:
		return A[p]
	q = RANDOMIZED-PARTITION(A,p,r)
	k = q - p + 1
	if i == k:		// The pivot value is the answer
		return a[q] 
		
	else if i < k:
		return RANDOMIZED-SELECT(a,p,q-1,i)
	else:
		return RANDOMIZED-SELECT(a,q+1,i-k) 
```
* Trykk for [video](https://www.youtube.com/watch?v=AHaaFVmAsvA) for bedre forklaring!

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
