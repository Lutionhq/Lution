project('Lution',
          version: '0.1.0',
    meson_version: '>= 1.0.0',
  default_options: [ 'warning_level=2', 'werror=false', ],
)

# In src/meson.build, outside of subdir('Lution')
app_id = 'org.wookhq.Lution' # Define your application ID

# Install the desktop file
install_data(
    'data/' + app_id + '.desktop', # Path to your .desktop file
    install_dir: get_option('datadir') / 'applications'
)

# Optional: If you have an icon (e.g., in src/data/icons/hicolor/scalable/apps/org.wookhq.Lution.svg)
install_data(
    'data/svg/' + app_id + '.svg',
    install_dir: get_option('datadir') / 'icons/hicolor/scalable/apps'
 )

subdir('Lution')

