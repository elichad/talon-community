question [mark]: "?"
(downscore | underscore): "_"
dash: " – "
double dash: "--"
(bracket | left bracket): "("
(are bracket | right bracket): ")"
triple quote: "'''"
(triple grave | triple back tick | gravy):
    insert("```")
(dot dot | dotdot): ".."
ellipses: "..."
(comma and | spamma): ", "
plus: "+"
arrow: "->"
dub arrow: "=>"
new line: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"
empty dubstring:
    '""'
    key(left)
empty escaped (dubstring|dub quotes):
    '\\"\\"'
    key(left)
    key(left)
empty string:
    "''"
    key(left)
empty escaped string:
    "\\'\\'"
    key(left)
    key(left)
prekris:
	insert("()")
	key(left)
brax:
	insert("[]")
	key(left)
curly:
	insert("{}")
	key(left)
centuries:
	insert("%%")
	key(left)
thin quotes:
	insert("''")
	key(left)
quotes:
    insert('""')
	key(left)
tickris:
	insert("``")
	key(left)
hug angles:
    text = edit.selected_text()
    user.paste("<{text}>")
hug brax:
    text = edit.selected_text()
    user.paste("[{text}]")
hug curly:
    text = edit.selected_text()
    user.paste("{{{text}}}")
hug prekris:
    text = edit.selected_text()
    user.paste("({text})")
hug percent:
    text = edit.selected_text()
    user.paste("%{text}%")
hug quotes:
    text = edit.selected_text()
    user.paste('"{text}"')
(double quote | dubquote) that:
    text = edit.selected_text()
    user.paste('"{text}"')
hug (graves | back ticks):
    text = edit.selected_text()
    user.paste('`{text}`')
