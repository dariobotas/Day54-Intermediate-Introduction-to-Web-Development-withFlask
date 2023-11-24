{ pkgs }: {
  deps = [
    pkgs.mkinitcpio-nfs-utils
    pkgs.unixtools.ifconfig
    pkgs.python38Packages.flask
  ];
}