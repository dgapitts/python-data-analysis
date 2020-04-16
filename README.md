## Overview

Sample python scripts from python-data-analysis course on Linkedin Learning  (https://www.linkedin.com/learning/python-data-analysis-2015).

My objectives are to 
- enhance my python scripting
- starting moving from python2.7 to python3.x
- familiarizer myself with python numpy, pandas, matplotlib (I've already done simple line charts with pylab)
- work with jupyter notebook

## Setup

I've been using both python3 (3.7) (installed via brew)

```
~/projects/python-data-analysis $ python3
Python 3.7.7 (default, Mar 10 2020, 15:43:03)
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
>>> exit()
```

and especially regular python (2.7) for quite a while 
```
~/projects/python-data-analysis $ python
Python 2.7.10 (default, Feb 22 2019, 21:55:15)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> import panda
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named panda
>>> import pandas
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named pandas
>>> import matplotlib
>>>
```



For this course, I want to use `Anaconda`

> Anaconda is a free and open-source distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment. Package versions are managed by the package management system conda.

so again using brew

```
~/projects/python-data-analysis $ brew cask install anaconda
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
...
```




finally and I think I like this (no affect on my regular python usage) you need to use the z-shell (I'm typically a bash shell person)

```
~ $ cat ~/.zshrc
export PATH="/usr/local/anaconda3/bin:$PATH"
```

now I can use Anaconda python 

```
Last login: Thu Mar 26 20:30:22 on ttys014
~ $ zsh
Daves-MacBook-Pro% python
Python 3.7.4 (default, Aug 13 2019, 15:17:50)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> import pandas
i>>> import matplotlib
>>> exit ()
```
and jupyter notebooks:
```
Daves-MacBook-Pro% jupyter notebook
[I 21:12:21.784 NotebookApp] The port 8888 is already in use, trying another port.
[I 21:12:21.846 NotebookApp] JupyterLab extension loaded from /usr/local/anaconda3/lib/python3.7/site-packages/jupyterlab
[I 21:12:21.846 NotebookApp] JupyterLab application directory is /usr/local/anaconda3/share/jupyter/lab
[I 21:12:21.848 NotebookApp] Serving notebooks from local directory: /Users/dpitts
[I 21:12:21.849 NotebookApp] The Jupyter Notebook is running at:
[I 21:12:21.849 NotebookApp] http://localhost:8889/?token=4bfb635934506cbc764660146e2e6d019f8282e6fa260df1
[I 21:12:21.849 NotebookApp]  or http://127.0.0.1:8889/?token=4bfb635934506cbc764660146e2e6d019f8282e6fa260df1
[I 21:12:21.849 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 21:12:21.855 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///Users/dpitts/Library/Jupyter/runtime/nbserver-93038-open.html
    Or copy and paste one of these URLs:
        http://localhost:8889/?token=4bfb635934506cbc764660146e2e6d019f8282e6fa260df1
     or http://127.0.0.1:8889/?token=4bfb635934506cbc764660146e2e6d019f8282e6fa260df1
^C[I 21:12:36.561 NotebookApp] interrupted
Serving notebooks from local directory: /Users/dpitts
0 active kernels
The Jupyter Notebook is running at:
http://localhost:8889/?token=4bfb635934506cbc764660146e2e6d019f8282e6fa260df1
 or http://127.0.0.1:8889/?token=4bfb635934506cbc764660146e2e6d019f8282e6fa260df1
Shutdown this notebook server (y/[n])? No answer for 5s: resuming operation...
```

### A little Help with getting started with Jupyter Notebooks

Sounds a bit like vi i.e. a good start
{quote}
First, we need to know that they are 2 modes in the Jupyter Notebook App: command mode and edit mode.
https://towardsdatascience.com/jypyter-notebook-shortcuts-bf0101a98330
{quote}

The most important key to know is H for help, which appeaars to OS context sensitive:

 ![alt text](Help-shortcuts-Jupyter-Notebooks.png "Help-shortcuts-Jupyter-Notebooks.png")



### ex02-05-namedtuples-python27-script.py

Ref: https://pymotw.com/2/collections/namedtuple.html
```
~/projects/python-data-analysis $ cat ex02-05-namedtuples-python27-script.py
import collections
Person = collections.namedtuple('Person', 'name age gender')

print 'Type of Person:', type(Person)

bob = Person(name='Bob', age=30, gender='male')
print '\nRepresentation:', bob

jane = Person(name='Jane', age=29, gender='female')
print '\nField by name:', jane.name

print '\nFields by index:'
for p in [ bob, jane ]:
    print '%s is a %d year old %s' % p
```
output
```
~/projects/python-data-analysis $ python2.7 ex02-05-namedtuples-python27-script.py
Type of Person: <type 'type'>

Representation: Person(name='Bob', age=30, gender='male')

Field by name: Jane

Fields by index:
Bob is a 30 year old male
Jane is a 29 year old female
```



### ex03-text-manipulation-and-files

One confusing thing for me with jupyter is how to know and/or set my working directory within the host OS filesysteM? 
So needed to python ues the os package 

```
import os
arr = os.listdir()
print(arr)
```
https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

Also I was curious to load data from a more interesting dataset i.e. a txt version of Percy Bysshe Shelley's "Prometheus Unbound" (http://www.gutenberg.org/cache/epub/4797/pg4797.txt), but then I also need to convert words into lines

```
You need str.split() to split each string into words:
word_list = [word for line in sentence for word in line.split()]
```
https://stackoverflow.com/questions/8478602/convert-a-list-of-string-sentences-to-words


### ex03-reading-a-file-python2.7

Ref: https://stackabuse.com/read-a-file-line-by-line-in-python/
```
~/projects/python-data-analysis $ cat ex03-filehandling.py
filepath = 'Prometheus_Unbound.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1
```
Running this:
```
~/projects/python-data-analysis $ python2.7 ex03-filehandling.py|head
Line 1: PROMETHEUS UNBOUND. A LYRICAL DRAMA IN FOUR ACTS.
Line 2:
Line 3:
Line 4: PROMETHEUS UNBOUND. A LYRICAL DRAMA IN FOUR ACTS.	1
Line 5: PREFACE.	1
Line 6: ACT 1.	4
Line 7: ACT 2.	23
Line 8: ACT 3.	38
Line 9: ACT 4.	49
Line 10:
```
and...
```
~/projects/python-data-analysis $ python2.7 ex03-filehandling.py|tail
Line 4197: a month or two I shall send it. It is a drama, with characters and
Line 4198: mechanism of a kind yet unattempted; and I think the execution is
Line 4199: better than any of my former attempts.'
Line 4200:
Line 4201: I may mention, for the information of the more critical reader, that
Line 4202: the verbal alterations in this edition of "Prometheus" are made from a
Line 4203: list of errata written by Shelley himself.
Line 4204:
Line 4205: ***
Line 4206:
```

### Developing word split logic


Create file with first 100 words
```
~/projects/python-data-analysis $ head -100 Prometheus_Unbound.txt > Prometheus_Unbound_first100_lines.txt
~/projects/python-data-analysis $ cat Prometheus_Unbound_first100_lines.txt
PROMETHEUS UNBOUND. A LYRICAL DRAMA IN FOUR ACTS.


PROMETHEUS UNBOUND. A LYRICAL DRAMA IN FOUR ACTS.	1
PREFACE.	1
ACT 1.	4
ACT 2.	23
ACT 3.	38
ACT 4.	49


AUDISNE HAEC AMPHIARAE, SUB TERRAM ABDITE?

[Composed at Este, September, October, 1818 (Act 1); at Rome,
March-April 6, 1819 (Acts 2, 3); at Florence, close of 1819 (Act 4).
Published by C. and J. Ollier, London, summer of 1820. Sources of the
text are (1) edition of 1820; (2) text in "Poetical Works", 1839,
prepared with the aid of a list of errata in (1) written out by
Shelley; (3) a fair draft in Shelley's autograph, now in the Bodleian.
This has been carefully collated by Mr. C.D. Locock, who prints the
result in his "Examination of the Shelley Manuscripts in the Bodleian
Library", Oxford (Clarendon Press), 1903. Our text is that of 1820,
modified by edition 1839, and by the Bodleian fair copy. In the
following notes B = the Bodleian manuscript; 1820 = the editio
princeps, printed by Marchant for C. and J. Ollier, London; and 1839 =
the text as edited by Mrs. Shelley in the "Poetical Works", 1st and
2nd editions, 1839. The reader should consult the notes on the Play at
the end of the volume.]


PREFACE.

The Greek tragic writers, in selecting as their subject any portion of
their national history or mythology, employed in their treatment of it
a certain arbitrary discretion. They by no means conceived themselves
bound to adhere to the common interpretation or to imitate in story as
in title their rivals and predecessors. Such a system would have
amounted to a resignation of those claims to preference over their
competitors which incited the composition. The Agamemnonian story was
exhibited on the Athenian theatre with as many variations as dramas.

I have presumed to employ a similar license. The "Prometheus Unbound"
of Aeschylus supposed the reconciliation of Jupiter with his victim as
the price of the disclosure of the danger threatened to his empire by
the consummation of his marriage with Thetis. Thetis, according to
this view of the subject, was given in marriage to Peleus, and
Prometheus, by the permission of Jupiter, delivered from his captivity
by Hercules. Had I framed my story on this model, I should have done
no more than have attempted to restore the lost drama of Aeschylus; an
ambition which, if my preference to this mode of treating the subject
had incited me to cherish, the recollection of the high comparison
such an attempt would challenge might well abate. But, in truth, I was
averse from a catastrophe so feeble as that of reconciling the
Champion with the Oppressor of mankind. The moral interest of the
fable, which is so powerfully sustained by the sufferings and
endurance of Prometheus, would be annihilated if we could conceive of
him as unsaying his high language and quailing before his successful
and perfidious adversary. The only imaginary being resembling in any
degree Prometheus, is Satan; and Prometheus is, in my judgement, a
more poetical character than Satan, because, in addition to courage,
and majesty, and firm and patient opposition to omnipotent force, he
is susceptible of being described as exempt from the taints of
ambition, envy, revenge, and a desire for personal aggrandisement,
which, in the Hero of "Paradise Lost", interfere with the interest.
The character of Satan engenders in the mind a pernicious casuistry
which leads us to weigh his faults with his wrongs, and to excuse the
former because the latter exceed all measure. In the minds of those
who consider that magnificent fiction with a religious feeling it
engenders something worse. But Prometheus is, as it were, the type of
the highest perfection of moral and intellectual nature, impelled by
the purest and the truest motives to the best and noblest ends.

This Poem was chiefly written upon the mountainous ruins of the Baths
of Caracalla, among the flowery glades, and thickets of odoriferous
blossoming trees, which are extended in ever winding labyrinths upon
its immense platforms and dizzy arches suspended in the air. The
bright blue sky of Rome, and the effect of the vigorous awakening
spring in that divinest climate, and the new life with which it
drenches the spirits even to intoxication, were the inspiration of
this drama.

The imagery which I have employed will be found, in many instances, to
have been drawn from the operations of the human mind, or from those
external actions by which they are expressed. This is unusual in
modern poetry, although Dante and Shakespeare are full of instances of
the same kind: Dante indeed more than any other poet, and with greater
success. But the Greek poets, as writers to whom no resource of
awakening the sympathy of their contemporaries was unknown, were in
the habitual use of this power; and it is the study of their works
(since a higher merit would probably be denied me) to which I am
willing that my readers should impute this singularity.

One word is due in candour to the degree in which the study of
contemporary writings may have tinged my composition, for such has
been a topic of censure with regard to poems far more popular, and
indeed more deservedly popular, than mine. It is impossible that any
one who inhabits the same age with such writers as those who stand in
the foremost ranks of our own, can conscientiously assure himself that
his language and tone of thought may not have been modified by the
study of the productions of those extraordinary intellects. It is
```