def power_operation(**kwargs):
    if len(kwargs) == 3:
        mod = kwargs['base'] % kwargs['mod']
        print(mod)
    power = kwargs['base'] ** kwargs['pow']
    print(power)
power_operation(base=2, pow =2,mod=2 )    
    
#[2023-12-13 12:10:29] #[2023-12-13 12:13:19] 