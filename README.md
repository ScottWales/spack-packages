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
