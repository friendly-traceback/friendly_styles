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

base_style = {
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
    "markdown.code": base_style["code"],
    "repr.tag_name": base_style["code"],  # for consistency with Python
    "markdown.h1": base_style["diagnostics"],
    # Exception message; location header H2
    "markdown.h2": base_style["Exception"],
    "markdown.h3": colours["mauve"],  # likely cause
    "markdown.h4": colours["orange"],  # warning header
    "markdown.link": f"underline {base_style['keywords']}",
    "repr.url": base_style["keywords"],
    "repr.number": base_style["numbers"],
    # The next three are identical for pygments, so we keep them identical
    "repr.bool_false": base_style["TrueFalseNone"],
    "repr.bool_true": base_style["TrueFalseNone"],
    "repr.none": base_style["TrueFalseNone"],
    #
    "repr.str": base_style["string"],
    "repr.error": base_style["Exception"],
    "repr.indent": base_style["comments"],
    "repr.attrib_name": base_style["builtins"],
    "repr.attrib_value": base_style["code"],
    "repr.attrib_equal": base_style["operators"],
    "repr.call": base_style["code"],
}

base_style.update(**rich_style)


class FriendlyDarkStyle(Style):
    """Theme designed for friendly/friendly-traceback
    suitable for a black or very dark background.
    """
    background_color = colours["black"]
    default_style = "#363636"
    base_style = base_style

    styles = {
        Text: base_style["text"],  # class:  ''
        Whitespace: "",  # class: 'w'
        Error: "bg:#ff0000 #ffffff",  # class: 'err'
        Other: base_style["string"],  # class 'x'
        #
        Comment: base_style["comments"],  # class: 'c'
        Comment.Multiline: base_style["comments"],  # class: 'cm'
        Comment.Preproc: base_style["comments"],  # class: 'cp'
        Comment.Single: base_style["comments"],  # class: 'c1'
        Comment.Special: base_style["comments"],  # class: 'cs'
        #
        Generic: base_style["text"],  # class: 'g'
        Generic.Deleted: base_style["Exception"],  # class: 'gd'
        Generic.Emph: base_style["text"],  # class: 'ge'
        Generic.Error: base_style["Exception"],  # class: 'gr'
        Generic.Heading: base_style["text"],  # class: 'gh'
        Generic.Inserted: base_style["text"],  # class: 'gi'
        Generic.Output: base_style["text"],  # class: 'go'
        Generic.Prompt: base_style["keywords"],  # class: 'gp'
        Generic.Strong: base_style["text"],  # class: 'gs'
        Generic.Subheading: base_style["text"],  # class: 'gu'
        Generic.Traceback: base_style["Exception"],  # class: 'gt'
        #
        Keyword: base_style["keywords"],  # class: 'k'
        Keyword.Constant: base_style["TrueFalseNone"],  # class: 'kc'
        Keyword.Declaration: base_style["keywords"],  # class: 'kd'
        Keyword.Namespace: base_style["keywords"],  # class: 'kn'
        Keyword.Pseudo: base_style["keywords"],  # class: 'kp'
        Keyword.Reserved: base_style["keywords"],  # class: 'kr'
        Keyword.Type: base_style["keywords"],  # class: 'kt'
        #
        Literal: base_style["text"],  # class: 'l'
        Literal.Date: base_style["text"],  # class: 'ld'
        #
        Name: base_style["code"],  # class: 'n'
        Name.Attribute: base_style["code"],  # class: 'na'
        # The following is for file path in tracebacks and Python builtins.
        Name.Builtin: base_style["builtins"],  # class: 'nb'
        Name.Builtin.Pseudo: base_style["builtins"],  # class: 'bp'
        Name.Class: base_style["code"],  # class: 'nc'
        Name.Constant: base_style["code"],  # class: 'no'
        Name.Decorator: base_style["code"],  # class: 'nd'
        Name.Entity: base_style["code"],  # class: 'ni'
        Name.Exception: base_style["Exception"],  # class: 'ne'
        Name.Function: base_style["code"],  # class: 'nf'
        Name.Property: base_style["code"],  # class: 'py'
        Name.Label: base_style["code"],  # class: 'nl'
        Name.Namespace: base_style["code"],  # class: 'nn'
        Name.Other: base_style["diagnostics"],  # class: 'nx'
        Name.Tag: base_style["code"],  # class: 'nt' - like a keyword
        Name.Variable: base_style["text"],  # class: 'nv'
        Name.Variable.Class: base_style["code"],  # class: 'vc'
        Name.Variable.Global: base_style["code"],  # class: 'vg'
        Name.Variable.Instance: base_style["text"],  # class: 'vi'
        #
        Number: base_style["numbers"],  # class: 'm'
        Number.Float: base_style["numbers"],  # class: 'mf'
        Number.Hex: base_style["numbers"],  # class: 'mh'
        Number.Integer: base_style["numbers"],  # class: 'mi'
        Number.Integer.Long: base_style["numbers"],  # class: 'il'
        Number.Oct: base_style["numbers"],  # class: 'mo'
        #
        Operator: base_style["operators"],  # class: 'o'
        Operator.Word: base_style["keywords"],  # class: 'ow'
        #
        Punctuation: base_style["operators"],  # class: 'p'
        #
        String: base_style["string"],  # class: 's'
        String.Backtick: base_style["string"],  # class: 'sb'
        String.Char: base_style["string"],  # class: 'sc'
        String.Doc: base_style["string"],  # class: 'sd'
        String.Double: base_style["string"],  # class: 's2'
        String.Escape: base_style["string"],  # class: 'se'
        String.Heredoc: base_style["string"],  # class: 'sh'
        String.Interpol: base_style["string"],  # class: 'si'
        String.Other: base_style["string"],  # class: 'sx'
        String.Regex: base_style["string"],  # class: 'sr'
        String.Single: base_style["string"],  # class: 's1'
        String.Symbol: base_style["string"],  # class: 'ss'
    }
