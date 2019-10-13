import pytest
import io
import sys
from team import Team
import superheroes
import tournament
import math
import random

# Helper Function


def capture_console_output(function_body):
    # _io.StringIO object
    string_io = io.StringIO()
    sys.stdout = string_io
    function_body()
    sys.stdout = sys.__stdout__
    return string_io.getvalue()

# Test Abilities Class


def test_ability_instance():
    # Test instantiation without error
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    assert big_strength


def test_ability_name():
    # Test for Correct Name
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    assert big_strength.name == "Overwhelming Strength"


def test_ability_attack():
    # Test for correct attack value
    test_runs = 400
    big_strength = superheroes.Ability("Overwhelming Strength", 400)
    for _ in range(0, test_runs):
        attack = big_strength.attack()
        assert attack >= 0 and attack <= 400


# Test Heroes Class
def test_hero_instance():
    Athena = superheroes.Hero("Athena")
    assert Athena


def test_hero_add_ability():
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    Athena = superheroes.Hero("Athena")
    assert len(Athena.abilities) == 0
    Athena.add_ability(big_strength)
    assert len(Athena.abilities) == 1
    # Check for correct type
    assert "Ability" in str(Athena.abilities[0])
    assert Athena.abilities[0].name == "Overwhelming Strength"


def test_hero_add_multi_ability():
    big_strength = superheroes.Ability("Overwhelming Strength", 300)
    speed = superheroes.Ability("Lightning Speed", 500)
    Athena = superheroes.Hero("Athena")
    assert len(Athena.abilities) == 0
    Athena.add_ability(big_strength)
    assert len(Athena.abilities) == 1
    Athena.add_ability(speed)
    assert len(Athena.abilities) == 2
    # Check for correct type
    assert "Ability" in str(Athena.abilities[0])
    assert Athena.abilities[0].name == "Overwhelming Strength"


def test_hero_attack_ability():
    big_strength = superheroes.Ability("Overwhelming Strength", 30000)
    athena = superheroes.Hero("Athena")
    athena.add_ability(big_strength)
    attack = athena.attack_value()
    assert attack <= 30000 and attack >= 0

def test_hero_ability_attack_standard_deviation():
    willow_waffle = superheroes.Hero("Willow Waffle")
    strength = random.randint(400, 30000)
    willow = superheroes.Ability("Willowness", strength)
    willow_waffle.add_ability(willow)
    attacks = list()
    total_attack = 0
    number_tests = 1000
    for _ in range(number_tests):
        cur_attack = willow_waffle.attack_value()
        attacks.append(cur_attack)
        total_attack += cur_attack
    mean = total_attack / number_tests
    
    # Get Square Deviations
    for index, value in enumerate(attacks):
        attacks[index] = math.pow(value - mean, 2)
    
    standard_dev = math.sqrt(sum(attacks) / len(attacks))
    print("Standard Deviation Cannot be 0.\nRandom Numbers not generated for attack.")
    assert standard_dev != 0.0
      
    
# This tests if the average of all attacks is correct.
# This test will faile if the random range of values is not correct. 

# This method uses statistics to check that a random value is given.
# This test will only fail if the same value is returned over the course of 1000 runs.
def test_hero_attack_standard_deviation():
    willow_waffle = superheroes.Hero("Willow Waffle")
    strength = random.randint(400, 30000)
    
    willow_waffle.add_ability(superheroes.Ability('arf', 100))
    attacks = list()
    total_attack = 0
    number_tests = 1000
    for _ in range(number_tests):
        cur_attack = willow_waffle.attack_value()
        attacks.append(cur_attack)
        total_attack += cur_attack
    mean = total_attack / number_tests
    
    # Get Square Deviations
    for index, value in enumerate(attacks):
        attacks[index] = math.pow(value - mean, 2)
    
    standard_dev = math.sqrt(sum(attacks) / len(attacks))
    print("Random values not given. Please make sure you're not returning the same value every time.")
    assert standard_dev != 0.0

def attack_avg(object, low, high):
    test_runs = 100
    for _ in range(0, test_runs):
        attack = object.attack()
        assert attack <= high and attack >= low

# Test Teams


def test_team_instance():
    team = Team("One")
    assert team


def test_team_name():
    team = Team("One")
    assert team.name == "One"


def test_team_hero():
    team = Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    assert len(team.heroes) == 1
    assert team.heroes[0].name == "Jodie Foster"


def test_print_heroes():
    team = Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    team.add_hero(jodie)
    athena = superheroes.Hero("Athena")
    team.add_hero(athena)
    output_string = ''
    for hero in team.heroes:
        output_string += hero.name

    assert "Jodie Foster" in output_string
    assert "Athena" in output_string