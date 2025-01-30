{pkgs}: {
  deps = [
    pkgs.sqlite-interactive
    pkgs.rustc
    pkgs.libiconv
    pkgs.cargo
    pkgs.imagemagick_light
  ];
}
