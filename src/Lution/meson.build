# File: /run/media/chip/fd781af7-611c-4356-ad15-3f6bf2cbcfca/the gibhub/Lution/src/Lution/meson.build
gnome = import('gnome')
python = import('python').find_installation() # Ensure python is imported here

gres = custom_target(
    'org.wookhq.Lution.gresource',
    input: 'org.wookhq.Lution.gresource.xml',
    output: 'org.wookhq.Lution.gresource',
    command: [find_program('glib-compile-resources'),
              '--sourcedir=' + meson.current_source_dir() / '../data/ui', # Adjust if your UI files are elsewhere
              '@INPUT@',
              '--target=@OUTPUT@'],
    install: true,
    install_dir: join_paths(get_option('datadir'), 'org.wookhq.Lution')
)

python.install_sources(
  ['main.py', 'window.py', '__init__.py'],
  subdir: 'Lution'
)

# --- ADD THIS BLOCK HERE ---
# Install the 'modules' directory as a Python package
# 'modules' is now relative to src/Lution/meson.build, which is correct
install_subdir(
    'modules', # Source directory is 'modules' relative to this meson.build
    install_dir: python.get_install_dir() # Install directly into site-packages
)
# --- END OF ADDED BLOCK ---