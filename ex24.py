# prints the statement to the screen
print("Let's practice everything.")
# prints the statement to the screen
print('you\'d need to know \'bout escapes with \\ that do:')
# learn to make a new line \n  and tab \t
print('\n new lines and \t tabs.')

# here is a poem that is in a string literal
# it has a tab to begin it a new line in the middle
# there is a new line and tab, tab in seqence near the end
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# prints a dashed line and then prints the poem and then another dashed line
print("------------------")
print(poem)
print("------------------")

# assigns a value to a variable of 5
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")
#creates a function called secret_formula that has variables and returns
# 3 values
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# define a variable of start_point
start_point = 10000
# sets beans, jars, crates equal to secret_formula with argument of start_point
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("with a starting point of: {}".format(start_point))
# its just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("we can also do that this way:")
formula = secret_formula(start_point)

# this is an easy way to apply a list to a format string
print("We\'d have {} beans, {} jars, and {} crates.".format(*formula))
