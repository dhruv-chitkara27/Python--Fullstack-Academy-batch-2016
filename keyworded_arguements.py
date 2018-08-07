def print_val(**val):
    for key,val in val.items():
        print("%s has got %d marks"%(key,val))
        print("{} has got {}".format(key,val))
print_val(Ram=20,X=30,Y=31)
