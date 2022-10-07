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

|                     |Frankenstein         |The_Problems_of_Philosophy|
|---------------      |---------------      |---------------     |
|Sentences:           |3075                 |1546                |
|Tokens:              |85253                |48292               |

|                               |Frankenstein         |The_Problems_of_Philosophy|
|---------------                |---------------      |---------------     |
|Mean sentence lenght:          |24.75                |28.01               |
|Mean token lenght:             |4.39                 |4.56                |

|                                        | Frankenstein         |The_Problems_of_Philosophy|
|---------------                         | ---------------      |---------------     |
|Hapax in the firsts 1000 tokens:        | 371                  |258                 |


### Type Token Ratio

![image](https://user-images.githubusercontent.com/81376065/193135144-f474736f-8c73-49a5-a954-c7084b9974a7.png)


![image](https://user-images.githubusercontent.com/81376065/193135327-afdc41a2-cd12-44d3-8927-1fd280ce9589.png)


|                               |Frankenstein         |The_Problems_of_Philosophy|
|---------------                |---------------      |---------------     |
|Lexical words:                 |48.67%	              |50.24%	             |
|Functional words:              |40.18%	              |38.22%	             |


## Information Extraction

|Frankenstein   |                | The_Problems_of_Philosophy|                |
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

|Frankenstein   |                | The_Problems_of_Philosophy|                |
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

|Frankenstein   |                | The_Problems_of_Philosophy|                |
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
|miserable      | 61             | only           | 97             |
|few            | 61             | yet            | 94             |
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
|strange        | 31             | away           | 43             |

**The_Problems_of_Philosophy**
|Adjective      | Frequency      | Adverb         | Frequency      |
|-------------- | -------------- | -------------- | -------------- |
|such           | 150            | not            | 520            |
|other          | 140            | Thus           | 112            |
|true           | 129            | only           | 94             |
|physical       | 94             | so             | 88             |
|same           | 92             | more           | 62             |
|certain        | 89             | therefore      | 58             |
|different      | 76             | very           | 58             |
|particular     | 68             | also           | 47             |
|general        | 68             | really         | 47             |
|many           | 56             | even           | 44             |
|possible       | 56             | as             | 41             |
|real           | 45             | never          | 39             |
|first          | 40             | however        | 37             |
|more           | 34             | thus           | 33             |
|common         | 32             | quite          | 32             |
|complex        | 30             | merely         | 31             |
|present        | 28             | now            | 30             |
|least          | 28             | then           | 30             |
|great          | 28             | far            | 27             |
|false          | 27             | just           | 27             |

**Frankenstein**
|Bigram                        | Frequency            |Bigram                         |ConditionalProb     | Bigram                         |LMI                 |
|--------------                | --------------       |--------------                 |--------------      | --------------                 |--------------      |
|old man                       | 34                   |old man                        |0.00361             | old man                        |298.83              |
|native country                | 15                   |native country                 |0.00166             | natural philosophy             |150.93              |
|natural philosophy            | 13                   |natural philosophy             |0.00145             | native country                 |148.57              |
|fellow creatures              | 10                   |fellow creatures               |0.00114             | fellow creatures               |108.7               |
|young man                     | 9                    |young man                      |0.00103             | ’ s                            |79.07               |
|first time                    | 8                    |first time                     |0.00093             | few minutes                    |71.84               |
|many months                   | 8                    |many months                    |0.00093             | young man                      |69.73               |
|long time                     | 8                    |long time                      |0.00093             | long time                      |66.98               |
|’ s                           | 8                    |’ s                            |0.00093             | many months                    |65.36               |
|poor girl                     | 7                    |poor girl                      |0.00083             | poor girl                      |64.71               |
|several hours                 | 7                    |several hours                  |0.00083             | dear Victor                    |62.27               |
|few minutes                   | 7                    |dear Victor                    |0.00083             | several hours                  |61.59               |
|dear Victor                   | 7                    |few minutes                    |0.00082             | next morning                   |60.84               |
|many hours                    | 7                    |many hours                     |0.00082             | native town                    |58.11               |
|human beings                  | 6                    |next morning                   |0.00073             | many hours                     |57.35               |
|” “                           | 6                    |short time                     |0.00073             | human beings                   |53.34               |
|next morning                  | 6                    |human beings                   |0.00072             | first time                     |53.23               |
|own heart                     | 6                    |” “                            |0.00072             | short time                     |51.05               |
|native town                   | 6                    |own heart                      |0.00072             | gentle manners                 |48.48               |
|short time                    | 6                    |native town                    |0.00072             | ” Such                         |48.38               |

**The_Problems_of_Philosophy**
|Bigram                        | Frequency            |Bigram                         |ConditionalProb     | Bigram                         |LMI                 |
|--------------                | --------------       |--------------                 |--------------      | --------------                 |--------------      |
|physical objects              | 42                   |physical objects               |0.00959             | physical objects               |330.72              |
|_a priori_                    | 21                   |_a priori_                     |0.00499             | _a priori_                     |205.31              |
|physical object               | 19                   |physical object                |0.00446             | inductive principle            |141.57              |
|physical space                | 16                   |physical space                 |0.00379             | physical object                |126.07              |
|inductive principle           | 15                   |inductive principle            |0.00363             | physical space                 |109.91              |
|real table                    | 14                   |real table                     |0.00338             | real table                     |103.62              |
|other people                  | 13                   |other people                   |0.00309             | other people                   |88.62               |
|intuitive knowledge           | 12                   |intuitive knowledge            |0.00295             | intuitive knowledge            |82.81               |
|different people              | 11                   |different people               |0.00269             | different people               |82.14               |
|such knowledge                | 11                   |other things                   |0.00265             | complex unity                  |80.45               |
|other things                  | 11                   |such knowledge                 |0.00264             | logical principles             |78.52               |
|common sense                  | 10                   |derivative knowledge           |0.0025              | late Prime                     |76.4                |
|derivative knowledge          | 10                   |common sense                   |0.00249             | common sense                   |74.97               |
|general proposition           | 9                    |logical principles             |0.00227             | derivative knowledge           |73.23               |
|logical principles            | 9                    |general proposition            |0.00224             | daily life                     |72.92               |
|general principles            | 9                    |general principles             |0.00224             | human beings                   |69.81               |
|complex unity                 | 8                    |complex unity                  |0.00204             | general principles             |64.26               |
|such things                   | 8                    |general law                    |0.00202             | private spaces                 |62.58               |
|general law                   | 8                    |such things                    |0.00198             | general proposition            |61.2                |
|general propositions          | 7                    |daily life                     |0.00182             | general law                    |56.39               |

**Frankenstein**
|Frase                                                                                                                                                                 |Frequenza media|
|--------------                                                                                                                                                        |--------------|
|I thought of the occurrences of the day                                                                                                                               |2009.25   |
|I abhorred the face of man                                                                                                                                            |1589.83   |
|I took the hand of Elizabeth                                                                                                                                          |1588.0    |
|I lay on the deck looking at the stars and listening to the dashing of the waves                                                                                      |1582.53   |
|I examined the materials of the fire and to my joy found it to be composed of wood                                                                                    |1423.44   |

|Frase                                                                                                                                                                 |Frequenza media|
|--------------                                                                                                                                                        |--------------|
|Letter 4 _To Mrs. Saville England._ August 5th 17—                                                                                                                    |4.22      |
|Dear Victor banish these dark passions                                                                                                                                |34.17     |
|She fell however into good hands                                                                                                                                      |51.5      |
|Yet why were these gentle beings unhappy                                                                                                                              |80.71     |
|The most learned philosopher knew little more                                                                                                                         |91.86     |

|Frase                                                                                                                                                                 |Probabilità|
|--------------                                                                                                                                                        |--------------|
|I will proceed with my tale                                                                                                                                           |9.17618284055179e-22|
|I was formed for peaceful happiness                                                                                                                                   |9.17618284055179e-22|
|I abhorred the face of man                                                                                                                                            |9.17618284055179e-22|
|I took the hand of Elizabeth                                                                                                                                          |9.17618284055179e-22|
|I pressed on but in vain                                                                                                                                              |9.17618284055179e-22|

**The_Problems_of_Philosophy**
|Frase                                                                                                                                                                 |Frequenza media|
|--------------                                                                                                                                                        |--------------|
|They did not prove that the colour is in the mind of the percipient                                                                                                   |892.14    |
|Nevertheless the probability of the general law is increased by repetitions just as the probability of the particular case is                                         |828.55    |
|the sense-datum as the mark of some physical object                                                                                                                   |811.67    |
|But the conclusion that the law of contradiction is a law of _thought_ is nevertheless erroneous                                                                      |793.88    |
|This question is of the greatest importance                                                                                                                           |791.43    |

|Frase                                                                                                                                                                 |Frequenza media|
|--------------                                                                                                                                                        |--------------|
|Suppose some statement made about Bismarck                                                                                                                            |47.67     |
|Common words even proper names are usually really descriptions                                                                                                        |66.89     |
|All such immediate data he calls 'ideas '                                                                                                                             |79.0      |
|If he doubted he must exist if he had any experiences whatever he must exist                                                                                          |83.13     |
|This function at least philosophy can perform                                                                                                                         |90.71     |

|Frase                                                                                                                                                                 |Probabilità|
|--------------                                                                                                                                                        |--------------|
|and 'What beliefs are false '                                                                                                                                         |2.543808140726536e-20|
|not 'What beliefs are true '                                                                                                                                          |1.5769113010141103e-20|
|This difficulty is no light one                                                                                                                                       |2.942184267351111e-21|
|Such philosophers are called 'idealists '                                                                                                                             |6.202986380696356e-22|
|Such philosophers are called 'idealists '                                                                                                                             |6.202986380696356e-22|

|Frankenstein         |                     |The_Problems_of_Philosophy|                     |
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
| Mr. Kirwin          |9                    | Brown              | 6                   |
| Ernest              |8                    | Socrates           | 6                   |
| Victor              |8                    | Robinson           | 6                   |
| Mont Blanc          |7                    | Leibniz            | 5                   |
| Frankenstein        |7                    | Edinburgh          | 5                   |
| Krempe              |5                    | Hegel              | 4                   |
