gnome = import('gnome')
python = import('python').find_installation()

# Use custom_target to run glib-compile-resources directly
# This will create a .gresource binary file
compiled_gresource = custom_target(
    'org.wookhq.Lution.gresource',
    input: 'org.wookhq.Lution.gresource.xml',
    output: 'org.wookhq.Lution.gresource',
    # ADD THIS LINE: '--sourcedir=' + meson.current_source_dir() / '../data'
    command: [find_program('glib-compile-resources'),
              '--sourcedir=' + meson.current_source_dir() / '../data/ui', # <-- Change this line
              '@INPUT@',
              '--target=@OUTPUT@'],
    install: true,
    install_dir: join_paths(get_option('datadir'), 'org.wookhq.Lution')
)

python.install_sources(
  ['main.py', 'window.py', '__init__.py'],
  subdir: 'Lution'
)