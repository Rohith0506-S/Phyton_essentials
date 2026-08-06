Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#NON PRIMITIVE DATATYPE
#----------------------

# tuple
# -----

# tuple is enclosed with ()
# tuple values are also ordered collection
# tuple values are indexed
# tuple values support duplicates
# tuple values are IMMUTABLE

t = ('rohith','avinash','monish','uthay','rohith','subeer',)
t
('rohith', 'avinash', 'monish', 'uthay', 'rohith', 'subeer')
type(t)
<class 'tuple'>

#Tuple operations - count() and index()
\
t
('rohith', 'avinash', 'monish', 'uthay', 'rohith', 'subeer')
\
t.count('rohith')
2
t.index('uthay')
3
>>> 
>>> #Ways to update values in a tuple
>>> t = list(t) #convert tuple to list
>>> t.append('alwin')
>>> t
['rohith', 'avinash', 'monish', 'uthay', 'rohith', 'subeer', 'alwin']
>>> type(t)
<class 'list'>
>>> 
>>> t = tuple(t)
>>> t
('rohith', 'avinash', 'monish', 'uthay', 'rohith', 'subeer', 'alwin')
>>> type(t)
<class 'tuple'>
>>> 
>>> #Tuple concatenation
>>> t1 = (10,20,30,40)
>>> t = t + t1
>>> t
('rohith', 'avinash', 'monish', 'uthay', 'rohith', 'subeer', 'alwin', 10, 20, 30, 40)
