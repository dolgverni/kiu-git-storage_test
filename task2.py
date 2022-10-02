def warn_the_sheep(queue): 
    if 'wolf' == queue[-1]: 
        return "Pls go away and stop eating my sheep"
    else: 
        n = str(len(queue) - queue.index('wolf') - 1)
        phrase = list("Oi! Sheep number N! You are about to be eaten by a wolf!")
        phrase[17], n = n, phrase[17]
        return (''.join(phrase))