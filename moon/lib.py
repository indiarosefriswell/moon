""" This script determines wether you weigh more than the moon or not """

MOON_WEIGHT = 7.3e22


def am_i_as_heavy_as_the_moon(my_weight: float=0.):
    """ Compute if you are heavier than the moon """
    if not my_weight:
        return "You are either lying about your weight (0 kg) or you forgot to enter your weight."
    
    if my_weight >= MOON_WEIGHT:
        return (f"Your weight is {my_weight}kg and the moon weighs less than you .... join my bootcamp!")
    
    return (f"Your weight is {my_weight}kg and the moon weighs more than you .... you are smashing it!")