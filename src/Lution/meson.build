gnome = import('gnome')
python = import('python').find_installation()

gres = custom_target(
    'org.wookhq.Lution.gresource',
    input: 'org.wookhq.Lution.gresource.xml',
    output: 'org.wookhq.Lution.gresource',
    command: [find_program('glib-compile-resources'),
              '--sourcedir=' + meson.current_source_dir() / '../data/ui', 
              '@INPUT@',
              '--target=@OUTPUT@'],
    install: true,
    install_dir: join_paths(get_option('datadir'), 'org.wookhq.Lution')
)

python.install_sources(
  ['main.py', 'window.py', '__init__.py'],
  subdir: 'Lution'
)


install_subdir(
    'modules', 
    install_dir: python.get_install_dir() 
)
