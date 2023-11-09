# shared

Shared kernel for nix flakes.

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-shared-nix-flake/shared-artifact/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-nix-flake-shared = {
      [optional follows]
      url =
        "github:pythoneda-shared-nix-flake/shared-artifact/[version]?dir=shared";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is under the [https://github.com/pythoneda-shared-nix-flake/shared-artifact/tree/main/shared](shared "shared") folder of <https://github.com/pythoneda-shared-nix-flake/shared-artifact>.


