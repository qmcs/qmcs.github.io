# EECS Society Site theme

Sources for the theme of the EECS society static website

Meant to replace [Pelicanium](https://github.com/qmcs/pelicanium) with the themes [here](https://github.com/HSkogmo/EECS-Society-Website).

Instead of a separate repository the themes are simply in the 'theme' folder. 

In addition to the theme there are a bunch of issues that need fixing, which should get documented in 'issues'

To work on theme look up the pelican, [documentation](http://docs.getpelican.com/en/3.6.3/themes.html) on how it works.

Rebuild the website to check your changes **on branch pelican**:

```
python boostrapy.py
bin/buildout 
make devserver
open localhost:8000
```

Eventually we should make sure the output goes to branch master automatically.

