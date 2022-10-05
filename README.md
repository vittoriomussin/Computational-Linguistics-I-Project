#### -----------------------------

# Computational-Linguistic-I-Project

Program 1 - Compare two texts (at least 5000 words each) based on the following statistical information:

- the number of sentences and tokens

- the average length of sentences in terms of tokens and tokens (excluding punctuation) in terms of characters

- the number of hapaxes on the first 1000 tokens

- the vocabulary size and lexical richness calculated through the Type Token Ratio (TTR), in both cases calculated as the corpus increases for incremental portions of 500 tokens*

- percentage distribution of the set of full words (Adjectives, Nouns, Verbs, Adverbs) and functional words (Articles, Prepositions, Conjunctions, Pronouns)


Program 2 - For each of the two corpora extract the following information:
- extract and sort in order of decreasing frequency, indicating also the relative frequency:
  - the 10 most frequent PoS (Part-of-Speech)
  -  the 10 most frequent PoS bigrams
  -  the 10 most frequent PoS trigrams
  -  the 20 most frequent Adjectives and 20 most frequent Adverbs

- extract and sort the 20 bigrams composed of Adjective and Noun and where each token has a frequency greater than 3:
  - with maximum frequency, also indicating the relative frequency
  - with maximum conditional probability, also indicating the relative probability
  - with maximum associative strength (calculated in terms of Local Mutual Information), also indicating the relative strength of association

- extract sentences with at least 6 tokens and shorter than 25 tokens, where each individual token occurs at least twice in the reference corpus**:
    - with the average frequency distribution of the highest tokens in one case and lowest in the other, also reporting the average frequency distribution. The average frequency distribution should be calculated by taking into account the frequency of all tokens in the sentence (calculating the frequency in the corpus from which the sentence was extracted) and dividing the sum of the frequencies by the number of tokens in the sentence
    - with higher probability, where the probability must be calculated through a model Markov model of order 2. The model must use statistics extracted from the corpus that contains the sentences


after identifying and classifying the Named Entities (NEs) in the text, extract:
- the 15 most frequent proper names of persons (types), ordered by frequency

*output replaced here with a plot

**shown here only the first 5 senteces

# Output Exemple

## General Statistics

|                     |Frankenstein.txt     |The_Problems_of_Philosophy_by_Bertrand_Russell.txt|
|---------------      |---------------      |---------------     |
|Sentences:           |3075                 |1546                |
|Tokens:              |85253                |48292               |

|                               |Frankenstein.txt     |The_Problems_of_Philosophy_by_Bertrand_Russell.txt|
|---------------                |---------------      |---------------     |
|Mean sentence lenght:          |24.75                |28.01               |
|Mean token lenght:             |4.39                 |4.56                |

|                                        | Frankenstein.txt     |The_Problems_of_Philosophy_by_Bertrand_Russell.txt|
|---------------                         | ---------------      |---------------     |
|Hapax in the firsts 1000 tokens:        | 371                  |258                 |

### Type Token Ratio

![image](https://user-images.githubusercontent.com/81376065/193135144-f474736f-8c73-49a5-a954-c7084b9974a7.png)


![image](https://user-images.githubusercontent.com/81376065/193135327-afdc41a2-cd12-44d3-8927-1fd280ce9589.png)


|                               |Frankenstein.txt     |The_Problems_of_Philosophy_by_Bertrand_Russell.txt|
|---------------                |---------------      |---------------     |
|Lexical words:                 |48.67%	              |50.24%	             |
|Functional words:              |40.18%	              |38.22%	             |


## Information Extraction




|Frankenstein.txt|                | The_Problems_of_Philosophy_by_Bertrand_Russell.txt|                |
|-------------- | -------------- | -------------- | -------------- |
|POS            | Frequency      | POS            | Frequency      |
|NN             | 11739          | IN             | 6389           |
|IN             | 9470           | NN             | 6232           |
|DT             | 7276           | DT             | 4702           |
|PRP            | 6768           | JJ             | 3507           |
|VBD            | 5609           | RB             | 2523           |
|JJ             | 4809           | PRP            | 2410           |
|CC             | 3933           | NNS            | 2112           |
|RB             | 3771           | VBZ            | 2109           |
|NNS            | 3286           | VB             | 1979           |
|PRP$           | 3267           | CC             | 1561           |

|Frankenstein.txt|                | The_Problems_of_Philosophy_by_Bertrand_Russell.txt|                |
|-------------- | -------------- | -------------- | -------------- |
|POS Bigram     | Frequency      | POS Bigram     | Frequency      |
|DT NN          | 4054           | DT NN          | 2530           |
|NN IN          | 3378           | NN IN          | 2303           |
|IN DT          | 3217           | IN DT          | 2029           |
|PRP VBD        | 2630           | JJ NN          | 1204           |
|JJ NN          | 2026           | DT JJ          | 1108           |
|PRP$ NN        | 1874           | IN NN          | 1085           |
|NN CC          | 1773           | PRP VBP        | 752            |
|DT JJ          | 1529           | MD VB          | 746            |
|IN PRP$        | 1406           | TO VB          | 713            |
|IN NN          | 1355           | JJ NNS         | 693            |

|Frankenstein.txt|                | The_Problems_of_Philosophy_by_Bertrand_Russell.txt|                |
|-------------- | -------------- | -------------- | -------------- |
|POS Trigram    | Frequency      | POS Trigram    | Frequency      |
|IN DT NN       | 1756           | DT NN IN       | 1135           |
|DT NN IN       | 1682           | IN DT NN       | 1120           |
|NN IN DT       | 1085           | DT JJ NN       | 722            |
|DT JJ NN       | 1008           | NN IN DT       | 688            |
|IN PRP$ NN     | 799            | NN IN NN       | 518            |
|NN PRP VBD     | 738            | JJ NN IN       | 462            |
|IN DT JJ       | 691            | IN DT JJ       | 458            |
|NN IN PRP$     | 590            | PRP MD VB      | 338            |
|JJ NN IN       | 572            | IN NN IN       | 251            |
|NN IN NN       | 563            | DT NN VBZ      | 237            |


**Frankenstein**
|Adjective      | Frequency      | Adverb         | Frequency      |
|-------------- | -------------- | -------------- | -------------- |
|own            | 104            | not            | 551            |
|first          | 78             | so             | 189            |
|other          | 75             | now            | 147            |
|many           | 66             | more           | 114            |
|same           | 62             | then           | 104            |
|few            | 61             | only           | 97             |
|miserable      | 61             | yet            | 94             |
|dear           | 59             | even           | 81             |
|such           | 59             | again          | 78             |
|human          | 54             | most           | 76             |
|little         | 53             | ever           | 75             |
|old            | 50             | very           | 73             |
|more           | 48             | also           | 66             |
|“              | 46             | still          | 64             |
|great          | 45             | never          | 63             |
|happy          | 45             | soon           | 60             |
|several        | 43             | indeed         | 54             |
|new            | 39             | often          | 50             |
|poor           | 38             | thus           | 48             |
|last           | 31             | away           | 43             |


**The_Problems_of_Philosophy_by_Bertrand_Russell**
|Adjective      | Frequency      | Adverb         | Frequency      |
|-------------- | -------------- | -------------- | -------------- |
|such           | 150            | not            | 520            |
|other          | 140            | Thus           | 112            |
|true           | 129            | only           | 94             |
|physical       | 94             | so             | 88             |
|same           | 92             | more           | 62             |
|certain        | 89             | therefore      | 58             |
|different      | 76             | very           | 58             |
|general        | 68             | also           | 47             |
|particular     | 68             | really         | 47             |
|many           | 56             | even           | 44             |
|possible       | 56             | as             | 41             |
|real           | 45             | never          | 39             |
|first          | 40             | however        | 37             |
|more           | 34             | thus           | 33             |
|common         | 32             | quite          | 32             |
|complex        | 30             | merely         | 31             |
|great          | 28             | now            | 30             |
|least          | 28             | then           | 30             |
|present        | 28             | far            | 27             |
|false          | 27             | just           | 27             |

**Frankenstein**
|Bigram                        | Frequency            |Bigram                         |ConditionalProb     | Bigram                         |LMI                 |
|--------------                | --------------       |--------------                 |--------------      | --------------                 |--------------      |
|old man                       | 34                   |old man                        |0.00361             | old man                        |448.8               |
|native country                | 15                   |native country                 |0.00166             | native country                 |197.18              |
|natural philosophy            | 13                   |natural philosophy             |0.00145             | natural philosophy             |170.7               |
|fellow creatures              | 10                   |fellow creatures               |0.00114             | fellow creatures               |131.0               |
|young man                     | 9                    |young man                      |0.00103             | young man                      |117.78              |
|’ s                           | 8                    |’ s                            |0.00093             | first time                     |104.61              |
|first time                    | 8                    |first time                     |0.00093             | many months                    |104.59              |
|long time                     | 8                    |long time                      |0.00093             | ’ s                            |104.57              |
|many months                   | 8                    |many months                    |0.00093             | long time                      |104.54              |
|several hours                 | 7                    |several hours                  |0.00083             | few minutes                    |91.36               |
|poor girl                     | 7                    |poor girl                      |0.00083             | many hours                     |91.36               |
|few minutes                   | 7                    |dear Victor                    |0.00083             | dear Victor                    |91.35               |
|dear Victor                   | 7                    |few minutes                    |0.00082             | several hours                  |91.34               |
|many hours                    | 7                    |many hours                     |0.00082             | poor girl                      |91.33               |
|human beings                  | 6                    |short time                     |0.00073             | own heart                      |78.16               |
|short time                    | 6                    |next morning                   |0.00073             | same time                      |78.13               |
|native town                   | 6                    |human beings                   |0.00072             | human beings                   |78.12               |
|own heart                     | 6                    |native town                    |0.00072             | native town                    |78.1                |
|” “                           | 6                    |own heart                      |0.00072             | ” “                            |78.1                |
|next morning                  | 6                    |” “                            |0.00072             | short time                     |78.09               |


**The_Problems_of_Philosophy_by_Bertrand_Russell**
|Bigram                        | Frequency            |Bigram                         |ConditionalProb     | Bigram                         |LMI                 |
|--------------                | --------------       |--------------                 |--------------      | --------------                 |--------------      |
|physical objects              | 42                   |physical objects               |0.00959             | physical objects               |508.03              |
|_a priori_                    | 21                   |_a priori_                     |0.00499             | _a priori_                     |252.83              |
|physical object               | 19                   |physical object                |0.00446             | physical object                |229.06              |
|physical space                | 16                   |physical space                 |0.00379             | physical space                 |192.68              |
|inductive principle           | 15                   |inductive principle            |0.00363             | inductive principle            |180.19              |
|real table                    | 14                   |real table                     |0.00338             | real table                     |168.2               |
|other people                  | 13                   |other people                   |0.00309             | other people                   |156.49              |
|intuitive knowledge           | 12                   |intuitive knowledge            |0.00295             | intuitive knowledge            |143.88              |
|different people              | 11                   |different people               |0.00269             | such knowledge                 |132.25              |
|other things                  | 11                   |other things                   |0.00265             | other things                   |132.21              |
|such knowledge                | 11                   |such knowledge                 |0.00264             | different people               |131.98              |
|derivative knowledge          | 10                   |derivative knowledge           |0.0025              | common sense                   |119.72              |
|common sense                  | 10                   |common sense                   |0.00249             | derivative knowledge           |119.65              |
|general proposition           | 9                    |logical principles             |0.00227             | general proposition            |107.73              |
|general principles            | 9                    |general proposition            |0.00224             | general principles             |107.73              |
|logical principles            | 9                    |general principles             |0.00224             | logical principles             |107.59              |
|such things                   | 8                    |complex unity                  |0.00204             | such things                    |95.82               |
|general law                   | 8                    |general law                    |0.00202             | general law                    |95.61               |
|complex unity                 | 8                    |such things                    |0.00198             | complex unity                  |95.51               |
|same thing                    | 7                    |daily life                     |0.00182             | same thing                     |83.56               |


|Frankenstein.txt     |                     |The_Problems_of_Philosophy_by_Bertrand_Russell.txt|                     |
|--------------       |--------------       |--------------      | --------------      |
|Person               |Frequency            |Person              | Frequency           |
| Elizabeth           |70                   | Berkeley           | 23                  |
| Felix               |36                   | Cassio             | 22                  |
| Clerval             |36                   | Desdemona          | 18                  |
| Justine             |25                   | Othello            | 14                  |
| William             |22                   | Bismarck           | 12                  |
| Henry               |20                   | Kant               | 9                   |
| Safie               |18                   | Plato              | 9                   |
| Agatha              |16                   | Jones              | 7                   |
| De Lacey            |9                    | Smith              | 6                   |
| Mr. Kirwin          |9                    | Socrates           | 6                   |
| Ernest              |8                    | Robinson           | 6                   |
| Victor              |8                    | Brown              | 6                   |
| Mont Blanc          |7                    | Leibniz            | 5                   |
| Frankenstein        |7                    | Edinburgh          | 5                   |
| Arabian             |5                    | Hegel              | 4                   |
