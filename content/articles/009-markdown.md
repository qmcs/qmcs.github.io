Title: A small Markdown introduction
Date: 2014-03-04
Tags: markdown, markup, languages
Category: languages
Author: Henrik O. Skogmo


Giving writers a WYSIWYG makes the assumption that they know how to make stuff
look good. This is wrong. People who work with words should only have to care
about words. Leaving the design choices to the designers. Markdown does an
excellent job in accomplishing this compromise.

Many of the web's most populare publishing tools are now supporting Markdown.
And you might recognise it from Stack Overflow and GitHub. So maybe it's time
you get down with the M-down?

How the hell do you harvest the sweet markdown nectar? Easy. Kick-start your
favourite (plain)text editor and fire away. Since Markdown is a lightweight
markup language, all of you oldschool BBCode forum writers out there will find
yourselves quite confortable.

Even though you can find the reference to [Markdown's
syntax](http://daringfireball.net/projects/markdown/syntax) online, I'll walk
you through some of the basics. Do note that there is alternatives for some of
the elements, so I encourouge you to gaze over the documenation.

## Headers

Use hashtags to mark the level of a header.

    # This is an H1
    ## This is an H2
    ### This is an H3

## Emphasis
Asterisks or underlines

    The quick *brown fox* jumps over the **lazy dog**

Becomes "The quick *brown fox* jumps over the **lazy dog**"

## Links There are multiple ways of making links in MD, either inline or by
reference. However here is the most used way.

    [an example](http://example.com "Title")

## Lists
Simply use something that looks listy (\*, \+ or \-).

### Unordered

    * Red
    - Green
    + Blue

Becomes

* Red
* Green
* Blue

### Ordered
(What the numbers are does't matter)

    4. Red
    0. Green
    4. Blue

Becomes

4. Red
0. Green
4. Blue

## Code
### Inline
Use the backtick quotes (\`) for `inline code`.

### Block
4 spaces or 1 tab indention

    HAI 1.2
      CAN HAS STDIO?
      VISIBLE "HAI WORLD!!!1!"
    KTHXBYE

If you would like to start using Markdown locally on your own system I have a
couple of Markdown readers to recommend. Even though you don't strickly need
anything fancy to write Markdown, you still need something to parse it.

[Mou](http://mouapp.com/) for Mac
[MarkdownPad](http://markdownpad.com/) for Windowns
[ReText](http://sourceforge.net/p/retext/home/ReText/) for Linux
