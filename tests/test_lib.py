from moon.lib import am_i_as_heavy_as_the_moon


def test_ignoring_without_a_weight():
    assert am_i_as_heavy_as_the_moon() == "You are either lying about your weight (0 kg) or you forgot to enter your weight."

def test_heavier_than_the_moon():
    assert am_i_as_heavy_as_the_moon(1e27) == "Your weight is {}kg and the moon weighs less than you .... join my bootcamp!".format(1e27)

def test_lighter_than_the_moon():
    assert am_i_as_heavy_as_the_moon(64.) == "Your weight is {}kg and the moon weighs more than you .... you are smashing it!".format(64.)