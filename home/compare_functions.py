f = lambda x,y: x+y
g = lambda x,y: (x**2 - y**2)/(x-y)

def checkio(f,g):
    def h(*args,**kwargs):
        error = 0
        try:
            result_f = f(*args,**kwargs)
            if result_f==None:
                raise Exception
        except:
            error += 1
        try:
            result_g = g(*args,**kwargs)
            if result_g==None:
                raise Exception
        except:
            error += 2

        if (error==0):
            if (result_f==result_g):
                return result_f,'same'
            else:
                return result_f,'different'
        elif (error==1):
            return result_g,'f_error'
        elif (error==2):
            return result_f,'g_error'
        elif (error==3):
            return None,'both_error'
    return h

print checkio(f,g)(1)
