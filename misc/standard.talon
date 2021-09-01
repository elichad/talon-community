(jay son | jason ): "json"
(http | htp): "http"
#tls: "tls"
#M D five: "md5"
#word (regex | rejex): "regex"
#word queue: "queue"
#word eye: "eye"
#word iter: "iter"
#word no: "NULL"
#word cmd: "cmd"
#word dup: "dup"
#word shell: "shell".
zoom in: edit.zoom_in()
zoom out: edit.zoom_out()
scruffy: edit.page_up()
scrawny: edit.page_down()
stash: edit.copy()
cut: edit.cut()
spark: edit.paste()
stoke: key(win-v)
undo: edit.undo()
redo: edit.redo()
spark match: edit.paste_match_style()
save file: edit.save()
clear: key(backspace)
(pad | padding):
	insert("  ")
	key(left)
slap: edit.line_insert_down()

