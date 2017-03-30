Spack config files for NCI
==========================

Setup

```
source $SPACK/share/spack/setup-env.sh
cp configs/* ~/.spack

cat > ~/.spack/repos.yaml << EOF
repos::
  - ${PWD}
EOF
```

The double colon after `repos` means that the default Spack packages won't be
used (there are conflicts with their provided openmpi package)

Spack's packages are in `$SPACK/var/spack/repos/builtin`, they can be copied to
this repository as required.

Build a package with
```
spack build hdf5
```

Set up modules with
```
module use $SPACK/share/spack/modules/linux-centos6-x86_64/
```
