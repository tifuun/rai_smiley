from rai_smiley.smiley import Smiley

# The `__init__.py` file is necessary for Python to detect `rai_smiley` as
# a module.
# Other `.py` files, like `smiley.py` are detected as modules automatically.
# Currently, our package `rai_smiley` packages a single module
# called `rai_smiley`, with a submodule called `rai_smiley.Smiley`,
# which in turn has a single class called
# `rai_smiley.Smiley.Smiley`.
# This can get annoying to type,
# so the above line of code
# imports the *class* Smiley into the root of the package,
# so now rai_smiley.Smiley points directly to the class
# instead of the module.
#
#
# This technique is called *namespace flattening*.
# Note that we could have accomplished the same result
# had we simply defined the Smiley class
# right here inside this __init__.py file.
# You are free to also do this,
# but please note that many people don't like it,
# For one, the file `Smiley.py` immediately makes it clear what
# is inside the file,
# while `__init__.py` communicates absolutely nothing about its content.
# As a result, many people expect `__init__.py` to contain technical
# boilerplate (like namespace flattening imports),
# or be empty altogether,
# so putting critical code inside `__init__.py` may come off
# as if you are trying to play hide-and-go-seek.

