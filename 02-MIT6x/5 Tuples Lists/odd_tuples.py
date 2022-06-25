########################################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 23, 2022
## Exercise: odd tuples
''' 
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every 
## other element of the input tuple is copied, starting with the first one. So if test is the tuple 
## ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
'''
########################################################################################################################

def oddTuples(aTup):
    '''
    aTup: a tuple
    return: tuple, every other element of tuple
    '''

    if len(aTup) == 1:
        return aTup
    elif len(aTup) == 2:
        return aTup[0]

    OddTup = ()
    a = 0
    for i in aTup:
        if a%2 == 0:
            OddTup = OddTup + (i,)
        a += 1
    return OddTup

myTup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(myTup))


def oddTuples2(aTup):
    '''
    Another way to solve the problem
    :param aTup: a tuple
    :return: a tuple, every other element of aTup
    '''

    # Here is another solution to the problem that uses tuple
    # slicing by 2 to achieve the same result
    return aTup[::2]

    ## DUHH SO MUCH SIMPLER