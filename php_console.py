#!/usr/bin/env python

from gi.repository import Gtk, Gio, Gdk, GtkSource, Pango
import os.path, subprocess

class PhprWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PHP Console")
        self.set_default_size(600, 400)
        self.connect("delete-event", Gtk.main_quit)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "PHP Console"
        self.set_titlebar(hb)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")
        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="media-playback-start-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        box.add(button)

        button.connect('clicked', self.run)

        hb.pack_start(box)


        scrolled_result = Gtk.ScrolledWindow()
        scrolled_result.set_hexpand(True)
        scrolled_result.set_vexpand(True)
        scrolled_source = Gtk.ScrolledWindow()
        scrolled_source.set_hexpand(True)
        scrolled_source.set_vexpand(True)

        self.result = Gtk.TextView()
        self.result.set_editable(False)
        self.result.props.is_focus = False
        scrolled_result.add(self.result);

        self.make_source()
        if os.path.isfile('/tmp/vxphpconsole.php'):
            file = open('/tmp/vxphpconsole.php', 'r')
            self.source.get_buffer().set_text(file.read())
            file.close()
        scrolled_source.add(self.source)

        paned = Gtk.Paned().new(Gtk.Orientation(1))
        paned.set_border_width(4)
        paned.pack1(scrolled_source, True, True)
        paned.pack2(scrolled_result, False, True)
        paned.set_position(260)
        self.add(paned)
        self.source.grab_focus()

        self.connect('key-press-event', self.run)

        self.show_all()

    def run(self, sender, key=None):
        if key:
            if key.get_keyval()[1] != 65474:
                return
        rbuffer = self.result.get_buffer()
        sbuffer = self.source.get_buffer()
        file = open('/tmp/vxphpconsole.php', 'w')
        file.write(sbuffer.get_text(
            sbuffer.get_start_iter(), sbuffer.get_end_iter(), False))
        file.close()
        # c = subprocess.call("/usr/bin/env php -f /tmp/vxphpconsole.php", shell=True)
        # c = subprocess.Popen("/usr/bin/env php -f /tmp/vxphpconsole.php",
            # shell=True).stdout.read()
        lines = ''
        p = subprocess.Popen('/usr/bin/env php -f /tmp/vxphpconsole.php',
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(p.stdout.readline, b''):
            lines = lines + line.decode('UTF-8')
        rbuffer.set_text(lines)
        p.stdout.close()
        p.wait()
        # rbuffer.set_text(p.stdout.readlines())

    def make_source(self):
        scheme = GtkSource.StyleSchemeManager()
        scheme.set_search_path()

        language = GtkSource.LanguageManager()

        buffer = GtkSource.Buffer()
        buffer.set_language(language.get_language('php'))
        buffer.set_style_scheme(scheme.get_scheme('tango'))
        buffer.set_highlight_syntax(True)

        font = Pango.FontDescription()
        font.set_family('Droid Sans Mono, DejaVu Sans Mono, Ubuntu Mono, Monospace')
        font.set_absolute_size(11 * Pango.SCALE)

        self.source = GtkSource.View.new_with_buffer(buffer)
        self.source.override_font(font)
        self.source.set_show_line_numbers(True)
        self.source.set_insert_spaces_instead_of_tabs(False)
        self.source.set_auto_indent(True)
        self.source.set_tab_width(4)
        self.source.set_indent_width(4)
        self.source.set_smart_home_end(True)
        self.source.set_highlight_current_line(True)

win = PhprWindow()
Gtk.main()
