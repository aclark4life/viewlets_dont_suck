
Introduction
============

*Viewlets don't suck! They are just really annoying.*

Explanation
-----------

This is a small Plone ``viewlet`` tutorial that adds/removes a bit of template code to the portal top viewlet manager. The *tongue-in-cheek* title refers to the following:

* In essence, ``viewlets`` are really cool. They allow you to customize any part of a Plone page without touching any Plone code.
* In practice, they are hard to work with (in the author's opinion) due to, but not limited to, the following reasons (many of which may be limitations of Plone):

  * They require GenericSetup [1]_
  * They require a Python package [2]_
  * They require an understanding of the ZCA [3]_

Details
-------

The goal of this package was to add/remove a viewlet as quickly as possible. The steps were roughly:

1. Create a Python package (viewlets_dont_suck)
2. Create namespace packages (they.are.just.really.annoying)
3. Create generic setup profiles (default AKA install, uninstall)
#. Create ZCML to configure viewlet (added to the portal top viewlet manager)
#. Create template (viewlets_dont_suck.pt)
#. Add GS code to hide the viewlet on uninstall (is there any more we can do?)
#. Add GS code to customize the order on install (last but not least)

.. image:: https://github.com/aclark4life/viewlets_dont_suck/raw/master/viewlets_dont_suck.png


.. [1] Technically, they don't; i.e. you can add viewlets and viewlet managers with ZCML.
.. [2] Technically, they don't; i.e. you can add ZCML without a Python package via the `plone.recipe.zope2instance` recipe, but GenericSetup requires a Python package (to register a directory full of XML configuration).
.. [3] Viewlet managers provide an interface that viewlets may configure themselves to use (via manager=<INTERFACE> in ZCML)
