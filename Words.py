st = 'Print only the words that start with s in this sentence'
R = st.split()
for a in R:
    if a[0]=="s":
        print(a)

st_2= 'Print every word in this sentence that has an even number of letters'  
K=st_2.split()
for b in K:
    if (len(b))%2==0:
        print(b+ " is even")   


st_3 = 'Create a list of the first letters of every word in this string'
List=[]
G=st_3.split()
for c in G:
    List.append(c[0])
print(List)