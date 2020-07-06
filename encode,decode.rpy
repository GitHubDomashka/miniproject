def forma():
    d = {}
    iter = 0
    for i in range(0,127):
        d[iter] = chr(i)
        iter = iter +1
    return d
 

def encode_val(word):
    list = []
    lent = len(word)
   
    d = forma() 
   
    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list.append(value)
    return list
 
def comparator(value, key):
    len_key = len(key)
    x = {}
    iter = 0
    full = 0
    for i in value:
        x[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0
 
    return x  
   
def encode(value, key):
 
    dic = comparator(value, key)
    print ('encode',dic)
 
    lis = []
    d = forma()
 
    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go)
    return lis
 
 
def decode(value, key):
 
    dic = comparator(value, key)
   
    print ('Deshifre=', dic)
    d = forma() # получаем словарь кода
 
    lis =[]
    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        lis.append(go)
    return lis
   
 
def decode_val(list_in):
 
    list_code = []
    lent = len(list_in)
 
    d = forma() # получаем словарь кода
   
    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value])
    return list_code
 
 
if __name__ == "__main__":
    print('Введите текст,который нужно зашифровать на eng')
    word = (input())
    key = 'key'
   
    print ('Слово ', word)
    print ('', key)
    print (forma())
    key_encoded = encode_val(key)
    value_encoded = encode_val(word)
 
    print ('Значение=',value_encoded)
    print ('Ключ=', key_encoded)
 
    shifre = encode(value_encoded, key_encoded)
    print ('Шифр=', ''.join(decode_val(shifre)))
 
    decoded = decode(shifre, key_encoded)
    print ('Decode list=', decoded)
    decode_word_list = decode_val(decoded)
    print ('Слово=',''.join(decode_word_list))
