# -*- coding: utf-8 -*-

from gi.repository import GObject, Gtk, Gdk, Gedit

class PanelSwitcher(GObject.Object, Gedit.WindowActivatable):
	__gtype_name__ = "PanelSwitcher"

	window = GObject.property(type=Gedit.Window)

	def __init__(self):
		GObject.Object.__init__(self)

	def do_activate(self):
		handlers = []
		handler_id = self.window.connect('key-press-event', self.on_key_press_event)
		handlers.append(handler_id)
		self.window.set_data(self.__gtype_name__+"Handlers", handlers)

	def do_deactivate(self):
		handlers = self.window.get_data(self.__gtype_name__+"Handlers")
		for handler_id in handlers:
			self.window.disconnect(handler_id)

	def do_update_state(self):
		pass

	def on_key_press_event(self, window, event):
		key = Gdk.keyval_name(event.keyval)

		if event.state & Gdk.ModifierType.CONTROL_MASK and key in ('Tab'):
			active_view = window.get_active_view()

			if active_view.has_focus():
				window.get_bottom_panel().grab_focus()

			else:
				active_view.grab_focus()

			return True
