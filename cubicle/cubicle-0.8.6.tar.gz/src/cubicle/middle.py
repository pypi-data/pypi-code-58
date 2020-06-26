"""
This module focuses on the transformation from AST to static structure.
There's not really too much magic here, but it's good to have the separation.
It's also completely unusable at the moment; just a parking lot for excised code.
But things will get better...
"""

import collections
from typing import List, Union, Mapping, MutableMapping
from boozetools.support import foundation, failureprone
from . import AST, static, formulae, xl_schema, veneer


class SemanticError(Exception):
	"""
	Catch-all for things that should not be.
	"""

class UndefinedNameError(KeyError): pass
class RedefinedNameError(KeyError): pass
class BadAttributeValue(ValueError): pass
class NoSuchAttrbute(KeyError): pass

BLANK_STYLE = collections.ChainMap({
	'_texts':(), '_hint':None,
	'level':0, 'hidden':False, 'collapsed':False,
	'height':None, 'width':None,
})

VOCABULARY = {
	**xl_schema.FORMAT_PROPERTIES,
	**xl_schema.OUTLINE_PROPERTIES,
	**{k: xl_schema.FORMAT_PROPERTIES[v[0]] for k, v in xl_schema.SPECIAL_CASE.items()},
}


class SymbolTable:
	""" I've a sense I'll want a "smart" symbol table object: a bit more than a dictionary. """
	def __init__(self):
		self.__entries = {} # For now entries are just a <Name, object> pair. Keys are strings.
	
	def __contains__(self, item):
		if isinstance(item, str): return item in self.__entries
		if isinstance(item, AST.Name): return item.text in self.__entries
		raise TypeError(item)
	
	def let(self, name:AST.Name, item):
		""" Enforce single-assignment... """
		assert isinstance(name, AST.Name), type(name)
		key = name.text
		if key in self.__entries: raise RedefinedNameError(name, self.__entries[key][0])
		else: self.__entries[key] = (name, item)
	
	def get(self, name:AST.Name):
		try: return self.__entries[name.text][1]
		except KeyError: raise UndefinedNameError(name) from None
	
	def get_declaration(self, key:str) -> AST.Name:
		""" Go find where was the name that declared the symbol. """
		return self.__entries[key][0]
	
	def as_dict(self) -> dict:
		""" Just string keys and semantic items; no location-tracking fluff. """
		return {key: entry[1] for key, entry in self.__entries.items()}
	

class Transducer(foundation.Visitor):
	"""
	A form of interpreter: not from source lines of code, but from a list of
	AST nodes for top-level declarations. It can also be considered a kind of
	tree-transducer, if you squint.
	
	Someone will object that this should not be written as an object (I pun)
	but the alternative (a nest of procedures) gets ugly fast.
	"""
	def __init__(self, source:failureprone.SourceText):
		self.source = source
		
		self.named_styles = SymbolTable()
		self.named_fields = SymbolTable()
		self.translated_shapes = SymbolTable()
		self.named_canvases = SymbolTable()
		
		self.numbered_styles = foundation.EquivalenceClassifier()
		self.numbered_outlines = foundation.EquivalenceClassifier()
	
	def interpret(self, declarations:List[Union[AST.StyleDef, AST.Field, AST.Canvas]]) -> static.CubModule:
		for d in declarations: self.visit(d)
		return static.CubModule(
			self.named_canvases.as_dict(),
			self.numbered_styles.exemplars,
			self.numbered_outlines.exemplars,
		)
	
	def visit_Field(self, field:AST.Field):
		self.named_fields.let(field.name, field.shape)

	def visit_Canvas(self, canvas:AST.Canvas):
		""" Build a static.CanvasDefinition and add it to self.named_canvases """
		def mk_style_rule(sel, elts):
			style_rules.append(veneer.Rule(sel, style_index(elts)))
		
		def style_index(elts):
			env = {}
			self.build_style(elts, env)
			return self.make_numbered_style(env)

		style_rules = []
		formula_rules = []
		merge_rules = []
		
		background_style = style_index(canvas.style_points)
		for is_merge, selector, content, style in canvas.patches:
			assert isinstance(selector, formulae.Selection)
			if style: mk_style_rule(selector, style)
			if is_merge: merge_rules.append(veneer.Rule(selector, content))
			elif content: formula_rules.append(veneer.Rule(selector, content))
		self.named_canvases.let(canvas.name, static.CanvasDefinition(
			horizontal=self.get_translated(canvas.across),
			vertical=self.get_translated(canvas.down),
			background_style=background_style,
			style_rules=style_rules,
			formula_rules=formula_rules,
			merge_specs=merge_rules,
		))
		pass
	
	def get_translated(self, name:AST.Name) -> static.ShapeDefinition:
		if name not in self.translated_shapes:
			shape = self.named_fields.get(name)
			item = FieldBuilder(self, BLANK_STYLE, name).visit(shape)
			self.translated_shapes.let(name, item)
		return self.translated_shapes.get(name)
	
	def visit_StyleDef(self, styledef:AST.StyleDef):
		"""
		Build up a named-style as a root-level object and store it in the style namespace.
		At least, that's the happy path. Various things can go wrong. What gets reported
		first is sort of a matter of happenstance: what mistake do we stumble over first?
		At any rate, report definitions should not ever get huge, so reporting an error
		and quitting is probably an OK strategy for now.
		"""
		env = {}
		self.build_style(styledef.elts, env)
		try: self.named_styles.let(styledef.name, env)
		except RedefinedNameError as e:
			self.source.complain(*e.args[0].span, message="Redefined style name")
			self.source.complain(*e.args[1].span, message="First defined here")
			raise
	
	def build_style(self, elts:List, env:MutableMapping):
		"""
		elts are -- style names, activations, deactivations, or attribute assignments.
		This works by mutating an environment you pass in, so the same code therefore works
		regardless of use in creating named-styles or actually-used styles.
		"""
		def try_assign(name:AST.Name, value, value_span):
			"""
			The key must be a properly recognized style property as defined in module `xl_schema`.
			There are two special cases (`border` and `border_color`) which behave as if corresponding
			top, left, bottom, and right properties are all set at once.
			The value must be consistent with the expectations for the property the key names.
			The spans give locations in a source text to complain about if something goes wrong.
			"""
			key = name.text
			if key not in VOCABULARY:
				self.source.complain(*name.span, message="There's no such attribute as '%s'." % key)
				raise NoSuchAttrbute(key)
			kind = VOCABULARY[key]
			if not kind.test(value):
				self.source.complain(*value_span, message="Value for %s must be %s" % (key, kind.description))
				raise BadAttributeValue(value)
			if key in xl_schema.SPECIAL_CASE:
				for k in xl_schema.SPECIAL_CASE[key]: env[k] = value
			else: env[key] = value
		
		for item in elts:
			if isinstance(item, AST.Assign):
				try_assign(item.word, item.const.value, item.const.span)
			elif isinstance(item, AST.Sigil):
				if item.kind == 'ACTIVATE': try_assign(item.name, True, item.name.span)
				elif item.kind == 'DEACTIVATE': try_assign(item.name, False, item.name.span)
				elif item.kind == 'STYLE_NAME': env.update(self.named_styles.get(item.name))
			else: assert False, item
	
	def make_numbered_style(self, env:Mapping) -> int:
		digest = sorted((k, v) for k, v in env.items() if k in xl_schema.FORMAT_PROPERTIES)
		return self.numbered_styles.classify(tuple(digest))
	
	def make_numbered_outline(self, env:Mapping) -> int:
		digest = (env['level'], env['hidden'], env['collapsed'])
		return self.numbered_outlines.classify(digest)

class FieldBuilder(foundation.Visitor):
	"""
	I have this idea that the answer to translating fields is properly recursive only on
	a slightly reduced form of the original problem.
	"""
	def __init__(self, module_builder:Transducer, style_context:collections.ChainMap, name:AST.Name):
		self.mb = module_builder
		self.sc = style_context.new_child()
		self.name = name
	
	def subordinate(self, name:AST.Name) -> "FieldBuilder":
		return FieldBuilder(self.mb, self.sc, name)
	
	def interpret_margin_notes(self, notes:AST.Marginalia) -> static.Marginalia:
		"""
		Two phases: Update the fields of the style context (self.sc) according to the notes,
		and then capture the result in the appointed structure.
		"""
		# FIXME: This neglects to transduce the texts and hints.
		if notes.texts is not None:
			self.sc['_texts'] = notes.texts
		if notes.hint is not None:
			self.sc['_hint'] = self.interpret_hint(notes.hint)
		self.mb.build_style(notes.appearance, self.sc)
		return static.Marginalia(
			style_index=self.mb.make_numbered_style(self.sc),
			outline_index=self.mb.make_numbered_outline(self.sc),
			texts=self.sc['_texts'],
			hint=self.sc['_hint'],
			height=self.sc['height'],
			width=self.sc['width'],
		)
	
	def interpret_hint(self, hint:object):
		if hint is AST.GAP_HINT: return static.Hint(formulae.THE_NOTHING, 999)
		if isinstance(hint, AST.Constant) and hint.kind == 'INT':
			# It's a reference to a perpendicular text. It has precedence above marginal formulas.
			assert isinstance(hint.value, int), hint
			assert hint.value > 0, hint.value
			return hint.value - 1
		boilerplate, prio_spec = hint
		if prio_spec is None: priority = 0
		elif isinstance(prio_spec, AST.Constant):
			assert prio_spec.kind == 'INT'
			priority = prio_spec.value
		else: assert False, type(prio_spec)
		assert isinstance(priority, int)
		return static.Hint(boilerplate, priority)
	
	def visit_Marginalia(self, notes:AST.Marginalia) -> static.LeafDefinition:
		return static.LeafDefinition(self.interpret_margin_notes(notes))
	
	def visit_LinkRef(self, linkref:AST.LinkRef) -> static.ShapeDefinition:
		sub = self.subordinate(linkref.name)
		sub.interpret_margin_notes(linkref.margin)
		return sub.visit(self.mb.named_fields.get(linkref.name))
	
	def visit_Tree(self, tree:AST.Tree) -> static.TreeDefinition:
		margin = self.interpret_margin_notes(tree.margin)
		key = tree.key or self.name
		if isinstance(key, AST.Name):
			reader = static.SimpleReader(key.text)
		elif isinstance(key, AST.Sigil):
			assert key.kind == 'COMPUTED', key.kind
			key = key.name
			reader = static.ComputedReader(key.text)
		else:
			assert False, type(key)
		pseudo_symbol = AST.Name('per_'+key.text, key.span)
		within = self.subordinate(pseudo_symbol).visit(tree.within)
		return static.TreeDefinition(reader, within, margin)
	
	def visit_Frame(self, frame:AST.Frame) -> static.FrameDefinition:
		# Expanding on this first because it's called first.
		# The margin notes are the easy bit:
		margin = self.interpret_margin_notes(frame.margin)
		children = self.__children(frame.fields)
		
		# There are three possible key types: name, sigil, and None.
		key = frame.key or self.name
		if isinstance(key, AST.Name):
			axis = key.text
			if '_' in children: reader = static.DefaultReader(axis)
			else: reader = static.SimpleReader(axis)
			# However, if there's a field called '_', then we want a default-reader instead?
		elif isinstance(key, AST.Sigil):
			assert key.kind == 'COMPUTED', key.kind
			try: symbol = children.get_declaration('_')
			except KeyError: pass
			else:
				self.mb.source.complain(*key.name.span, message="This tells me the environment will supply a field name...")
				self.mb.source.complain(*symbol.span, message="Therefore, a 'default' field makes no sense.")
				raise SemanticError()
			reader = static.ComputedReader(key.name.text)
		else:
			assert False, type(key)
		
		return static.FrameDefinition(reader, children.as_dict(), margin)
	
	def __children(self, fields:list) -> SymbolTable:
		# Recursion on the children should be a useful trick...
		children = SymbolTable()
		for symbol, definition in fields:
			children.let(symbol, self.subordinate(symbol).visit(definition))
		return children
	
	def visit_Menu(self, menu:AST.Menu) -> static.MenuDefinition:
		# Expanding on this first because it's called first.
		# The margin notes are the easy bit:
		margin = self.interpret_margin_notes(menu.margin)
		children = self.__children(menu.fields)
		assert '_' not in children, "This is grammatically impossible!"
		
		# There are three possible key types: name, sigil, and None.
		key = menu.key or self.name
		if isinstance(key, AST.Name):
			reader = static.SimpleReader(key.text)
		elif isinstance(key, AST.Sigil):
			assert key.kind == 'COMPUTED', key.kind
			reader = static.ComputedReader(key.name.text)
		else:
			assert False, type(key)
		
		return static.MenuDefinition(reader, children.as_dict(), margin)

