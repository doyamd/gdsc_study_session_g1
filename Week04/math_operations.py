def apply_operations(args):
    results = map(lambda op: op[0](*op[1]), args)
    return list(results)

    

def basic_operations(n1,n2):
    d = {'sum':0,'sub':0,'div':0,'multi':0}
    d['sum'] = n1+n2
    d['sub'] = n1-n2
    d['div'] = n1/n2
    d['multi'] = n1*n2
    return d
# print(basic_operations(1,2))

def power_operation(base, exponent,**kwargs):
    result = base ** exponent
    
    if 'mod' in kwargs:
        result %= kwargs['mod']
    
    return result
# power_operation(base=2, pow =2,mod=2 )    
    
#[2023-12-13 12:10:29] #[2023-12-13 12:13:19] 