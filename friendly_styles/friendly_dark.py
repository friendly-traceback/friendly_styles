"""Theme designed for friendly [friendly-traceback]

This theme has colours chosen for a dark (black) background.

friendly uses Pygments themes mostly through
Rich [https://github.com/willmcgugan/rich].

Rich's console has styles for some objects that are defined
independently from a chosen Pygments theme.
In this file, we define a consistent theme which results
in the same colour shown for a certain object type whether
the colouring is done by Pygments or directly by Rich.
"""

from pygments.style import Style
from pygments.token import (
    Keyword,
    Name,
    Comment,
    String,
    Error,
    Text,
    Number,
    Operator,
    Generic,
    Whitespace,
    Punctuation,
    Other,
    Literal,
)


colours = {
    "yellow": "#F0E68C",
    "orange": "#FF8243",
    "red": "#D92121",
    "white": "#F4F0EC",
    "beige": "#DEB887",
    "blue": "#87CEEB",
    "gray": "#999999",
    "green": "#87A96B",
    "mauve": "#9370DB",
    "black": "#101010",
}

friendly_style = {
    "builtins": colours["yellow"],
    "code": colours["beige"],
    "comments": colours["gray"],
    "keywords": colours["yellow"],
    "numbers": colours["white"],
    "operators": colours["blue"],
    "string": colours["green"],
    "text": colours["white"],
    "TrueFalseNone": colours["orange"],
    "Exception": colours["red"],
    "diagnostics": "#FF00FF",  # Magenta; when trying to figure out a category
}

# Since we use Rich's pretty(), we try to ensure that the colours
# are consistent.  pretty() highlight objects based on their repr name
# with the following choices:

rich_style = {
    "markdown.code": friendly_style["code"],
    "repr.tag_name": friendly_style["code"],  # for consistency with Python
    "markdown.h1": friendly_style["diagnostics"],
    # Exception message; location header H2
    "markdown.h2": friendly_style["Exception"],
    "markdown.h3": colours["mauve"],  # likely cause
    "markdown.h4": colours["orange"],  # warning header
    "markdown.link": f"underline {friendly_style['keywords']}",
    "repr.url": friendly_style["keywords"],
    "repr.number": friendly_style["numbers"],
    # The next three are identical for pygments, so we keep them identical
    "repr.bool_false": friendly_style["TrueFalseNone"],
    "repr.bool_true": friendly_style["TrueFalseNone"],
    "repr.none": friendly_style["TrueFalseNone"],
    #
    "repr.str": friendly_style["string"],
    "repr.error": friendly_style["Exception"],
    "repr.indent": friendly_style["comments"],
    "repr.attrib_name": friendly_style["builtins"],
    "repr.attrib_value": friendly_style["code"],
    "repr.attrib_equal": friendly_style["operators"],
    "repr.call": friendly_style["code"],
}

friendly_style.update(**rich_style)


class FriendlyDarkStyle(Style):
    """Theme designed for friendly/friendly-traceback
    suitable for a black or very dark background.
    """
    background_color = colours["black"]
    default_style = "#363636"
    friendly_style = friendly_style

    styles = {
        Text: friendly_style["text"],  # class:  ''
        Whitespace: "",  # class: 'w'
        Error: "bg:#ff0000 #ffffff",  # class: 'err'
        Other: friendly_style["string"],  # class 'x'
        #
        Comment: friendly_style["comments"],  # class: 'c'
        Comment.Multiline: friendly_style["comments"],  # class: 'cm'
        Comment.Preproc: friendly_style["comments"],  # class: 'cp'
        Comment.Single: friendly_style["comments"],  # class: 'c1'
        Comment.Special: friendly_style["comments"],  # class: 'cs'
        #
        Generic: friendly_style["text"],  # class: 'g'
        Generic.Deleted: friendly_style["Exception"],  # class: 'gd'
        Generic.Emph: friendly_style["text"],  # class: 'ge'
        Generic.Error: friendly_style["Exception"],  # class: 'gr'
        Generic.Heading: friendly_style["text"],  # class: 'gh'
        Generic.Inserted: friendly_style["text"],  # class: 'gi'
        Generic.Output: friendly_style["text"],  # class: 'go'
        Generic.Prompt: friendly_style["keywords"],  # class: 'gp'
        Generic.Strong: friendly_style["text"],  # class: 'gs'
        Generic.Subheading: friendly_style["text"],  # class: 'gu'
        Generic.Traceback: friendly_style["Exception"],  # class: 'gt'
        #
        Keyword: friendly_style["keywords"],  # class: 'k'
        Keyword.Constant: friendly_style["TrueFalseNone"],  # class: 'kc'
        Keyword.Declaration: friendly_style["keywords"],  # class: 'kd'
        Keyword.Namespace: friendly_style["keywords"],  # class: 'kn'
        Keyword.Pseudo: friendly_style["keywords"],  # class: 'kp'
        Keyword.Reserved: friendly_style["keywords"],  # class: 'kr'
        Keyword.Type: friendly_style["keywords"],  # class: 'kt'
        #
        Literal: friendly_style["text"],  # class: 'l'
        Literal.Date: friendly_style["text"],  # class: 'ld'
        #
        Name: friendly_style["code"],  # class: 'n'
        Name.Attribute: friendly_style["code"],  # class: 'na'
        # The following is for file path in tracebacks and Python builtins.
        Name.Builtin: friendly_style["builtins"],  # class: 'nb'
        Name.Builtin.Pseudo: friendly_style["builtins"],  # class: 'bp'
        Name.Class: friendly_style["code"],  # class: 'nc'
        Name.Constant: friendly_style["code"],  # class: 'no'
        Name.Decorator: friendly_style["code"],  # class: 'nd'
        Name.Entity: friendly_style["code"],  # class: 'ni'
        Name.Exception: friendly_style["Exception"],  # class: 'ne'
        Name.Function: friendly_style["code"],  # class: 'nf'
        Name.Property: friendly_style["code"],  # class: 'py'
        Name.Label: friendly_style["code"],  # class: 'nl'
        Name.Namespace: friendly_style["code"],  # class: 'nn'
        Name.Other: friendly_style["diagnostics"],  # class: 'nx'
        Name.Tag: friendly_style["code"],  # class: 'nt' - like a keyword
        Name.Variable: friendly_style["text"],  # class: 'nv'
        Name.Variable.Class: friendly_style["code"],  # class: 'vc'
        Name.Variable.Global: friendly_style["code"],  # class: 'vg'
        Name.Variable.Instance: friendly_style["text"],  # class: 'vi'
        #
        Number: friendly_style["numbers"],  # class: 'm'
        Number.Float: friendly_style["numbers"],  # class: 'mf'
        Number.Hex: friendly_style["numbers"],  # class: 'mh'
        Number.Integer: friendly_style["numbers"],  # class: 'mi'
        Number.Integer.Long: friendly_style["numbers"],  # class: 'il'
        Number.Oct: friendly_style["numbers"],  # class: 'mo'
        #
        Operator: friendly_style["operators"],  # class: 'o'
        Operator.Word: friendly_style["keywords"],  # class: 'ow'
        #
        Punctuation: friendly_style["operators"],  # class: 'p'
        #
        String: friendly_style["string"],  # class: 's'
        String.Backtick: friendly_style["string"],  # class: 'sb'
        String.Char: friendly_style["string"],  # class: 'sc'
        String.Doc: friendly_style["string"],  # class: 'sd'
        String.Double: friendly_style["string"],  # class: 's2'
        String.Escape: friendly_style["string"],  # class: 'se'
        String.Heredoc: friendly_style["string"],  # class: 'sh'
        String.Interpol: friendly_style["string"],  # class: 'si'
        String.Other: friendly_style["string"],  # class: 'sx'
        String.Regex: friendly_style["string"],  # class: 'sr'
        String.Single: friendly_style["string"],  # class: 's1'
        String.Symbol: friendly_style["string"],  # class: 'ss'
    }
