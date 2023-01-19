def safeOpen(filename):
    try:
        file=open(filename)
    except:
        file= None
        
    return file

def safeFloat(x):
    try:
        number = float(x)
    except:
        number = 0.0
        
    return number

def averageSpeed():
    chances= 2
    while chances > 0:
        filename = input('Please enter the name of file:')
        try:
            file = open(filename)
            fileRead = file.read()
            file.close()
            chances = 0
            lines = fileRead.split('\n')
            values=[]
            for line in lines:
                values.append(line.split())
            count=0
            sum=0
            for value in values:
                try:
                    floatValue = float(value)
                    if(floatValue>2.0):
                        count+=1
                        sum += floatValue
                except:
                    pass
            average = sum / count
            print('Average speed is ' + average + 'miles per hour' )
        except:
            chances -= 1
            if(chances > 0):
                print('File not found. Please try again.')
            else:
                print('File not found. Yet another human error. Goodbye.')
                        
                

    
