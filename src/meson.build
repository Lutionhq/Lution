project('Lution',
          version: '1.2.3',
    meson_version: '>= 1.0.0',
  default_options: [ 'warning_level=2', 'werror=false', ],
)

app_id = 'org.wookhq.Lution'

install_data(
    'data/' + app_id + '.desktop',
    install_dir: get_option('datadir') / 'applications'
)

install_data(
    'data/svg/' + app_id + '.png',
    install_dir: get_option('datadir') / 'icons/hicolor/scalable/apps'
)


python = import('python').find_installation()

subdir('Lution')